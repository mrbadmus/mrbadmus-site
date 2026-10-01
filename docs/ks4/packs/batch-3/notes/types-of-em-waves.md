# types-of-em-waves — author notes (batch 3)

## Lesson record

```python
dict(slug="types-of-em-waves", source_file="types-of-em-waves.dc.html",
     subject="physics", topic_id="waves", title="Types of electromagnetic waves",
     spec="6.6.2.1", family="Model", routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-spectrum": "figure"},
     withhold=[W("Which EM wave has the highest frequency?", "B3-W?")]),
```

The spec is 8464 6.6.2.1 = 8463 4.6.2.1 (identical text). The page eyebrow and key-note spec switch on `R.isTriple`: "AQA Combined Science (8464) 6.6.2.1 · Model" on CF and CH, and "AQA Physics (8463) 4.6.2.1 · Model" on TF and TH.

`block_map`: `s-spectrum` is the flagship bench. On the real compiler the heuristic already reads it as "figure", through the `{{ spectrumFig }}`/`{{ pairFig }}` bindings. The entry is listed so it stays stable. The build classified every other section without help: hook, explainer, `s-energy` as check (Ks4Chain), `s-equation` as equation, `s-calc` as worked-example, command words as keyword, key-fact, `s-ladder` as check, `s-keynote` as summary, and the bank as quiz.

## Family: MODEL, and why

One structure explains every behaviour in this lesson. It is a single continuous spectrum, every group has the same speed in a vacuum, and v = f λ makes shorter wavelength mean higher frequency. The pupil uses that model to predict at each change of regime: neighbouring groups, within visible light, the far short-wavelength end, and backwards towards radio. The architecture's MODEL flagship is "a parameter instrument with predictions at each change of regime", and this bench does exactly that. CLASSIFY is wrong for this lesson because there is no category decision here. It belongs to `uses-em-waves` (batch 4, CLASSIFY), so leaving it out also keeps the two adjacent lessons from sharing a block line-up.

## Flagship (L): the spectrum bench, `s-spectrum`

**Part 1: build the spectrum.** Demand: recall and produce the order. This is AQA's "Complete the spectrum" item.
- Seven shuffled group cards. The pupil taps them into seven numbered places, longest wavelength first, and taps a placed card to take it back.
- Real `<button>`s, so Enter and Space work. This was driven by CDP key events.
- **Predict-gated:** "Show the spectrum" stays locked until all seven cards are placed.
- The reveal marks each place ✓ or ✗ and draws the true spectrum: seven rows, each wave visibly shorter than the one above. With motion allowed, the waves draw on one after another; with reduced motion they appear at once.
- For each neighbouring pair the pupil put the wrong way round, one corrective note names the misconception (microwave/infrared swap, X-ray/gamma swap, and so on). A fully reversed order gets its own note.
- Word shape cannot solve it.

**Part 2: same family, different waves.** Demand: apply the model to predict wavelength, frequency and speed.
- Three pairs: red light → violet light, microwaves → radio waves (the direction reverses, so a pattern cannot be guessed), X-rays → gamma rays.
- For each pair the pupil commits to B's wavelength, frequency and speed in a vacuum before "Send both waves" unlocks.
- The reveal animates both waves travelling right at the **same** on-screen speed (SMIL `animateTransform`, one wavelength every λ/v seconds) past a dashed "fixed point". Frequency becomes visible as crests per second at that point. Reduced motion gets static waves.
- One verdict line per prediction ("Speed: the same, not faster.") and one "why" sentence.
- When all three pairs are revealed, the part-1 spectrum switches to all seven waves moving at the same speed, and its heading becomes "Same speed: shorter λ, higher frequency".

## Mid-size activity (M): `s-energy`, Ks4Chain, unscored

Demand: give an example that illustrates energy transfer by EM waves (spec 6.6.2.1, "Students should be able to give examples…"). The examiner found this spec requirement **missing** from the source (R5).

The chain is the Sun warming your face: source (Sun) → waves cross the vacuum → skin absorbs → energy transferred, temperature rises. The two herrings confront "EM waves carry air or matter" and "sound or a medium carries it". The done-note generalises to the examiner's examples: a microwave oven heating food, and an aerial picking up a radio signal.

## Worked and do pairs (outside the instrument budget): CFIFA on v = f λ, `s-calc`

The source has no FIFA examples (`fifas: []`), so every example is authored ⚑. Foundation and Higher numbers differ.

**Foundation:** speeds and wavelengths written in full, no standard form.

| item | kind | working | answer |
|---|---|---|---|
| WE1 | nothing to convert | v from 3 000 000 Hz and 100 m | 300 000 000 m/s |
| WE2 | convert | 600 kHz → 600 000 Hz, then rearrange for λ | 500 m |
| Q1 | nothing to convert | 200 000 Hz × 1500 m | 300 000 000 m/s |
| Q2 | convert | 3 km → 3000 m | 300 000 000 m/s |

**Higher:** standard form, and rearrangement in every item.

| item | kind | working | answer |
|---|---|---|---|
| WE1 | nothing to convert | 9.0 × 10⁷ Hz (the examiner's typical question) | 3.3 m |
| WE2 | convert | 5.0 cm → 0.050 m | 6.0 × 10⁹ Hz |
| Q1 | nothing to convert | 1500 m | 2.0 × 10⁵ Hz |
| Q2 | convert | 900 MHz → 9.0 × 10⁸ Hz | 0.33 m |

Each write-it-out opens with the convert decision, as the architecture requires.

## Micro-widgets

- Hook `Ks4Choice`: how much of the spectrum the eye detects.
- Speed misconception confront inside the bench (see below).

## Misconceptions, and where each is confronted

| misconception (examination §5) | where |
|---|---|
| "Higher-frequency waves travel faster" | Born at bench part 2, pair 1, where the pupil first predicts speed. Three-beat confront appears with the reveal: quote → frequency counts waves per second, not speed; the crests keep pace → every EM wave has the same speed in a vacuum or air, 3 × 10⁸ m/s. Re-tested at pairs 2–3, as a rung-3 herring and as a rung-4 reject. |
| Spectrum order wrong (microwave/IR, X-ray/gamma, reversed; λ vs f confused) | Bench part 1: a named corrective note for each inverted neighbouring pair, plus a dedicated note for a fully reversed order. Rung-4 reject. |
| "Visible light is (most of) the spectrum" / "light is not an EM wave" / "radio waves are sound" | Hook options B, C and D, each with corrective feedback. |
| "EM waves need a medium" / "carry matter" | `s-energy` chain herrings. |
| "EM waves are longitudinal" | Rung-3 herring and rung-4 reject. The explainer defines transverse. |

## Command words

Give (rung 1), Complete (bench part 1, the AQA spectrum item), Calculate (CFIFA, rung 2), Explain (rung 3), Describe (rung 4). All five are taught in the command-words block.

## Ladder

**r1 · Give · 1 mark:** frozen q2, "All electromagnetic waves in a vacuum have the same what?", found with the needle `have the same what?`. It is present and identical on all four routes.
- Option-length parity: the key is 14 tokens and 71 characters; the longest distractor is 11 tokens and 60 characters. The difference is under 4 words and under 1.4×, so it passes.
- Its `why` adds the contrast and does not restate the key.

**r2 · Calculate · 3 marks, tiered ⚑:**
- **F:** 100 MHz radio. Convert MHz → Hz, then λ = v ÷ f = 3 m.
- **H:** 2.4 GHz wifi. Convert GHz → Hz, then λ = 0.125 m = 12.5 cm; tolerance accepts 12–13 cm.
- Answers are plain decimals, so the numeric grader never has to parse standard form.

**r3 · Explain · 3 marks ⚑:** why gamma rays have a higher frequency than radio waves.
- Links: shorter λ → same speed in a vacuum → v = f λ, so more waves pass each second.
- Herrings: "gamma travels faster" and "gamma is longitudinal".

**r4 · Describe · 4 marks, marking points ⚑:**
- Points: transverse and transfers energy; the order; λ decreases and f increases; same speed in a vacuum or air; eye detects only visible light.
- Rejects: faster gamma, longitudinal, swapped order.
- The examination says no 6-markers arise from 6.6.2.1 alone, so the rung is 4 marks.

## Exam tip

None. The subtopic has no `examiner_tip` in `all_subtopics_*.py` on any route, so the slot is omitted.

## Route tags: none

Every point taught is **base**:
- 6.6.2.1 for everything in the spectrum.
- 6.6.1.2 for v = f λ, which is base in both specs.
- The transverse definition is 6.6.1.1 wording, base.

These were deliberately **left out** rather than tagged, as the examination and the commander's brief direct:
- Radio waves produced by oscillating circuits: HT 6.6.2.3 / 4.6.2.3, lesson `properties-em-waves-2`.
- Refraction caused by the change of speed in materials: HT 6.6.2.2 / 4.6.2.2, lesson `properties-em-waves-1`.
- "All objects emit infrared": 8463 4.6.3.1, physics only, lesson `infrared-black-bodies`.

## Equation label

v = f λ is labelled **"On the sheet"**. It is on the recall list (8463 Appendix A eq 16, so the spec says recall), but both June 2026 sheets print it (examination §5). The label follows the batch-2 ruling: "On the sheet" when the June 2026 sheet prints it. The frozen `equations` field reads "c = f × λ". It is kept verbatim as data and rendered as v = f λ, per C18.

## Frozen items flagged wrong, and how they are handled

**Withhold, all routes:** q1, "Which EM wave has the highest frequency?" (needle: `Which EM wave has the highest frequency?`). Its wx3 teaches the microwave-resonance myth (C21). It is not used as a rung anywhere.

⚠ With q1 withheld, the practice bank holds **one** item (q2) on every route. The frozen source has only two quiz items. The commander may prefer the examination's alternative: keep q1 in the bank with a corrected wx3. That correction would be a frozen-text edit, so it is not mine to make.

Frozen source text not shown on the page:
- **theory 2, band numbers:** dropped. C8 and C9 are self-contradicting, and the numbers are not in the spec.
- **theory 1 and common_mistake, "Energy ∝ frequency" / "more energy per photon":** not taught (C4, C19 — photon energy is not in the spec).
- **theory 3:**
  - radio production (HT), refraction-by-speed (HT) and IR from all objects (Triple): left out, see Route tags above;
  - X-ray production from electron deceleration: not in the spec, not shown;
  - "All are produced by changes in energy levels of electrons…": imprecise (C16), not shown.
- **key_note:** lines 1, 2, 3 and 5 are shown verbatim. Three changes:
  - line 4, "Higher frequency = shorter λ = more energy.", is shown as "Higher frequency = shorter λ." (C4);
  - line 6, "Gamma from nucleus; X-rays from electron deceleration.", is dropped. X-ray production is not in the spec, and gamma's origin is taught in `properties-em-waves-2`;
  - "Our eyes detect only visible light." is added ⚑. This is the spec's R4, which the examiner said "needs a home".
- **matching:** replaced by bench part 1. It printed its own answers, and its microwave range repeats C9.
- **q2 wx3** (photon energy): kept verbatim as feedback. The examiner calls it harmless; the page does not teach it.

## ⚑ Net-new science-bearing items

Every claim below traces to 6.6.2.1, 6.6.1.1 or 6.6.1.2 unless noted.

**Hook and explainer**
1. Hook copy: a phone signal, warmth from a fire, screen light, UV tanning skin and X-rays photographing bone are all EM waves; the eye responds to one group.
2. Hook options and replies. The reveal says that an aerial, a camera sensor or your skin can detect other groups. Camera sensors detecting IR is a general fact, not taken from the spec.
3. Explainer: definitions of transverse (6.6.1.1 wording), wavelength and frequency (6.6.1.2 wording); EM waves need no medium and cross the vacuum of space (6.6.2.1).

**Bench**

4. Bench order notes: "infra-red means below red" and "ultraviolet means beyond violet", as positional aids.
5. Bench "why" sentences, and the drawings, which are schematic and not to scale.
6. Speed confront, with 3 × 10⁸ m/s from the source (C2).

**Energy chain**

7. Energy chain links and herrings. The Sun emits EM waves including infrared, which is not the Triple "all objects emit" claim. The done-note examples (microwave oven heats food; aerial) come from examination §5.

**Equation and CFIFA**

8. Equation card: the speed card says "the question gives you this value" (examination C2).
9. All CFIFA examples and write-it-outs. The source had none. Real-world framings used: a 900 MHz phone signal, 2.4 GHz wifi, a 100 MHz radio station.

**Ladder**

10. r1 `why`; r2 in both tiers; r3 chain; r4 marking points and rejects.

**Key note and legal line**

11. Key-note line 6.
12. Legal line: real wavelengths run from kilometres (radio) to far smaller than an atom (gamma); groups have no sharp edges and neighbouring groups merge (examination C6: X-ray and gamma overlap).

## New instrument and helpers

There is no `_ext` file. Everything lives in the lesson's Component.

- **`wave(id, x0, x1, top, h, lam, col, mode, delay)`** draws a clipped sine wave in one of three modes. `still`. `draw` (SMIL stroke-dashoffset draw-on). `move` (SMIL `animateTransform` translate by one wavelength over λ/SPEED seconds, repeat indefinitely). The loop is seamless, and every wave has the same on-screen speed.
- **`spectrumSvg(mode)`** draws the seven-row spectrum plate.
  - Band colours match `figlib/physics.py em_spectrum()`: radio #C8102E, microwave #E0892E, IR #FBBF24, UV #3B82F6, X-ray #9333EA, gamma #3A2B1F.
  - Visible is a white chip with a ROYGBIV stripe.
- **`pairSvg(pr, mode)`** draws the two-row comparison plate with the dashed fixed point.
- **`chip(...)`** draws the band label chip.
- Clip ids are prefixed `emw-`.
- Plates use `KS4D.svg`, `T`, `line` and `circ` in the house style: cream plate, Georgia labels.

## Body prose word count

Counted from the template; the prose runs before commitments.

| piece | words |
|---|---|
| hook | 60 |
| explainer | 89 |
| bench part-1 reveal | 23 |
| speed confront | 38 |
| equation lead | 21 |

That is about 231 words. Adding the reveals and replies (hook reveal 40, pair "why" lines about 50) gives about 320 in all. The longest run before a commitment is 89 words; the limits are ≤150 and ≤700.

## Self-check (scratch APFS clone of the worktree; temporary `batch_3.py` holding only this record)

- `build_ks4.py --batch batch-3`: compiled, 4 pages, and the build's own sweep found zero console errors at 1280 and 360 px.
- Headless Chrome on all four routes at 390 and 1280 px:
  - no `undefined`, `NaN`, `{{`, `[object` or `null` text;
  - no sideways scroll;
  - zero console errors, apart from the CORS-blocked `/api/health` that every localhost page makes.
- **Full play-through by tap:**
  - TH, wrong order: notes fire; speed predicted wrong; confront shows.
  - CF, right order.
  - The spectrum switches to moving waves after pair 3.
- **Keyboard:** CF placement by focus + Enter.
- **Reduced motion:** no `<animate>` in any figure.
- **Dark theme:** checked at 390 px.
