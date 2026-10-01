# KS4 batches — run report

Mide's ruling, 1 Oct 2026: Code writes the KS4 lessons. This report is
updated after each batch. Plan: `docs/ks4/BATCH-PLAN.md`. Engine:
`docs/ks4/batch-engine.md`. Brief: `docs/ks4/AUTHORING-BRIEF.md`.

## Batch status

| batch | lessons | state |
|---|---|---|
| 1 (pilot) | 14 | live since 26 Sep 2026 |
| 2 | 16 | pushed 1 Oct 2026 (`64a0cb303..09c6146a2`); live hash proof pending (see below) |
| 3 | 13 | pushed 1 Oct 2026 (`f928cd136..05cba344a`); live hash proof pending |
| 4–18 | 222 | not started (budget) |

## Batch 2

16 lessons, 52 pages (11 on all four routes, using-moles on CH TH, five
chemistry/physics-only lessons on TF TH). First Rainford teaching week: 5.

| lesson | family | routes | flagship | live (Triple Higher) |
|---|---|---|---|---|
| Chromosomes, the cell cycle and mitosis | Process | CF CH TF TH | run-the-cell-cycle stepper with DNA-mass graph | https://mrbadmus.com/triple/higher/biology/cell-biology/chromosomes-mitosis.html |
| Eukaryotes and prokaryotes | Contrast | CF CH TF TH | cell builder (animal / bacterium / both) | https://mrbadmus.com/triple/higher/biology/cell-biology/eukaryotes-prokaryotes.html |
| Enzymes | Required practical | CF CH TF TH | RP4/RP5 pH–amylase spotting tile, anomaly, means, graph | https://mrbadmus.com/triple/higher/biology/organisation/enzymes.html |
| The carbon cycle | Process | CF CH TF TH | follow one carbon atom | https://mrbadmus.com/triple/higher/biology/ecology/carbon-cycle.html |
| Decomposition | Required practical | CF CH TF TH | Triple: RP10 milk–lipase pink-to-white timer; Combined: follow a fallen leaf | https://mrbadmus.com/triple/higher/biology/ecology/decomposition.html |
| Atoms, elements and compounds | Classify | CF CH TF TH | zoom-in particle boxes | https://mrbadmus.com/triple/higher/chemistry/atomic-structure/atoms-elements-compounds.html |
| Relative formula mass | Quantitative | CF CH TF TH | formula unpacker | https://mrbadmus.com/triple/higher/chemistry/quantitative/relative-formula-mass.html |
| Using moles — calculations and limiting reactants | Quantitative | CH TH | reaction bench (0.01 mol counters) | https://mrbadmus.com/triple/higher/chemistry/quantitative/using-moles-calculations.html |
| Concentration of solutions | Quantitative | CF CH TF TH | solution bench | https://mrbadmus.com/triple/higher/chemistry/quantitative/concentration-of-solutions.html |
| Percentage yield | Quantitative | TF TH | yield bench (where product is lost) | https://mrbadmus.com/triple/higher/chemistry/quantitative/percentage-yield.html |
| Titrations | Required practical | TF TH | burette bench (RP2), concordant titres | https://mrbadmus.com/triple/higher/chemistry/chemical-changes/titrations.html |
| Metal hydroxides | Classify | TF TH | precipitate bench + unknown tubes | https://mrbadmus.com/triple/higher/chemistry/analysis/metal-hydroxides.html |
| Tests for carbonates, halides and sulfates | Required practical | TF TH | RP7 test rack of unknown salts | https://mrbadmus.com/triple/higher/chemistry/analysis/carbonates-halides-sulfates.html |
| Changes in energy | Quantitative | CF CH TF TH | store bench (×2 / ×4 / ×9) | https://mrbadmus.com/triple/higher/physics/energy/changes-in-energy.html |
| Internal energy | Model | CF CH TF TH | heating bench (ice → steam) | https://mrbadmus.com/triple/higher/physics/particle-model/internal-energy.html |
| Lenses | Model | TF TH | lens bench + tap-on-diagram ray construction | https://mrbadmus.com/triple/higher/physics/waves/lenses.html |

**New instruments** (all built in the lesson's own logic from pilot tokens; no
shared helper): every flagship above, plus the equation forge, ionic-equation
builder, spectator strike-out, titre-error sort, balance pans, burette and
spotting-tile simulations.

**Science.** Source examination: 16 files in `packs/batch-2/examination/`.
Fresh examiners (4) on every route: 13 required changes in round 1, 1 in round
2, all applied; final verdict SCIENCE PASS on all 16. Register:
`packs/batch-2/DEPARTURES.md` — 10 frozen quiz items withheld, 32 frozen
source lines not shown, 83 review changes, 6 considered-not-changed.

**Quality.** Fresh reviewers (2): round 1 FIX ×16; round 2 SHIP ×14; round 3
SHIP ×16. Reviews in `packs/batch-2/review/`.

**Pages.** `ks4_parity.py --batch batch-2`: 728/728 (1280/820/390, light and
dark, console, sideways scroll, keyboard, route layers, prerendered text).
Pilot unchanged: 54/54 pages + 17 assets equal to `ks4_pilot_manifest.json`
after the full build.

**Landing.** Rebased on `64a0cb303`; `CONSUMER_SIGNUP_ENABLED=true python3
build_all.py`; batch-2 52/52 and pilot 54/54 equal their manifests; gates
`--record-all` (ks4_chrome_drive, ks4_parity PASS) and `--check` green;
pushed `64a0cb303..09c6146a2`.

**Live proof: not run.** The session's permission classifier refused the
polling of mrbadmus.com. Run: `python3 check_ks4_live.py --batch batch-2`
(and `--batch pilot`).

**Teacher Lessons cards** link by URL (`ks4TopicHref`), and the URLs are the
old pages' URLs, so the cards now open the new lessons with no change.

## Batch 3

13 lessons, 44 pages (10 on all four routes, atom-economy on TF TH, sound and
detection on TH only). First Rainford teaching week: 6.

| lesson | family | routes | flagship | live (Triple Higher) |
|---|---|---|---|---|
| Temperature changes and specific heat capacity | Quantitative | CF CH TF TH | SHC required practical rig (RP14 Combined / RP1 Physics), results always high | https://mrbadmus.com/triple/higher/physics/particle-model/temperature-changes-shc.html |
| Changes of state and specific latent heat | Quantitative | CF CH TF TH | energy ledger: steam vs boiling water on skin | https://mrbadmus.com/triple/higher/physics/particle-model/specific-latent-heat.html |
| Particle motion in gases | Model | CF CH TF TH | live gas bench; Triple piston (pV = constant); TH bicycle pump | https://mrbadmus.com/triple/higher/physics/particle-model/particle-motion-pressure.html |
| Power | Quantitative | CF CH TF TH | the lift test (two-lane motor race) | https://mrbadmus.com/triple/higher/physics/energy/power.html |
| Types of electromagnetic waves | Model | CF CH TF TH | spectrum bench: build, then compare pairs at one speed | https://mrbadmus.com/triple/higher/physics/waves/types-of-em-waves.html |
| Sound waves and hearing | Process | TH | from air to ear stepper | https://mrbadmus.com/triple/higher/physics/waves/sound-waves-hearing.html |
| Waves for detection and exploration | Investigation | TH | read the Earth (seismic shadow zones) + ultrasound scan | https://mrbadmus.com/triple/higher/physics/waves/waves-detection-exploration.html |
| Microscopy | Quantitative | CF CH TF TH | RP1 microscope bench | https://mrbadmus.com/triple/higher/biology/cell-biology/microscopy.html |
| Mixtures and separation techniques | Classify | CF CH TF TH | separation desk | https://mrbadmus.com/triple/higher/chemistry/atomic-structure/mixtures.html |
| Conservation of mass and balanced equations | Quantitative | CF CH TF TH | sealed flask on a balance | https://mrbadmus.com/triple/higher/chemistry/quantitative/conservation-of-mass.html |
| Atom economy | Quantitative | TF TH | mass strip (AQA reactants form); TH route choice | https://mrbadmus.com/triple/higher/chemistry/quantitative/atom-economy.html |
| The Earth's early atmosphere and how it changed | Process | CF CH TF TH | run the clock | https://mrbadmus.com/triple/higher/chemistry/atmosphere/early-atmosphere.html |
| Greenhouse gases and climate change | Model | CF CH TF TH | radiation bench | https://mrbadmus.com/triple/higher/chemistry/atmosphere/greenhouse-gases.html |

**Science.** Source examination (2 Opus) found sound-waves-hearing's own spec
core missing from the frozen pack (written from the spec) and atom economy's
frozen common-mistake text teaching the wrong formula. Fresh examiners (3):
round 1 — 7 required changes; round 2 — SCIENCE PASS on all 13.
`packs/batch-3/DEPARTURES.md`: 9 frozen quiz items withheld, 36 frozen
source lines not shown, 68 review changes, 6 considered-not-changed.

**Quality.** Fresh reviewers (2): round 1 SHIP 3 / FIX 10; round 2 SHIP 13.

**Landing.** Rebased on `f928cd136`; full build; manifests equal; gates green (verify_ks3, ks4_chrome_drive, ks4_parity); pushed `f928cd136..05cba344a`. Live proof: `python3 check_ks4_live.py --batch batch-3`.

**Pages.** `ks4_parity.py --batch batch-3` 616/616. After the full build:
pilot 54/54, batch-2 52/52, batch-3 44/44 equal their manifests.

## For Mide

1. **Ee = ½ke² is base, not HT.** Two examiners read 8463 4.1.1.2/4.5.3 and
   8464 6.1.1.2 (no HT marker) and both June 2026 sheets. `findings-for-mide.md`
   row 3 is annotated; confirm.
2. **Ek and Ep: "Equation sheet" or "Learn it"?** The spec lists them as
   recall; both June 2026 sheets print them. Labelled "Equation sheet", the
   pilot's V = I R precedent (resistors-C9).
3. **Ten wrong frozen quiz items are withheld from the pages** (B2-W1…W10 in
   `packs/batch-2/DEPARTURES.md`). Rule whether to correct the frozen rows.
4. **Practice banks are tiny.** The frozen quizzes give 1–5 items per lesson
   per route, below content standards' floor of 5; withholding made some
   smaller. New items need authoring.
5. **No approved examiner tip on any batch-2 lesson.** The slot is omitted,
   as for the two pilot physics lessons.
6. **Wrong `rp` fields in the frozen data** (not shown on the new pages):
   enzymes "RP3" (is 8464 RP4 / 8461 RP5); decomposition "RP7", bread-mould
   method (is 8461 RP10, milk–lipase, biology only); metal-hydroxides and
   carbonates-halides-sulfates "RP Chemistry 4" (is 8462 RP7).
7. **Decomposition is almost all Biology-only** (8461 4.7.2.3); the old pages
   taught it to Combined. The new lesson teaches Combined only 4.7.2.2.
8. **Frozen items kept but debatable:** using-moles "0.1 mol Na + 0.05 mol Cl₂
   → Neither"; decomposition q1 (detritivores, not in spec); carbonates q2
   (HT ionic equation shown to Foundation); metal-hydroxides q2 (amphoteric).
9. **Key-note lines changed on the examiners' advice** (percentage-yield
   "usually less than 100%"; Fe³⁺ "brown"; "acidify to remove carbonate
   ions"; carbon-cycle key note replaced). Listed in DEPARTURES.
10. **Site flags as Triple-only some content AQA Combined teaches**: meiosis,
    classification, resolving forces, free-body diagrams, motion in a circle,
    wave-front refraction, thermal conductivity (planner + rainford mapping).
    Affects the routes of later batches.
11. **Rainford's Foundation sequence teaches 10 pages the site ships
    Higher-only** (BATCH-PLAN odd things).
12. **Shared Ks4Sort never ticks its rail stop** (pilot too). Fixing the
    shared block moves all 54 pilot pages; needs your yes.
13. **B2C regression on main, not this lane:** `64a0cb303` (the teacher-panel
    design port) rebuilt the B2C pages with the consumer flag off — it deleted
    `robots.txt`, `sitemap.xml` and the consumer/parents 404/error pages and
    put `noindex` back on the parents pages, undoing `37284388a` "B2C flag-on".
    This push leaves them exactly as main has them.
14. **Live proof for batch 2** needs running (`python3 check_ks4_live.py
    --batch batch-2`): this session was not permitted to poll the live site.

15. **Pilot-block defects found by batch 3** (each needs the shared block,
    so a pilot-page change): the ladder's calc rung reads "63,000"/"63 000"
    as 63 (batch lessons keep every numeric answer below 1000); `sc-for`
    inside `<table>` renders no rows.
16. **`findings-for-mide.md` row 8 holds only in part** (annotated): pV =
    constant is Physics-only but not HT; the qualitative p–T relation is base;
    only kelvin and the quantitative p/T law are outside AQA.
17. **Frozen data for batch 3**: sound-waves-hearing's pack held 4.6.1.5
    content, not its own spec point; atom-economy's frozen equation and
    common-mistake divide by products (AQA divides by reactants); nine quiz
    items withheld (B3-W1…W9); atom-economy now has no practice bank.

## Decisions I made

1. **Lesson format.** Code-authored lessons use Design's own `.dc.html`
   format, compiled by the same engine as the pilot, so the runtime, blocks,
   ladder, badges and visual language are the pilot's by construction.
2. **Pilot isolation.** Each batch ships its own `shared/ks4-*-<batch>`
   assets; the pilot's shared KS4 assets never change as batches are added,
   so the 54 pilot pages stay byte-identical. Cross-lesson links on batch
   pages resolve through a separate `shared/ks4-nav.js` covering every KS4
   subtopic.
3. **Route layers are data.** `data-route="higher|triple|triple-higher"` on
   an element; the build removes it off-route and adds the badge.
4. **Current teaching week** = week 5 (week 1 starts Sun 30 Aug 2026, the
   backend's `currentTeachingWeek()` rule). No term dates exist in either
   repo, so half-terms were assumed: weeks 5–8, then 10–16.
5. **Wrong frozen quiz items** stay verbatim in the practice bank (Mide's
   brief: keep verbatim and flag), are never ladder rungs, and are listed
   for Mide. Wrong frozen theory claims are not repeated in the re-cut
   prose. A wrong frozen `rp` field is not displayed; the RP block is
   written from the spec.
6. **Pilot classify gap left as is.** `states-of-matter`'s `sc-if`-wrapped
   section has always been unclassified; fixing it would move a pilot page,
   so the fix applies to batch lessons only.
7. **Full-build proofs set `CONSUMER_SIGNUP_ENABLED=true`**, matching what
   main's committed tree was built with; without it the B2C pages differ and
   swamp the diff.
8. **Withhold, don't show, wrong frozen quiz items** (engine `withhold`
   field). Kept verbatim in the data; never served. True-but-off-topic items
   (detritivores, SONAR in sound, Rf in mixtures, the Na/Cl₂ "Neither" key)
   stay in the bank so banks are not emptied for no science reason.
9. **Equation labels follow the June 2026 sheet the page links to** (pilot
   ruling resistors-C9): Ek, Ep, P = E/t, P = W/t, pV = constant are "On
   the sheet" even where the spec lists them as recall. The quality
   reviewer's contrary Q-CE3 was overruled.
10. **Science reviewer wins a conflict with the quality reviewer** on numbers
    (conservation-of-mass rung 2 = 640 g); quality wins on presentation.
11. **B2C files restored to main's state on both pushes.** Main's latest
    build output (64a0cb303) has the consumer flag off; this lane does not
    change another lane's surface (reported in For Mide 13).
12. **Live hash proof not run.** The session's permission classifier
    refused polling mrbadmus.com; per its instruction I did not route around
    it. Cloudflare deploys from main automatically; the proof command is in
    For Mide 14.
13. **Batch 3 started after batch 2 was pushed and its full build, gates and
    manifests were proved**, not after a live proof (see 12).
14. **Adjacent-lesson rule enforced**: lessons taught close together in one
    topic may not share a hook, flagship or line-up (decomposition's hook was
    rewritten; slh's cooling-curve step replaced).
15. **Ladder answers kept below 1000** to dodge the shared parser defect
    rather than editing the pilot block.
16. **Reviewers time-boxed** after two stalled for hours on hung headless
    Chrome calls; round-2 confirmations read source and rendered text first.
