# sound-waves-hearing — author's notes (batch-3)

## Lesson record

```python
dict(slug="sound-waves-hearing", source_file="sound-waves-hearing.dc.html",
     subject="physics", topic_id="waves",
     title="Sound waves and hearing", spec="8463 4.6.1.4", family="Process",
     routes=["TH"], review_state="draft", batch="batch-3",
     block_map={"s-path": "worked-example"},
     withhold=[W("used for foetal scanning rather than X-rays", "<B3 DEP id>")])
```

`block_map`: `s-path` (the flagship stepper) has no import and a `{{ pathFig }}`
binding, so the heuristic would call it "figure"; it is a predict-gated
worked sequence, mapped to "worked-example" as chromosomes-mitosis maps its
stepper. Every other section classifies on its own (`s-build` Ks4Chain →
check, `s-sort` Ks4Sort → check, `s-equation` → equation, `s-calc` → worked-example).
A scratch build with exactly this record compiled and prerendered with zero
console errors at 1280 and 360 px.

Spec: AQA 8463 **4.6.1.4** Sound waves (physics only, HT only). Not in 8464.
The pack's "6.6.1.4" is wrong (examination §1). Eyebrow: "AQA Physics (8463)
4.6.1.4 · Process"; key note "AQA 4.6.1.4 (8463)". Ships on **TH only**, so the
page carries no `data-route` tags; the head shows the route chip only (the
build fills it, falling back to "Triple Higher"), and no hard-coded pills.

## Family: PROCESS, and why

4.6.1.4 is a chain of conversions: a sound wave in air → a vibrating solid (the
ear drum) → the parts behind it → a sensation, which only works over a limited
range of frequencies. That is a mechanism unfolding in steps, so PROCESS
(BATCH-PLAN's provisional family, confirmed). Watch: a predict-gated stepper.
Do: the pupil builds the same sequence. Produce: the ladder's 4-mark describe.

## Coverage — the spec core is written here; the ultrasound material is not

Per the examination, the pack teaches mostly 4.6.1.5. This lesson teaches the
whole of 4.6.1.4 from the spec (R2–R6) and moves **all** ultrasound, SONAR,
echo-sounding and d = vt/2 material to `waves-detection-exploration`
(including the SONAR FIFA, which that lesson reads from this slug's source
record). Nothing about ultrasound imaging or echo timing is taught on this page.
The hook names a sound "too high for a human ear" (a dog whistle) without
teaching ultrasound uses. "Sound travels faster in denser media" appears
nowhere, not even as a quoted mistake.

## Line-up

hook (Ks4Choice, dog whistle) → video → explainer → **hearing-path stepper (L)**
→ **build the path (M1, Ks4Chain)** → explainer → **conversion sort (M2,
Ks4Sort)** → explainer (frequency fixed, speed and wavelength change) →
equation (v = f λ) → CFIFA → command words → key fact → ladder → key note →
bank → end. No exam-tip slot: the source has no `examiner_tip`.
`waves-detection-exploration` (taught next) has a different hook, flagship
and mid-size shapes.

## Instruments and the demand each trains

- **Flagship (L) — "From air to ear"** (`s-path`, new instrument, in-lesson
  logic only). A drawn ear: loudspeaker, a field of air particles, ear canal,
  ear drum, then (hidden behind a dashed "?" until step 3) three small bones,
  the cochlea and a nerve. Four predict-gated steps, each locked until the
  pupil commits:
  1. what the air particles do (vibrate about one place vs travel vs stay
     still) → the particles animate as a travelling longitudinal wave;
  2. how often the ear drum moves for a 500 Hz note → the drum vibrates in
     step with the air (frequency unchanged);
  3. what passes the vibrations on → the hidden parts appear, bones vibrate,
     impulses run up the nerve; misconception panel;
  4. five tones in mixed units (15 000 Hz, 25 kHz, 12 Hz, 19.5 kHz, 0.8 kHz),
     each predicted Heard / Not heard against the stated 20 Hz–20 kHz range →
     per-tone verdicts with the kHz→Hz conversion, then "Play" buttons put any
     tone on the ear: the air always vibrates, but the drum, bones and nerve
     only respond in range.
  SMIL motion (particle phase offsets give real compressions travelling
  right; drum/bones oscillate; impulses run along the nerve); reduced motion
  gets a static snapshot with the compression pattern and double-headed /
  single arrows. Real buttons throughout. Demand: describe the sound →
  solid → sensation process and apply the limited range (with unit
  conversion) — R2, R3, R5, R6.
- **M1 — build the path** (`s-build`, Ks4Chain, unscored): five links from a
  phone speaker to the brain, two herrings (air flows into the ear; the ear
  drum makes the nerve impulses). Demand: produce the sequence (Law 5's "do"
  after the stepper's "watch").
- **M2 — which way is the conversion?** (`s-sort`, Ks4Sort, 7 cards, two
  bins: sound waves → vibrating solid / vibrating solid → sound waves).
  Demand: the spec's "describe, with examples, processes which convert wave
  disturbances between sound waves and vibrations in solids" (R4). Word shape:
  no keyword predicts a bin ("vibrat-" and "sound" appear on both sides).
- **CFIFA** on v = f λ across a medium change (the 4.6.1.2 link the
  examination lists as the one calculation this point supports). TH-only
  lesson, so there is one tier of numbers (all Higher): worked 1 nothing to
  convert (500 Hz into water, 1500 m/s → 3.0 m, the examiner's typical item);
  worked 2 kHz → Hz (20 kHz in air at 340 m/s → 0.017 m, with the note that
  unconverted 340 ÷ 20 = 17 m is the 20 Hz wavelength); attempts: 250 Hz in
  a steel rail at 5000 m/s → 20 m (nothing to convert); 1.5 kHz in water →
  1.0 m (convert). Every attempt opens with the convert decision.
  ⚠️ The pack's own FIFA (SONAR distance) is 4.6.1.5 content and is used,
  verbatim with a Convert step, by `waves-detection-exploration` instead
  (examination §4). So this lesson's CFIFA has no verbatim source FIFA.
- **Equation block**: v = f λ "On the sheet" (printed on both June 2026
  sheets; the spec lists it as recall, eq 16 — labelled per the batch-2
  ruling, difference noted here), rearrangements, and a kHz → Hz units card.

## Misconceptions and where each is confronted

| misconception | where | form |
|---|---|---|
| Air from the source travels to the ear | stepper step 1 (the moment the wave is drawn) | predict-trap + correction; M1 herring; r4 reject |
| A faster wave in a solid means a higher frequency | stepper step 2 | predict-trap distractor + correction |
| "The ear drum is the part that hears the sound" (examination §5) | stepper step 3 | three-beat panel: the mistake → only vibrates, senses nothing → the spec's correct version |
| The ear's limit is loudness / the sound cannot reach the ear | hook distractors; r3 herrings | corrective replies |
| kHz not converted | stepper step 4 verdicts; CFIFA convert notes; r1 distractor (20 000 kHz); r2 | conversion shown on each verdict |

## Route tags (spec citations)

None. The whole lesson is 8463 4.6.1.4 "(physics only) (HT only)" and ships on
TH only. Supporting content at lower layers is still correct on TH: sound is
longitudinal / needs a medium (8464 6.6.1.1, base); speed in different media
and v = f λ with frequency unchanged (8463 4.6.1.2, physics only).

## Ladder

1. Recall · State · 1 — ⚑ authored (no frozen item covers 4.6.1.4; both frozen
   items are 4.6.1.5): "State the range of normal human hearing." Options at
   parity (20 Hz to 20 000 kHz / 0 Hz to 20 kHz / 20 Hz to 20 kHz / 20 Hz to
   2 kHz), each distractor a named slip with a correcting reply.
2. Apply · Calculate · 3 — ⚑ 2.0 kHz sound into a wooden door at 3400 m/s →
   λ = 1.7 m; conversion choice kHz→Hz; unit m.
3. Explain · Explain · 3 — ⚑ chain: why 40 kHz is not heard (examiner's
   typical item) with two herrings (cannot travel through air; amplitude too
   small).
4. Produce · Describe · 4 — ⚑ a lorry makes a window vibrate and is heard;
   five marking points (one per conversion step plus the in-range condition),
   two rejects.

## ⚑ Net-new science-bearing items

1. Hook text and replies (dog whistle above the human range; dogs hear it — C10
   says dogs hear ultrasound).
2. Stepper copy, all four steps (prompts, options, replies, why lines) —
   from 4.6.1.4 and examination §5 (small bones → cochlea → nerve impulses).
3. Misconception panel (step 3).
4. Tone set and verdicts (20 Hz–20 kHz from 4.6.1.4).
5. M1 chain links and herrings (cochlea "sends electrical impulses along a
   nerve to the brain" — examination §5 wording).
6. M2 sort cards and whys (microphone diaphragm, window, loudspeaker cone —
   examination §5 examples; table top, tuning fork, guitar string added).
7. Explainer 3: "Sound usually travels fastest in solids and slowest in gases,
   because the particles in a solid are closer together and more strongly
   linked" — the examination's own correction text (C5); 340 / 1500 m/s from
   theory 1 (C4).
8. CFIFA examples and attempts (speeds given as data: water 1500, air 340,
   steel 5000, wood 3400 m/s).
9. All four ladder rungs, marking points and rejects.
10. Key-note lines 2, 3, 4 (first sentence) and 6; key fact; command-word
    definitions; legal line.

## Frozen items flagged wrong, and how handled

| item | verdict | handling |
|---|---|---|
| q2 "Why is ultrasound used for foetal scanning rather than X-rays?" — wx2 says X-rays penetrate soft tissue less well than bone (C23) | WRONG on its only route | **Withhold** on TH: needle `used for foetal scanning rather than X-rays`. Not used as a rung. The correct fact (ultrasound is non-ionising) is taught in `waves-detection-exploration`. |
| q1 "Why must you divide the echo time by 2 in SONAR calculations?" | correct, but 4.6.1.5 content | Not used as a rung here. Left in this slug's practice bank (it is frozen to this slug); commander may prefer to withhold it here too. |
| theory 1 / common_mistake: "Sound travels faster in denser media" (C5, C15) | WRONG | Re-cut theory; never displayed, never quoted. The `common_mistake` field is not rendered anywhere. |
| theory 2 "(conversational speech frequencies)" (C8); "dogs" use ultrasound (C10) | IMPRECISE | Not displayed. |
| `equations` "d = v × t / 2" (C17) | not an AQA equation | Not displayed here. |
| key_note "Infrasound <20 Hz, ultrasound >20 kHz." "Ultrasound uses…" "d = v × t/2…" | infrasound not an AQA term; the rest 4.6.1.5 | Not displayed; the key note uses verbatim lines 1, 2 ("Human range: 20 Hz–20 kHz.") and 4 ("Speed: solid > liquid > gas.") plus authored 4.6.1.4 lines (precedent: carbon-cycle Q-C4, enzymes). |

**Bank size:** after the withhold the TH bank is one item (q1), below
content_standards §1's floor of 5. For Mide's list.

## New instrument / helper

The hearing-path stepper (`pathSvg`, `look`, `STAGES`, `TONES`) lives entirely
in the lesson's Component logic. No `_ext` file. Section CSS: none added.

## Word count

Hook 26 + explainers 68 + 59 + 80 = **233 words** of body prose; the longest
run before a commitment is 68 words. Instrument copy (prompts, why lines, the
panel) is extra and short.

## Self-check

Scratch clone of the worktree, scratch `ks4_lessons/batch_3.py` with only this
lesson and its sibling: `build_ks4.py --batch batch-3` compiled both, zero
console errors at 1280 and 360 px. Headless-Chrome drive (390 light by
programmatic click, 1280 dark with reduced motion): every stepper step,
Play buttons, chain, sort, both CFIFA attempts and all four rungs completed
(Score 4 of 4); no `undefined`/`NaN`/`null`/`{{`/`[object` text; no sideways
scroll at 390 px; only the usual CORS-blocked health call in the console.
