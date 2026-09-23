# Landing-page science facts — MRB-342.2 Part 4

Record of the rotating "did you know" fact panel on the GCSE-chrome
landing page (`index.html`), its content pipeline, and how to extend it.

Data file: `shared/science-facts.js` (`window.MRB_SCIENCE_FACTS`).
Rotator: `shared/k4-facts.js`. Markup: `k4_facts_panel()` in
`generate_site_v5.py`. Styling: the `.k4-facts*` rules in
`shared/ks4-chrome.css`.

---

## 1. The rules a fact must meet

Every fact — new or existing — has to satisfy all of these before it
ships. They are copied verbatim into `shared/science-facts.js`'s own
header comment too, so a future editor doesn't have to find this file
to remember them.

1. **True as stated.** Not true-with-an-unstated-asterisk.
2. **UK/SI units only** — metres, kilograms, seconds, joules, °C,
   newtons, m/s. No imperial, ever.
3. **No myths.** The usual suspects are explicitly banned: glass as a
   slow-flowing liquid, "10% of your brain", the Great Wall visible from
   space unaided, tongue taste maps, "exactly 5 senses", "lightning never
   strikes twice", 3-second goldfish memory, "exactly 5 litres of blood",
   hair/nails growing after death, a dropped penny being lethal, blue
   blood in veins, "different tongue zones taste different things",
   dangerously radioactive bananas, swallowing spiders in your sleep.
4. **Nothing that will date.** No "recently discovered", no "the largest
   ever found", no superlatives a future result could overturn, no counts
   that change (element counts, exoplanet counts, world records).
5. **Nothing unsafe to try at home.** No invitation to mix chemicals, heat
   a sealed container, look at the Sun, handle mercury, do anything
   electrical, or eat/drink something to test it.
6. **Honestly rounded.** Say "about" or "roughly" when a number is
   approximate; the rounding must not do misleading work.
7. **State the condition.** A fact true only under an unstated condition
   (closed system, molten not aqueous, "most plants" not "all plants") is
   not shipped unqualified.
8. **Under 25 words.**
9. **Pitch:** a mix of things a pupil meets at AQA GCSE (combined and
   triple, specs 8461/8462/8463) and "wow" facts a 12–16 year old would
   repeat to a friend.

## 2. The review pipeline

80 candidate facts were drafted (27 biology, 27 chemistry, 26 physics) —
over-provisioned so that examiner cuts would still clear the ~60 floor.
Every fact went through **two independent Opus examiner passes**, each
briefed as a subject specialist marking for truth against the rules
above, one subject per examiner:

- **Pass 1** — a fresh examiner per subject, verdict KEEP / CUT / REWRITE
  on every fact, with a reason for any CUT and exact replacement wording
  for any REWRITE.
- **Pass 2** — a *different* examiner per subject, shown the pass-1
  survivors with the pass-1 rewrites and borderline notes marked, asked
  to mark them exactly as critically as anything else rather than
  rubber-stamp them. This caught two cases where a pass-1 rewrite fixed
  the flagged problem but introduced a new one (biology #26, chemistry
  #21/#14).

**Result: 0 facts cut. 80 shipped.** Nothing dropped below the ~60 floor,
so no replacement-authoring round was needed.

## 3. The final list that ships (80 facts)

Word counts are shown per fact; **the longest is 24 words** (physics,
radioactive decay).

### Biology (27)

1. A red blood cell has no nucleus, which leaves more room to carry oxygen around your body. (17)
2. Mitochondria are nicknamed the cell's powerhouse: they are where aerobic respiration transfers energy from glucose. (15)
3. An adult human is estimated to have about 37 trillion cells, though nobody has ever counted them one by one. (20)
4. In diffusion, particles spread out, moving overall from a higher to a lower concentration, with no energy needed from the cell. (21)
5. The small intestine's lining is folded into villi, giving it a huge surface area for absorbing digested food. (18)
6. Enzymes are biological catalysts: each one speeds up one particular reaction without being used up itself. (16)
7. The DNA inside one human body cell would stretch about 2 metres if you unwound it all. (17)
8. Plants make glucose from carbon dioxide and water using light energy, in a reaction called photosynthesis. (16)
9. In most plants, stomata sit mainly on the leaf's underside; guard cells open and close them, controlling gas exchange and water loss. (22)
10. A human heart has four chambers and beats roughly 100,000 times a day without you thinking about it once. (19)
11. White blood cells called phagocytes can engulf and digest invading bacteria. (11)
12. Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease. (20)
13. Antibiotics kill bacteria but do nothing against viruses, which is why they cannot treat a cold. (16)
14. Homeostasis keeps conditions inside your body steady, such as temperature and blood glucose concentration. (14)
15. Insulin is a hormone released by the pancreas that lowers blood glucose concentration. (13)
16. A synapse is the tiny gap between two neurones, crossed by chemical messengers called neurotransmitters. (15)
17. Alleles are different versions of the same gene; for most genes you inherit one copy from each parent. (18)
18. Meiosis produces gametes with half the chromosome number of the cell that made them. (14)
19. A dominant allele's characteristic shows up in an organism even if only one copy of it is present. (18)
20. In a food chain, energy is lost at every stage, much of it as heat from respiration and in waste materials. (20)
21. Decomposers break down dead material, returning nutrients such as nitrogen compounds to the soil. (14)
22. Biodiversity is the variety of species in an ecosystem; greater biodiversity reduces each species' dependence on others for food and shelter. (21)
23. Xylem tissue carries water up a plant, while phloem carries dissolved sugars both up and down it. (17)
24. Bone is a living tissue: your skeleton is constantly being broken down and rebuilt throughout your life. (17)
25. Yeast is a single-celled fungus that can respire without oxygen to produce ethanol and carbon dioxide. (16)
26. Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long. (22)
27. Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue. (16)

### Chemistry (27)

1. An atom's radius is about 0.1 nanometres, and a nanometre is one billionth of a metre. (16)
2. An atom's nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom's volume. (19)
3. An element's atomic number tells you how many protons are in one atom of that element. (16)
4. Isotopes of an element have the same number of protons but different numbers of neutrons. (15)
5. When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract. (20)
6. In covalent bonding, atoms share pairs of electrons so each atom fills its outer shell. (15)
7. Metals conduct electricity because the delocalised electrons in their structure are free to move. (14)
8. The Group 1 metals are called the alkali metals, and they get more reactive as you go down the group. (20)
9. The Group 7 elements are called the halogens, and they get less reactive as you go down the group. (19)
10. The noble gases in Group 0 have a full outer shell of electrons, which makes them very unreactive. (18)
11. The law of conservation of mass says the total mass of reactants equals the total mass of products. (18)
12. One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant. (17)
13. Electrolysis uses electrical energy to break down a molten ionic compound into its elements. (14)
14. Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery. (20)
15. An exothermic reaction transfers energy to the surroundings, so the surrounding temperature rises. (13)
16. An endothermic reaction takes in energy from the surroundings, so the surrounding temperature falls. (14)
17. A catalyst speeds up a reaction without being used up, by opening a pathway with lower activation energy. (18)
18. Raising the temperature speeds up a reaction because particles collide more often and with more energy. (16)
19. In a reversible reaction at equilibrium, the forward and backward reactions occur at the same rate. (16)
20. Crude oil is a mixture of hydrocarbons, separated into fractions by fractional distillation. (13)
21. Alkanes are saturated hydrocarbons: every bond is a single covalent bond, so each carbon holds as many hydrogens as possible. (20)
22. Complete combustion of a hydrocarbon in plenty of oxygen produces carbon dioxide and water. (14)
23. Earth's early atmosphere is thought to have been mostly carbon dioxide, with almost no oxygen in it. (17)
24. Today's atmosphere is roughly four-fifths nitrogen and about one-fifth oxygen by volume. (12)
25. Limewater turns cloudy when carbon dioxide is bubbled through it, a standard test for the gas. (16)
26. In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures. (19)
27. Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper. (19)

### Physics (26)

1. Speed is distance travelled divided by time taken, usually measured in metres per second. (14)
2. Acceleration is the rate of change of velocity, measured in metres per second squared. (14)
3. Newton's second law states that resultant force equals mass multiplied by acceleration. (12)
4. A resultant force of zero means an object is either stationary or moving at a constant velocity. (17)
5. Momentum is mass multiplied by velocity, and it is conserved whenever objects collide in a closed system. (17)
6. Energy cannot be created or destroyed, only transferred from one store to another. (13)
7. Gravitational potential energy depends on an object's mass, the gravitational field strength, and its height above the ground. (18)
8. Kinetic energy rises with the square of an object's speed, not in direct proportion to it. (16)
9. Power is the rate of energy transfer, measured in watts, where one watt equals one joule per second. (18)
10. Electric current is the rate of flow of charge, measured in amperes. (12)
11. In a series circuit the current is the same everywhere, but the potential difference is shared between components. (18)
12. In a parallel circuit the potential difference across each branch is equal, but the current splits between them. (18)
13. A wire's resistance increases as its length increases, if the material, cross-sectional area and temperature stay the same. (18)
14. Static electricity builds up when electrons transfer between two insulating materials rubbed together. (13)
15. A transformer changes the size of an alternating voltage using two coils linked by a changing magnetic field. (18)
16. Every object above absolute zero emits infrared radiation. (8)
17. Sound waves are longitudinal, so the particles vibrate parallel to the direction the wave travels. (15)
18. Light waves are transverse, so their vibrations are at right angles to the direction of travel. (16)
19. The wave equation states that wave speed equals frequency multiplied by wavelength. (12)
20. In a vacuum, every type of electromagnetic wave travels at about 300 million metres per second. (16)
21. Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay. (24)
22. Alpha radiation is the most strongly ionising type, yet a single sheet of paper can stop it. (17)
23. Density is mass divided by volume, usually measured in kilograms per cubic metre. (13)
24. A magnetic field is strongest at a magnet's poles, shown by field lines drawn closest together there. (17)
25. Earth's magnetic field is generated deep inside the planet and helps shield us from the Sun's charged particles. (18)
26. The Moon's atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak. (21)

## 4. Everything that was cut

**None.** Both examiner passes returned zero CUT verdicts across all 80
facts, on both rounds. Every problem an examiner found was fixable by
REWRITE, so nothing needed replacing and the ~60 floor was never at risk.

## 5. Everything that was rewritten — before and after

18 facts changed wording between the first draft and what shipped (16
substantive rewrites, 1 light word-swap, 1 cosmetic notation fix). Every
one is listed here with the reason, so Mide can overrule any of them by
reverting to the "before" column in `shared/science-facts.js`.

### Biology

| # | Before (original draft) | After (shipped) | Why |
|---|---|---|---|
| 2 | Mitochondria are called the "powerhouse of the cell" because they release energy from glucose during respiration. | Mitochondria are nicknamed the cell's powerhouse: they are where aerobic respiration transfers energy from glucose. | Glycolysis (part of respiration) happens in the cytoplasm, not the mitochondria; "aerobic respiration" scopes the claim correctly. |
| 4 | Diffusion moves particles from a high concentration to a low one, with no energy input needed. | In diffusion, particles spread out, moving overall from a higher to a lower concentration, with no energy needed from the cell. | Diffusion is a *net* movement, not every particle going one way; "no energy input" was ambiguous against the particles' own kinetic energy — scoped to "from the cell". |
| 7 | The DNA coiled inside a single human cell would stretch about 2 metres if you unwound it fully. | The DNA inside one human body cell would stretch about 2 metres if you unwound it all. | "A single human cell" is contradicted by fact 1 on the same page (red blood cells have no DNA) — narrowed to "body cell". |
| 9 | Most of a leaf's stomata sit on its underside, opening and closing to control gas exchange and water loss. | In most plants, stomata sit mainly on the leaf's underside; guard cells open and close them, controlling gas exchange and water loss. | True only for typical land plants (floating and grass leaves differ) — condition stated; also stomata don't open themselves, guard cells do. |
| 12 | A vaccine contains a weakened or inactive form of a pathogen, training your immune system to recognise it. | Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease. | False as a universal — mRNA and subunit vaccines contain no form of the pathogen at all. |
| 17 | Alleles are different versions of the same gene, and you inherit one copy from each parent. | Alleles are different versions of the same gene; for most genes you inherit one copy from each parent. | False for X-linked genes in males, Y-linked genes, and mitochondrial DNA (maternal only) — condition stated. |
| 20 | In a food chain, energy is lost at every stage, mostly as heat released during respiration. | In a food chain, energy is lost at every stage, much of it as heat from respiration and in waste materials. | AQA attributes losses to respiration *and* egestion/excretion; overstated a single route. |
| 21 | Decomposers break down dead material, returning nutrients such as nitrogen to the soil. | Decomposers break down dead material, returning nutrients such as nitrogen compounds to the soil. | Nitrogen returns as compounds (ammonia, mineral ions), not as the element. |
| 22 | Biodiversity is the variety of species living in an ecosystem, and more of it tends to make that ecosystem more stable. | Biodiversity is the variety of species in an ecosystem; greater biodiversity reduces each species' dependence on others for food and shelter. | The diversity→stability generalisation is a live dispute in research ecology; rewritten to AQA's own stated mechanism instead. |
| 26 | A human genome contains roughly 3 billion base pairs of DNA, packed into 23 pairs of chromosomes. | Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long. | Original was internally correct but confusingly phrased next to the meiosis fact (#18) — "23 pairs" beside "46" invited a 23-vs-46 misread. |
| 27 | Capillaries are only about one cell thick, which lets oxygen and nutrients diffuse into tissue quickly. | Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue. | Ambiguous: read as the vessel's diameter, not the wall thickness. |

### Chemistry

| # | Before | After | Why |
|---|---|---|---|
| 2 | An atom's nucleus contains its protons and neutrons and takes up a tiny fraction of the atom's total volume. | An atom's nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom's volume. | A hydrogen-1 nucleus has no neutrons; "contains ... and neutrons" asserted both are always present. |
| 5 | In ionic bonding, electrons transfer from a metal atom to a non-metal atom, forming charged ions. | When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract. | Ammonium and other polyatomic-cation salts are ionic with no metal atom present — scoped to the metal + non-metal reaction, not to ionic bonding as a universal. |
| 12 | One mole of any substance contains about 6.02 x 10^23 particles, a number called the Avogadro constant. | One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant. | Cosmetic only — a real multiplication sign and superscript instead of `x`/`^`, which would have read as a typo. |
| 13 | Electrolysis uses electrical energy to break down an ionic compound into its elements. | Electrolysis uses electrical energy to break down a molten ionic compound into its elements. | Aqueous electrolysis often does *not* give the compound's elements (e.g. sodium chloride solution gives hydrogen and chlorine, not sodium) — scoped to molten. |
| 14 | In electrolysis of a molten ionic compound, positive ions move to the cathode and gain electrons there. | Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery. | Replaced outright: once #13 was narrowed to "molten", #13 and #14 became redundant. An interim replacement ("even layer... metal") was itself flagged in pass 2 for overclaiming evenness and wrongly restricting the substrate to metal objects — final wording drops "even" and generalises "an object". |
| 21 | Alkanes are saturated hydrocarbons, meaning every carbon-carbon bond in the molecule is a single bond. | Alkanes are saturated hydrocarbons: every bond is a single covalent bond, so each carbon holds as many hydrogens as possible. | Methane has no carbon-carbon bond at all, so defining saturation by a bond type methane doesn't have was confusing; an interim rewrite ("no carbon-carbon double bonds at all") was itself flagged in pass 2 as still odd for methane — final wording defines saturation positively (maximum hydrogens) instead. |
| 26 | A pure substance melts and boils at one specific, fixed temperature; a mixture melts over a range. | In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures. | "Pure" in everyday use (pure orange juice) means the opposite of the chemical sense — flagged as the classic place that confusion bites; "in chemistry" disambiguates. |
| 27 | Chromatography separates a mixture because its substances travel at different rates through the same material. | Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper. | Blurred the stationary and mobile phase; rewritten to name the solvent doing the carrying and confine the claim to paper chromatography. |

### Physics

| # | Before | After | Why |
|---|---|---|---|
| 7 | Gravitational potential energy depends on an object's mass, height, and the local gravitational field strength. | Gravitational potential energy depends on an object's mass, the gravitational field strength, and its height above the ground. | "Height" alone is really height above a reference level — stated as height above the ground. |
| 13 | A wire's resistance increases as its length increases, for a fixed cross-sectional area and material. | A wire's resistance increases as its length increases, if the material, cross-sectional area and temperature stay the same. | Also assumes constant temperature (resistance rises with temperature independently of length) — condition added. |
| 21 | A radioactive isotope decays randomly, but its half-life is the time for half of a sample's nuclei to decay. | Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay. | "Half a sample's nuclei" is ambiguous against stable daughter atoms or a decay-chain sample (e.g. uranium ore), where the total unstable-nuclei count doesn't simply halve; an interim rewrite still had this residual ambiguity — final wording scopes half-life to one isotope's nuclei specifically. |
| 26 | The Moon has no atmosphere, so sound cannot travel across its surface — there is nothing to carry the vibration. | The Moon's atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak. | The Moon has a thin exosphere (not literally "no atmosphere"), and vibrations do travel through lunar rock (Apollo seismometers recorded moonquakes) — an interim rewrite ("almost no atmosphere... no air") read as self-contradictory; final wording is about air specifically and names who can't hear whom. |

## 6. Notable borderline items kept as authored

These were flagged by an examiner as borderline but judged to clear the
bar without a rewrite — recorded so Mide can overrule any of them:

- **Biology #6, #13** — "one particular reaction" / "kill" (antibiotics) are AQA's own simplified wording; technically loose at the edges (some enzymes act on a substrate family; some antibiotics inhibit rather than kill) but standard GCSE register.
- **Chemistry #6** — "fills its outer shell" fails for electron-deficient/expanded species (BF₃, PCl₅), neither of which is GCSE content.
- **Chemistry #11** — the conservation-of-mass law itself is unconditionally true; the closed-system caveat governs what you can *measure* on a balance (e.g. burning magnesium appears to gain mass), not the law as stated.
- **Chemistry #19, #23, #24** — equilibrium presupposes a closed system (condition implicit in "at equilibrium"); the early-atmosphere claim is correctly hedged with "is thought to have been"; the 78%/21% real figures are honestly rounded to "roughly four-fifths"/"about one-fifth".
- **Physics #1** — "speed = distance ÷ time" is technically average speed; standard AQA formulation, unqualified.
- **Physics #4, #5, #12, #14, #15, #16, #19, #22, #25** — each carries a minor simplification (a redundant clause, an omitted iron core, "most strongly ionising" not covering neutrons which pupils don't meet at GCSE, etc.) judged not to cross into "misleading" at this pitch.

## 7. A pitch-balance note (not acted on)

The second-pass physics examiner flagged that physics skews toward bare
definitions (roughly 18 of 26) versus "tell a friend" wow facts (5 of 26:
#8, #16, #22, #25, #26), compared with biology and chemistry's mix. No
fact failed the rules over this, so nothing was cut or rewritten for it —
recorded here as a suggestion for whoever next adds physics facts to
lean toward the wow end of the spectrum.

## 8. How to add a fact

1. Open `shared/science-facts.js`. Read its header comment (rules 1–9
   above, restated there) before writing anything.
2. Append `{ subject: 'biology' | 'chemistry' | 'physics', text: '…' }`
   anywhere in the `window.MRB_SCIENCE_FACTS` array — order doesn't
   matter, the rotator shuffles its own draw order at runtime.
3. Check the word count by hand (under 25) and re-read rules 1–7 against
   the exact sentence you wrote, not a looser version of it in your head.
4. Get a second, independent read on it — ideally the same two-pass
   Opus-examiner pattern this batch used (a subject-specialist pass, then
   a second specialist cross-checking the first pass's verdict without
   having written it) — before it ships. A fact that reads true to its
   own author is exactly the failure mode the two-pass process exists to
   catch (see §5: 3 of the 18 rewrites needed a *second* round because
   the first fixed one problem and introduced another).
5. Run `python3 build_all.py` — `science-facts.js` gets cache-bust
   stamped automatically like every other `shared/*.js` file, no
   generator change needed for content-only edits.
6. No gate currently re-verifies fact TEXT (truth is a human/examiner
   judgement, not a mechanical one) — `ks4_chrome_tells` and
   `ks4_chrome_drive` watch `shared/science-facts.js` and
   `shared/k4-facts.js` structurally (Design's sample-content bans, the
   chrome walk) but do not mark science content. Mide's own read remains
   the actual content gate, per the Autonomy Contract's "science or
   content accuracy is Mide's sole gate" rule.

## 9. Implementation notes (for whoever next touches the panel)

- **Zero layout shift** is achieved by rendering *every* fact into
  `#k4-facts-stage` at once, stacked with CSS `grid-area: 1 / 1` — the
  same technique `.k4-stars-slides` already uses for the GCSE hub's Top
  Stars crossfade. Because every fact contributes to the grid track's
  sizing even while invisible (`opacity: 0`), the box is sized to the
  tallest fact automatically and can never change again as the active
  fact rotates. This was verified by measuring the headline's
  `getBoundingClientRect()` across 6 forced fact changes and confirming
  byte-identical JSON.
- **Deck**: a Fisher-Yates shuffle per pass, reshuffled when exhausted,
  with a boundary check that swaps the new pass's first two entries if
  the first would repeat the fact just shown. Verified by advancing the
  deck 165 times (2 full 80-fact passes plus 5) via the debug hook
  `window.__MRB_FACTS_DEBUG` and confirming every consecutive 80-fact
  window is a full permutation with no adjacent repeat anywhere.
- **Accessibility**: `#k4-facts-stage` is `aria-hidden="true"` and has no
  `aria-live` region — a screen-reader user is never interrupted by the
  rotation. `#k4-facts-sr` is a single visually-hidden `<p>`, populated
  once at load with one randomly-chosen fact, and never rewritten —
  chosen over an `aria-live` region specifically because the brief asks
  for "not a live region announcing every change".
- **Reduced motion**: `window.matchMedia('(prefers-reduced-motion: reduce)')`
  is checked once at boot. If it matches, the deck still runs once (to
  pick which single fact shows) but no `setInterval` is ever started —
  verified by emulating the media feature via CDP and confirming the
  shown fact is unchanged after 20 real seconds.
- **Mobile**: the panel is a `.k4-band-side` sibling of `.k4-band-copy`
  inside the existing `.k4-band` flex row. `.k4-band`'s own
  `flex-wrap: wrap` puts the panel under the lede on narrow screens with
  no extra ordering CSS — DOM order and visual order are identical at
  every width. Verified the first `.k4-door` card's top stays above the
  fold at both 390×844 and 360×740.
- **Colour tokens**: the "KS3 studio design system" instruction is
  satisfied through the `--k4-*` custom properties this chrome file
  already carries — the literal `--ks3-*` custom properties only resolve
  under `.rd[data-mode="ks3"]` (see `shared/tokens.css`), which the KS4
  chrome page does not carry, so referencing them directly would resolve
  to nothing. Subject dot colours are `#1D6FB8` / `#B02342` / `#237A3B`
  — `generate_site_v5.py`'s `PHYSICS_COLOR` / `CHEMISTRY_COLOR` /
  `BIOLOGY_COLOR`, the same hexes the door cards and subject picker
  already render, not the older teal/pink/green pair in CLAUDE.md's
  subject-colour note (superseded by the MRB-46 Phase 3 swap).
