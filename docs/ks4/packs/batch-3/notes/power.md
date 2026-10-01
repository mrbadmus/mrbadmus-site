# power — author's notes (batch-3)

## Lesson record

```python
dict(slug="power",
     source_file="power.dc.html",
     subject="physics", topic_id="energy",
     title="Power",
     spec="6.1.1.4",            # 8464 6.1.1.4 = 8463 4.1.1.4, base on both; no HT, no physics-only content
     family="Quantitative",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3")
```

No `withhold` (examination §4: both frozen items correct on every route). No
`block_map` entries needed: the build classifies `s-bench` → figure,
`s-flaw` → misconception, `s-equation` → equation, `s-calc` →
worked-example, `s-rate` → check. Checked on the real compiler.

## Family: QUANTITATIVE, and why

The architecture names power as a QUANTITATIVE example, and the examination
agrees: the concept (rate of energy transfer) is carried by P = E/t and
P = W/t, and its two classic errors (time left in minutes; power confused with
energy) are calculation errors. The flagship is the QUANTITATIVE shape: a
simulation whose readings feed straight into the calculation.

Efficiency is **not** taught here: the examination gives 6.1.1.4 no
efficiency content, and `efficiency` is its own batch-4 lesson (BATCH-PLAN).
It appears only as an End connect.

It differs from the batch-2 QUANTITATIVE neighbour `changes-in-energy`
(same topic): different hook (two kettles, not braking), a two-lane race
instead of a single-store bench, the spot-the-flaw on power vs force placed
straight after the bench, the CFIFA before the mid-size activity, and a
calculate-then-classify sort instead of a units sort. It has a Key fact
block (A-CE1 advisory from batch 2).

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`, unscored: a 3000 W and a 1500 W kettle heat the same water through the same rise. Which transfers more energy? | Commit before teaching; seeds the power-vs-energy confusion. Reveal: the same energy; the 3000 W kettle has more power (it does not say "half the time", so race 1 is not pre-answered). |
| Explainer | ≤90 words: definition, the watt as 1 J/s, lifted crates gain Ep = m g h. | — |
| Flagship (L) | **The lift test** (`#s-bench`), new instrument: two lanes, each a motor lifting a crate 3.0 m, with live energy (J) and time readouts and the power appearing when the lane finishes. Race 1: A and B, 20 kg, 4.0 s vs 8.0 s (same work, half the time). Race 2: A vs C, 20 kg vs 40 kg, both 4.0 s. Race 3: A vs winch D, 2 minutes, clocks ×40 (said under the figure). Predict-gated, animated; reduced motion jumps to the finished readings. | Compare powers from work and time (the spec's own two-motor example), then calculate one with a unit conversion. |
| Misconception, in the flagship | Race 3's minutes trap: picking 294 W opens a three-beat panel (the mistake as written → why a watt needs seconds → 120 s and "sixty times too big"). | The source `common_mistake`, where it is born. |
| Misconception (micro) | `#s-flaw` spot-the-flaw: "Motor X has the bigger power, so it can lift the heavier load." | Explain why power is not force (examination §5). |
| Equation | `#s-equation`: P = E ÷ t and P = W ÷ t, both chipped **On the sheet**, with rearrangements; a Units first card (kW, MW, kJ, MJ, minutes, hours). | — |
| CFIFA | Source FIFA (stair climb) verbatim behind "Nothing to convert"; a second nothing-to-convert example; a convert example; two attempts each opening with the convert decision. Foundation and Higher differ in every number and in demand (Higher rearranges, chains Ep = m g h into t = E ÷ P, and converts kW/kJ/MJ). | Calculate power, energy, work or time. |
| Mid (M) | `Ks4Sort` **Rate the machines** (`#s-rate`): eight cards "energy in a time" (J/kJ/MJ with s/minutes/hour), three bins (< 1 kW, 1–10 kW, > 10 kW). Units are spread across bins on purpose, so no unit predicts the bin (e.g. 1.8 MJ in 1 hour = 500 W); cards carry no device names, so world knowledge cannot solve them. | Convert, calculate and compare — fluency at rising stakes. |
| Key fact, command words | Define, Calculate, Explain, Describe — the four the ladder uses. | — |
| Exam tip | **Omitted.** No `examiner_tip` on any route. | — |
| Ladder | r1 authored ⚑ Define, 1 mark (definition of power; four options at parity, the key is not the longest). r2 Calculate, 3 marks: Foundation 54 kJ in 90 s → 600 W (convert kJ); Higher 1.2 kW for 2.5 min → 180 kJ (convert minutes, rearrange; review fix S-3/Q-PW2). r3 chain, Explain, 3 marks: motors X (6 s) and Y (9 s), two red herrings. r4 Describe, 4 marks: measuring your own power on a flight of stairs (points + reject list). | — |
| Key note | `K.keyLines(slug)` verbatim (examination C14 OK). | — |
| Bank | `K.bank(slug, route)` — both frozen items. | — |
| End | Tutor line; legal line (g = 9.8 N/kg, steady lifting, nothing dissipated; kettles transfer all their energy to the water). | — |

Rail: HOOK, LIFT, FLAW, CFIFA, RATE, LADDER (same on every route).

## Misconceptions and where each is confronted

1. **Time left in minutes** (`common_mistake`; q1 wx1) — race 3 three-beat panel; CFIFA convert example and Foundation Q2 "close" lines; r2.
2. **Power confused with energy** (examination §5) — hook; race 1 option "The same: they do the same work"; r1 distractor "total energy".
3. **"Takes longer, so works harder"** (q2 wx2) — race 1 option; r3 red herring.
4. **Power confused with force** (examination §5) — `#s-flaw`; r1 distractor.
5. **Rearranging upside down / multiplying instead of dividing** — race 3 options 0.20 W and 70 560 W.
6. **Mass used as the force in climbing problems** (examination §5) — r4 reject list.

## Route tags

None. Examination §1–§2: 6.1.1.4 / 4.1.1.4 has no HT and no physics-only
content. Tier difference is by numbers and demand only (`R.isHigher` chooses
the CFIFA examples, attempts and r2), per content standards §2. Eyebrow:
"AQA Combined Science (8464) 6.1.1.4" on CF/CH, "AQA Physics (8463) 4.1.1.4"
on TF/TH.

## Equations — chip decision

P = E/t and P = W/t (and E = Pt) are on the spec's **recall** list (8463
Appendix A; "recall and apply both equations") **and** printed on both June
2026 sheets (examination §5). Following the batch-2 commander ruling (chip by
the sheet the page links to, `EQ_YEAR`), both cards say **On the sheet**. The
r4/command-word training still asks pupils to produce the equations
themselves.

## ⚑ Net-new science-bearing items

- ⚑ Hook (3000 W vs 1500 W kettles, same energy to the water) and its reveal.
- ⚑ Lift-test numbers: 20 × 9.8 × 3.0 = 588 J; 588 ÷ 4 = 147 W; 588 ÷ 8 = 73.5 W; 40 kg → 1176 J ÷ 4 = 294 W; 588 ÷ 120 = 4.9 W; distractors 588 ÷ 2 = 294 W (minutes), 588 × 120 = 70 560 W, 120 ÷ 588 = 0.20 W. All rechecked.
- ⚑ Spot-the-flaw (power vs force) options, replies and reveal.
- ⚑ CFIFA: F 4800 ÷ 12 = 400 W; F convert 36 000 ÷ 120 = 300 W (theory example 2, re-cut); H 1500 × 40 = 60 000 J; H convert 360 000 ÷ 2400 = 150 s; attempts F 1500 ÷ 25 = 60 W, 18 000 ÷ 180 = 100 W; H 400 × 9.8 × 15 = 58 800 J ÷ 2000 = 29.4 s, 540 000 ÷ 360 = 1500 W = 1.5 kW.
- ⚑ Rate-the-machines cards: 1200 W, 30 000 W, 500 W, 1200 W, 300 W, 18 000 W, 150 W, ≈ 6700 W.
- ⚑ Ladder: r1 (authored at parity), r2 F 600 W and H 180 kJ (adapted from the examination's typical question), r3 links (examination §5's 2-mark question, set as a 3-link chain), r4 points (personal power by stair-running — the examination notes it is a class activity, not an AQA RP).
- ⚑ Key fact; equation-card wording "Here W on the right is work done, not watts".

## Frozen items flagged wrong

None (examination §4). Both quiz items are in the bank on every route. Neither
is a rung: q1 is a calculation MCQ whose key carries its whole working and is
much the longest option (fails parity); q2 is a compare/apply item, not
recall — so r1 is authored, as the batch-2 lesson learned (A-CE2) asks.
Theory imprecisions C2 ("energy being used") and C8 ("elite sprinter
sustained 1 kW") are not reproduced; the typical-power list is not used.

## New instruments / helpers

- **The lift test**: two-lane race drawn with `KS4D` primitives in the lesson's own logic (`liftSvg`), a 40 ms timer, predict-gated, reduced-motion instant swap, real `<button>` controls. No `_ext` file.

## Body prose

Hook + explainer, measured on the built page: 120 words on every route.

## Self-check

Built with `build_ks4.py --batch batch-3` in an APFS scratch clone (a scratch
`batch_3.py` holding only this lesson and `particle-motion-pressure`): compile
clean, the build's own zero-console-error check at 1280 and 360 px passed.
Driven in headless Chrome on all four routes at 390 px, motion on and
reduced: all three races (figure readings checked), the flaw, CFIFA, ladder,
bank; no `undefined`/`NaN`/`{{`/`null` text, no sideways scroll, zero console
errors (other than the CORS-blocked health ping).

## Review fixes

Reviews: `docs/ks4/packs/batch-3/review/science-phys-a.md` §4, `quality-a.md` (power).

| row | what I did / why not |
|---|---|
| S-3 / Q-PW2 (REQUIRED) | Higher r2 rewritten to the quality reviewer's item: 1.2 kW for 2.5 minutes, energy in kilojoules; convert minutes → s (× 60); answer 180, unit kJ (kW × s = kJ). Every numeric ladder answer is now < 1000. Driven in a scratch build: typing 180 + kJ grades Correct. |
| Q-PW1 (REQUIRED) | Every wrong hook option now has a corrective reply ("More watts means faster, not more." / "Running longer at a lower rate ends at the same total energy." / "The times only say how fast the energy went in, not how much."). The shared reveal was reworded ("same water, same temperature rise … more of is power") so it does not repeat any reply. |
| S-A11 | Applied: an Ep = m g h card, chip "On the sheet" (printed on both June 2026 sheets), in the equation block on every route — the source FIFA (all routes) and Higher Q1 both use it. |
| A-PW1 | Not changed: recorded for the family review; the order and demands already differ from changes-in-energy. |
| A-PW2 | Not changed: 588 × 120 already uses seconds, so "leaves the minutes as seconds" would not describe that error; the existing reply ("multiplies the energy by the time") is the accurate diagnosis. |
