# Batch 5 — science log

Every science decision made while porting Design's batch 5 (15 lessons), with its source. Design's lesson files stay
byte-identical on disk (`docs/ks4/design-reference/batch-5/`, `MD5SUMS`). Changes are NAMED rulings in
`ks4_batch_rulings.py` (`SCIENCE`), applied at compile time, each failing the build if its target text is not found
exactly once. "Pack" = `docs/ks4/packs/batch-5/` (`FLAGS.md`, `04-checked-science-source/`, `examination/`).
Rulings were made by the lead (Prompt AB, 8 Oct 2026, audit of the delivery); the builder applied them verbatim.

## Rulings applied (six, plus one port mechanic)

| id | lesson | layer | decision | source |
|---|---|---|---|---|
| B5-ER-SPEC | earths-resources | template | "Sustainable development" card now carries the spec sentence verbatim (8464 5.10.1.1 / 8462 4.10.1.1) in place of Design's paraphrase. | lead's lane ruling 8.3; `examination/earths-resources.md:15` |
| B5-ENR-F6 | energy-resources | logic | Quiz 2, wrong-answer reply 2 (shown on "too much electricity at peak times"): "intermittent" means VARIABLE, WEATHER-DEPENDENT output, not "UNPREDICTABLE" (tides are predictable and not intermittent in the sense that matters). | FLAGS ENERGY-RESOURCES-F6; consistent with wx1's wording |
| B5-ENR-LABEL | energy-resources | template | The trends chart is labelled where the pupil reads it: "This country is made up and its figures are not real data." | lead's lane ruling 4.2 (keep the made-up country, label it) |
| B5-PT-F6 | plant-tissues | logic | The concession that stomata can absorb water vapour is dropped; the reply now says stomata are pores for gas exchange and water enters through the roots. (It contradicted rung 4's own reject, "Stomata take in water.") | FLAGS PLANT-TISSUES-F6 |
| B5-MNM-B | metals-non-metals | logic | Element picker: boron (3 outer electrons) reads "3 outer electrons, but boron is a non-metal", as hydrogen's line already does, because the page has just said metals have 1, 2 or 3. | lead's lane ruling 2.2 |
| B5-MNM-H | metals-non-metals | logic | Element picker: hydrogen's info head reads "not in a group" instead of "Group 1", matching the page's "hydrogen sits on its own at the top". | lead's lane ruling 2.2 |
| B5-RSBB-CHIP | red-shift-big-bang | logic | **Port mechanic, not science.** Its `renderVals` returns a fresh object instead of spreading the route helper, so the one route chip (B-R12) had no words or menu. Same repair as batch 4's B4-IRB-CHIP. | engine |

Each applied exactly once (the build would have stopped otherwise). Visible in the built pages: ER-SPEC, ENR-LABEL,
MNM-B, MNM-H in the rendered DOM at 390 px; ENR-F6 and PT-F6 in the rendered reply after pressing the wrong option
(ENR-F6: quiz question 2, third option; PT-F6: quiz question 3, first option) on CF and TH.

## Kept as Design wrote it

- **Football analogy kept: 0.30 m × 10 000 = 3 km diameter to diameter, pack examination C5 OK.** Structure of an
  atom says an atom is "at least 3 km across" against a football-sized nucleus; the sum is right (nucleus less than
  1/10 000 of the atom), so nothing was changed.
- **Lane rulings 3.2, 4.2, 7.2, 14.2 kept.** 3.2 (reactivity: K, Na, Li, Ca with acid shown as "not done: too
  violent; its place comes from the water test"), 4.2 (energy resources: made-up country; its label is B5-ENR-LABEL
  above), 7.2 ("acid rain falling on land and into lakes is one way", waste management) and 14.2 ("radiation goes
  out in all directions" as the reason count-rate is below activity, radioactive decay) are Design's wording and
  stand unchanged.
- Design's other numbered flags (NOTES-KS4-batch-5.md) were resolved by Design in the delivery; none was reopened.

## Frozen content

None of the 15 slugs is a frozen-correction slug (`docs/ks4/FROZEN-CORRECTIONS.md`); this branch touches no
`all_subtopics_*.py`. The batch is frozen after build (`ks4_lessons/frozen_batch-5.json`), `review_state`
`examiner-reviewed`, draft banner off, as batch 4.

## Fixes from the independent pupil walk (lead, 8 Oct 2026)

| id | lesson | change | why |
|---|---|---|---|
| ext SVG subscripts | plant-tissues, land-use | `ks4-ext-batch-5.js` now writes an SVG `<tspan baseline-shift="sub">` inside figure labels instead of an HTML `<sub>`, which SVG does not draw. Batch 4's ext is unchanged (none of its figure labels carries a subscript). | The leaf figure read "CO in" (carbon monoxide) instead of "CO₂ in"; land-use's "CO₂ released" had the same fault. |
| B5-RS-CAP-1/2 | reactivity-series | Displacement feedback capitalises the metal's name at the start of its sentence. Words unchanged. | "Not this time. copper is less reactive…" |
