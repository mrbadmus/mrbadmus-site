# titrations — author's notes (batch-2)

## Lesson record

```python
dict(slug="titrations",
     source_file="titrations.dc.html",
     subject="chemistry", topic_id="chemical-changes",
     title="Titrations",
     spec="8462 4.4.2.5 + Required practical 2 (chemistry only; one HT bullet)",
     family="Required practical",
     routes=["TF", "TH"],
     review_state="draft", batch="batch-2",
     block_map={"s-indicator": "check", "s-bench": "required-practical", "s-rp": "required-practical", "s-conc": "worked-example"})
```

`block_map` is needed: the classifier cannot infer `s-indicator` or `s-bench`. With these entries the lesson built cleanly in a scratch copy: 2 routes, zero console errors at 1280 and 360 px.

## Family and why

**REQUIRED PRACTICAL.** AQA names this practical as 8462 **Required practical 2**. It has no Combined Science number (8464 has no titration RP, and the examiner confirmed this). The examined skill is the method and its data processing.

The lesson is modelled on the pilot's I–V lesson in this order:

1. RP block: drawn apparatus, method, variables, risks.
2. Misconception.
3. Simulated practical with messy data.
4. Equation.
5. CFIFA.
6. A 6-mark "describe a method" as rung 4.

## Instruments and the demand each trains

| tier | block | demand |
|---|---|---|
| RP block | `#s-rp`. Drawn rig (clamp stand, burette graduated 0–50 cm³, tap, conical flask on a white tile). The AQA method in 6 steps from the examination's §5. The strong-acids-only rule (4.4.2.5). Measured / kept-the-same / risks cards | Know the method well enough to describe it |
| Misconception (three beats) | **Rinsing the burette with water** (`#s-rinse`, graded `Ks4Choice`): what happens to the titre? Placed straight after "rinse the burette with the acid", where the error is born | Predict the direction of an error |
| Micro | **Choose the indicator** (`#s-indicator`, graded `Ks4Choice` with a drawn figure): colour strips for phenolphthalein, universal indicator and methyl orange against the volume of acid added | Identify the unsuitable indicator from a representation (examiner C7) |
| Flagship (L) | **The burette bench** (`#s-bench`, new). It is predict-gated: the pupil first calls whether the rough titre will be larger, smaller or about the same. **Rough run:** +5.00 / +1.00 cm³ splashes only, so it overshoots (typically 25.00 cm³). **Accurate runs:** "Run in to 1 cm³ below the rough titre", then +0.50 cm³ or single 0.05 cm³ drops. The flask is pink, then flashes colourless near the end point, then stays colourless for good. The burette level animates (reduced motion: instant swap). Next to it, a close-up of the scale shows 0.10 cm³ graduations and the bottom of the meniscus on a dashed eye line. Each run uses a different initial reading (0.00, 0.50, 1.20, 0.35 …), and each recorded row shows "final − initial = titre". Accurate run 2 is planted as anomalous (25.05 cm³). The pupil then taps the titres that belong in the mean and checks. The feedback names the specific error (rough run included, anomalous titre included, a concordant titre left out, only one titre chosen), then gives the mean. | Run the method (dropwise near the end point, rough then accurate); titre = final − initial; identify concordant titres; mean of concordant titres only |
| Equation | "Learn it · chemistry has no equation sheet": titre = final − initial (verbatim); mean of concordant titres, to 2 d.p. | — |
| CFIFA (base) | The verbatim FIFA, with Convert = "Nothing to convert: all titres in cm³." (examiner C23). Worked convert: titres given in dm³ → cm³, because the 0.10 cm³ rule only works in cm³. Q1: rough 18.20, then 17.65 / 17.70 / 17.95 / 17.60 → 17.65 cm³. Q2: titres in dm³ → 18.20 cm³ | Production: calculate a mean titre |
| CFIFA (Higher, `data-route="higher"`) | Worked: HCl/NaOH with volumes already in dm³ → 0.0800 mol/dm³. Worked: the examiner's checked H₂SO₄/NaOH example (convert cm³ → dm³, 1 : 2 ratio) → 0.160 mol/dm³ and 6.40 g/dm³. It uses the same volumes as the first worked example, so the ratio visibly doubles the answer. Q1: HNO₃ from known NaOH → 0.250 mol/dm³. Q2: H₂SO₄/KOH 18.75 cm³ → 0.150 mol/dm³ and 8.40 g/dm³ | RP2's HT sentence: concentration in mol/dm³ **and** g/dm³ (examiner R7/R8) |
| Ladder | r1: verbatim q2 "dropwise" (Give, 1). r2: TF the examiner's mean-titre item (22.40, 22.10, 22.15, 22.20 → 22.15 cm³, 2 marks); TH HCl/NaOH concentration (22.50 cm³ → 0.0900 mol/dm³, 3 marks, convert cm³ → dm³). r3: a chain on why repeat to concordance and take the mean, with 2 red herrings (Explain, 3). r4: the examiner's 6-mark "Describe how … titration", with levels, indicative content and a reject list | — |

## Misconceptions and where each is confronted

1. **Rinsing the burette (or pipette) with water.** Confronted in `#s-rinse`, where the error is born. The reveal adds the reverse case: rinse the flask with distilled water only (examiner C17). It is also an r4 reject.
2. **Universal indicator chosen.** Confronted in `#s-indicator`, with an r4 reject.
3. **Including the rough or an anomalous titre in the mean.** Confronted in the bench's pick-and-check, the CFIFA close lines and the r3 herring.
4. **"Repeat to make it more accurate."** r3 herring. The chain uses AQA's wording: repeatable, and reduces the effect of random error (examiner C12).
5. **Titre = final reading only.** Every bench row shows "final − initial = titre", and the initial readings are deliberately non-zero.
6. **Overshooting.** The bench's +1.00 / +0.50 buttons let it happen. The flask text says "You cannot see how far past the end point you went."
7. **HT: ignoring the 1 : 2 ratio; not converting cm³ to dm³.** Covered by the Higher worked-2 note ("0.0800, the commonest Higher slip") and the TH r2 conversion choice.

## Route tags

The whole lesson ships only on TF and TH (8462 4.4.2.5 "(chemistry only)"; no section and no RP in 8464), so nothing is tagged `triple`.

| element | tag | citation |
|---|---|---|
| `#s-conc`: explainer, n = c × V and g/dm³ cards, Higher CFIFA | `higher` | 8462 4.4.2.5 "(HT Only) calculate the chemical quantities in titrations involving concentrations in mol/dm3 and in g/dm3"; RP2 "(HT only) determination of the concentration … in mol/dm3 and g/dm3"; 4.3.4 (chemistry only, HT only) |
| r2 TH variant, chosen by `R.isHigher` in logic | higher | as above |
| Key-note Higher line, added by `R.isHigher` in logic | higher | as above |

## ⚑ Net-new science-bearing items

- ⚑ RP method, variables and risks, written from the examination's §5 and not from the frozen `rp` field. The examiner says the field is correct but missing the HT sentence; that sentence is carried by `#s-conc`.
- ⚑ Strong-acids-only sentence, re-cut from th1 without "at Foundation level" (C2).
- ⚑ Hook: phenolphthalein in alkali is pink. Near the end point a splash makes a colourless patch that fades on swirling. At the end point one drop changes the colour permanently. Sources: th1 (indicator colours) and th2 step 6.
- ⚑ Rinse misconception: water dilutes the acid, so the titre is larger; rinse the flask with distilled water only (C17).
- ⚑ Indicator strips. Phenolphthalein: sharp pink → colourless. Methyl orange: sharp yellow → red. Universal indicator: a gradual purple → red sequence, so it is unsuitable (C7). The strips are schematic, with the end point at a fixed position.
- ⚑ Bench model:
  - every run's end point is near 24.70 cm³ (24.65–24.75), and run 2 is planted at 25.05 cm³;
  - "flash" within 0.50 cm³ of the end point;
  - readings move in 0.05 cm³ drops, with the rough-titre run-in;
  - the legal line names the model.

  The typical values (titres 20–25 cm³, rough titre high, reported to 2 d.p.) are from examination §5.
- ⚑ New calculations, checked by hand:
  - Base: worked convert 24.60 / 24.70 → 24.65 cm³ (24.87 with the outlier left in); Q1 52.95 ÷ 3 = 17.65 cm³; Q2 36.40 ÷ 2 = 18.20 cm³.
  - Higher worked: 0.00200 mol ÷ 0.0250 dm³ = 0.0800 mol/dm³; the examiner's 0.160 mol/dm³ and 6.40 g/dm³, verbatim.
  - Higher questions: 0.00500 ÷ 0.0200 = 0.250 mol/dm³; 0.001875 × 2 = 0.00375 mol ÷ 0.02500 = 0.150 mol/dm³ × 56 = 8.40 g/dm³.
  - Ladder: r2 TH 0.00225 ÷ 0.02500 = 0.0900 mol/dm³.
  - Mr: KOH 56, NaOH 40.
- ⚑ The r3 chain wording and the r4 levels and indicative content come from the examination's §5 examiner-drafted 6-marker.

## Frozen items flagged wrong, and how they are handled

- **None are WRONG** (examination §4). Both quiz items are clean and stay verbatim in the bank. q2 is rung 1.
- **q1 wx1** ("25.10 is 0.50 cm³ away from the other three", C27, IMPRECISE). Kept verbatim in the bank, and not used as a rung.
- **th1 "at Foundation level"** (C2) and **th2 "reliability"** (C12). Neither is reproduced.
- **Key note.** Verbatim, through `K.keyLines(slug)`. One extra line on TH covers the Higher calculation.
- The frozen matching activity is replaced by the drawn rig, the bench and the indicator check.
- There is no `examiner_tip` for this subtopic, so the slot is omitted.

## New instrument and helpers

**The burette bench** is built inside the lesson's own Component; there is no shared `_ext` file. Its parts:

- the `INIT` / `EP` tables, which hold every volume in hundredths of a cm³ so readings never pick up float noise;
- `rig(reading, colour)`, the apparatus drawing;
- `zoom(reading)`, the close-up of the scale;
- `strips()`, the indicator figure, with gradient ids prefixed `ks4tit-`;
- `judge(rows, sel)`, which checks the concordance choice;
- a 40 ms animation tick, cleared on unmount, that snaps instantly under `prefers-reduced-motion`.

## Word count

About 465 words of body prose in the template, from the hook to the Higher section (instrument strings excluded). The RP method list is about 170 of those words. Hook paragraph: 55 words before its commitment.

## Checks run

- A node harness confirmed that every `{{ }}` resolves on TF and TH, tags are balanced, `dc-import` props are valid, and no `undefined`/`NaN` text appears. It drove a rough run and three accurate runs, then three picks: rough included → refused; anomalous run included → refused; runs 1 and 3 → accepted, mean 24.68 cm³.
- A scratch-copy `build_ks4.py --batch` run built the lesson with zero console errors.
- The same drive in headless Chrome at 390 px: no horizontal scroll; the Higher badge appears only on TH. Light and dark screenshots were reviewed.
