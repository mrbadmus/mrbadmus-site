# waves-detection-exploration — author's notes (batch-3)

## Lesson record

```python
dict(slug="waves-detection-exploration", source_file="waves-detection-exploration.dc.html",
     subject="physics", topic_id="waves",
     title="Waves for detection and exploration", spec="8463 4.6.1.5",
     family="Investigation", routes=["TH"], review_state="draft", batch="batch-3",
     block_map={"s-quake": "practical", "s-scan": "practical"})
```

`block_map`: the two bespoke benches (`s-quake`, `s-scan`) have no import and a
`{{ …Fig }}` binding, so the heuristic would call them "figure"; mapped to
"practical" as the pilot's circuit bench and the batch-2 lens bench are. All
other sections classify on their own. No `withhold`: the examination finds no
frozen item wrong (§4).

Spec: AQA 8463 **4.6.1.5** Waves for detection and exploration (physics only,
HT only). Not in 8464. The pack's "6.6.1.5" is wrong (examination §1).
Eyebrow "AQA Physics (8463) 4.6.1.5 · Investigation"; key note "AQA 4.6.1.5
(8463)". Ships on **TH only**: no `data-route` tags, the head carries the route
chip only.

⚠️ **Cross-slug read.** Ex. 1 of the CFIFA is the SONAR FIFA, which is frozen
under `sound-waves-hearing` (examination C18 and §4 move it here). The logic
reads it with `K.fifas('sound-waves-hearing')[0]`, which works because both
lessons are in batch-3 and share `ks4-source-batch-3.js`. A literal copy of the
same verbatim object (`SONAR`) is the fallback if that record is ever not on
the page. If batch-3 is split, keep the two lessons in one batch or this
example falls back to the literal (same text).

## Family: INVESTIGATION, and why

The spec's demand is to "explain … how differences in velocity, absorption and
reflection … can be used for detection and exploration of structures which are
hidden from direct observation", with WS 1.1 (new evidence). The skill is
evidence → model: test a hypothesis against data, revise the model, then use
timing data to locate a hidden boundary. BATCH-PLAN's provisional family is
confirmed. (MODEL was considered — the flagship has regime changes — but the
pupil never controls a parameter freely; every step is "which hidden structure
fits these records".)

## Line-up

hook (Ks4Choice, nobody has seen the core) → video → explainer (P and S) →
**seismic bench (L)** → explainer (new evidence, WS 1.1) → **P/S/both sort
(M1)** → explainer (ultrasound) → **ultrasound scan (M2)** → explainer
(safety, industrial imaging, echo sounding) → equation (s = v t + the echo
step) → CFIFA → command words → key fact → ladder → key note → bank → end. No
exam-tip slot: the source has no `examiner_tip`. Different hook, flagship and
mid-size shapes from `sound-waves-hearing`.

## Instruments and the demand each trains

- **Flagship (L) — "Read the Earth"** (`s-quake`, new instrument, in-lesson
  logic). An Earth cross-section (layers to scale: outer core 0.546 R, inner
  core 0.19 R), an earthquake at the top and six seismometers at 30°–180°.
  Four predict-gated steps:
  1. *Test a solid Earth* — with the interior hidden, predict which stations
     would record S-waves if the Earth were solid throughout → curved S paths
     draw on to all six;
  2. *The real records* — P/S badges appear at each station (P everywhere but
     120°; S only to 90°); predict which hidden structure explains them (liquid
     layer / waves fade / hollow centre) → the Earth is cut open, S paths stop
     at the outer core with a ✕, the S shadow arc appears; misconception panel;
  3. *The P-wave gap* — predict why no P arrives at 120° → P paths draw on,
     the ones entering the core bend at its boundary and land at 140°+, the
     grazing one lands before 104°; P shadow arc;
  4. *How big is the core?* — predict where the S shadow would start for a
     bigger core → a dashed bigger core and its grazing S path landing at ~78°.
  A key under the figure (HTML, phone-legible) names the layers, badges and
  shadow arcs. Rays draw on (SMIL stroke-dash, 1.4 s); reduced motion shows
  them complete. Demand: use wave data to infer the structure and size of the
  core (R2, R3) and why the evidence is new (R4).
- **M1 — P-wave, S-wave or both?** (`s-sort`, Ks4Sort, 8 cards, 3 bins).
  Demand: discriminate P and S properties. Word shape checked: "liquid" and
  "travel" appear in P and S cards; "both" cards share no keyword.
- **M2 — the ultrasound scan** (`s-scan`, new instrument). A probe on four
  layers (fat, muscle, fluid, fetus; boundaries A, B, C at 2, 5, 8 cm) and an
  echo trace. Step 1: predict how many echoes return (one / three / none) → a
  pulse travels in, a smaller pulse reflects back from each boundary and each
  spike appears on the trace when its echo arrives (SMIL; reduced motion
  shows the final trace). Misconception panel. Step 2: "Use the trace" — how
  deep is C compared with A (×2 / ×4 / ×8) → a depth scale appears. Demand:
  partial reflection at boundaries and time → distance (R1).
- **CFIFA** (s = v t, then the echo halving). TH only, so one tier of numbers:
  worked 1 = the SONAR FIFA, **verbatim** via `K.cfifa` with "Nothing to
  convert: the time is in s and the speed in m/s." in front; worked 2 = 0.080 ms
  → s, 1540 m/s in tissue → 0.062 m (note: unconverted gives ~62 m);
  attempts: fish shoal 0.12 s at 1500 m/s → 90 m (nothing to convert); crack in
  steel 0.020 ms at 6000 m/s → 0.060 m (convert). The examination's own advice
  (§5): SONAR FIFA as the nothing-to-convert example, an ms → s second.
- **Equation block**: s = v t "On the sheet" (printed on both June 2026 sheets;
  the spec lists it as recall, Appendix A eq 6 — labelled per the batch-2
  ruling, difference noted here); an "For an echo" card saying the halving is a
  method step, not an equation (examination C22); a ms → s units card. The
  frozen `equations` string "d = v × t / 2" is not rendered as an equation; it
  survives only inside the verbatim FIFA lines and the verbatim key-note line
  "Echo sounding: d = vt/2."

## Misconceptions and where each is confronted

| misconception | where | form |
|---|---|---|
| "S-waves can't pass through the core" (examination §5) | bench step 2, as the outer core is revealed | three-beat panel: the mistake → P-waves do pass, only the liquid outer core stops S → the correct sentence; r4 reject |
| S-waves just fade out with distance | bench step 2 distractor | correction: the edge is sharp and P still reaches 180°; r4 reject |
| P-waves cannot travel through a liquid | bench step 3 distractor; M1 | correction from the 150°/180° records |
| Seismic waves travel in straight lines | bench step 1 why, the drawn curves | why line + figure |
| "Ultrasound is completely reflected" (examination §5) | scan step 1 | three-beat panel; r3 herring |
| Forgetting to halve / ms not converted | scan step 2 distractors; CFIFA notes; r2 conversion choice | corrective replies and notes |

## Route tags (spec citations)

None. The whole lesson is 8463 4.6.1.5 "(physics only) (HT only)" and ships
on TH only. The pack's general absorb/transmit/refract/reflect block (theory 3,
8463 4.6.2.2 / 8464 6.6.2.2, EM, HT) is **not** taught here (owned by
`properties-em-waves-1`, examination R7); only mechanical-wave examples appear.

## Ladder

1. Recall · Give · 1 — frozen q1 via `K.find(slug, R.route, 'S-waves are not
   detected on the opposite side')` (TH). Length parity passes (key 15 words,
   longest distractor 16).
2. Apply · Calculate · 3 — ⚑ echo sounder, 160 ms at 1500 m/s → 120 m;
   conversion choice ms → s; unit m (km left out of the unit list so 0.12 km
   cannot be marked wrong).
3. Explain · Explain · 4 — ⚑ chain: how ultrasound finds a boundary's depth
   (examiner's 4-mark typical item, four links) with two herrings (total
   reflection; louder echo = deeper).
4. Produce · Explain · 6 — ⚑ "Explain how seismic waves provide evidence
   about the structure of the Earth": levels descriptor (examination §5),
   seven indicative points, two rejects.

## ⚑ Net-new science-bearing items

1. Hook text and replies ("thousands of kilometres", no drill near the core;
   lava comes from far nearer the surface than the core).
2. Explainer 1 (P/S properties from 4.6.1.5 and theory 1); explainer 2 (WS 1.1
   wording from the spec); explainer 3 (ultrasound definition, 4.6.1.5);
   explainer 4 (non-ionising — theory 2 of the sound pack, C11; industrial
   imaging — C12; echo sounding — spec).
3. Bench copy, all four steps; the drawn geometry: S shadow from ~104°, P
   shadow ~104°–140° (examination C7/C8 figures), P-waves slow on entering the
   outer core (refraction toward the normal is drawn), a bigger core moves the
   S shadow edge towards the earthquake (spec: evidence for the size of the
   core).
4. Bench misconception panel.
5. M1 sort cards and whys.
6. Scan figure and copy: layers, 1540 m/s, echo times 0.026 / 0.065 / 0.104 ms
   for 2 / 5 / 8 cm (checked: 2d ÷ 1540), weaker deeper echoes; scan panel.
7. CFIFA worked 2 and both attempts (speeds given as data: tissue 1540, sea
   water 1500, steel 6000 m/s). Arithmetic: 1540 × 0.000080 = 0.1232 → 0.0616;
   1500 × 0.12 = 180 → 90; 6000 × 0.000020 = 0.12 → 0.060; 1500 × 0.16 = 240
   → 120.
8. Rungs 2–4, marking points, levels, rejects.
9. Key-note line 4 (ultrasound; examination C21 asks for it); key fact;
   command-word definitions; legal line.

## Frozen items flagged wrong / imprecise, and how handled

| item | verdict | handling |
|---|---|---|
| q1, q2 | OK | q1 is rung 1; both in the bank. |
| theory 1 "P-waves are refracted (change speed) at the core boundary → core is DENSER than mantle" (C5) | IMPRECISE | Not displayed. The bench says the refraction marks a boundary and the shadow edges give the core's size. |
| theory 1 shadow-zone definitions (C7, C8) | IMPRECISE | Not displayed; the bench draws the two zones separately (S ~104°–180°, P ~104°–140°). |
| theory 2 glacier radar, oil surveying (C12, C13) | NOT-IN-SPEC | Not displayed. Key-note line "Seismic surveying: find oil layers." dropped for the same reason. |
| theory 3 absorb/transmit/refract/reflect (C14) | 4.6.2.2 EM content | Not taught here (see route tags). |
| `equations` "d = v × t / 2" (C22) | not an AQA equation | Equation card shows s = v t; halving shown as a method step. |

Sound-pack items taken into this lesson: the SONAR FIFA (verbatim, see the
cross-slug note). Sound q1 ("divide the echo time by 2") stays frozen to the
sound slug's bank and is not reused here, to avoid the same item appearing on
both pages; sound q2 is withheld (its wx2 is wrong).

**Bank size:** two items on TH, below content_standards §1's floor of 5. For
Mide's list.

## New instruments / helpers

`earthSvg` (with `pt`, `bez`, `stopAt`, `badge`, `arc`, `ray`, `xmark`) and
`scanSvg` live in the lesson's Component logic. No `_ext` file. Two tiny
lesson-scoped CSS classes for the figure key (`.wd-key`, `.wd-bar`).

## Word count

Hook 37 + explainers 65 + 48 + 56 + 73 = **279 words** of body prose; the
longest run before a commitment is 65 words.

## Self-check

Same scratch build as `sound-waves-hearing` (scratch clone, scratch
`batch_3.py` with the two lessons only): compiled, zero console errors at 1280
and 360 px. Headless-Chrome drive at 390 light and 1280 dark + reduced motion:
all four bench steps (right and wrong picks), sort solved, both scan steps,
both CFIFA attempts, all four rungs (Score 4 of 4); no `undefined`/`NaN`/
`null`/`{{`/`[object` text; no sideways scroll at 390 px; only the usual
CORS-blocked health call in the console. Figures re-laid out on 640-wide
plates after the first 390 px screenshots showed labels too small.

## Review fixes (science-phys-b, quality-a)

| row | change |
|---|---|
| A-7 | Hook: "…how big the core is, and which part of it is solid and which is liquid." → "…how big the core is, and that part of it is liquid." |
| A-8 | The P-wave path to 150° now enters the core at 44° (was 47°), so the two core-crossing paths no longer cross. |
| A-WD1 | At step 4 (bigger core), the earlier S paths are dimmed with their ✕ marks removed, and the station badges are dimmed to 35 %, so the moved shadow edge and the 78° tick stand out. |
| A-WD2 | Hook reveal: cut the signpost "Below, you read them yourself." |

Validated in a scratch clone: `build_ks4.py --batch batch-3` passed with zero console errors. A drive through all four bench steps at 1280 px gave no bad text, and screenshots of steps 3 and 4 were checked.
