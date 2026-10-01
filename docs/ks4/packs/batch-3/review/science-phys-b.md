# Science review — batch 3, group phys-b

Reviewer: fresh AQA GCSE examiner (Opus), 1 Oct 2026. I wrote none of these lessons.
Lessons: `types-of-em-waves`, `sound-waves-hearing`, `waves-detection-exploration`.
Specs: 8463 Physics, 8464 Combined Trilogy. The examination files in `docs/ks4/packs/batch-3/examination/`
were my starting evidence. I re-checked them rather than taking them on trust.

## Method

- **Spec text.** I downloaded AQA-8463-SP-2016.PDF (v1.1) from filestore.aqa.org.uk and read 4.6.1.1–4.6.1.5 and
  4.6.2.1–4.6.2.2 as text. Then I deleted the PDF.
  - 4.6.1.4 and 4.6.1.5 are headed verbatim "(physics only) (HT only)", so Triple Higher is the only correct route.
  - The examination quotes both statements verbatim and correctly, and the same holds for 4.6.2.1.
  - The 4.6.1.2 "(Physics only)" line, "how changes in velocity, frequency and wavelength … of sound waves from one medium
    to another, are inter-related", is also confirmed. The sound lesson's v = f λ material is built on it.
- **Lesson sources.** I read each one in full: the template and all of the Component logic. That covered:
  - the stage tables and every `r`/`why` reply;
  - the ORDER_NOTES and PAIRS truth tables;
  - the TONES verdict logic (`inRange`);
  - the figure geometry: Earth radii and ray construction, scan boundary positions and echo times, the ear plate;
  - the CFIFA steps, rungs, levels, rejects, key notes and bank calls.
- **Built pages.** I served `mrbadmus_site` on :8722 and drove headless Chrome with `prefers-color-scheme: light`.
  - I captured the client-rendered text of all six built pages: EM on CF/CH/TF/TH, and sound and detection on TH.
  - I diffed EM's routes against each other. The only differences are the 8463/8464 eyebrow, key-note label, sheet
    label, route chip and the tiered CFIFA/rung-2 numbers. That is correct: everything taught is base.
  - I played each flagship with wrong picks and checked every verdict line:
    - the EM bench, both parts and all three pairs;
    - the hearing path, all four steps plus the tone verdicts;
    - the seismic bench, all four steps;
    - the scan, both steps.
  - I exported the seismic, scan and ear SVGs and inspected them as images.
  - Console: only the expected localhost CORS block on `/api/health`.
- **Arithmetic.** I re-did every calculation by hand. All of it is correct (listed per lesson).
- **Frozen items.** I checked the frozen items in `shared/ks4-source-batch-3.js` and the `withhold` list in `batch_3.py`.
  The page text confirms the withheld items are absent.

---

## 1. types-of-em-waves — AQA 8464 6.6.2.1 / 8463 4.6.2.1 (base)

**Routes: CF / CH / TF / TH.** The page is the same on every route apart from the eyebrow, sheet label, key-note label
and the tiered calculation numbers. That is right, because every point taught is base:
- 6.6.2.1 for the spectrum;
- 6.6.1.2 for v = f λ, recall-listed in the spec and printed on both June 2026 sheets, so "On the sheet" follows the
  batch-2 ruling.

The three route-wrong points in the source are **gone** from the page text on every route (grep of the client-rendered
text):
- radio waves from oscillating circuits (HT, 6.6.2.3);
- refraction because the speed changes (HT, 6.6.2.2);
- "all objects emit IR" (physics only, 4.6.3.1).

Also gone are the self-contradictory band numbers (C8/C9), "energy ∝ frequency" and "per photon" as taught content
(C4/C19), and X-ray production (C14/C16). The equation is rendered as v = f λ, not c (C18). The spec's "examples that
illustrate the transfer of energy" (R5, missing from the source) is now taught by `s-energy`. "Eyes detect only a limited
range" (R4) is in the hook reveal, rung 4 and the key note.

**Verified correct**
- **Spectrum order and bench truth table.** Every ORDER_NOTES line, including "infra-red = below red" and "ultra-violet =
  beyond violet" as positional aids, and the REVERSED note.
- **PAIRS truth.** red→violet = shorter / higher / same; microwave→radio = longer / lower / same; X→gamma = shorter /
  higher / same. Each verdict line is correct when driven with wrong picks.
- **The moving-wave figures.** Every wave moves at one on-screen speed, so frequency = speed ÷ λ really is higher for
  the shorter drawn wave.
- **Speed confront** ("vacuum or air", 3 × 10⁸ m/s).
- **The energy chain and its herrings** (Sun → vacuum → skin absorbs → temperature rises; no air or sound across space).
- **The hook options and replies.**
- **CFIFA arithmetic:**
  - F: 3 000 000 × 100 = 3 × 10⁸ m/s; 600 kHz → 500 m, unconverted 500 000 m; Q1 3 × 10⁸; Q2 3 km → 3 × 10⁸, unconverted
    3 × 10⁵.
  - H: 9.0 × 10⁷ Hz → 3.3 m; 5.0 cm → 6.0 × 10⁹ Hz, unconverted 6.0 × 10⁷; 1500 m → 2.0 × 10⁵ Hz; 900 MHz → 0.33 m.
- **Rung 2:** F 100 MHz → 3 m; H 2.4 GHz → 0.125 m = 12.5 cm, with tolerance covering 12–13 cm.
- **Rungs 3 and 4:** the rung 3 chain and both herrings; rung 4's points and rejects.
- **The key note**, including line 4 trimmed to "Higher frequency = shorter λ."
- **The legal line.** Gamma wavelengths (≲10⁻¹¹ m) are indeed "far smaller than an atom" (~10⁻¹⁰ m).

**Frozen items.** q1 ("Which EM wave has the highest frequency?", wx3 = microwave-resonance myth) is withheld on all four
routes (B3-W7) and absent from rung 1 and the bank on every route. q2 is rung 1 and the only bank item on every route.
Its key and wx1–wx2 are correct.

### REQUIRED

None.

### ADVISORY

| # | lesson · routes | where | note |
|---|---|---|---|
| A-1 | types-of-em-waves · all | explainer (`ks3-explainer` after Ks4Video) | "**wavelength** (the length of one complete wave)" → "**wavelength** (the distance from a point on one wave to the same point on the next wave)". The current gloss is acceptable, but the spec defines it in the second form (8463 4.6.1.2 / 8464 6.6.1.2), and mark schemes credit that wording. |
| A-2 | types-of-em-waves · CH, TH | `cfQuestions` (hi) Question 2 `close` | "Unconverted, 3.0 × 10⁸ ÷ 900 gives 330 000 m: an aerial bigger than a city." → "Unconverted, 3.0 × 10⁸ ÷ 900 gives 330 000 m: a wavelength of 330 km for a phone signal." As written, it ties a wavelength to an aerial's size, which the lesson never teaches and which is not a simple equality. |
| A-3 | types-of-em-waves · all | rung 1 / bank feedback (frozen q2 wx3) | "Energy per photon = hf …" is correct physics beyond GCSE (photons are not in the spec). It is shown only as feedback when a pupil picks option D ("Energy"), on every route including Foundation. It is frozen and harmless (examination C27), so no action unless the commander collects beyond-spec feedback for Mide. |

**Verdict: SCIENCE PASS.**

---

## 2. sound-waves-hearing — AQA 8463 4.6.1.4 (physics only, HT only)

**Routes: TH only.** This is correct (confirmed from the spec heading), and there is no 8464 counterpart. The page has no
`data-route` tags, which is right for a TH-only page.

The page now teaches the whole of 4.6.1.4, which the source pack lacked (R2–R5):
- sound travelling into a solid makes it vibrate (explainer 2, sort);
- the ear drum and the parts behind it vibrate and cause the sensation of sound (stepper steps 2–3, chain, misconception
  panel);
- examples of the conversion in both directions (the sort: microphone, ear drum, window, table, loudspeaker, tuning fork,
  guitar string, each in the right bin);
- the conversion only works over a limited frequency range, and the range is 20 Hz–20 kHz (step 4, rung 3, key note).

The supporting 4.6.1.2 (physics only) content is correct on TH: frequency is unchanged on entering a new medium, and the
speed and wavelength change. "Sound travels faster in denser media" (C5/C15) appears nowhere. The replacement
("usually fastest in solids … particles closer together and more strongly linked") is the examination's own corrected
wording. No ultrasound imaging or echo timing is taught here. That correctly leaves 4.6.1.5 to the detection lesson.

**Verified correct**
- **Stepper truth and verdicts:**
  - step 1: particles vibrate about one place;
  - step 2: the drum moves 500 times a second;
  - step 3: the small bones;
  - step 4: 15 000 Hz heard, 25 kHz not heard, 12 Hz not heard, 19.5 kHz heard, 0.8 kHz heard. Each kHz → Hz conversion
    is shown and correct.
  - Every wrong-pick reply is correct, including "a faster wave is not a more frequent one".
- **The step 4 "why".** It matches the spec and AQA mark-scheme wording ("only vibrate enough … over a limited range").
- **The legal line.** It correctly says the real response fades towards both limits, differs between people and its
  upper limit falls with age, so the drawn hard cut-off is not taught as literal.
- **The ear plate.** Loudspeaker → particles → canal → drum → three small bones → coiled cochlea → nerve.
  - The particle phase offsets make compressions travel towards the ear. I checked the sign of the `begin` offsets.
  - Higher frequency is drawn with a shorter pattern at a similar speed.
  - At 25 kHz the drum, bones and nerve are still, while the air still vibrates.
- **The chain and herrings.** The impulses start in the cochlea, not the ear drum.
- **CFIFA:** 1500 ÷ 500 = 3.0 m; 340 ÷ 20 000 = 0.017 m, where the unconverted 17 m is correctly identified as the 20 Hz
  wavelength; 5000 ÷ 250 = 20 m; 1.5 kHz in water → 1.0 m, unconverted 1000 m.
- **Rungs:**
  - rung 1 options and replies;
  - rung 2: 3400 ÷ 2000 = 1.7 m, with "frequency unchanged in the wood";
  - rung 3: the chain and both herrings. A dog does hear 40 kHz, since the dog range reaches about 45 kHz;
  - rung 4: points and rejects.
- **The hook.** Dog whistles run at about 23–54 kHz, above the human limit.

**Frozen items.**
- q2 ("Why is ultrasound used for foetal scanning rather than X-rays?", wx2 reverses bone/soft-tissue absorption) is
  withheld (B3-W2) and absent from the page.
- q1 (SONAR, "divide the echo time by 2") is the only bank item. It is correct and on its true route (TH), but see A-2.
- The `equations` string "d = v × t / 2", the `common_mistake` field and the `higher` field are not rendered.

### REQUIRED

None.

### ADVISORY

| # | lesson · routes | where | note |
|---|---|---|---|
| A-4 | sound-waves-hearing · TH | `keyLines[4]` | "Speed: solid > liquid > gas." → "Speed: usually solid > liquid > gas." This matches explainer 3's "usually fastest in solids". The order holds for typical materials but is not a law: some liquids carry sound faster than some solids, as examination C5 notes. Key-note text is re-cuttable, not frozen. |
| A-5 | sound-waves-hearing · TH | practice bank (frozen q1 SONAR) | This page's only bank item tests echo timing, which this lesson deliberately does not teach. The examination (§4) calls it usable here "only if the lesson keeps a short ultrasound bridge", and the lesson has no bridge. The science is right and the route is right, so this is not a required change. The commander should consider withholding it on this slug. The same content is taught and tested on `waves-detection-exploration`, and that lesson's frozen q2 is the same method. Bank size then becomes 0, which goes on Mide's list either way. |
| A-6 | sound-waves-hearing · TH | key fact | "The conversion only works from 20 Hz to 20 kHz." → "In a human ear, the conversion only works from about 20 Hz to 20 kHz." The hook is about a dog that hears beyond that range, so the key fact should be unambiguously about humans. |

**Verdict: SCIENCE PASS.**

---

## 3. waves-detection-exploration — AQA 8463 4.6.1.5 (physics only, HT only)

**Routes: TH only.** This is correct (confirmed from the spec heading), and there is no 8464 counterpart. The page
contains every element of 4.6.1.5:
- ultrasound defined as above the upper limit of hearing (explainer 3, rung 3);
- partial reflection at boundaries between media (scan step 1, panel, rung 3);
- timing → distance (scan step 2, CFIFA, rung 2);
- medical and industrial imaging (explainer 4, CFIFA Q2);
- seismic waves from earthquakes; P longitudinal, at different speeds in solids and liquids; S transverse and not through
  liquids (explainer 1, sort);
- P and S as evidence for the structure **and size** of the core (bench steps 2–4);
- echo sounding for depth and objects in deep water (explainer 4, CFIFA Q1, rung 2);
- WS 1.1 "new evidence … not directly observable" (explainer 2), which was missing from the source.

The imprecise source claims are not shown:
- C5 "refraction shows the core is denser";
- C7/C8 shadow-zone definitions. The bench now separates them correctly: S shadow from about 104° to 180°, which still
  receives P; P shadow from about 104° to 140°;
- the 4.6.2.2 EM absorb/transmit/refract/reflect block.

**Figure geometry, checked numerically and visually**
- **Radii.** Outer core 139/255 = 0.545 R and inner core 48/255 = 0.188 R. Real values: 3480/6371 = 0.546 and
  1220/6371 = 0.19. **To scale**, as the legal line says.
- **S-wave rays.** The rays are quadratic Béziers whose deepest point is at about 0.875 R cos(θ/2). They are concave
  towards the surface, which is the right sense for speed increasing with depth.
  - A ray reaches the real core when cos(θ/2) < 0.545/0.875, i.e. θ > ≈103°. The drawn S shadow edge (103°) therefore
    matches the stated ~104°.
  - For the dashed bigger core (173/255 = 0.678 R) the grazing ray lands at θ ≈ 78.4°. That matches "about 78°", and it
    correctly moves the edge towards the earthquake.
- **P-wave rays.**
  - The 100° Bézier just misses the core (deepest point 0.56 R > 0.545 R) and lands before 104°.
  - Both core-crossing rays bend **towards** the normal on entry (incidence ≈ 80° → refraction 62–68°), as they should:
    P slows in the outer core.
  - They bend **away** from the normal on exit, landing at 140° and 150°.
  - The 0°→180° ray passes straight through the centre. P recorded at 150° and 180° but not 120° is correct.
- **Arcs.** The S arc runs 103°–180° and the P arc 103°–140°, consistent with the stated edges.
- **Scan.** Boundaries are at 2, 5 and 8 cm (50 px per cm). Echo times 2d ÷ 1540 m/s are 0.026, 0.065 and 0.104 ms,
  all correct, and the spikes are placed on the time axis at those values. The deeper echoes are drawn weaker. C ÷ A is
  4 in both time and depth, so the keyed answer "four times as deep" is right, and both distractor replies are true.

**Verified correct**
- **Bench step keys and replies:**
  - step 1: all six would record S-waves in a solid Earth;
  - step 2: a liquid layer. The "fading" and "hollow centre" replies are correct, and P reaching 180° rules out an
    empty centre;
  - step 3: refraction at the core boundary. "Absorbed" and "cannot cross liquid" are rebutted from the 150°/180°
    records;
  - step 4: the edge moves closer.
- **The misconception panel** (liquid *outer* core).
- **The sort, all eight cards:** "both refract" and "arrives first = P" are correct, and S is never recorded beyond about
  104°.
- **The scan panel** (partial reflection, the rest transmitted).
- **Explainer 4.** Ultrasound is non-ionising; industrial crack detection; echo sounding.
- **The equation card.** s = v t; the halving is called a method step, which is right (examination C22).
- **CFIFA:**
  - the SONAR FIFA is verbatim: 1500 × 0.06 ÷ 2 = 45 m;
  - 0.080 ms → 1540 × 8.0 × 10⁻⁵ = 0.1232 m → 0.062 m, unconverted ≈ 62 m;
  - 1500 × 0.12 = 180 → 90 m;
  - 6000 × 2.0 × 10⁻⁵ = 0.12 → 0.060 m, unconverted 60 m.
- **Rungs:**
  - rung 1 is frozen q1 (key and wx1–wx3 correct; P is detected at 180°);
  - rung 2: 160 ms → 0.16 s; 1500 × 0.16 = 240 → 120 m;
  - rung 3: the four links and both herrings;
  - rung 4: the levels, the seven points (all accurate, including the curved paths from gradual speed change) and both
    rejects.
- **Frozen q2 in the bank.** 300 m is the key; 600, 3750 and 150 m are correct as stated, with correct feedback.
- **The key note and key fact.**

**Frozen items.** None need withholding (q1 and q2 are both correct for TH). The frozen "d = v × t / 2" survives only
inside the verbatim FIFA and the verbatim key-note line "Echo sounding: d = vt/2." Both are acceptable: the halving is
right, and the card explains that it is a method step.

### REQUIRED

None.

### ADVISORY

| # | lesson · routes | where | note |
|---|---|---|---|
| A-7 | waves-detection-exploration · TH | hook `<p>` | "…geologists can tell you how big the core is, and which part of it is solid and which is liquid." → "…geologists can tell you how big the core is, and that part of it is liquid." This is true as written: inner-core solidity is also seismic evidence. But the lesson never teaches how solidity is known, and the spec asks only for the liquid outer core and the size of the core. The promise in the hook is then never paid off. |
| A-8 | waves-detection-exploration · TH | `earthSvg` P-ray list (`pRays`) | The two core-crossing rays, `[pt(0,R), pt(48,rc), pt(92,rc), pt(140,R)]` and `[pt(0,R), pt(47,rc), pt(103,rc), pt(150,R)]`, enter the core about 1° apart but leave 11° apart, and cross near the exit. Each is refracted in the right sense (checked above), and the legal line says the paths are schematic, so this is not an error. For a cleaner plate, separate the entry points, e.g. 44° for the 150° ray. Optional. |

**Verdict: SCIENCE PASS.**

---

## Frozen items still served that should be withheld

| lesson · route | item | status |
|---|---|---|
| types-of-em-waves · all | q1 "Which EM wave has the highest frequency?" | Withheld (B3-W7). Confirmed absent from the page. |
| sound-waves-hearing · TH | q2 "Why is ultrasound used for foetal scanning rather than X-rays?" | Withheld (B3-W2). Confirmed absent from the page. |
| sound-waves-hearing · TH | q1 "Why must you divide the echo time by 2 in SONAR calculations?" | **Not wrong; recommend withholding on this slug** (A-5). It tests content this lesson does not teach. Commander's call. |
| waves-detection-exploration · TH | — | None. |

## For Mide

None on science. The specs are unambiguous: 8463 4.6.1.4 and 4.6.1.5 are physics only and HT only, and 4.6.2.1 is
identical to 8464 6.6.2.1. The bank sizes are 1 (EM), 1 (sound, 0 if A-5 is taken) and 2 (detection). They sit below
the content-standards floor and go on Mide's list as the authors noted, but they are not a science defect.

## Verdicts

| lesson | verdict |
|---|---|
| types-of-em-waves | **SCIENCE PASS** |
| sound-waves-hearing | **SCIENCE PASS** |
| waves-detection-exploration | **SCIENCE PASS** |

---

## Round 2 — commit 2ddea6225 (feat/ks4-batches)

I checked the commit's diff to the three lesson sources, then grepped the built pages. The browser was not needed: every change is either text or a geometry constant I could check by hand.

| lesson | change | check | result |
|---|---|---|---|
| types-of-em-waves | Explainer wavelength → "the distance from a point on one wave to the same point on the next wave" (A-1) | This is the spec definition (4.6.1.2 / 6.6.1.2). It is present on all four built routes, and the old gloss is gone. | Correct |
| types-of-em-waves | Higher Q2 close → "330 000 m: a wavelength of 330 km for a phone signal" (A-2) | 3.0 × 10⁸ ÷ 900 = 333 333 m ≈ 330 km. The aerial claim is gone. The new close is in the logic of every route's page and shows only on Higher, as before. | Correct |
| types-of-em-waves | `p1Reveal` trimmed to "The groups join with no gaps: one continuous spectrum." | This is still true. The "shorter wavelength going down" point is still carried by the figure title, the key fact and the key note. | Correct |
| sound-waves-hearing | Key note "Speed: usually solid > liquid > gas." (A-4) | Matches the explainer's "usually". | Correct |
| sound-waves-hearing | Key fact "In a human ear, the conversion only works from about 20 Hz to 20 kHz." (A-6) | 8463 4.6.1.4 gives the normal human range as 20 Hz – 20 kHz. | Correct |
| sound-waves-hearing | Tone aria-labels ("<tone>: heard / not heard"); hook reveal's last sentence trimmed | These are accessibility and wording changes only, with no science claim. | Correct |
| waves-detection-exploration | Hook ends "…how big the core is, and that part of it is liquid." (A-7) | Matches 4.6.1.5 (structure and size of the core; S-waves cannot travel through a liquid). | Correct |
| waves-detection-exploration | The P-wave ray to 150° now enters the core at 44° (A-8) | **Entry.** The incoming segment reaches the core boundary from outside: the closest approach falls beyond the entry point. The angle of incidence is ≈ 76° and the angle of refraction ≈ 60°, so the ray bends towards the normal (P-waves slow in the outer core). **Exit** at 103°: ≈ 60° inside → ≈ 79° outside, bending away from the normal. **Crossing.** The two core-crossing rays (44°→103°→150° and 48°→92°→140°) no longer cross: the 48–92 chord lies inside the 44–103 arc, and the exit legs keep their order. | Correct, and cleaner |
| waves-detection-exploration | Step 4: S rays drawn faded, without ✕ marks; station badges dimmed to 35 % | This is presentation only. The records and the dashed bigger core with its grazing S path at ≈ 78° are unchanged. | Correct |

No new science defects. Nothing route-wrong has been introduced: everything taught on the EM page is still base, and the other two pages remain TH-only.

### Final verdicts (round 2)

| lesson | verdict |
|---|---|
| types-of-em-waves | **SCIENCE PASS** |
| sound-waves-hearing | **SCIENCE PASS** |
| waves-detection-exploration | **SCIENCE PASS** |

A-5 (withholding the SONAR bank item on `sound-waves-hearing`) stays a commander's call. It is not a science defect.
