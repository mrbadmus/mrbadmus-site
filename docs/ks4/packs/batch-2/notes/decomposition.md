# Decomposition — lesson notes (batch-2)

## Lesson record

```python
dict(slug="decomposition",
     source_file="decomposition.dc.html",
     subject="biology", topic_id="ecology",
     title="Decomposition",
     spec="4.7.2.2",            # base slice; Triple layer is 8461 4.7.2.3 + RP10
     family="Required practical",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

Spec, per the examination (§1): base content is the last sentence of **4.7.2.2** (both
specs); everything else is **8461 4.7.2.3 (biology only)** with **8461 RP10**. 8464 has no
4.7.2.3 and no decay practical. The pack header "4.7.3" is wrong (that is Biodiversity).
Eyebrow and key-note spec are computed per route: `(8464) 4.7.2.2` on Combined;
`(8461) 4.7.2.2–4.7.2.3 · Required practical` / `· RP10` on Triple. The `spec` field above
holds the base number; the commander may prefer "4.7.2.2–4.7.2.3".

## Family, and why

**REQUIRED PRACTICAL** on Triple routes (as BATCH-PLAN proposed): RP10 is the flagship
and its 6-mark method is rung 4. On Combined routes there is no practical, so the page is
honestly small: hook → explainer → the "follow the leaf" PROCESS instrument → misconception
→ ladder. The Combined eyebrow carries no family word, and the RP and "Contains Triple"
pills render on Triple routes only (`sc-if isTriple`, the R9 pattern), so no Combined pupil
is told about a practical that is not theirs. Line-up differs from both enzymes and
resistors (a process stepper, a compost sort, a continuous colour end-point judged by eye).

## Activities and the demand each trains

| block | route | size | demand |
|---|---|---|---|
| Hook `Ks4Choice` (a fallen leaf disappears) | all | micro | commit to where the carbon goes (unscored) |
| **Follow the leaf** (`s-cycle`, new, in-lesson) | all | M | PROCESS: three predicted steps — what decomposers do with digested food (respiration), where mineral ions go (soil), who takes both back (a plant) — each animated (leaf shrinks, CO₂ rises then enters leaves, nitrate sinks then enters roots); wrong picks get named corrections and the true step plays |
| Spot the flaw (`s-think`) | all | micro | add the missing marking point: respiration, not "eating" |
| Explainer: temperature, water, oxygen; compost; methane; biogas | triple | — | |
| Compost `Ks4Sort` (`s-compost`) | triple | M | classify six gardener's choices as speed up / slow decay (incl. sealed bin → anaerobic, methane; frost slows, does not kill) |
| **RP10 flagship** (`s-rp` + `s-sim`, new, in-lesson) | triple | L | predict-gated (drawn time-vs-temperature thumbnails); five water-bath temperatures; the tube fades pink → white as the stopwatch runs (animated; reduced motion steps 30 s at a time); the pupil judges the end point and stops the clock (stopping while still pink is refused with the end-point rule); 60 °C never clears (denatured); then rate = 1 ÷ time at 40 °C from their own time, the graph from their data, and a Suggest-an-improvement choice |
| Spot the flaw (`s-pink`) | triple | micro | why the pink goes: lipase → fatty acids → pH falls (not bacteria) |
| Equation block + `Ks4Cfifa` | triple | — | rate of decay = mass lost ÷ time; rate = 1 ÷ time (both Learn it); days→weeks and kg→g conversions |
| Ladder (Combined) | CF, CH | — | r1 Name (authored, 1), r2 Identify (data, 3), r3 Explain chain (3), r4 Explain (4, points) |
| Ladder (Triple) | TF, TH | — | r1 Give (verbatim q2), r2 Calculate (TF 80→50 g in 6 weeks; TH 260→176 g in 42 days), r3 Explain chain (compost holes), r4 Describe RP10 method (6, levels) |

## Misconceptions and where each is confronted

| misconception | where |
|---|---|
| "Decomposers eat it" with no respiration | `s-think`, straight after the stepper shows respiration releasing CO₂; base r4 reject list |
| Decomposers photosynthesise | stepper gates 1 and 3; base r3 herring; triple r3 herring |
| Matter/minerals destroyed on rotting | hook reply; stepper gate 2; base r3 herring |
| Cold kills bacteria | compost sort (frost) ; verbatim q2 wx2 in the bank; triple r1 `why` |
| Sealed bin makes good compost | compost sort item (anaerobic, slower, methane) |
| Milk goes acidic because of bacteria (RP10) | `s-pink`, immediately after the practical |
| Indicator goes colourless → pink | RP method wording, `pinkReveal`, triple r4 reject list |
| Rate reported as time | gate thumbnails are time graphs; result text "a time graph dips where a rate graph would peak"; rate column after processing |

## Route tags (every one is `triple`, 8461 4.7.2.3 / RP10, "biology only")

| element | tag | citation |
|---|---|---|
| explainer (temperature, water, oxygen, compost, anaerobic → methane, biogas) | `data-route="triple"` | 8461 4.7.2.3 |
| `s-compost` sort | triple | 8461 4.7.2.3 (gardeners/compost; anaerobic decay) |
| `s-rp` RP10 block | triple | 8461 RP10 |
| `s-sim` flagship | triple | 8461 RP10; 4.7.2.3 "calculate rate changes … translate numerical/graphical" |
| `s-pink` misconception | triple | 8461 RP10 (lipase: 4.2.2.1 base, but this context is RP10) |
| `s-equation`, `s-calc` | triple | 8461 4.7.2.3 "calculate rate changes in the decay of biological material" |
| header pills, eyebrow, big question tail, key-note lines 5–7, legal tail, command words 3–5, rungs, rail | logic on `R.isTriple` | same |

Base (all routes): hook, explainer 1, `s-cycle`, `s-think`, key fact, key-note lines 1–4 — all 4.7.2.2.
The examination's R11 note (old `higher` field was Triple content mis-tagged as Higher) is
honoured: nothing here is HT; TF gets the full Triple layer. 4.7.2.4 (HT, biology only) is
not in this lesson.

## ⚑ Net-new science-bearing items

1. ⚑ Hook (leaf vanishes; carbon leaves as CO₂ via microbial respiration) — 4.7.2.2.
2. ⚑ Stepper copy and replies (respiration not photosynthesis; nitrate ions into soil water; plant takes CO₂ for photosynthesis and ions through roots) — 4.7.2.2; plant uptake of nitrate: 4.4.1.3.
3. ⚑ Spot-the-flaw options (combustion / photosynthesis / evaporation) and reveal.
4. ⚑ Triple explainer re-cut from theory 2–3 per examination C6, C7 (optimum, not "~40 °C"), C9; peat and pH dropped (C10/C11 — not spec factors).
5. ⚑ Compost sort items and reasons.
6. ⚑ RP10 method volumes (5 cm³ milk, 7 cm³ sodium carbonate, 5 drops phenolphthalein, 1 cm³ lipase), variables and risks — examination §5 handbook values ("from memory, indicative").
7. ⚑ Simulated model: time for pink to clear 430/260/150/230 s at 20/30/40/50 °C; denatured at 60 °C (pink stalls at 55%) — matches examination "time falls to ~35–45 °C, then rises; 60 °C may not change".
8. ⚑ `s-pink` reveal: lipase → fatty acids and glycerol (4.2.2.1), pH falls, phenolphthalein pink → colourless.
9. ⚑ Improvement choice (more temperatures between 30 and 50 °C).
10. ⚑ rate of decay = mass lost ÷ time and all CFIFA/r2 numbers.
11. ⚑ Both ladders' r1 (Combined, authored), r2–r4 marking points and levels (from examination §5 typical questions).
12. ⚑ Key-note lines 3–7 are authored; lines 1–2 are the verbatim source key note ("Decomposers = bacteria and fungi." "Recycle nutrients, complete carbon cycle.").

## Frozen items flagged wrong, and handling

| item | verdict | handling |
|---|---|---|
| `rp` "RP7 — bread … mould … respirometers" | WRONG number, method and route (C21) | Not displayed anywhere. RP block written from 8461 RP10 (milk, lipase, pH change), Triple only. Its bread-mould method is a named reject in triple r4. |
| q2 (refrigerator) on CF, CH | wrong route (4.7.2.3 content) | Used as r1 on TF/TH only; never a rung on CF/CH. Stays in the CF/CH practice bank verbatim (the route's frozen quiz, pilot flag-7 precedent). Commander: consider removing from Combined copies. |
| q1 (decomposers vs detritivores) | not in either spec | Never a rung; stays in the bank verbatim on all routes. |
| key_note lines 3–5 (detritivores; "higher temperature … neutral pH"; uses) | NOT-IN-SPEC / IMPRECISE (C17) | Not used; key-note lines authored instead (pilot keyLines precedent). |
| `higher` field | mis-tagged (Triple, not HT) | Not rendered; its content is taught in the Triple layer. |
| theory: detritivores, pH, peat, food preservation, sewage | NOT-IN-SPEC / other spec | Cut. |
| examiner tip | none in source | slot omitted |

## New instruments / helpers

All in the lesson's own Component logic; no `_ext` file.
- "Follow the leaf" stepper: `cycFigure` (scene with soil band, dead leaf, plant with roots; progress per step drives positions; reduced motion jumps to the end state).
- RP10 bench: `pinkAt` (linear fade model, denaturing stall at 60 °C), `tube` (colour interpolated pink → milk white, swirling stirrer, thermometer, stopwatch dial), `rig`, `thumb`, `plot` (time vs temperature from the pupil's own times).
- Route-dependent rail (`RAIL_BASE` 4 nodes / `RAIL_TRIPLE` 8 nodes), chosen in `componentDidMount`.

## Body prose word count

Hook 28 + explainer 1 (43) on every route = **71 words** on Combined; plus the Triple
explainer (71) = **142 words** on Triple (RP method, variables and risks ≈ 170 words more).
