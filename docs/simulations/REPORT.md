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
3. **"Distance moved along the wave: 0.0 m"** is clear for the transverse rope. For the longitudinal wave the particle does move back and forth along the line, so a pupil may read "0.0 m" as "doesn't move along it". Worth confirming the readout means net travel.
4. **"Examples: ripples on water"** under transverse waves is the standard AQA example, and sound as longitudinal is right; water ripples are in fact a mix, so it is fine for GCSE but not strictly true.
5. T = 1 ÷ f, the hertz definition, compression/rarefaction, "energy not matter is transferred", and the S-wave/P-wave question are all correct and match AQA wording.
