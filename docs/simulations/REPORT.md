# Simulations — report (5 Oct 2026)

## What was built
- **Menu:** `Simulations` row in the hamburger drawer (`shared/nav.js`, `MENU`), straight after 3D Studio. Nothing else in the menu changed.
- **`/simulations/`:** three cards — Biology, Chemistry, Physics. Public, no sign-in. Light by default, with the site's Light / Dark / System control.
- **Biology, Chemistry:** a page that says "Coming soon" and nothing else (plus the back link and theme control).
- **Physics:** a list by name. Tonight: **Wave Motion Lab**, at `/simulations/physics/wave-motion-lab/`, with a "Physics" way back.
- **The lab:** Design's page served as-is (static, with its own `support.js` and `_ds/`), so it behaves exactly as it does locally. Edits to Design's file, all small:
  - her top bar (the old "MrBadmusAI" wordmark) removed; the page now carries the site's ONE mark (`brand.py`, stamped on every build), a back link and the theme control in a bar above it;
  - five hard-coded quiz-feedback colours became tokens with her original values as fallbacks, and the canvas re-reads its colours when the theme changes;
  - `sim-theme.css` holds the dark values for her `--st-*` tokens. Light is untouched.
- **Build:** `generate_site_v5.py` copies `simulations/` to the deploy tree and names it in the round-trip safety net (same as `parents/`, `go/`, `org/`).

## Second lab: Seismic Wave Lab
`/simulations/physics/seismic-wave-lab/`, from `Seismic Wave Lab.html` (one self-contained file, Design's). Changes: site chrome added (one mark, "Physics" back link, theme control), the Google Fonts link replaced by the site's own font files, title suffix. Her page already carried light and dark tokens, so it follows the theme; the Earth cross-section and seismogram plates stay light in dark mode (hard-coded drawing colours), which is her design.

Seismic physics, read as an examiner: S-waves transverse so stopped by the liquid outer core (evidence the core is liquid), P-waves longitudinal so pass through and refract at the mantle–core boundary, P-wave and S-wave shadow zones, P arrives before S, quiz answers all correct. Not checked: the exact angles and travel times in her ray data. Note: AQA 4.6.1.5 is Physics-only, so Combined pupils are not examined on it, and the page does not say so.

## Third lab: Circuit Lab
`/simulations/physics/circuit-lab/`, from `Circuit Lab.dc.html` (Design's circuit builder: drag parts onto paper, KS3/KS4 switch, 12 challenges, inspector with live readings). Served static like the Wave Motion Lab. Changes: her "MrBadmusAI" wordmark and divider removed, the site bar (one mark, "Physics" back link, Full screen, theme) added above it, her unused design bundle not published, `sim-theme.css` for the rest.
- **Dark mode:** the top bar, parts palette and inspector go dark; the workbench "paper" stays light (wires and parts are drawn for a light ground), same as the seismic plates. Her colours are written straight into the markup, so the dark rules match them by value.
- **Phone layout (new, hers had none):** below 860px the three panes stack: workbench on top, the parts in a strip you scroll sideways, the inspector beneath, and the page scrolls. The workbench keeps `touch-action:none`, so dragging a part never scrolls the page. Tested as layout and with a synthetic drag; **not tested with a real finger on a phone**.
- **Full screen:** the app is already a full-window page, so full screen just drops the site bar.
- **Physics, read as an examiner:** series and parallel behaviour, ammeter in series / voltmeter in parallel, I = V ÷ R, series resistances add, potential divider ratio, LDR and thermistor falling resistance with light and temperature, fuse blowing above its rating are all correct. For Mide: it defaults to *electron* flow with a "conventional" toggle; AQA teaches conventional current, so the default may confuse. "Double the EMF, double the current — much brighter" is right for current, and brightness (power) goes up fourfold. The AC supply runs at 0.25–2 Hz so it can be seen, not at 50 Hz mains.

## Full screen (Wave Motion Lab and Seismic Wave Lab)
A "Full screen" button in each lab's top bar (`simulations/fullscreen.js` + `fullscreen.css`, shared). It uses the browser's Fullscreen API; iPhone Safari has none, so there the page just fills the screen with the same layout. Esc or the button leaves it. Full screen keeps only the simulation, its controls and its tickboxes: Wave Motion Lab keeps the wave-type tabs, stage, play / speed / frequency / amplitude and the seven tickboxes; Seismic Wave Lab keeps the Earth, clock, play / restart / speed, legend and the two toggle rows. Everything else (titles, step guide, readouts, definitions, tally, seismogram, key words, quiz) is hidden, not removed. To give a new lab full screen: add the button markup, `data-sim="<name>"` on `<html>` and its keep-list in `fullscreen.css`.

## Where the data file is
`simulations/simulations.json` — a list of `{subject, name, path}`. `simulations/simulations.js` draws each subject page from it: at least one entry shows the list, none shows "Coming soon".

## Adding the next simulation (two steps)
1. Put its files in `simulations/<subject>/<slug>/` (an `index.html` plus whatever it needs). Give the page the same header as the Wave Motion Lab (copy it: brand + back link + theme slot).
2. Add one entry to `simulations/simulations.json`, then `python3 build_all.py`.

## Things to know
- ~~The lab loads React and Babel from unpkg at run time.~~ Fixed 11 Oct 2026: every lab now loads `/simulations/dc-runtime.js` and React from `/simulations/vendor/`. See "No CDN" below.
- Hub files `simulations.css` / `simulations.js` / `.json` are not under `/shared/`, so they carry no cache-bust stamp; they revalidate on each load.

## Physics for Mide (not changed)
1. **Wavelength and amplitude are never taught.** The header cites AQA 4.6.1.1–4.6.1.2, but the definitions cover only transverse, longitudinal, frequency and period. Amplitude has a slider and wavelength appears only in the footnote ("changing the frequency changes the wavelength") and in the readout formula. No step defines either, and no step derives v = f λ — it is a readout label only. 4.6.1.2 expects amplitude, wavelength, frequency, period and wave speed.
2. **v = f λ is shown, never worked.** The "Wave speed 1.5 m/s, v = f × λ" readout is there, but no question or step uses the equation (AQA: wave speed in m/s, frequency in Hz, wavelength in m).
3. **"Orange particle, distance moved along the wave" contradicts itself in the longitudinal wave.** The readout shows the signed displacement (e.g. +0.25 m) under that heading, while the subtitle says it "never travels with the wave" and step 3 says it "stays at 0.0 m". Transverse shows 0.0 m; longitudinal does not. Relabel it as displacement from the rest position, or show net distance (0.0 m).
4. **"Examples: ripples on water"** under transverse waves is the standard AQA example, and sound as longitudinal is right; water ripples are in fact a mix, so it is fine for GCSE but not strictly true.
5. T = 1 ÷ f, the hertz definition, compression/rarefaction, "energy not matter is transferred", and the S-wave/P-wave question are all correct and match AQA wording.
6. **"Back at rest after each one"** (the vibrations readout) is loose: at the rest position the particle is moving fastest. "Passes through its rest position" is the accurate phrase.
7. **The yellow energy highlight "rides on one crest / compression"** can leave the idea that energy sits in one crest. Energy is transferred along the whole wave; the highlight just follows one point of the pattern.
8. The "In both waves" card says particles of the material vibrate, but the transverse examples include electromagnetic waves, which need no material. The seismic-wave question (S and P waves) is Physics-only content (AQA 4.6.1.5), outside the cited 4.6.1.1–4.6.1.2.

## Changes made after the Opus review
Dark-mode contrast on the yellow energy labels fixed (fixed dark ink on yellow, both chip and canvas); slider and checkbox accent tokenised for dark; the lab's unused Design bundle and her internal README / manifest files are not published (the bundle carried the retired chevron drawing and `brand_one_mark` would have failed on it); compact theme control in the header so phones never overflow; `lang="en"` on the lab.

Known, not changed: Design's own lab layout is about 16px wider than the screen on a 320px-wide phone (the hub pages fit at 320; the lab fits cleanly at 360 and up).

## 11 Oct 2026 — Waves Practical Lab, Seismic redesign, no CDN

From Design's `Simulations Lab Redesign.zip`. Wave Motion Lab's copy in the zip was NOT a redesign (same lab, minus our header and dark fixes) and was left alone.

- **Waves Practical Lab** — `/simulations/physics/waves-practical-lab/` (AQA 4.6.1.2 required practical: ripple tank and waves on a string). Ported like the Wave Motion Lab; `data-sim="practical"` keep-list in `fullscreen.css`. Layout fixes: the "PATTERN ON THE PAPER" label sits on a backing chip; the rulers label fewer marks when narrow (0, 5, 10 … at 390px); strobe −/+ centred. Science fixes: the string's live wavelength steps counted loops on the whole string, not between markers A and B (dragging B to 0.50 m gave λ = 0.333 m; now 1.000 m), and divided by zero off resonance; the string length shows to 3 d.p. so the working is arithmetically true; "1 loop" not "1 loops".
- **Seismic Wave Lab** — same URL, now Design's redesign (house lab look, Restart-during-play double-speed bug fixed by her). Checked item by item against the old page: every step, control, seismogram, key word and quiz item is there with identical text and identical ray data. Science fixes (both were in the old page too): the tally counted S-only seismometers (solid-core "what if") as "P-waves only" — there is now an "S-waves only" row shown only when non-zero; Lehmann (1936) showed there *is* an inner core, not that it is solid. The redesign adds Hide/Show for Seismogram, Key words and Quiz, remembered per browser.
- **No CDN.** `simulations/dc-runtime.js` is Design's `support.js` with React 18.3.1 + ReactDOM served from `simulations/vendor/` (byte-identical to the unpkg files; the SRI hashes are unchanged and still checked) and Babel removed: Babel was only ever fetched for JSX `x-import`s, and no lab has one, so there is nothing to precompile. A future lab that needs one fails loudly ("precompile them") instead of reaching for a CDN. The per-lab `support.js` copies are gone. Adding a lab: `<script src="/simulations/dc-runtime.js"></script>` (root-relative, so the build cache-busts it).
- **Proof**: headless Chrome at 390 and 1366, light and dark, on all four labs and the physics page: console clean, every request to mrbadmus.com, full screen in and out, every step clicked through; practical lab v = f × λ on both set-ups; Seismic tallies sum to 24 in both models.

### Science for Mide (arguable, not changed)
Waves Practical Lab:
1. Shadow magnification is never mentioned: the paper pattern is drawn at the same scale as the water, so measured λ = true λ. Accepted at GCSE (AQA measures on the paper), but an exam question can ask why the measured λ is too large.
2. "Frozen pattern: strobe frequency = wave frequency" — it also freezes at f/2, f/3…; the strobe reaches 0.5 Hz. Common GCSE wording; stricter is "the highest strobe frequency that freezes it".
3. The motor runs at 2.99 / 4.85 / 6.71 Hz and the strobe steps in 0.1 Hz, so the pattern never fully stops creeping (one wavelength about every 20 s at best).
4. "The stopwatch still shows real time" means experiment time (4× slower on screen in slow motion).
5. The footer's "The motor frequency is not printed anywhere: you have to measure it." comes after the string sentence, where it reads as contradicting "read the frequency off the signal generator". Moving it after the ripple-tank sentence would fix it.
6. "A" is both an antinode label and marker A in the same step.
7. Quiz 4 answer 0.225 m/s from 2 s.f. data (0.23 strictly); AQA credits either.
8. The lab never explains why the string only shows a pattern at certain frequencies.
9. Ripple steps state a whole number of waves between A and B even if the markers are off the bright lines (the step tells pupils to put them on bright lines).

Seismic Wave Lab:
1. The P-wave shadow zone in Design's data is 103.5°–131.5°; textbooks say about 105°–140°. No figures are stated on the page.
2. "every S-wave that reaches the liquid outer core is stopped" — physically S converts to P at the boundary; "stopped" is standard GCSE wording.
3. Gradual speed change attributed to density changing with depth (AQA-style; really mainly stiffness). Creditworthy.
4. In the solid-core model S still shows a shadow band (104.5°–125.5°) from refraction at the boundary; pupils may ask.
5. Travel times run about 10–20% short of real values; no text claims exact values.
6. AQA 4.6.1.5 is Physics-only; Combined pupils aren't examined on it, and the page does not say so (unchanged from before).

## 15 Oct 2026 — Refraction Lab

`/simulations/physics/refraction-lab/`, from Design's `Refraction Lab (export)`. Ported like the Waves Practical Lab: site bar (one mark, "Physics" back link, Full screen, theme), her "MrBadmusAI" bar, her in-stage full-screen button and her `_ds_bundle.js` (retired chevron) removed, `/simulations/dc-runtime.js` for the runtime, `data-sim="refraction"` keep-list in `fullscreen.css`, `sim-theme.css` for dark. The lab paper and the wavefront tank stay light in dark mode (drawn as paper, like the Circuit Lab workbench); the sin i / sin r graph follows the theme.

**Mide's seven corrections, all fixed and driven in headless Chrome with real mouse input (30/30):**
1. **Ruler round the block.** Drag roughly along a side of the block (or its traced outline) and the line snaps to that whole side, corner to corner; ends snap to corners and edges. A free line now stops exactly where the ruler stopped (it used to run 0.8 cm past both ends). With any tool but Move, the block and ray box stay put, so drawing near the block no longer drags it.
2. **Block from the tray.** Hovering used to place it (the cursor check had a side effect). It now leaves the tray only when pressed and dragged, and lands where it is dropped.
3. **Normal.** Works on an outline drawn with the ruler as well as Trace outline. With the glass on the paper it refuses: "Lift the block first. The normal is drawn on the paper, not on the glass." With no outline at all it says how to make one.
4. **Ray box** 2.6 × 1.8 cm (was 3.6 × 2.6). Dragging or turning it can never push the box or its knob off the paper; turning brings it closer to the block instead.
5. **Protractor reads at once.** Placed where the ray meets the edge, it opens on the side of the normal that was clicked and lines its hairline up with the ray there: "i = 40°" where the ray went in, "r = 25°" after Flip. The hairline snaps onto a ray within 2.5°. Wrong placement is explained on the paper and in the Protractor card: nowhere near the edge, on the edge with no ray, no ray on this side ("Press Flip protractor"), hairline off the ray ("Drag the red hairline onto the ray").
6. **One number.** The "29° · 151°" pair is gone. The protractor still has its two printed scales (as a real one does), but the scale being read is drawn strong and the other faded.
7. **Wavefront tickboxes.** "Rays and angles" and "Follow one wavefront" carried a `checked` attribute, which the runtime turned into a locked (controlled) input: after one click the box looked ticked but stayed off. Now they switch off and on.

Also fixed: the page was 794px wide on a 390px phone after the graph had been drawn at desktop width (it never redrew); the graph now redraws when its card resizes and the page grid cannot grow past the screen. The ray box is drawn under the pencil work so it never hides a protractor reading. Messages clear when the tool changes.

### Science for Mide
1. **Fixed (arithmetic):** quiz Q2 offered "26°" as the answer while its own explanation gives r = 25°; sin⁻¹(sin 40° ÷ 1.5) = 25.4°. The option now reads 25°.
2. **Not changed:** refractive index and n = sin i ÷ sin r are not in the AQA 8463 specification (Snell's law is A-level). The lab's results table, graph, readout card and quiz Q6 are built on it. Keep as extension, or cut back to "r is smaller than i"?
3. **Not changed:** the practical is Physics-only (4.6.1.3, required practical 10); the wavefront explanation of refraction is Higher tier (4.6.2.2). The page says neither.
4. **New wording, mine:** at the exit point the protractor names "the angle of the ray inside the block" and "the angle of the ray leaving the block" rather than i / r, since i and r in the practical mean the entry point.

## 8 Nov 2026 — Red-shift Lab

`/simulations/physics/red-shift-lab/`, from Design's `Red-shift Lab.dc.html`. Ported like the Refraction Lab: site bar, `/simulations/dc-runtime.js`, `data-sim="redshift"` keep-list in `fullscreen.css`, `sim-theme.css` for dark. Her top bar, in-stage full-screen button, `support.js`, `_ds_bundle.js` and `F` key are gone. The stage is a dark room in both themes; the Results graph follows the theme. Every `value=` and `checked` is out of the markup and set from JS.

**GCSE / A level switch (Mide).** `GCSE | ✱ A LEVEL` in the header, also in full screen. It always opens on GCSE and is never remembered. A level shows a full-width band under the site bar and a `✱ A LEVEL` chip on the canvas on every tab. Switching keeps the tab (first step), keeps the rows and recalculates them; GCSE from the Binary tab goes to Doppler.
- **GCSE:** 12 steps, nothing off 8463 4.8.2. Table: Galaxy, Distance (Mly), Hα seen, Shift Δλ, Check. Graph: shift (nm) against distance (Mly), best fit through the origin. No speed, z, equation or age. Two Big Bang cards. Quiz Q4 is the qualitative X and Y question.
- **A level (AQA 7408 3.9.3):** 20 steps. Distances in Mpc. Table adds z and Speed away. Graph: speed against distance, `H = 70 km/s/Mpc · Age ≈ 1 ÷ H = 14 billion years`. Doppler adds a z card, Big Bang adds Glow, the quiz is its own set of eight, and there is a `5 · Binary stars` tab.

**Improvements on her file:**
1. **Graph in the stage.** From a 720px canvas the graph is a panel in the sky, and the galaxies stay left of it. One painter draws this and the Results graph.
2. **Measure on the stage.** `Hα seen [ ] nm [Record]`. The pupil still types the reading. A rejected value adds no row, keeps focus and shows the reason on the stage. A good value adds the row, clears the input and selects the next unmeasured galaxy. "Close. Zoom in." records but stays on that galaxy.
3. **Doppler shows the motion.** A dot marks where each of the last 8 waves started. Below 520px the spectrum panels stack.
4. **Saves the machine.** The drawing loop stops when the lab is scrolled off-screen. Under `prefers-reduced-motion` it starts paused. Wavefronts drop from 56 pieces to 32, skipping pieces off the canvas (strokes per frame 1407 → 394, frame time with a forced flush 3.3 → 1.6 ms at 1366).
5. **Teacher values.** `?teacher=1` shows true values and Fill all, with no visible link.

**Changed from the brief, accepted by the coordinator:**
- Steps 2, 8, 11 and 14 no longer autoplay, because their words say "Press…" and the button would already have read Pause.
- Andromeda: zoom goes to 650–662 nm, `ok` is within 0.3 nm, "close" is within 1 nm and on the blue side, and the lab value is refused. Without this its 0.66 nm shift cannot be read on a phone.
- Under 1060px the step guide sits above the stage.
- Canvas `touch-action` is `pan-y`, so a swipe on the stage scrolls the page; horizontal drags still work.
- The keys line leaves out `Space play` on spectra, where nothing plays.
- Success messages name the galaxy, and comma decimals are accepted.

**Choices made:**
- The `✱` in the switch's own label shows on GCSE. Mide's control is `GCSE | ✱ A LEVEL`, so the "no ✱ at GCSE" check excludes the control.
- Binary sliders carry no numbers, only Slower/Faster and Shorter/Longer, so the pupil reads Δλ from the strip and T from the clock; true values show only under `?teacher=1`. The clock in the controls row shows only in full screen, because the `Time` card shows it otherwise and full screen hides the cards.
- Step 6 has no equation at either level; A level gets it on the next step.
- Binary star A is green and B amber, so a star's colour cannot be mistaken for its shift.
- Shared bar on every lab: the back link loses its word at 380px and under. The home button is hidden where it was measured to overflow: Sign in at 662px and under, signed-in labels at 731px and under. The menu has Sign in and the account actions.
- "Measure 3 distant galaxies." counts down as galaxies are recorded.
- A level quiz answer positions are 3/3/2 (0: Q2, Q5, Q8; 1: Q1, Q4, Q7; 2: Q3, Q6), ruled fine. GCSE is 2/3/3.

**Proof, on the built tree, in headless Chrome with real mouse, key and touch input (347/347 at the final build):**
- Opening and steps, 39/39: 29 requests all same-origin; console clean; a fresh load and a reload after A level both open on GCSE, with no level stored; GCSE visible text clean across all 12 steps; 12 and 20 steps forward and back; keys 1 to 5; flips keep the tab.
- Measuring, 70/70: every rejection message. At 1366, 8 galaxies plus Andromeda at GCSE, flipped to A level: rows survive, H = 70 km s⁻¹ Mpc⁻¹, age 14. At 390, 6 galaxies measured from scratch at A level: H = 69.53, age 14.06.
- Controls, 14/14: sliders stay, 7 drawing checkboxes obey, slow motion wave rate 10 → 3 → 10.
- Binary and quiz, 26/26: v = 150 gives ±0.33 nm; v = 300 gives 0.65 against 0.656; T = 2 gives merges 1.0 day apart; teacher card r = 2.1 × 10⁷ km; both quizzes right, wrong and locked.
- Review checks and the site bar, 67/67: stretched light frozen at 747 nm; P and Q exactly 100 and 200 Mly; 5 minutes reads 950 million K with the stage glowing; light curve fits at 360 and 1366; chip clear at 760; star A green; Sign in hidden at 662px and whole at 663px, signed-in labels hidden at 731px and whole at 732px, on all six labs.
- Full screen, 109/109: all tabs at both levels at 1366 and 390; hidden parts checked by rendered size; 16 to 19px unused at 1366×768 at A level with no overflow; at 390 the controls need a scroll of up to about 190px.
- Pause, teacher, reduced motion and touch, 16/16: rAF 120 → 0 → 120; `?teacher=1` on and off; nothing autoplays under reduced motion; a horizontal drag moves the cursor and a vertical swipe scrolls the page.
- Widths, 6/6: no sideways scroll on 72 width, tab, level and theme combinations.
- `brand_one_mark` passes. The node run of the page's script against a stub DOM covers the sums.
- Not proved: a real phone or Chromebook, and a real signed-in session (signed-in bar widths were measured with the real labels placed in the bar).

### Science decisions
Mide left the science on this topic to Claude on 8 Nov 2026. These are decisions made, not questions. Reviewed by an independent AI examiner; no human physics check on this topic.

1. **GCSE is qualitative plus a measured shift.** The speed column, v = c × Δλ ÷ λ, the gradient and the age are A level only, because none of them is in AQA 8463 4.8.2.
2. **Frequency is A level only.** The Doppler `Frequency you see` card moved there: 3.9.3.1 covers Δf/f, and GCSE 4.8.2 speaks only of wavelength. GCSE Doppler has two cards.
3. **A level follows AQA 7408 3.9.3.1, 3.9.3.2 and 3.9.2.6.** All A level text and the Binary tab are new authoring, not Design's. The sign convention z = −v/c follows AQA, and the table's "Speed away" is z × c, positive when receding.
4. **Quasars (3.9.3.3) and exoplanets (3.9.3.4) are not covered.**
5. **"No centre" stays at GCSE as enrichment.** It is beyond 4.8.2. The microwave background is A level only.
6. **Wording.** "Dark mass" is kept: it is the AQA 8463 4.8.2 wording. "Suggest" replaces "show" for supernovae. The 1100× stretch figure and "fills all of space" are removed.
7. **The Binary `Line shift` card stays.** Δλ is a reading, not the answer: the pupil still has to catch the maximum and do the calculation.
8. **Kept from Design:**
   - The fit passes through the origin and includes Andromeda.
   - Galaxy speeds carry Design's own motions, so real readings give about 70 rather than exactly H0 × 3.26 = 70.09.
   - Andromeda reads −320 km/s, not its true −300, because a reading to 0.1 nm rounds the shift to −0.7 nm.
   - Binary orbits are drawn at a fixed size whatever r is, and one second of play is one day.

**Changes from the review:**
- Binary step 1: both lines shift at once, so it now says one star moves towards you as the other moves away, in the plane of the orbit.
- Stretched light: the wavelength stops at arrival, 430 → 747 nm (red), and no longer grows into infrared. The step says "violet", which 430 nm is.
- Big Bang labels: the model accelerates from 7.6 billion years, so "speeding up" no longer reads as future-only, and the future reads "if it keeps speeding up".
- `aOf`: a grows as √t before 50 000 years. The old numbers were up to 40× too hot at 10 minutes.
- Hydrogen and helium step: the stage sits at about 5 minutes and reads 950 million K. The clock can now say minutes.
- Sky caption: "In this survey, fainter means further away." On canvases under 390px the "Click a galaxy." half is dropped, because the sentence does not fit.
- Doppler caption: "The view follows it."
- Range check: readings above 750 nm are outside visible light.
- Expansion: P and Q are exactly 1:2 from the Milky Way.
- GCSE wording: hydrogen absorbs certain wavelengths and the red line is Hα; "the light given out never changes"; further galaxies move away faster, as evidence of expansion.
- GCSE quiz: Q2 uses galaxies M and N. Q6 is now speed increasing with distance as evidence for expansion. The Andromeda step stays.
- Card: `Temperature of space`, at both levels.
- Footers: "Doppler and Expansion not to scale"; GCSE gives "c = speed of light".
- z step: adds Δf ÷ f = v ÷ c, "for v ≪ c (optical and radio)", and how the sign of v is used.
- A level table and graph: "Velocity away", since Andromeda is negative. Doppler z and frequency cards note "equations need v ≪ c".
- A level units: km s⁻¹ Mpc⁻¹. Hubble's law step gives AQA's data booklet value, 65 km s⁻¹ Mpc⁻¹.
- Age step: put H in s⁻¹ first, 70 km s⁻¹ Mpc⁻¹ = 2.3 × 10⁻¹⁸ s⁻¹.
- AQA wording: "Cosmological microwave background radiation", in the step and quiz Q6. That option is now the longest; it stays as AQA words it.
- Supernova step: "type 1a", absolute magnitude, standard candles, "evidence suggests… is debated", and a typical light curve with the peak at about −19.3.
- Binary step 2: "speed = c × Δλ ÷ λ"; r is each star's orbit radius; the stars have equal mass.
- Also fixed in passing: readouts printed "9.5e+2 million K" for temperatures with three figures before the unit.
- Also fixed in passing, a bug in Design's file: the colour lookup for the hot early universe returned no valid colour, so the stage stayed dark before light could travel. It now glows hot blue-white, cooling to orange.
