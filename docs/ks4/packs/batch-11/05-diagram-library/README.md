# Batch 11 — diagram library audit

Method: grepped `figlib/chemistry.py`, `figlib/biochem.py`, `figlib/physics.py`,
`figlib/biology.py`, `figlib/charts.py`, `shared/ks4-diagrams.js`,
`ks3_art/*.py` and `ks4_lessons/authored/batch-2/` + `batch-3/*.dc.html` for
function names and docstrings naming each lesson's subject matter, then read
the matching function/docstring to confirm it is a real match and not a
substring collision. **Three genuine forward references found, all from
already-authored KS4 pilot lessons:** `ks4_lessons/authored/batch-2/
using-moles-calculations.dc.html`'s own `endConnects` array links forward to
BOTH `['moles', 'Moles']` and `['amounts-in-equations', 'Amounts of
substances in equations']` via `K.hrefFor`; `ks4_lessons/authored/batch-3/
conservation-of-mass.dc.html`'s `endConnects` links forward to BOTH
`['mass-changes-reactions', 'Mass changes when a gas is involved']` and
`['amounts-in-equations', …]`; `ks4_lessons/authored/batch-2/
titrations.dc.html`'s `endConnects` links forward to `['salts-
neutralisation', 'Salts and neutralisation']`. Same pattern as batch-10's
carbon-cycle→deforestation link and batch-6/batch-8's forward links — real
links to pages that do not yet exist. **A second genuine finding: three of
this batch's atomic-structure figures already exist, but in `figlib/
physics.py`, not `figlib/chemistry.py`** — physics draws them for its own
radioactivity/atomic-structure topic, and they are exact content matches for
this batch's chemistry lessons of (almost) the same name.

| # | Lesson | Existing drawing code that already covers it |
|---|---|---|
| 1 | model-of-the-atom | **Direct match, cross-subject:** `figlib/physics.py:1497 history_of_atom()` — "Three-panel strip: plum pudding → nuclear (Rutherford) → Bohr" — exactly this lesson's model-history content, drawn for physics' atomic-structure topic. |
| 2 | subatomic-particles | **Direct match, cross-subject:** `figlib/physics.py:1390 atom_diagram(symbol, protons, neutrons)` — nucleus-plus-shells diagram parameterised by proton/neutron count, exactly this lesson's p/n/e content. **Reusable, JS:** `shared/ks4-diagrams.js:54 atom(cx, cy, sym, shells, opt)` draws the same shell structure for bonding diagrams. **KS3 bench:** `ks3_art/c8.py:1213 r_shell_strip()` — "eight dots a row, `n` of them filled" — shows electron count only (outer shell, deliberately not shells-within-shells), a simpler slice of the same content. |
| 3 | relative-atomic-mass | **Direct match, cross-subject:** `figlib/physics.py:1455 isotope_notation(symbol, mass, atomic, name)` — an isotope notation card (e.g. Carbon-14), exactly this lesson's isotope-labelling content. **Figure still needed:** nothing draws the weighted-mean Ar CALCULATION itself (the `Σ(% abundance × mass number) ÷ 100` arithmetic) — see below. |
| 4 | electronic-structure | **Direct match:** `figlib/chemistry.py:934 electronic_configuration(symbol)` — full shell-filling diagram for any element H–Ca (Z=1–20), exactly this lesson's content and range. **Reusable, JS:** `shared/ks4-diagrams.js:54 atom()` (cited under #2). **KS3 bench:** `ks3_art/c8.py:1213 r_shell_strip()` (cited under #2) — outer-shell count only, a simpler companion. |
| 5 | group-7 | **Direct match, KS3 bench:** `ks3_art/c8.py:1038 r_halogen_grid()` — "three halogens against three halide solutions" — exactly this lesson's displacement-reaction content ("will it displace?"), every cell authored not composed. No figlib figure found for halogen displacement specifically. |
| 6 | transition-metals | **Reusable, contingent, three pieces:** `figlib/chemistry.py:1181 reactivity_series()` — vertical reactivity ladder — frames the whole series, not transition-metals-vs-Group-1 specifically; `ks3_art/c8.py:893 r_water_trough()` — "three metals, one trough, one at a time" — the Group 1 side of the contrast (Li/Na/K in water); `ks3_art/c9.py:182 r_reaction_audit()` — "six metals down, two liquids across, twelve cells" — a broader reactivity grid including transition metals as the low-reactivity end. None of the three classifies transition-metal PROPERTIES (density, melting point, variable oxidation state, coloured compounds, catalytic use) against Group 1 directly — that figure is still needed. |
| 7 | mass-changes-reactions | **Direct match, two pieces:** `figlib/chemistry.py:1271 conservation_sealed()` — "sealed conical flask on a balance (mass unchanged)" — exactly the closed-container half of this lesson; `figlib/chemistry.py:1318 gas_syringe()` — open-container gas-escape measurement, exactly the open-container half. Also see the Method note above: `conservation-of-mass.dc.html` already forward-links to this exact slug. |
| 8 | chemical-measurements | None found anywhere searched. No burette/pipette/measuring-cylinder apparatus drawer exists in `figlib` or `ks3_art` — the only place a burette or pipette is drawn at all is inline inside `ks4_lessons/authored/batch-2/titrations.dc.html`'s own markup, not as a reusable function. |
| 9 | moles | None found anywhere searched for the mole/Avogadro-constant content. See the Method note above: `using-moles-calculations.dc.html` already forward-links to this exact slug. |
| 10 | amounts-in-equations | None found anywhere searched for molar-ratio/percentage-yield/atom-economy content. See the Method note above: BOTH `conservation-of-mass.dc.html` and `using-moles-calculations.dc.html` already forward-link to this exact slug. **Near-hit checked and ruled out:** `ks3_art/c3.py:741 r_crystal_bench()` ("three solutes × three methods, and one yield") is a genuine yield concept but is about SEPARATION/crystallisation yield (MIX-09: "faster evaporation gives more product"), not reacting-mass percentage yield — different mechanism entirely. |
| 11 | oxidation-reduction | **Reusable, contingent:** `ks3_art/c5.py:1355 r_rust_stop()` — "five ways to stop it, and one of them is not" — iron rusting is ONE example of oxidation, but the bench is about prevention methods, not the general gain/loss-of-electrons (OIL RIG) classification; `figlib/chemistry.py reactivity_series()` (cited under #6) is reactivity, not redox specifically. No figure found that classifies a reaction as oxidised/reduced by electron transfer directly. |
| 12 | salts-neutralisation | **Direct match, KS3 bench:** `ks3_art/c6.py:1202 r_salt_namer()` — "three acids, four bases, twelve salts" — exactly this lesson's acid+base→salt naming content, generated by the same `base.metal + acid.ending` rule this lesson teaches. **Reusable, contingent:** `ks3_art/c6.py:728 r_titration_dial()` — a pH-cliff titration instrument, related but a different (Triple-only) technique from this lesson's RP3 (making a soluble salt by add-excess-solid). Also see the Method note above: `titrations.dc.html` already forward-links to this exact slug. |
| 13 | ph-scale | **Direct match, two pieces:** `figlib/chemistry.py:1225 ph_scale()` — "0–14 pH scale with acid/neutral/alkali zones" — and `figlib/biochem.py:303 ph_strip()` — fifteen equal pH cells with a pointer, pastel tints, no acid/alkali/neutral words — both generic and exactly this lesson's content. **KS3 bench:** `ks3_art/c6.py:548 r_ph_bench()` — "pick a sample, BAND THE GUESS, then test it" — the same scale as a guess-then-test KS3 instrument. |
| 14 | strong-weak-acids | None found anywhere searched. No full-vs-partial-ionisation figure exists in `figlib` or `ks3_art` — strong/weak acid dissociation is Triple-only content with no KS3 precursor. |
| 15 | electrolysis-principles | **Direct match:** `figlib/chemistry.py:1068 electrolysis(setup=...)` — a labelled electrolysis-cell diagram, generic across all four authored setups (see #16 and batch-12 #1–#2) — this is the general-principles lesson, so any one setup illustrates it. |
| 16 | electrolysis-molten | **Direct match, exact setup:** `figlib/chemistry.py` `ELECTROLYSIS["molten_PbBr2"]` via `electrolysis(setup="molten_PbBr2")` — the dict's own cathode (`Pb²⁺ + 2e⁻ → Pb`) and anode (`2Br⁻ → Br₂ + 2e⁻`) match this lesson's molten lead bromide demonstration — not a required practical; the electrolysis RP is aqueous, Combined RP9 / Chemistry RP3 — (electrolysis of lead(II) bromide) exactly, same substance and the same fume-cupboard/bromine-toxicity safety note. |

## Figures still needed

1. **model-of-the-atom** — none needed; `history_of_atom()` already covers it directly (cross-subject reuse from physics).
2. **subatomic-particles** — none needed; `atom_diagram()` / `shared/ks4-diagrams.js atom()` already cover it directly.
3. **relative-atomic-mass** — a weighted-mean bar figure: two (or more) isotope bars at their abundance%, with the Ar arithmetic worked alongside, distinct from `isotope_notation()`'s single-isotope card.
4. **electronic-structure** — none needed; `electronic_configuration()` already covers the full H–Ca range directly.
5. **group-7** — none needed; `r_halogen_grid()` already covers displacement directly (a KS4-styled static version would still help for visual consistency with the rest of the pack).
6. **transition-metals** — a transition-metals-vs-Group-1 property-contrast figure (density, melting point, reactivity, catalytic use, coloured compounds), the one genuinely missing figure for this lesson.
7. **mass-changes-reactions** — none needed; `conservation_sealed()` and `gas_syringe()` already cover both the closed- and open-container cases directly.
8. **chemical-measurements** — a labelled apparatus figure: burette, pipette and measuring cylinder side by side with their precision/uncertainty, the one genuinely missing figure for this lesson.
9. **moles** — a mole/Avogadro-constant figure: a counted particle grid scaled by Nₐ, or a simple n=m÷Mr balance-style figure.
10. **amounts-in-equations** — a molar-ratio "scaling" figure (balanced-equation coefficients as a bar/ratio diagram) distinct from the crystallisation-yield near-hit ruled out above.
11. **oxidation-reduction** — an electron-transfer (OIL RIG) figure: two half-reactions side by side, one losing electrons (oxidised), one gaining them (reduced), distinct from `r_rust_stop()`'s prevention framing.
12. **salts-neutralisation** — none needed for naming; `r_salt_namer()` already covers it directly. A soluble-salt RP (Combined RP8 / Chemistry RP1) add-excess-solid apparatus sequence (excess copper oxide stirred into acid, filter, evaporate, crystallise) would complete the practical picture.
13. **ph-scale** — none needed; `ph_scale()` / `ph_strip()` / `r_ph_bench()` already cover this directly from three angles.
14. **strong-weak-acids** — a full-vs-partial-dissociation figure: HCl splitting completely into ions vs CH₃COOH's equilibrium arrow, the one genuinely missing figure for this lesson.
15. **electrolysis-principles** — none needed; `electrolysis()` already covers a generic labelled cell directly.
16. **electrolysis-molten** — none needed; `electrolysis(setup="molten_PbBr2")` already covers this molten lead bromide set-up (a demonstration, not a required practical).
