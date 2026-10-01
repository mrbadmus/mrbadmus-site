# Enzymes — lesson notes (batch-2)

## Lesson record

```python
dict(slug="enzymes",
     source_file="enzymes.dc.html",
     subject="biology", topic_id="organisation",
     title="Enzymes",
     spec="4.2.2.1",
     family="Required practical",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-2")
```

Spec: 8464 4.2.2.1 / 8461 4.2.2.1 (the pack filename's "4.2.2.2" is wrong, per the
examination §1). Required practical: 8464 RP4 / 8461 RP5. Eyebrow and key-note spec
are computed per route in logic: `(8464) … RP4` on Combined, `(8461) … RP5` on Triple.

## Family, and why

**REQUIRED PRACTICAL** (BATCH-PLAN said MODEL). The commander asked for the RP
lessons to be modelled on the pilot's resistors I–V lesson, and AQA examines this
practical directly (method 6-markers, end point, rate = 1/time). The lock-and-key
MODEL is still taught, but as the mid-size activity that sets up the practical, not
the flagship. Line-up differs from resistors: a model bench and a temperature sketch
come before the RP; the RP flagship has a spotting-tile end-point decision and
class-data processing (anomaly, mean) rather than a meter reading.

## Activities and the demand each trains

| block | size | demand |
|---|---|---|
| Hook `Ks4Choice` (cracker turns sweet) | micro | commit to a cause before the word "enzyme" appears (unscored) |
| **Lock and key bench** (`s-fit`, new, in-lesson) | M | apply the model: pick the substrate by complementary shape (R/Q/P drawn, no names); predict what heating to 60 °C does; predict whether cooling restores it. Each pick animates (approach, dock, complex, products released; or bounce off a denatured site); enzyme count stays 1 while products count up ("not used up"). |
| Spot the flaw (`s-think`) | micro | replace "killed" with the marking point (denatured → active site changes shape → substrate no longer fits) |
| Sketch it (in `s-think`) | micro | choose the drawn rate–temperature sketch (command word Sketch) |
| **RP flagship** (`s-rp` + `s-sim`, new, in-lesson) | L | predict-gated (drawn rate–pH thumbnails A–D); run five buffers; samples drop into a spotting tile every 30 s (animated, instant under reduced motion); pupil taps the FIRST well that stays orange-brown (the AQA end point; wrong taps get named corrections); then identifies the planted anomaly in class data and calculates a mean; the rate–pH graph is drawn from the means and checked against the prediction |
| Variables `Ks4Sort` | M | classify IV / DV / control for this RP |
| Equation block + `Ks4Cfifa` | — | rate = 1 ÷ time (Learn it); CFIFA with min→s conversions |
| Ladder | — | r1 State (verbatim q5), r2 Calculate (calc, tier numbers differ), r3 Explain chain with red herrings, r4 Describe a method (6, levels) |

## Misconceptions and where each is confronted

| misconception | where |
|---|---|
| Enzymes are "killed" | `s-think` spot-the-flaw, immediately after the bench shows the heated site; also r3 herring |
| Cooling restores a denatured enzyme | bench gate 3 (predict, then watch P still bounce) |
| Hotter is always faster | bench gate 2 option a; sketch B; r3 herring (slow molecules = cold explanation) |
| "Same shape" rather than complementary | bench gate 1 reply (AQA's word: complementary) |
| Enzymes are used up | bench counter (products climb, enzyme stays 1); gate 2 option c |
| Cold denatures | sketch D feedback; `thinkReveal` |
| RP end point read wrongly (orange read as positive) | flagship tap: blue-black → "starch was still there"; later orange → "the time is the first drop that stays orange-brown"; r4 reject list |
| Rate given as time / no unit | equation block, CFIFA, r2 units select |

## Route tags

None. Everything in 4.2.2.1 and RP4/RP5 is base (no HT, no separate-only marker) —
examination §2 "No HT content in 4.2.2.1. No separate-only content." Tier differences
are numeric only (content standards §2): CFIFA worked examples, write-it-out questions
and the r2 rung choose Foundation or Higher numbers by `R.isHigher` (Higher adds
min+s conversions and a rearrangement, time = 1 ÷ rate).

## ⚑ Net-new science-bearing items

1. ⚑ Hook: chewed cracker tastes sweet because salivary amylase breaks starch into sugars (4.2.2.1: amylase is a carbohydrase that breaks down starch; carbohydrases → simple sugars).
2. ⚑ Explainer: "the protease made in the stomach works best in strong acid; enzymes in the small intestine work best near neutral, because bile, which is alkaline, neutralises the stomach acid" (re-cut of theory 4, rephrased per examination C11; pepsin not named, per R6).
3. ⚑ Lock-and-key bench copy (gate replies, "complementary"); simplified-model caveat in `legal`.
4. ⚑ Sketch replies (rate rises with collisions, peaks at optimum, falls as more enzyme denatures — examination C7 wording).
5. ⚑ RP method volumes (2 cm³ amylase, 1 cm³ buffer, 2 cm³ starch, 35 °C, 5 min) — examination §5 handbook values; risks from examination §5.
6. ⚑ Simulated data: model times 900/165/75/105/255 s at pH 4–8 (optimum near pH 6, examination "pH 6–7 typical"); Groups B/C invented, anomaly 240 s at pH 6.
7. ⚑ rate = 1 ÷ time, unit s⁻¹; all CFIFA numbers and r2 numbers are new.
8. ⚑ Ladder r3 chain, r4 levels and indicative points (from examination §5 typical questions).
9. ⚑ Key-note lines 1, 4, 5, 6 are authored (lines 2–3 are the verbatim source key note via `K.keyLines`).

## Frozen items flagged wrong, and handling

| item | verdict | handling |
|---|---|---|
| q1 wx1 "Above the optimum … the rate does increase" | WRONG on every route (C19) | Never a rung. Withheld from the practice bank by the engine (`batch_2.py` B2-W1); the lesson's own filter was removed in the review pass. |
| `rp` field "RP3 …" | WRONG number (C17) | Not displayed. RP block written from the spec: RP4 Combined / RP5 Biology, 30 s sampling, water bath. |
| q4 (substrate concentration) | not a spec factor | kept in bank verbatim; not a rung |
| q3 wx1 "produced in the mouth", q5 wx3 "reform" | IMPRECISE, keep | kept verbatim; q5 used as r1 (its key is correct) |
| theory 4 charges/hydrogen bonds (C9) | NOT-IN-SPEC | cut |
| examiner tip | none in source | slot omitted |

Practice bank therefore shows 4 items (q2–q5) on every route while wx1 stands.

## New instruments / helpers

All in the lesson's own Component logic; no `_ext` file.
- Lock-and-key bench: `fitFigure`, `enzymePath` (five-point active site morphing to a denatured outline), `mol`, `path`; DUR table; reduced motion jumps to each end state.
- Spotting-tile RP: wells are real `<button>`s (aria-label gives colour and time), on a cream plate in both themes; `onMix`, `endRun`, `onWell`; class-data table as rows of cards (pilot NOTES §10.10); rate–pH `plot` (Catmull-Rom through the means).
- Thumbnail sketcher `thumb(fn, xLabel, alt)` for rate–temperature and rate–pH sketches.

## Body prose word count

Hook 33 + explainer 1 (74) + explainer 2 (65) = **172 words** of body prose (RP method list
and risks ≈ 150 words more, as in the pilot's RP block).

## Review fixes (1 Oct 2026)

| row | what I did / why not |
|---|---|
| S-3 (science-bio-a, REQUIRED) | `TRUE_T[6]` 75 → 60. Re-driven in the order pH 6 then 7 (the failing order): pH 6 mean 90 s, pH 7 mean 100 s, so the peak stays at pH 6 and matches the verdict text. |
| B2-W1 (commander) | Removed the in-lesson q1 bank filter; `bank` is now `K.bank(slug, R.route)` and the engine withholds q1. |
| Q-EN1 (quality-a, REQUIRED) | Deleted the last sentence of `thinkReveal` ("Cold is different…"), which was said for the third time. |
| Q-EN2 (REQUIRED) | Deleted the authored key-note line that repeated the source line "Denaturation is permanent…". The key note now has 5 lines. |
| Q-EN3 (REQUIRED) | `hookOptions[0].reply` → `''`. |
| A-7 / A-EN2 (ADVISORY) | The curve of best fit now joins the measured means only (pH 5–8). pH 4 stays as a hollow marker on the axis, labelled "no end point / in 10 min". The alt text says so. |
| A-EN1 (ADVISORY) | That label moved up and right, clear of the y-axis. |
| A-8 (ADVISORY) | Unsampled wells are now pale orange-brown (`#F2D9A8`, iodine already in them, as in method step 1), not white. Their aria-label still says "Not sampled yet". |
| A-9, A-10 | Not changed: frozen text, imprecise but not wrong (keep, per the reviewer). |
| A-11 | Not changed: AQA credits enzyme = lock either way. |

No new section ids, so there is no block_map change.
