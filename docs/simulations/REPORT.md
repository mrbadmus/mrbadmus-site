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

## Full screen (both labs)
A "Full screen" button in each lab's top bar (`simulations/fullscreen.js` + `fullscreen.css`, shared). It uses the browser's Fullscreen API; iPhone Safari has none, so there the page just fills the screen with the same layout. Esc or the button leaves it. Full screen keeps only the simulation, its controls and its tickboxes: Wave Motion Lab keeps the wave-type tabs, stage, play / speed / frequency / amplitude and the seven tickboxes; Seismic Wave Lab keeps the Earth, clock, play / restart / speed, legend and the two toggle rows. Everything else (titles, step guide, readouts, definitions, tally, seismogram, key words, quiz) is hidden, not removed. To give a new lab full screen: add the button markup, `data-sim="<name>"` on `<html>` and its keep-list in `fullscreen.css`.

## Where the data file is
`simulations/simulations.json` — a list of `{subject, name, path}`. `simulations/simulations.js` draws each subject page from it: at least one entry shows the list, none shows "Coming soon".

## Adding the next simulation (two steps)
1. Put its files in `simulations/<subject>/<slug>/` (an `index.html` plus whatever it needs). Give the page the same header as the Wave Motion Lab (copy it: brand + back link + theme slot).
2. Add one entry to `simulations/simulations.json`, then `python3 build_all.py`.

## Things to know
- The lab loads React and Babel from unpkg at run time (that is how Design's `.dc.html` family works). A school network that blocks unpkg.com would show a blank lab. Porting it into a vanilla runtime like the KS4 lessons would remove that dependency; not done tonight.
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
