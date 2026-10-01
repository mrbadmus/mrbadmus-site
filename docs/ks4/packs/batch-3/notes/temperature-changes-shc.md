# temperature-changes-shc — author's notes (batch-3)

## Lesson record

```python
dict(slug="temperature-changes-shc",
     source_file="temperature-changes-shc.dc.html",
     subject="physics", topic_id="particle-model",
     title="Temperature changes and specific heat capacity",
     spec="6.3.2.2",            # 8464 6.3.2.2 = 8463 4.3.2.2; RP14 (8464) = RP1 (8463), spec home 6.1.1.3 / 4.1.1.3
     family="Quantitative",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-race": "check", "s-rp": "required-practical", "s-sim": "required-practical"},
     withhold=[W("A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C", "B3-W<n>")])
```

`block_map` entries are needed for three sections. The compiler could not classify them, and the build confirmed this in a scratch clone:

- `s-race` is a predict-then-heat instrument.
- `s-rp` is the RP method block. Its eyebrow interpolates the RP number, so the "Required practical" text sniff does not see it.
- `s-sim` is the RP simulation. Its eyebrow reads "Run the practical".

## Family: QUANTITATIVE, and why

The idea is carried by one equation, ΔE = m c Δθ. The examined errors are arithmetic ones: Δθ taken as the final temperature, and the mass left in grams. The architecture names specific heat capacity as its own QUANTITATIVE example. The family's flagship shape is "simulation feeding straight into CFIFA". The required practical is the simulation here, so it is the flagship. I chose this over the REQUIRED PRACTICAL family because the RP is one teaching beat in a calculation lesson, not the whole lesson. The ranking, the flaw and CFIFA are about the equation. BATCH-PLAN's provisional family agrees.

The examination recommends that this lesson carries the full RP block, because Rainford teaches it here (w6–7). `energy-changes-in-systems` (batch 9, 6.1.1.3) shares the RP and should link here rather than duplicate it.

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`: dry sand and seawater, the same energy into 1 kg of each. Which warms more? Not scored. Wrong options get a one-line correction. The reveal names specific heat capacity and coastal climate. | Commit before teaching. Confronts "the same energy gives the same rise" and "liquids warm faster". |
| Explainer | Mass, material, energy. Definition of c (the spec's wording). Water 4200, aluminium 900. ~85 words. | — |
| `equation` | ΔE = m c Δθ and E = P t, both chipped **On the sheet**, with units and rearrangements. | — |
| Mid (M) | **Rank the rises** (`#s-race`), a new instrument. Four samples: P 1.0 kg water 42 000 J, Q 1.0 kg aluminium 42 000 J, R 2.0 kg water 42 000 J, S 1.0 kg water 84 000 J. The pupil taps them into 1st–4th, biggest rise first, then presses "Heat all four". Four thermometers rise together from identical heaters. S's heater runs twice as long, because energy = time at equal power. The rises are labelled at the end. A wrong order lists a correction for each inverted pair. | Proportional reasoning with Δθ = ΔE ÷ (m c), one factor at a time and then combined (Q against S). This covers the spec statement the examination found missing (R2): "the increase in temperature depends on the mass…, the type of material and the energy input". |
| RP block | `#s-rp`: **Required practical 14 / 1** (route-aware, see below). Method (6 steps), the independent, dependent and control variables, and risks. | Know the AQA method. |
| Flagship (L) | **Run the practical** (`#s-sim`), a new instrument. Predict-gated: "your c will be higher / about / lower than 900". Then an animated rig (lagged 1.00 kg aluminium block, heater glowing, joulemeter counting, stopclock, digital thermometer) beside a temperature–time graph that plots a cross every minute. At switch-off a second commitment asks which temperature to record. The thermometer keeps rising for about 1.5 minutes, then falls, so "the highest reading" is right. **Process your data:** the pupil types c, which is checked to ±2%. Two named errors are detected: Δθ taken as the highest temperature (this opens the three-beat confrontation), and the energy not divided. After two tries the working is shown. The **comparison** then resolves the opening bet: the value is always high, because energy is lost to the surroundings, the heater and the thermometer. **Run it again without lagging** gives a second set of crosses and a larger c. | Run, read and process an RP. Interpreting the systematic error (examination §5 misconceptions: "thermometer wrong" vs energy lost; reading the temperature at switch-off). |
| Misconception | `#s-flaw` spot-the-flaw: "500 g … 20 °C to 60 °C … ΔE = 500 × 4200 × 60". Options: only Δθ, only mass, both, nothing. | Identify both errors in the source `common_mistake` before CFIFA. The reveal adds the cooling case (Δθ = initial − final, C14). |
| CFIFA | `Ks4Cfifa`. Example 1 is the verbatim FIFA (0.5 kg water, 20 → 100 °C, 168 000 J) behind "Nothing to convert". Example 2 converts. **F:** 250 g water 18 → 65 °C, 49 350 J (examination's typical question). **H:** 500 g copper pan, 7.7 kJ: convert g→kg and kJ→J, rearrange for Δθ, 40 °C. Write-it-outs. **F:** Q1 2.0 kg aluminium 15 → 35 °C, nothing to convert, 36 000 J. Q2 800 g water cooling 70 → 25 °C, convert, 151 200 J. **H:** Q1 1.5 kg iron, 27 000 J, final temperature 60 °C, rearrange. Q2 50 W for 5.0 min, 1.2 kg, Δθ 13 °C, min→s, E = P t then c, 962 J/kg °C, a two-equation chain. | Watch then do. Convert first. Higher rearranges and chains (content standards §2). |
| Command words | Define, Calculate, Explain, Describe a method: the four the ladder uses. | — |
| Exam tip | **Omitted.** No `examiner_tip` on any route. I checked all four `all_subtopics_physics*.py`; only series-parallel and resistors carry one. | — |
| Ladder | **r1** ⚑ authored, *Define*, 1 mark (see "Frozen items"). **r2** *Calculate*, 3 marks. F: 40 g copper spoon 20 → 70 °C, g→kg, 770 J. H: 2.0 kg copper, 60 W × 4.0 min, min→s, E = P t then Δθ = 18.7 °C. **r3** *Explain* chain, 3 marks: why the measured c is above the data-book value. Two red herrings: "thermometer read too high" (that would make c smaller) and "mass increased". **r4** *Describe*, 6 marks: the RP method, with levels from the examination §5 plus 6 indicative points and 2 rejects. | — |
| Key note | `K.keyLines(slug)` verbatim, except the line "RP14: electric heater method." On Triple it reads "Required practical 1: electric heater method." and on Combined "Required practical 14: …" (examination C9/C15). | — |
| Bank | `K.bank(slug, route)`: the two frozen items, with q1 to be withheld by the engine. | — |
| End | Tutor line. Legal line: 48 W heater, a fixed loss share that is larger without lagging, heater warm-up lag, scatter; the ranking assumes even heating and no loss; real sand and sea also differ in absorption, mixing and evaporation. | — |

Rail: HOOK, RANK, RUN, FLAW, CFIFA, LADDER (6). RUN ticks when the pupil's c is accepted, or when the working is shown after two tries.

This line-up is deliberately different from `internal-energy` (heating-curve bench, cooling-curve sort, bath-vs-coffee flaw) and from `specific-latent-heat` (steam ledger, data-logger cooling curve). There is no heating curve in this lesson.

## The RP badge is route-aware

`rpNum = R.isTriple ? '1' : '14'` feeds three places: the header pill "Required practical {{ rpNum }} · specific heat capacity", the RP block eyebrow "Required practical {{ rpNum }} · the AQA method", and the key-note spec "AQA 6.3.2.2 (8464) · RP14" / "AQA 4.3.2.2 (8463) · RP1". The frozen `rp` field ("RP14 (Physics)") is not displayed, because it is the Combined number labelled as Physics (examination C9). The RP block is written from the examination's §5 RP details (8463 §8.2.1 / 4.1.1.3, AT 1 and 5). The formal spec home of the RP is 6.1.1.3 / 4.1.1.3. The page cites 6.3.2.2 / 4.3.2.2 as its spec, with the RP number alongside.

## Misconceptions and where each is confronted

1. **Δθ = the final temperature** (common_mistake; examination §5, "the single commonest lost mark"). It is born when the pupil first computes Δθ from their own data in **Process your data**. Typing the c that comes from the highest temperature opens the three-beat panel. The mistake as a pupil says it: "Δθ is the temperature it ended at." Why it is wrong: Δθ is a change, and the block started well above 0 °C. The correct version: Δθ = highest − start. Every pupil then meets it again in `#s-flaw` (three beats: quote, Spot the flaw, reveal), together with grams-for-kilograms. CFIFA F Q1's close names the 63 000 J wrong answer. The cooling direction is covered in the `#s-flaw` reveal and in F Q2.
2. **Mass left in grams.** In `#s-flaw`, and in every convert step (each CFIFA close names the unconverted answer). r2 F's wrong feedback covers it too.
3. **"High SHC means it heats up quickly" (reversed).** The hook (water versus sand), the ranking (Q against P), and bank q2.
4. **"The same energy gives the same rise" / material ignored.** Hook option C and ranking pairs P–Q and Q–S.
5. **RP: c above the data-book value blamed on the thermometer.** The flagship's opening bet, the comparison and the unlagged run. r3's herring "thermometer read too high" carries a corrective why.
6. **RP: reading the thermometer at switch-off.** The flagship's switch-off commitment. The thermometer visibly keeps rising.

## Route tags

**None.** 8464 6.3.2.2 / 8463 4.3.2.2 carry no HT and no "Physics only" label, and neither does RP14 / RP1 (examination §2: "No HT content and no physics-only content in 6.3.2.2 / 4.3.2.2 / RP14 / RP1"). Every route gets the whole lesson. Tiers differ only in numbers and demand, chosen by `R.isHigher`. That covers CFIFA example 2, both write-it-outs and r2. Higher rearranges and chains E = P t into ΔE = m c Δθ. The only route-dependent text is the RP number and the spec citation, chosen by `R.isTriple`.

## Equation chips

- ΔE = m c Δθ: **On the sheet.** It is on the 8463 Appendix A sheet list (eq 5) and both June 2026 sheets.
- E = P t: **On the sheet.** It is on both June 2026 sheets. Note: the spec lists it as a **recall** equation (8463 eq 21). It is chipped "On the sheet" under the batch-2 ruling, because the June 2026 sheets print it. When `KS4.EQ_YEAR` moves to a year whose sheet drops it, this chip should become "Learn it".

## ⚑ Net-new science-bearing items

1. Hook reveal: dry sand's specific heat capacity is "about a fifth" of water's. Typical dry sand is about 800–840 J/kg °C, against 4200. The comparison is qualitative and the page gives no exact figure for sand.
2. Hook reveal: coastal places have milder temperatures. This traces to the frozen theory ("Coastal areas have milder, more stable temperatures"; examination C12 OK).
3. Ranking: Δθ values 10, 46.7, 5 and 20 °C (from 42 000 / 84 000 J, 1.0 / 2.0 kg, c = 4200 / 900). Arithmetic: 42 000 ÷ 4200 = 10; 42 000 ÷ 900 = 46.67; 42 000 ÷ 8400 = 5; 84 000 ÷ 4200 = 20.
4. RP simulation model. P = 48 W for 600 s gives E = 28 800 J. m = 1.00 kg aluminium, c = 900. The share lost to the surroundings is 20% lagged and 38% unlagged. A first-order heater lag (τ = 40 s) makes energy keep flowing into the block after switch-off. After that there is a slow loss. Results: highest 45.4 °C from a start of 20.3 °C, so Δθ = 25.1 °C and c = 1147 J/kg °C. Unlagged: 39.5 °C, Δθ = 19.2 °C, c = 1500 J/kg °C. The lagged value sits in the examination's "typical results" range (1000–1200 for aluminium).
5. RP method, variables and risks, written from examination §5. Ammeter with voltmeter is given as the joulemeter alternative.
6. Switch-off commitment: "the heater was hotter than the block when it switched off, so energy kept flowing into the block". This traces to examination §5: "reading the thermometer immediately the heater is switched off — the temperature keeps rising for a while; record the maximum".
7. CFIFA example 2 F (examination's typical question, ⚑ examiner-drafted). Arithmetic: 0.25 × 4200 × 47 = 49 350 ✓. H: 0.5 × 385 = 192.5; 7700 ÷ 192.5 = 40 ✓.
8. Write-it-out arithmetic. F: 2.0 × 900 × 20 = 36 000 ✓; 0.80 × 4200 × 45 = 151 200 ✓; 2.0 × 900 × 35 = 63 000 ✓ (the close). H: 1.5 × 450 = 675; 27 000 ÷ 675 = 40, giving 60 °C ✓; 50 × 300 = 15 000; 1.2 × 13 = 15.6; 15 000 ÷ 15.6 = 961.5 → 962 ✓.
9. r1 (authored), r2 F (0.040 × 385 × 50 = 770 ✓), r2 H (60 × 240 = 14 400; 14 400 ÷ 770 = 18.70 ✓), r3 links and herrings, r4 levels and points (from examination §5).
10. `#s-flaw` reveal: 0.5 × 4200 × 40 = 84 000 J; 500 × 4200 × 60 = 126 000 000 J = 1500 × 84 000 ✓.

## Frozen items flagged wrong, and how each is handled

- **q1 (all routes)**, needle `A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C`. Examination C20/C21: option 4 "900 J — ΔE = c × Δθ (forgot mass)" states false arithmetic (c × Δθ = 67 500 J; 900 is m × c), and wx3 misdiagnoses it. **Withhold on all four routes** (the commander assigns the DEPARTURES id). The examination's correction, if Mide rules a fix: option 4 becomes "900 J — ΔE = m × c (forgot the temperature change)", and wx3 becomes "900 J is 2 × 450 — you left out Δθ. ΔE = 2 × 450 × 150 = 135,000 J." It is never used as a rung.
- **q2 (car coolant)** is correct. The examination calls the stem premise odd (C22) and wx2 imprecise (C25). It stays in the bank. It is **not used as r1**: its key (about 25 words) fails option-length parity against distractors of about 13–15 words. r1 is therefore authored ⚑ as a *Define* item at parity: four options of 14–16 words each, every distractor a named misconception (specific latent heat, inverted ratio, internal energy).
- Theory C11 (cast-iron versus ceramic cookware): **not displayed**. The examination says to drop it.
- Theory C13 (mixing, m₁c₁Δθ₁ = m₂c₂Δθ₂): **not displayed**. It is not in the spec. The examination makes it optional only, and the prose budget went to R2 instead.
- Theory C5 ("higher SHC = heats and cools more slowly"): not displayed as stated. Every comparison on the page keeps the same mass and the same energy explicit (hook, ranking).
- Key note C4 ("highest common"): kept verbatim. It is minor, and the key note is frozen text.

With q1 withheld, the practice bank has **one** item on every route. That is a content-standards gap (§1 floor 5) owned by the bank, not by the lesson.

## New instruments and helpers

All are inside the lesson's own logic. There is no `_ext` file.

- `raceSvg`: four thermometers, heater indicators, rise labels.
- `rigSvg`: block, lagging, heater, thermometer display, joulemeter, stopclock. It matches `figlib/physics.py`'s `shc_apparatus` in layout (block, heater in the left hole, thermometer in the right, lagging, joulemeter), restyled with KS4D tokens.
- `graphSvg`: a temperature–time plot of crosses, with lagged and unlagged runs.
- `num()`: tolerant number parsing (spaces, thousands commas, ×10^n, e-notation) for the pupil's c.

## Body prose word count

| block | words |
|---|---|
| Hook paragraph | 32 |
| Explainer | 82 |
| Ranking lead | 30 |
| **Total explainer + hook** | **~144** |

The longest stretch before a commitment is about 82 words. The RP method list (~110 words) and the variables and risks are reference blocks, not running prose.

## Self-check

- Built in a scratch APFS clone with a throwaway `batch_3.py` holding only this lesson and its sibling: `build_ks4.py --batch batch-3`. Result: 8 pages, zero console errors at 1280 and 360.
- `ks4_batch_check.py --batch batch-3`: clean.
- `ks4_parity.py --batch batch-3`: 112/112 PASS. That covers prerendered text, route layers, registry, no horizontal scroll at 1280/820/390, console, no-react and keyboard.
- Driven in headless Chrome at 390 px:
  - TH with motion: right path, all animations.
  - CF with reduced motion: every wrong path, including the Δθ confrontation, the second-try working, and the unlagged run.
  - No `undefined`, `NaN`, `{{`, `[object` or `null` text, and no console errors apart from the expected localhost CORS on `/api/health`.

## Engine note (not this lesson's to fix)

`Ks4Ladder`'s calc rung parses with `parseFloat(s.replace(',', '.'))`. "63,000" therefore reads as 63, and "63 000" reads as 63. Both r2 answers here are chosen below 1000 (770 J; 18.7 °C) so a pupil cannot be marked wrong for typing a thousands separator. The instruments' own inputs use `num()`.
