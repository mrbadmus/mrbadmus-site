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
