# specific-latent-heat — author's notes (batch-3)

## Lesson record

```python
dict(slug="specific-latent-heat",
     source_file="specific-latent-heat.dc.html",
     subject="physics", topic_id="particle-model",
     title="Changes of state and specific latent heat",
     spec="6.3.2.3",            # 8464 6.3.2.3 = 8463 4.3.2.3, base on both; no RP
     family="Quantitative",
     routes=["CF", "CH", "TF", "TH"],
     review_state="draft", batch="batch-3",
     block_map={"s-ledger": "worked-example", "s-logger": "check"})
```

Two `block_map` entries are needed, and a scratch-clone build confirmed both:

- `s-ledger`: a staged instrument with no import. It is classified `worked-example` because it works one calculation through stage by stage.
- `s-logger`: a graph-reading instrument with committed answers, so `check`.

## Family: QUANTITATIVE, and why

E = m L carries the lesson. The spec's two named skills are both quantitative distinctions:

- "Distinguish between specific heat capacity and specific latent heat": which equation applies in each stage.
- "Interpret heating and cooling graphs": a flat section's length is a measure of energy.

The flagship turns an everyday phenomenon into numbers and feeds the CFIFA two-stage calculations. I considered CONTRAST (SHC against SLH). I rejected it because that contrast happens inside every calculation here, not as a separate A/B instrument. BATCH-PLAN's provisional family agrees.

## Line-up and the demand each part trains

| # | block | demand |
|---|---|---|
| Hook | `Ks4Choice`, not scored. Steam against boiling water, both at 100 °C: why does the steam burn worse? Each of the three wrong options gets a one-line correction: hotter, faster particles, spreads more. The reveal says that condensing releases energy at constant temperature and passes the counting to the ledger. | Commit before teaching. |
| Explainer 1 | Latent heat, specific latent heat (spec wording), fusion and vaporisation, the reverse changes releasing energy, and water's two values. ~95 words. | — |
| Flagship (L) | **The energy ledger** (`#s-ledger`), a new instrument. Setup: 10 g of boiling water and 10 g of steam each land on skin at 37 °C. **Gate:** the pupil predicts how many times as much energy the steam gives (about the same / twice / ten times / a hundred times). There are then three stages. Before each one the pupil picks the equation, then presses "Transfer it":<br>1. Water cooling from 100 to 37 °C.<br>2. Steam condensing at 100 °C (options include "Neither: no energy is transferred").<br>3. The condensed water cooling.<br>The scene animates the change: gas particles converge into a droplet on the skin, the jiggle slows as it cools, and the thermometer holds at 100 °C while condensing, then falls. The energy bars grow to scale: water 2646 J; steam 22 600 J condensing (gold) plus 2646 J cooling (teal). Each stage shows its working line. The final verdict answers the opening bet: 25 246 ÷ 2646 = 9.5, so "about ten times". | Choose the equation by what is changing (SHC vs SLH, spec 6.3.2.3); two-stage energy accounting; confronting "constant temperature means no energy". |
| `equation` | E = m L, ΔE = m c Δθ and E = P t, each chipped **On the sheet**. Each card's first words say when it applies: "State changing, temperature constant" or "Temperature changing, state constant". | — |
| Explainer 2 | Slopes mean ΔE = m c Δθ; flats mean E = m L; on a cooling graph the flats are where energy is given out; at a steady rate, flat length ↔ energy via E = P t. ~75 words. | — |
| Mid (M) | **Read the cooling curve** (`#s-logger`), a new instrument. 60 g of liquid Y loses energy at a steady 30 W. "Start the data logger" draws the curve live (A 90 °C → B 50 °C at 3 min, flat to C at 10 min, D 20 °C at 12 min), with a tube of Y freezing from the bottom up during the plateau. Three commitments, each locked once answered:<br>1. *Determine* the melting point (90, 50, 20, or "None: this curve shows freezing").<br>2. *Determine* how long Y takes to freeze (3, 7 or 10 min).<br>3. *Calculate* L, typed with a unit chosen from J/kg, J or J/kg °C. Four named errors are detected: minutes not converted (3500), E not divided by m (12 600), grams left in (210), and the wrong unit. The working is shown after two tries. | Interpret a **cooling** graph quantitatively (examination R4 asks for this, and for a graph-reading activity); freezing point = melting point; duration vs clock time; E = P t → L = E ÷ m. |
| CFIFA | `Ks4Cfifa`. Example 1 is the verbatim FIFA (2 kg ice, 668 000 J) behind "Nothing to convert".<br>Example 2, convert first:<br>• **F:** 250 g ice, L = 334 kJ/kg (g→kg and kJ/kg→J/kg) = 83 500 J. This is the examination's typical question.<br>• **H:** 45.2 kJ released by condensing steam, Lv = 2.26 MJ/kg (kJ→J, MJ/kg→J/kg); rearrange for m = 0.020 kg.<br>Write-it-outs:<br>• **F:** Q1 boil away 1.5 kg (nothing to convert) = 3 390 000 J. Q2 400 g freezing (convert) = 133 600 J released.<br>• **H:** Q1 316 000 J melts 0.80 kg; rearrange for L = 395 000 J/kg (nothing to convert). Q2 200 g water from 20 °C to steam (convert; two stages, two equations) = 519 200 J, the examination's 4-mark typical. | Watch then do; convert first; Higher rearranges and does the two-stage chain. |
| Command words | Determine, Calculate, Explain, Compare. | — |
| Exam tip | **Omitted.** There is no `examiner_tip` on any route. | — |
| Ladder | **r1** ⚑ authored, *Name*, 1 mark (see frozen items).<br>**r2** *Calculate*, 3 marks. **F:** 2.5 g of crushed ice; g→kg; 835 J. **H:** heating curve of Z (figure; flat from 3 to 10 min at 60 °C), 50 W heater, L = 84 000 J/kg; min→s, E = P t, then m = 0.25 kg. This is a heating graph, so heating and cooling graphs are both trained.<br>**r3** *Explain* chain, 3 marks: why sweating cools the body. It transfers the ledger's idea in reverse. Red herrings: "sweat is colder than the skin" and "evaporating sweat releases energy into the skin".<br>**r4** *Compare*, 4 marks: SHC against SLH, 5 points and 2 rejects. | — |
| Key note | `K.keyLines(slug)`, verbatim. | — |
| Bank | `K.bank(slug, route)`: 2 frozen items, both kept. | — |
| End | A tutor line, and a legal line covering: all 10 g condenses; no other energy losses; particles drawn as spheres; bars to scale; Y and Z are illustrative; Y cools at a perfectly steady rate (straight slopes); water at normal atmospheric pressure. | — |

The rail has 5 nodes: HOOK, LEDGER, GRAPH, CFIFA, LADDER.

**Distinct from `internal-energy`, as the brief requires.** That lesson's flagship is the ice-heating bench: a heating curve plus particles, predicting whether the temperature rises or holds. It also has a cooling-curve section sort (KE vs PE) and a heating-curve data rung on X (melting point / state / KE). This lesson reuses none of them:

- the hook is the steam burn, not turning up the flame;
- the flagship is an energy ledger with equation choice and energy bars, not a heating curve;
- the graph activity is quantitative: plateau duration → E → L, on a different substance (Y);
- the Higher data rung computes a mass from a heating plateau.

It is also distinct from `temperature-changes-shc`, which has a ranking instrument and an RP heater simulation.

## Misconceptions and where each is confronted

1. **"Constant temperature, so no energy is transferred"** (frozen q1 option 3; examination §5). It is born at ledger stage 2, where the pupil must pick an equation for condensing at 100 °C. Picking "ΔE = m c Δθ" (which gives 0 J) or "Neither" opens the three-beat panel. The mistake, as the pupil says it: "It stays at 100 °C, so no energy is transferred." Why it is wrong: a steady temperature means the average KE is not changing; it does not mean that no energy is moving. The correct version: bonds form and release E = m L. The animation runs regardless, with the bar growing while the thermometer stays at 100 °C.
2. **Using m c Δθ for a change of state, m L across a temperature change, or doing only one stage.** The equation pick in all three ledger stages, each with a corrective reply. The equation cards say when each applies. CFIFA H Q2's close names the one-stage error.
3. **kJ/kg substituted as J/kg; mass in grams.** CFIFA example 2 (both tiers), F Q2, r2 F, and the logger's g check.
4. **Freezing point thought to differ from melting point / the plateau read as "melting" on a cooling curve.** Logger step 1, "None: this curve shows freezing, not melting", with a correction.
5. **Reading the end time as the duration.** Logger step 2 ("10 minutes").
6. **Evaporation releases energy (direction).** r3 red herring, with its why.
7. **"Steam is hotter" / "steam particles move faster".** Hook corrections.

## Route tags

**None.** 8464 6.3.2.3 / 8463 4.3.2.3 carry no HT label and no "Physics only" label (examination §2: "No HT content and no physics-only content"). There is **no required practical**: AT 5 "measure the latent heat of fusion of water" is a skills opportunity only (examination §5), so the page has no RP badge, pill or block. Tiers differ only in numbers and demand, chosen by `R.isHigher`: CFIFA example 2, the write-it-outs, and r2 (H has a graph, a rearrangement and two equations). The eyebrow and key-note spec are chosen by `R.isTriple`: "AQA Combined Science (8464) 6.3.2.3" or "AQA Physics (8463) 4.3.2.3".

## Equation chips

- E = m L: **On the sheet** (8463 Appendix A sheet list, eq 9; both June 2026 sheets).
- ΔE = m c Δθ: **On the sheet** (eq 5; both sheets).
- E = P t: **On the sheet**. Note that the spec lists it as a **recall** equation (8463 eq 21), but both June 2026 sheets print it. It is chipped under the batch-2 ruling. When `EQ_YEAR` changes it should become "Learn it".

## ⚑ Net-new science-bearing items

1. **Hook replies.** "At the same temperature, the particles have the same average kinetic energy" (spec 6.3.3.1 / 6.3.2.1, temperature ↔ average KE). "Even the same mass on the same patch of skin burns worse" is a premise of the comparison.
2. **Ledger numbers and arithmetic.**
   - Water cooling: 0.010 × 4200 × 63 = 2646 J ✓.
   - Condensing: 0.010 × 2 260 000 = 22 600 J ✓.
   - Total: 25 246 J. Ratio: 25 246 ÷ 2646 = 9.54 → "about ten times" ✓.

   Skin is taken as 37 °C. Steam is taken to condense entirely and the water to cool to skin temperature (stated in the legal line). This traces to the frozen theory ("Steam releases much more energy per kg than liquid water at the same temperature"; examination C10 OK).
3. **Confrontation text.** "As steam condenses, its particles come together and the bonds between them form, which releases energy". This traces to frozen q1 wx2 ("Energy is released as bonds FORM during condensation") and examination C2 ("say 'bonds between particles'").
4. **Logger Y (illustrative).**
   - Mass 60 g; energy lost at a steady 30 W; plateau 3 to 10 min = 420 s.
   - E = 12 600 J, so L = 210 000 J/kg ✓.
   - The slopes imply c(liquid) = 30 × 180 ÷ (0.060 × 40) = 2250 J/kg °C and c(solid) = 30 × 120 ÷ (0.060 × 30) = 2000 J/kg °C. Both are plausible and neither is shown.
   - "A pure substance freezes and melts at the same temperature": examination §5 misconception list.
5. **CFIFA arithmetic.**
   - F: 0.25 × 334 000 = 83 500 ✓; 1.5 × 2 260 000 = 3 390 000 ✓; 0.40 × 334 000 = 133 600 ✓.
   - H: 45 200 ÷ 2 260 000 = 0.020 ✓; 316 000 ÷ 0.80 = 395 000 ✓; 0.20 × 4200 × 80 = 67 200 and 0.20 × 2 260 000 = 452 000, total 519 200 ✓ (examination's typical).
6. **Ladder.** r1 is authored. r2 F: 0.0025 × 334 000 = 835 ✓. r2 H: 50 × 420 = 21 000; 21 000 ÷ 84 000 = 0.25 ✓; Z is illustrative. The r3 chain and its herrings follow frozen q2 and its wrong explanations (sweat at body temperature; evaporation absorbs latent heat). The r4 points use the spec definitions and units.

## Frozen items: verdicts and how each is handled

**No frozen item is wrong for any route** (examination §4). Both stay in the bank on all four routes. Nothing needs withholding.

- **q1** (steam condensing, 0.5 kg). It is IMPRECISE in two places:
  - option 2's label "used L as mass" (C18);
  - option 4's number, 168,000 J, which has no derivation from the stem (C20).

  It stays in the bank. It is **not used as r1**. The examination allows it, but it is a Calculate item rather than recall, and the imprecise option labels would sit on the scored rung. If a DEPARTURES fix is permitted, the examination suggests changing option 2 to "4,520,000 J — used 2 kg instead of 0.5 kg" (needle: `How much energy is released when 0.5 kg of steam at 100°C condenses`).
- **q2** (sweating). It is correct, but it fails option-length parity: the key is about 25 words against distractors of about 10. So it is not used as a rung. The idea is instead trained as the r3 chain.
- **r1** is therefore authored ⚑. It is a *Name* item at parity: four options of four to six words each, every distractor a named misconception (fusion, SHC, internal energy). The stem says "gas", not "vapour", so the answer cannot be matched by word shape alone.
- **Theory C12 (frozen ponds freeze from the top): not displayed** (examination: muddled causal chain, not in the spec).
- **Theory C5 (Lv > Lf, particle reasoning): not displayed.** It is not in the spec. The water values in explainer 1 show the size difference without the claim.

## New instruments and helpers

All of these live in the lesson's own logic; there is no `_ext` file.

- `ledgerSvg`: skin, particles condensing and cooling, thermometer, to-scale energy bars and legend.
- `curve()`: a temperature–time plot drawn up to `tEnd`, with an optional moving dot, A–D letters, and a freezing-tube inset. It is used by the logger and by the H r2 figure. It is drawn in the same plot style as `internal-energy`'s `curve()` (axes, grid, teal trace), but rewritten for a fixed 0–12 min, 0–100 °C frame with minute gridlines, so durations can be read.
- `num()`: tolerant number parsing for the typed L.

## Body prose word count

| block | words |
|---|---|
| Hook paragraph | 27 |
| Explainer 1 | 93 |
| Explainer 2 | 73 |
| Logger lead | 20 |
| **Total explainer + hook** | **~213** |

The longest stretch before a commitment is 93 words.

## Self-check

- **Build.** I built it in a scratch clone with a throwaway `batch_3.py` (this lesson and its sibling only), using `build_ks4.py --batch batch-3`. That produced 8 pages with zero console errors.
- **Gates.** `ks4_batch_check` is clean. `ks4_parity --batch batch-3` passed 112/112.
- **Driven at 390 px in headless Chrome.**
  - TH with motion: every right path.
  - CF with reduced motion: the wrong paths. These were the ledger "Neither" (the confrontation opens), logger 90 °C and 10 min, and L = 3500 (the minutes message).
- **Text and console.** No `undefined`, `NaN`, `{{`, `[object` or `null` text on the page. The only console messages are the expected localhost CORS errors on `/api/health`.
- **Bug found and fixed.** The first drive found a negative `<rect>` height in the freezing tube once Y was fully frozen. I fixed it and re-drove.

## Review fixes (science-phys-a, quality-a, 1 Oct 2026)

| row | what I did / why not |
|---|---|
| S-1 / Q-SLH2 (REQUIRED) | Used the science reviewer's text for the H "Convert first" Answer note: "Converting only L gives 45.2 ÷ 2 260 000 = 0.00002 kg (0.02 g): a thousand times too small." The old note mislabelled the error. |
| Q-SLH3 (REQUIRED) | F "Convert first" now gives Lf = 334 000 J/kg, so only the mass converts. The Convert line is "250 g ÷ 1000 = 0.25 kg", with the note "L is in joules per kilogram, so the mass goes in kilograms." The Answer note is "Left in grams, 250 × 334 000 = 83 500 000 J: a thousand times too big." This also settles S-A4. |
| Q-SLH1 (REQUIRED) | The ledger plate title is anchored to the right edge (x 630, end-anchored, font 20). The legend is stacked: condensing on the first row, cooling on the second. Re-checked at 390 px: nothing clips or overlaps. |
| Q-SLH4 (REQUIRED) | Explainer 2's "Run it backwards on a cooling graph…" sentence is deleted. The eyebrow (and rail label) is now "Energy from a flat section". Logger step 1 is replaced with the reviewer's "Which section of the graph does E = m L describe?" (A to B / B to C / C to D, with the reviewer's replies and right text). The duration step and the calculation are kept. The "freezing point = melting point" misconception is therefore no longer confronted on this page; internal-energy covers that graph reading. |
| Q-SLH5 (REQUIRED) | In `curve()` (the logger and the H r2 figure), tick labels are 24 in the 640 plate, labelled every 20 °C and every 2 min, with axis titles at 24. The left margin was widened so the rotated axis title clears the numbers. Minute and 10 °C gridlines are kept for reading durations. |
| A-SLH1 | The confrontation now reads "its particles come together and are held by the forces between them, which releases energy". This matches batch-2 internal-energy's "forces between particles". ⚑ item 3 above is superseded: the page no longer says "bonds". |
| A-SLH2 | Dropped "in kilograms" from the r2-H prompt; the unit is now the pupil's choice. |
| A-SLH3 | Cut "The ledger below counts both." from the hook reveal. |
| A-SLH4 | No change. The reviewer accepts it; the content differs. |
| A-SLH5 | Added a Key fact card before the ladder: E = m L when the state changes at constant temperature, ΔE = m c Δθ when the temperature changes, and the SLH definition. |
| S-A5 | Covered by Q-SLH1. |
| S-A6 | No change. It is a frozen bank item, and its wording is for Mide or DEPARTURES. |
| S-A7 | No change. The key note is frozen. |

Validated in a scratch APFS clone: the full batch-3 build, `ks4_batch_check` clean, parity 616/616, and drives at 390 px on TH (motion) and CF (reduced motion). No new `block_map` need: `s-ledger` and `s-logger` are unchanged, and the key-fact card is auto-classified.
