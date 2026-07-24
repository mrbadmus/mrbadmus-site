# Bonding Port — Spec-Match Compromises (MRB-113 Phase B)

Every place the vanilla build departs from Design's `.dc.html` hero specs, and what was done instead. Nothing here changes the science; these are presentation/engineering notes.

## Animation & motion
- **No scroll-driven animation existed in the specs** — they were React state + CSS transitions. Ports keep the same click-driven transitions plus CSS `@keyframes` (electron drift, ion jiggle, bulb glow, dot-focus pulse, FIFA reveal/pop).
- **Reduced-motion:** every *looping* animation is gated. Inline-applied loops (electron sea drift, ion jiggle, bulb glow, dot-focus pulse) check `matchMedia('(prefers-reduced-motion: reduce)')` in JS and are simply omitted when reduce is set; the static end-state renders instead. One-shot transitions (layer shear, step reveal) are user-triggered and left as-is.

## Fonts & colour (tokens vs the spec palette)
- Specs used **Space Grotesk / IBM Plex** + `#C0392B`. Ports resolve fonts through the shipped tokens (`--font-display` Fraunces, `--font-mono`) on `.rd` pages, matching the exemplar. Accent **text** uses `--accent-deep #B5341A` (AA on cream); `--accent-strong #C0392B` is used only for non-text (fills, borders, hover) and is never modified.
- **Dead font link:** `redesign_css` still emits the IBM Plex / Space Grotesk `<link>` (inherited from the pilot chrome). The heroes use CSS-var fonts, so this link is now dead weight on every `.rd` bonding page. Left in to keep the pilot chrome byte-consistent; safe to drop in a follow-up (also drops the dead `.rd .theory-line { font-size }` rule the exemplar no longer needs).

## Two-State Compare
- Added an **optional `force` demo** (spec Hero 3 Config A): a force button + per-state `forced` override that swaps the callout/legend/props and drives the renderer's shear. Used by `metals-alloys`. Backward-compatible — the exemplar (no `force`) is unchanged.
- New renderers `metalLayers` and `electronSea`/`delocalised` added to the RENDERERS registry; the existing `tetrahedral`/`hexLayers` untouched.

## Dot-and-Cross Stepper
- Spec ran **one molecule per instance**. Added an **optional molecule picker** so one hero (one teaching interaction) steps through several: `ionic-bonding` → NaCl / MgO / MgCl₂ (the `tri` layout is used for MgCl₂); `covalent-bonding` → H₂ / Cl₂ / HCl.
- **`covalent-bonding` is diatomic-only** (port map §6): H₂O / CH₄ / NH₃ / CO₂ exceed the 2-atom shell geometry, so they appear as static `feature-cards` in the theory, not in the hero.

## State Toggle Lab
- Ported 1:1 (lattice / jiggle / dissolved / sheared + force→shatter). No compromise.

## FIFA Step Reveal
- Spec ran **one problem per instance**. Added an **example picker** so ≥3 escalating examples live in one hero (content-standards §2). Worked spine = frozen `st["fifas"]` per variant; practice authored per tier in `NANO_FIFA`, zipped by `build_fifa_config`.
- **Input focus:** in vanilla there is no React reconciliation, so typing in a practice `<input>` updates state **without** re-rendering (keeps caret/focus); the section re-renders only on *Check this step* / mode / example / nav. Choice-selection does re-render (no focus to lose).
- **Locked-step styling:** the spec dimmed locked steps with `opacity:0.5`, which fails AA. Replaced with a muted inset background + AA-compliant muted text (`#6B635A`) + grey badge; the "locked" state is still signalled by badge colour/shape + the hint text (never colour alone).
- Practice option key is `correct` (aligned with the mistake-check block), not the spec's `ok`.

## Categorise Bins
- Reused as-is (shipped). New configs authored from frozen `matching`.

## Activity mechanics (Match pages)
- The 8 Match pages reuse the existing `make_matching_widget` (definitions column seeded-shuffled at build time; graded by category group, position-independent). A per-load browser shuffle of *both* columns is a site-wide mechanics refinement owned by **MRB-121 Phase 2** — deliberately **not** bundled here.

## Hero titles
- Long hero titles were shortened to fit the flex header (designed for short titles like "Diamond vs Graphite") so they don't clip at 390px: "The Sea of Delocalised Electrons"→"The Electron Sea", "Electron Transfer — Dot & Cross"→"Electron Transfer", "Sharing a Pair — Dot & Cross"→"Sharing a Pair", "Giant Ionic Lattice Lab"→"Ionic Lattice Lab", "Surface Area : Volume — FIFA"→"Surface Area : Volume". The subtitle carries the detail. A `min-width:0; overflow-wrap:anywhere` safety-net on the header `h3` was also added.

## Known gaps (raise back to Design as follow-up)
- **Zoom / Scale Explorer** (nanoparticles "one atom thick" wow-moment) — never delivered anywhere; FIFA was prioritised because it clears the practice flag (port map §6). Gap remains.
- Diamond↔graphite compare-cards on `giant-covalent-structures` deliberately mirror the hero as a static reference table (the frozen theory covers both).
