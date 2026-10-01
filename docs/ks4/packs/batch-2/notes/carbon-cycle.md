# carbon-cycle — author's notes (batch-2)

## Lesson record

```python
dict(slug="carbon-cycle", source_file="carbon-cycle.dc.html",
     subject="biology", topic_id="ecology",
     title="The carbon cycle", spec="4.7.2.2", family="Process",
     routes=["CF", "CH", "TF", "TH"], review_state="draft", batch="batch-2",
     block_map={"s-trace": "worked-example", "s-label": "check"})
```

`block_map` is needed: `s-trace` and `s-label` are lesson-built sections with no
single block import, so `classify_section` cannot infer them. Checked through
the real compile path in a scratch build: all 12 sections classify.

Spec: AQA 8461 4.7.2.2 = 8464 4.7.2.2 (identical text). The human-impact
explainer draws on 4.7.3.4 (deforestation) and 4.7.3.5 (global warming), both
base. The pack header's "4.7.3" is wrong (examination §1); the page uses 4.7.2.2.
The eyebrow and key-note spec are route-aware: "(8464)" on Combined, "(8461)" on
Triple, the same pattern as the pilot's D13 SPEC_TEXT.

## Family: PROCESS, and why

The architecture names the carbon cycle as its example PROCESS lesson. The
demand is a mechanism that unfolds in steps. AQA tests it as "name the process
at arrow X" and "describe the route of a carbon atom". So the flagship is a
worked stepper with predictions, and then the pupil builds the same cycle
(labels every arrow). BATCH-PLAN's provisional family is confirmed.

## Instruments and the demand each trains

- **Flagship (L) — "Follow one carbon atom"** (`s-trace`). Six predict-gated
  steps in two journeys: air → plant (photosynthesis) → rabbit (feeding) → dead
  matter (death and waste) → air (decomposers respire), then a fern 300 million
  years ago → coal (fossilisation) → air (combustion). The pupil commits to a
  process at each store, and only then does the arrow light, take its name and
  the atom animate along it (SMIL `animateMotion`; with reduced motion the atom
  is placed at the end of the arrow). Arrows not yet followed stay faint and
  unnamed. Every distractor is a named misconception with corrective feedback.
  Demand: sequence the processes and say which one moves carbon between which
  stores.
- **Mid-size 1 — "Name the process at every arrow"** (`s-label`). The full
  cycle with nine lettered arrows; one `<select>` per arrow, 7 process names.
  B and D (respiration by plants and by animals) were never travelled in the
  trace, so they have to be worked out, not remembered. A/B are a deliberate
  direction trap (two arrows between air and plants). A wrong label gets that
  arrow's own note. Demand: AQA's "interpret and explain the processes in
  diagrams of the carbon cycle" (production of the process name).
- **Mid-size 2 — Ks4Sort "What does it do to the air?"** (`s-sort`): adds CO₂
  / takes CO₂ / moves carbon not via the air. Seven processes, including
  deforestation and burning petrol. Demand: classify each process by its net
  effect on the air, which is the basis of the deforestation and fossil-fuel
  explain questions.
- **Micro — predict-trap** (`s-plants`, Ks4Choice inside the misconception
  block): a bean plant sealed in a jar in the dark.

No CFIFA, no equation block and no RP: there is no calculation, and no required
practical belongs to 4.7.2.2. RP7 (8464) / RP9 (8461) is field sampling, 4.7.2.1.

## Misconceptions and where each is confronted

| misconception | where | form |
|---|---|---|
| "Animals take in carbon as CO₂" (examination §5) | trace step 2, the moment carbon first enters an animal | distractor "As carbon dioxide from the leaf", then a three-beat Think-again panel |
| "Decomposers release CO₂ by decomposing" with no respiration (examination §5) | trace step 4, the moment carbon leaves dead matter | three-beat panel: "the mark is in the how" |
| "Plants take CO₂ in and don't give it out" (pack `common_mistake`) | `s-plants`, straight after the trace and before arrow B has to be labelled | quote, then a predict-trap; the reveal is the common_mistake re-cut |
| Arrow-direction errors (photosynthesis arrow pointing to the air) | `s-label`, arrows A/B | the per-arrow feedback names the direction |
| Carbon atoms destroyed by decay or burning | hook distractor, trace steps 3, 5 and 6, rung 3 red herring | feedback |
| "Burning turns carbon into energy" | trace step 6 distractor | feedback |
| Deforestation "only matters if burned" | bank q2, explainer 2, sort card | verbatim quiz feedback |

## Command words

Name (rung 2, labelling), Describe (rungs 1 and 4), Explain (rung 3). All three
are taught in the command-word block.

## Ladder

- r1: `K.find(slug, R.route, 'deforestation affect')`, which is quiz q2,
  verbatim, under Describe, 1 mark. It resolves on its own route on all four
  routes (the quiz is identical on every route), so there is no rung-1 fallback.
  The scratch build ran `check_rung1_fallback` and it printed no warnings.
- r2: `kind: 'data'`, Name, 2 marks: a new pond diagram (algae, fish, dead
  remains), arrows X (feeding) and Y (respiration by microorganisms).
  The shape is from the examiner's typical question.
- r3: chain, Explain, 3 marks: an apple core on a compost heap returned to the
  air. Two red herrings: atoms destroyed, and the core photosynthesising.
- r4: 6-mark Describe, levels of response. Indicative content is the
  examiner-drafted route from air to animal and back (examination §5).

## Route tags

None. Every point taught is base. 4.7.2.2, 4.7.3.3–4.7.3.5 and 4.4.2.1 carry
no HT and no "biology only" label (examination §2). The pack's `higher` field
(human impact, CH/TH only) is **WRONG ROUTE**. Its content is taught to all
four routes in the second explainer and the sort. Its last sentence
("short-term vs long-term geological cycle") is not in the spec and is not
taught.

## ⚑ Net-new science-bearing items

- ⚑ Hook: "A leaf that drops in autumn has mostly vanished a year later": soft
  wording on purpose, because leaf-litter decay rates vary.
- ⚑ Trace step texts and reveals: glucose → starch, cellulose and protein
  (4.4.1.3); feeding as carbon compounds; coal from ancient plants, and oil
  and gas from tiny sea organisms (chemistry 5.7.1.1, examination C10);
  burial in mud before decay as the condition for fossilisation. The last one
  is a GCSE-level simplification and is worth the examiner's eye.
- ⚑ Trace step 5 distractor: "Limestone formed from the shells of sea
  creatures, not from plants" (chemistry 5.9.1.4).
- ⚑ Explainer 2: "For most of history, carbon dioxide was taken out of the air
  about as fast as it was put back." This is a framing sentence not in the
  frozen text; it is consistent with theory 2's "faster than natural processes
  can remove it". Cut it if the examiner prefers.
- ⚑ The plants-in-a-jar predict-trap: in the dark only respiration happens, so
  CO₂ rises (4.4.2.1; common_mistake).
- ⚑ Key fact; command-word definitions; every distractor reply; rung 2–4
  marking points and levels (examiner-drafted shapes, written out by me).
- ⚑ One line added after the verbatim key note: "Feeding passes carbon
  compounds along food chains; it does not move carbon dioxide." Examination
  C18 asks for feeding to be added. The four verbatim key-note lines come from
  `K.keyLines(slug)` unchanged.

## Frozen items

- No quiz item is wrong for its route (examination §4). Both are used: q2 is
  rung 1, and both are in the bank.
- The q2 key (rung 1) is the longest option, a length-parity tell. It is
  frozen, so it is kept verbatim; flagged here for the bank's next re-freeze.
- The `higher` field: wrong route, handled as above. It is not displayed as
  Higher.
- The matching activity is replaced by the labelling activity and the sort.
- Oceans, volcanoes, cement and acidification are correct but not in the
  biology spec (R5, R7). They are not taught; the legal line says oceans,
  rocks and volcanoes are left out and taught in chemistry. The verbatim key
  note still names "dissolution in oceans" and "volcanic activity". Those
  lines are kept, and the explainer covers them with "Oceans and rocks hold
  carbon too, and you meet those in chemistry."

## New instruments and helpers

All of them live in the lesson's own Component logic; no `_ext` file. The
carbon-cycle diagram (STORES/ARROWS tables; `arrowSvg`, `storeSvg`, `tag`,
`halo`, `traceSvg`, `labelSvg`) and `pondSvg` are built from the `KS4D`
primitives (`svg`, `T`, `line`, `arrow`, `circ`) on the cream plate, in the
house stroke weights and with Georgia labels.

## Word count

About 340 words of template body prose, plus about 330 words of step text and
reveals in the trace. That is about 670 in total, under the ~700 budget. No
run of prose before a commitment exceeds 150 words (the longest is explainer 2,
85 words).

## Checks run

Built through `build_ks4`'s own `compile_batch_lesson` + `render_page` in a
scratch harness. Nothing was written into the worktree. All 4 routes load with
zero console errors at 390 and 1280 px. There is no `undefined`, `NaN` or
`[object Object]` before or after a scripted pass (all six trace steps,
including wrong picks and both confront panels, the plant trap, a wrong label
corrected to "All nine right", ladder rendered). Screenshots were inspected at
390 px. Dark mode was not checked visually; the page uses only `--ks3-*`
tokens, and the figure plates are cream in both themes, as in the pilot.
