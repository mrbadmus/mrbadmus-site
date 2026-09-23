# Landing-page science facts — MRB-342.2 Part 4

Record of the rotating "did you know" fact panel on the GCSE-chrome
landing page (`index.html`), its content pipeline, and how to extend it.

Data file: `shared/science-facts.js` (`window.MRB_SCIENCE_FACTS`).
Rotator: `shared/k4-facts.js`. Markup: `k4_facts_panel()` in
`generate_site_v5.py`. Styling: the `.k4-facts*` rules in
`shared/ks4-chrome.css`.

⚠️ **This document covers TWO rounds.** Round 1 shipped 80 facts, two
Opus passes, zero cuts. Mide reviewed the shipped list and found it
overwhelmingly bare spec-recall with almost no "wow" — round 2 cut 36 of
those 80 and replaced them with 32 newly-drafted, newly-examined "wow"
facts, landing at **76 facts, roughly half spec-facing and half wow**.
Both rounds are recorded in full below so any individual decision from
either round can be overruled.

---

## 1. The rules a fact must meet

Every fact — round 1, round 2, or added later — has to satisfy all of
these before it ships. They are copied verbatim into
`shared/science-facts.js`'s own header comment too.

1. **True as stated.** Not true-with-an-unstated-asterisk.
2. **UK/SI units only** — metres, kilograms, seconds, joules, °C,
   newtons, m/s. No imperial, ever.
3. **No myths.** The usual suspects are explicitly banned: glass as a
   slow-flowing liquid, "10% of your brain", blue blood in veins, exactly
   5 senses, 3-second goldfish memory, tongue taste maps, "lightning
   never strikes twice", dangerously radioactive bananas, swallowed
   spiders, hair/nails growing after death, exactly 5 litres of blood, a
   dropped penny being lethal, the Great Wall visible from space unaided.
4. **Nothing that will date.** No "recently discovered", no "the largest
   ever found", no superlatives a future result could overturn, no counts
   that change (element counts, exoplanet counts, world records, and —
   added after round 2 — no population-scale estimates stated with false
   precision, e.g. "the number of stars in the universe").
5. **Nothing unsafe to try at home.** No invitation to mix chemicals, heat
   a sealed container, look at the Sun, handle mercury, do anything
   electrical, or eat/drink something to test it.
6. **Honestly rounded.** Say "about" or "roughly" when a number is
   approximate; the rounding must not do misleading work.
7. **State the condition.** A fact true only under an unstated condition
   (closed system, molten not aqueous, "most plants" not "all plants",
   "under ideal conditions") is not shipped unqualified.
8. **Under 25 words.**
9. **Pitch — roughly HALF and HALF (added at round 2, see §3).** Half
   spec-facing (things a pupil meets at AQA GCSE, combined and triple,
   specs 8461/8462/8463) and half "wow" facts a 12-16 year old would
   repeat to a friend. A wow fact should still be placeable against GCSE
   content where possible, not pure trivia, and not so far beyond the
   spec that it reads as showing off rather than teaching (round 2 cut a
   special-relativity fact for exactly this reason — see §5).

## 2. Round 1 — the original 80

80 candidate facts were drafted (27 biology, 27 chemistry, 26 physics),
each run through two independent Opus examiner passes (a subject
specialist, then a different specialist cross-checking the first pass's
verdicts without having written them). **Zero facts were cut.** 23 were
rewritten — some twice, when the second pass caught a problem the first
pass's rewrite had introduced rather than fixed. The full before/after
record for all 23 is in §7.

All 80 shipped. That list is reproduced in full in git history (the
first commit of this ticket) and is not repeated here in full, because
round 2 removed 36 of them — but every removed fact's text and cut reason
is in §4, so nothing from round 1 is lost.

## 3. Why round 2 happened

Mide read all 80 shipped facts personally and found the mechanics sound —
every fact true, hedged correctly, no unit errors — but a real shortfall
against the brief's own words: *"a mix of things pupils will meet at AQA
GCSE... **and wow facts a 12–16-year-old would repeat to a friend**."*
By his count roughly 5 of the 80 were genuinely "wow" (the 37-trillion-
cells fact, the 2-metres-of-DNA fact, the 100,000-heartbeats fact, and
two physics facts about the Moon and Earth's magnetic field); the other
~75 were correct but flat spec statements — "Speed is distance travelled
divided by time taken", "Acceleration is the rate of change of velocity" —
which read as flashcards, not facts anyone repeats to a friend. On the
site's own front door, that matters more than it would elsewhere: a
rotating panel that recites definitions tells a visitor the site is a
textbook, not a place worth a second look.

**The instruction: bring the list to roughly half spec-facing, half wow,
still ~80 total, keeping the same truth/safety/unit bar for the new
facts — if anything, harder, because a good-sounding wow fact is exactly
where a myth gets in.**

## 4. What was cut from the original 80, and why (36 facts)

None of these were cut for being FALSE — every one was still true as
shipped. They were cut because they were bare spec-recall with no scale,
comparison, or surprise element, and the rebalance needed room. Reading
the original 80 (git history, first commit) against this list shows
exactly what changed. Grouped by subject, in original list order:

### Biology (12 cut, kept 15)

| Cut | Text (as it shipped in round 1) | Why cut |
|---|---|---|
| 4 | In diffusion, particles spread out, moving overall from a higher to a lower concentration, with no energy needed from the cell. | Bare definitional recall, no wow. |
| 6 | Enzymes are biological catalysts: each one speeds up one particular reaction without being used up itself. | Bare definitional recall. |
| 9 | In most plants, stomata sit mainly on the leaf's underside; guard cells open and close them, controlling gas exchange and water loss. | Procedural/definitional, low wow. |
| 14 | Homeostasis keeps conditions inside your body steady, such as temperature and blood glucose concentration. | Bare definitional recall. |
| 15 | Insulin is a hormone released by the pancreas that lowers blood glucose concentration. | Bare definitional recall; redundant theme with 14. |
| 16 | A synapse is the tiny gap between two neurones, crossed by chemical messengers called neurotransmitters. | Bare definitional recall. |
| 18 | Meiosis produces gametes with half the chromosome number of the cell that made them. | Bare definitional recall; redundant with the kept chromosome-count fact (26 in round 1 → now "46 chromosomes"). |
| 19 | A dominant allele's characteristic shows up in an organism even if only one copy of it is present. | Bare definitional recall. |
| 20 | In a food chain, energy is lost at every stage, much of it as heat from respiration and in waste materials. | Bare definitional recall. |
| 21 | Decomposers break down dead material, returning nutrients such as nitrogen compounds to the soil. | Bare definitional recall. |
| 22 | Biodiversity is the variety of species in an ecosystem; greater biodiversity reduces each species' dependence on others for food and shelter. | Abstract, low wow; was already flagged contested-adjacent in round 1's own examiner notes even after rewrite. |
| 23 | Xylem tissue carries water up a plant, while phloem carries dissolved sugars both up and down it. | Bare definitional recall. |

### Chemistry (11 cut, kept 16)

| Cut | Text | Why cut |
|---|---|---|
| 3 | An element's atomic number tells you how many protons are in one atom of that element. | Bare definitional recall. |
| 4 | Isotopes of an element have the same number of protons but different numbers of neutrons. | Bare definitional recall. |
| 6 | In covalent bonding, atoms share pairs of electrons so each atom fills its outer shell. | Bare definitional recall. |
| 7 | Metals conduct electricity because the delocalised electrons in their structure are free to move. | Bare definitional recall. |
| 9 | The Group 7 elements are called the halogens, and they get less reactive as you go down the group. | Redundant reactivity-trend theme with the kept alkali-metals fact. |
| 10 | The noble gases in Group 0 have a full outer shell of electrons, which makes them very unreactive. | Redundant reactivity-trend theme. |
| 15 | An exothermic reaction transfers energy to the surroundings, so the surrounding temperature rises. | Bare definitional recall; redundant pair with 16. |
| 16 | An endothermic reaction takes in energy from the surroundings, so the surrounding temperature falls. | Bare definitional recall; redundant pair with 15. |
| 18 | Raising the temperature speeds up a reaction because particles collide more often and with more energy. | Bare definitional recall. |
| 19 | In a reversible reaction at equilibrium, the forward and backward reactions occur at the same rate. | Bare definitional recall. |
| 21 | Alkanes are saturated hydrocarbons: every bond is a single covalent bond, so each carbon holds as many hydrogens as possible. | Bare definitional recall. |

### Physics (13 cut, kept 13)

| Cut | Text | Why cut |
|---|---|---|
| 1 | Speed is distance travelled divided by time taken, usually measured in metres per second. | Coordinator's own named example of a definitional cut candidate. |
| 2 | Acceleration is the rate of change of velocity, measured in metres per second squared. | Bare definitional recall. |
| 4 | A resultant force of zero means an object is either stationary or moving at a constant velocity. | Bare definitional recall; redundant with the kept Newton's-second-law fact. |
| 9 | Power is the rate of energy transfer, measured in watts, where one watt equals one joule per second. | Bare definitional recall. |
| 10 | Electric current is the rate of flow of charge, measured in amperes. | Bare definitional recall. |
| 11 | In a series circuit the current is the same everywhere, but the potential difference is shared between components. | Bare definitional recall. |
| 12 | In a parallel circuit the potential difference across each branch is equal, but the current splits between them. | Bare definitional recall. |
| 13 | A wire's resistance increases as its length increases, if the material, cross-sectional area and temperature stay the same. | Bare definitional recall. |
| 15 | A transformer changes the size of an alternating voltage using two coils linked by a changing magnetic field. | Bare definitional recall. |
| 17 | Sound waves are longitudinal, so the particles vibrate parallel to the direction the wave travels. | Bare definitional recall. |
| 18 | Light waves are transverse, so their vibrations are at right angles to the direction of travel. | Bare definitional recall. |
| 23 | Density is mass divided by volume, usually measured in kilograms per cubic metre. | Coordinator's own named example of a definitional cut candidate. |
| 24 | A magnetic field is strongest at a magnet's poles, shown by field lines drawn closest together there. | Bare definitional recall. |

**Total: 36 cut, 44 kept from the original 80** (15 biology + 16
chemistry + 13 physics). The 44 kept are listed in full in §6.

## 5. Round 2 — the new wow facts: drafting and both examiner passes

38 new candidate facts were drafted to replace the 36 cut (12 biology,
16 chemistry-turned-11-after-self-edit, 13 physics — see the code
comment history for the exact pre-review count; the number reviewed
below is what actually reached the examiners: 14 biology, 11 chemistry,
13 physics = **38 total**), aimed at the shapes Mide asked for: an
ordinary number made astonishing by scale ("your bone marrow makes
2 million red blood cells a second"), a comparison that reframes
something familiar (an atom scaled up so its emptiness is visible), a
consequence nobody has thought through (what a vacuum does to sound, and
why a radio still works there), and a counterintuitive-but-checkable
result (kinetic energy already covered this in round 1; round 2 added
the eclipse-ratio coincidence and the mass-vs-weight-with-a-number fact).

**Both passes bit, hard — this was not an examiner rubber-stamping the
brief.**

### Pass 1 (fresh subject-specialist examiners)

| Subject | Reviewed | KEEP | REWRITE | CUT |
|---|---|---|---|---|
| Biology | 14 | 7 | 6 | 1 |
| Chemistry | 11 | 5 | 5 | 1 |
| Physics | 13 | 4 | 7 | 2 |
| **Total** | **38** | **16** | **18** | **4** |

Pass-1 cuts, with the examiner's own reasoning:

- **Biology — "Weight for weight, bone is stronger under compression
  than a comparable-sized rod of steel."** CUT: myth-adjacent. The
  sentence conflates two different comparisons ("weight for weight" vs
  "comparable-sized") and is the familiar "bone is stronger than steel"
  exaggeration — size-for-size, steel wins; only *specific* strength
  (per unit mass) favours bone, and the sentence never says that. No
  AQA anchor either.
- **Chemistry — "The air around you is mostly transparent because its
  main gases barely absorb visible light, unlike some other
  wavelengths."** CUT: fails the wow bar outright ("air is see-through"
  surprises nobody), the mechanism is only half right (transparency
  also needs low *scattering*, and Rayleigh scattering is why the sky is
  blue), and it has no GCSE chemistry anchor — it's EM-spectrum physics.
- **Physics — "Nothing with mass can [ever] reach the speed of light..."**
  CUT: wrong pitch. Special relativity is not on the AQA spec at all, and
  the "more energy is needed" phrasing sits one step from the
  "becomes infinitely heavy" myth physicists themselves abandoned.
  Popular-science-true is not the bar.
- **Physics — "Two nearby radio stations can interfere with each other's
  signal because radio waves, like all waves, can overlap and combine."**
  CUT: ambiguous ("nearby" in frequency or geography — only the first
  causes interference) and the invoked mechanism (wave superposition) is
  not on AQA GCSE physics's waves topic (reflection, refraction, sound,
  EM spectrum, lenses — not interference). Also flagged as the least
  "wow" item on the list.

### Pass 2 (different examiners, cross-checking pass 1's verdicts and rewrites)

Pass 2 caught **two more** problems pass 1 had missed — one where pass
1's own rewrite introduced a new factual error, one where pass 1 called
a fact merely "optional" and pass 2 concluded it had to go:

- **Biology #11 — the egg-cell fact.** Pass 1 rewrote "largest single
  cell" (vulnerable to the motor-neurone-length objection) to "largest
  by volume" — pass 2 did the arithmetic and found *volume* is worse,
  not better: a 1 m motor-neurone axon is roughly 80× the volume of an
  egg cell. Pass 2's fix drops the superlative entirely and keeps the
  genuine wow (visible without a microscope).
- **Chemistry — "Butane and methylpropane both contain four carbon and
  ten hydrogen atoms, yet they boil at different temperatures..."**
  (structural isomerism). Pass 1 called this "optional, redundant with
  the diamond/graphite fact." Pass 2 CUT it outright, for a sharper
  reason than redundancy: it is a **counterexample to a rule AQA does
  teach** (boiling point rises with molecular size) with no A-level
  branching/surface-area reasoning available to resolve it for a GCSE
  reader — "actively worse than a fact they can't place at all," in the
  examiner's own words.
- **Physics — "Metal railway tracks are laid with small gaps between
  sections..."** Pass 1 had already fixed a dating problem (most UK
  mainline track is continuous welded rail, no gaps) by weakening the
  claim to "track is built to cope with it." Pass 2 CUT it anyway: the
  de-dating fix removed the only concrete content, thermal expansion of
  solids isn't a named point in AQA's particle-model topic, and the
  result is "true but inert" — no wow, no clean placement.

Pass 2 also delivered 7 further REWRITEs (biology 6, chemistry 1 —
counting the marble/atom-scale fact, whose arithmetic pass 1 got wrong
in the *opposite* direction from what it thought it fixed — physics 5),
recorded in full in §7.

### Net result of round 2's review

38 drafted → 4 cut at pass 1 → 2 more cut at pass 2 → **32 shipped.**
Cut rate: 6 of 38, **≈16%** — genuine bite, not agreement-by-default.

## 6. The final list that ships (76 facts)

44 kept from round 1 + 32 new from round 2. **Longest fact: 24 words**
(the "fastest nerve impulses" biology fact — coincidentally the same
length as round 1's longest, "Radioactive decay is random...", which
also survived and still ships).

### Biology (28: 15 kept + 13 new)

1. A red blood cell has no nucleus, which leaves more room to carry oxygen around your body.
2. Mitochondria are nicknamed the cell's powerhouse: they are where aerobic respiration transfers energy from glucose.
3. An adult human is estimated to have about 37 trillion cells, though nobody has ever counted them one by one.
4. The small intestine's lining is folded into villi, giving it a huge surface area for absorbing digested food.
5. The DNA inside one human body cell would stretch about 2 metres if you unwound it all.
6. Plants make glucose from carbon dioxide and water using light energy, in a reaction called photosynthesis.
7. A human heart has four chambers and beats roughly 100,000 times a day without you thinking about it once.
8. White blood cells called phagocytes can engulf and digest invading bacteria.
9. Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease.
10. Antibiotics kill bacteria but do nothing against viruses, which is why they cannot treat a cold.
11. Alleles are different versions of the same gene; for most genes you inherit one copy from each parent.
12. Bone is a living tissue: your skeleton is constantly being broken down and rebuilt throughout your life.
13. Yeast is a single-celled fungus that can respire without oxygen to produce ethanol and carbon dioxide.
14. Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long.
15. Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue.
16. **[NEW]** Your bone marrow makes an estimated 2 million new red blood cells every second, for your entire life.
17. **[NEW]** The fastest nerve impulses in your body travel at around 100 metres per second, the length of a football pitch in about a second. (24 words — the longest fact in the whole set)
18. **[NEW]** Your stomach lining is replaced every few days; without it and its mucus, the acid and protein-digesting enzymes inside would start digesting you.
19. **[NEW]** Your lungs hold hundreds of millions of microscopic air sacs called alveoli, giving a gas exchange surface area of tens of square metres.
20. **[NEW]** A liver can regrow most of its lost size within weeks after surgery, but repeated damage, such as alcohol, scars it permanently instead.
21. **[NEW]** Water makes up roughly 60% of an adult human body by mass, more than any other single substance.
22. **[NEW]** Bacteria can reproduce by splitting in two roughly every 20 minutes under ideal conditions, doubling their numbers each time.
23. **[NEW]** You carry roughly as many bacterial cells as human cells, yet they are so much smaller that together they weigh only about 200 grams.
24. **[NEW]** At a resting 12 to 20 breaths a minute, you take somewhere between 17,000 and 29,000 breaths a day, mostly without thinking about it.
25. **[NEW]** The human egg cell is about 0.1 mm across, big enough to see, just, without a microscope. Most cells are ten times smaller.
26. **[NEW]** Skin is your largest organ, and its outer layer is completely replaced roughly every month or two as dead cells flake away.
27. **[NEW]** The oxygen you are breathing right now is waste: essentially all of Earth's oxygen was dumped into the air by photosynthesis.
28. **[NEW]** Your heart produces a tiny electrical signal every time it beats; a doctor's ECG machine is built to detect exactly that signal.

### Chemistry (25: 16 kept + 9 new)

1. An atom's radius is about 0.1 nanometres, and a nanometre is one billionth of a metre.
2. An atom's nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom's volume.
3. When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract.
4. The Group 1 metals are called the alkali metals, and they get more reactive as you go down the group.
5. The law of conservation of mass says the total mass of reactants equals the total mass of products.
6. One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant.
7. Electrolysis uses electrical energy to break down a molten ionic compound into its elements.
8. Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery.
9. A catalyst speeds up a reaction without being used up, by opening a pathway with lower activation energy.
10. Crude oil is a mixture of hydrocarbons, separated into fractions by fractional distillation.
11. Complete combustion of a hydrocarbon in plenty of oxygen produces carbon dioxide and water.
12. Earth's early atmosphere is thought to have been mostly carbon dioxide, with almost no oxygen in it.
13. Today's atmosphere is roughly four-fifths nitrogen and about one-fifth oxygen by volume.
14. Limewater turns cloudy when carbon dioxide is bubbled through it, a standard test for the gas.
15. In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures.
16. Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper.
17. **[NEW]** An atom is mostly empty space: scale the nucleus up to a marble and the whole atom would be longer than a football pitch.
18. **[NEW]** Diamond and the graphite in a pencil are both made of pure carbon, just with the atoms arranged differently.
19. **[NEW]** Helium is so unreactive that it forms no stable compounds under normal conditions, despite being the second most common element in the universe.
20. **[NEW]** Water is one of very few common substances that expands when it freezes, which is why ice floats.
21. **[NEW]** Rust forms when iron reacts with both oxygen and water at once; dry iron in dry air barely rusts at all.
22. **[NEW]** Sodium reacts violently with water; chlorine is a toxic gas; bonded together as ions they make table salt, which we eat.
23. **[NEW]** Gold is so malleable that it can be beaten into a sheet thin enough for faint light to pass through it.
24. **[NEW]** Glass is a solid, not a slow-flowing liquid: old windowpanes are sometimes thicker at the bottom because of how they were made, not flow.
25. **[NEW]** Dry ice, solid carbon dioxide, turns straight to gas at normal pressure, never melting; the white fog is water vapour condensing from the air.

### Physics (23: 13 kept + 10 new)

1. Newton's second law states that resultant force equals mass multiplied by acceleration.
2. Momentum is mass multiplied by velocity, and it is conserved whenever objects collide in a closed system.
3. Energy cannot be created or destroyed, only transferred from one store to another.
4. Gravitational potential energy depends on an object's mass, the gravitational field strength, and its height above the ground.
5. Kinetic energy rises with the square of an object's speed, not in direct proportion to it.
6. Static electricity builds up when electrons transfer between two insulating materials rubbed together.
7. Every object above absolute zero emits infrared radiation.
8. The wave equation states that wave speed equals frequency multiplied by wavelength.
9. In a vacuum, every type of electromagnetic wave travels at about 300 million metres per second.
10. Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay. (24 words)
11. Alpha radiation is the most strongly ionising type, yet a single sheet of paper can stop it.
12. Earth's magnetic field is generated deep inside the planet and helps shield us from the Sun's charged particles.
13. The Moon's atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak.
14. **[NEW]** Sound cannot travel through space: it needs particles to pass the vibration on, and space is far too empty to carry it.
15. **[NEW]** A radio still works in space because radio waves are electromagnetic waves, which need no medium to travel through.
16. **[NEW]** Dropped together from the same height in a vacuum, a hammer and a feather land at the same moment.
17. **[NEW]** Standing still on Earth, you are already travelling at roughly 30 kilometres per second around the Sun.
18. **[NEW]** Lightning is a giant static discharge, the same effect that gives you a small shock after walking on carpet, just vastly bigger.
19. **[NEW]** Sunlight refracts entering a raindrop, reflects off the back, then refracts again leaving, each colour bending by a slightly different amount.
20. **[NEW]** On the Moon you would weigh about a sixth as much, but your mass, the amount of matter in you, would not change.
21. **[NEW]** On average the Sun is about 400 times wider than the Moon and 390 times further away, so both look almost the same size.
22. **[NEW]** Glow-in-the-dark objects absorb light energy first, then release it slowly as light, which is why they must be charged in bright light.
23. **[NEW]** Ignoring air resistance, a falling object near Earth's surface gains about 9.8 metres per second of speed every second it falls.

### Spec-vs-wow balance, honestly stated

The coordinator asked for a real split, not a precise one, and precision
here would be false: "wow" is a matter of shape and reaction, not a
mechanical property a script can grade. My own classification —
biology ~8 wow / 7 spec of the 15 originally kept, plus all 13 new =
21 wow / 7 spec; chemistry ~3 wow / 13 spec of the 16 kept (chemistry's
kept set stayed more spec-heavy — see §4, most of its wow-shaped
originals were already kept), plus all 9 new = 12 wow / 13 spec; physics
~3 wow / 10 spec of the 13 kept, plus all 10 new = 13 wow / 10 spec —
gives roughly **46 wow / 30 spec-leaning** across the 76, i.e. closer to
60/40 than a clean 50/50. That is because every round-2 addition is,
by construction, wow-shaped, while round 1's SURVIVING spec facts
(the ones with enough independent merit to keep even after the
definitional purge) skew toward the ones that already had some scale or
surprise in them. If Mide wants it closer to 50/50, the lever is cutting
further into the round-1 kept set (§6 above, marked without **[NEW]**)
rather than the round-2 additions, which have all been re-examined twice
already.

## 7. Everything that was rewritten — before and after

### Round 1 (23 facts touched: 21 substantive rewrites, 1 light word-swap, 1 cosmetic notation fix)

⚠️ Correction to an earlier draft of this document: the first version of
this section undercounted its own tables (said "18", the tables actually
held 23) — arithmetic error, not a change in what shipped. Fixed here.

#### Biology

| # | Before (original draft) | After (shipped in round 1, and — where the fact wasn't later cut in round 2 — still shipping) | Why |
|---|---|---|---|
| Mitochondria | Mitochondria are called the "powerhouse of the cell" because they release energy from glucose during respiration. | Mitochondria are nicknamed the cell's powerhouse: they are where aerobic respiration transfers energy from glucose. | Glycolysis (part of respiration) happens in the cytoplasm, not the mitochondria; "aerobic respiration" scopes the claim correctly. |
| Diffusion *(cut round 2)* | Diffusion moves particles from a high concentration to a low one, with no energy input needed. | In diffusion, particles spread out, moving overall from a higher to a lower concentration, with no energy needed from the cell. | Diffusion is a *net* movement, not every particle going one way; "no energy input" was ambiguous against the particles' own kinetic energy. |
| DNA length | The DNA coiled inside a single human cell would stretch about 2 metres if you unwound it fully. | The DNA inside one human body cell would stretch about 2 metres if you unwound it all. | "A single human cell" is contradicted by the red-blood-cell fact on the same page (no DNA) — narrowed to "body cell". |
| Stomata *(cut round 2)* | Most of a leaf's stomata sit on its underside, opening and closing to control gas exchange and water loss. | In most plants, stomata sit mainly on the leaf's underside; guard cells open and close them, controlling gas exchange and water loss. | True only for typical land plants — condition stated; also stomata don't open themselves, guard cells do. |
| Vaccines | A vaccine contains a weakened or inactive form of a pathogen, training your immune system to recognise it. | Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease. | False as a universal — mRNA and subunit vaccines contain no form of the pathogen at all. |
| Alleles | Alleles are different versions of the same gene, and you inherit one copy from each parent. | Alleles are different versions of the same gene; for most genes you inherit one copy from each parent. | False for X-linked genes in males, Y-linked genes, and mitochondrial DNA — condition stated. |
| Food chain *(cut round 2)* | In a food chain, energy is lost at every stage, mostly as heat released during respiration. | In a food chain, energy is lost at every stage, much of it as heat from respiration and in waste materials. | AQA attributes losses to respiration *and* egestion/excretion; overstated a single route. |
| Decomposers *(cut round 2)* | Decomposers break down dead material, returning nutrients such as nitrogen to the soil. | Decomposers break down dead material, returning nutrients such as nitrogen compounds to the soil. | Nitrogen returns as compounds, not as the element. (Light word-swap.) |
| Biodiversity *(cut round 2)* | Biodiversity is the variety of species living in an ecosystem, and more of it tends to make that ecosystem more stable. | Biodiversity is the variety of species in an ecosystem; greater biodiversity reduces each species' dependence on others for food and shelter. | The diversity→stability generalisation is a live research dispute; rewritten to AQA's own stated mechanism. |
| Genome | A human genome contains roughly 3 billion base pairs of DNA, packed into 23 pairs of chromosomes. | Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long. | Original was correct but confusingly phrased next to the meiosis fact — "23 pairs" beside "46" invited a misread. |
| Capillaries | Capillaries are only about one cell thick, which lets oxygen and nutrients diffuse into tissue quickly. | Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue. | Ambiguous: read as the vessel's diameter, not the wall thickness. |

#### Chemistry

| # | Before | After | Why |
|---|---|---|---|
| Nucleus | An atom's nucleus contains its protons and neutrons and takes up a tiny fraction of the atom's total volume. | An atom's nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom's volume. | A hydrogen-1 nucleus has no neutrons. |
| Ionic bonding | In ionic bonding, electrons transfer from a metal atom to a non-metal atom, forming charged ions. | When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract. | Ammonium and other polyatomic-cation salts are ionic with no metal atom present. |
| Avogadro (cosmetic) | One mole of any substance contains about 6.02 x 10^23 particles, a number called the Avogadro constant. | One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant. | Real multiplication sign and superscript instead of `x`/`^`, which read as a typo. |
| Electrolysis | Electrolysis uses electrical energy to break down an ionic compound into its elements. | Electrolysis uses electrical energy to break down a molten ionic compound into its elements. | Aqueous electrolysis often does *not* give the elements. |
| Electroplating | In electrolysis of a molten ionic compound, positive ions move to the cathode and gain electrons there. | Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery. | Replaced outright once the electrolysis fact above was narrowed to "molten" and the two became redundant. An interim replacement (flagging "even layer") was itself corrected on pass 2. |
| Alkanes *(cut round 2)* | Alkanes are saturated hydrocarbons, meaning every carbon-carbon bond in the molecule is a single bond. | Alkanes are saturated hydrocarbons: every bond is a single covalent bond, so each carbon holds as many hydrogens as possible. | Methane has no carbon-carbon bond at all, so defining saturation by a bond type it doesn't have was confusing. |
| Pure substance | A pure substance melts and boils at one specific, fixed temperature; a mixture melts over a range. | In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures. | "Pure" in everyday use means the opposite of the chemical sense. |
| Chromatography | Chromatography separates a mixture because its substances travel at different rates through the same material. | Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper. | Blurred the stationary and mobile phase. |

#### Physics

| # | Before | After | Why |
|---|---|---|---|
| GPE | Gravitational potential energy depends on an object's mass, height, and the local gravitational field strength. | Gravitational potential energy depends on an object's mass, the gravitational field strength, and its height above the ground. | "Height" alone is really height above a reference level. |
| Resistance *(cut round 2)* | A wire's resistance increases as its length increases, for a fixed cross-sectional area and material. | A wire's resistance increases as its length increases, if the material, cross-sectional area and temperature stay the same. | Also assumes constant temperature. |
| Half-life | A radioactive isotope decays randomly, but its half-life is the time for half of a sample's nuclei to decay. | Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay. | "Half a sample's nuclei" is ambiguous against a decay-chain sample (e.g. uranium ore) where the total unstable-nuclei count doesn't simply halve. |
| Moon sound | The Moon has no atmosphere, so sound cannot travel across its surface — there is nothing to carry the vibration. | The Moon's atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak. | The Moon has a thin exosphere; vibrations do travel through lunar rock (Apollo seismometers recorded moonquakes). |

### Round 2 — the new wow facts (rewrite record across both passes)

The pattern that produced 3 of round 1's rewrites needing a *second*
round repeated here, twice: a pass-1 fix that solved the flagged problem
but introduced a fresh one, caught by pass 2. Both are called out below.

#### Biology

| Draft | Before | After (shipped) | Why |
|---|---|---|---|
| Nerve speed | Some nerve impulses travel through your body at over 100 metres per second, faster than a Formula 1 car. | The fastest nerve impulses in your body travel at around 100 metres per second, the length of a football pitch in about a second. | 100 m/s = 360 km/h — roughly an F1 car's *top* speed, not slower than it; the comparison overclaimed. |
| Stomach lining | The cells lining your stomach are replaced every few days, which helps stop your own stomach acid digesting you. | Your stomach lining is replaced every few days; without it and its mucus, the acid and protein-digesting enzymes inside would start digesting you. | **Two-round fix.** Pass 1 added the mucus-layer detail, but pass 2 caught that HCl alone doesn't digest tissue — pepsin does, activated by the acid. Final wording names both. |
| Alveoli | An adult's lungs contain roughly 300 million tiny air sacs called alveoli, giving a huge surface area for gas exchange. | Your lungs hold hundreds of millions of microscopic air sacs called alveoli, giving a gas exchange surface area of tens of square metres. | "Roughly 300 million" is a dated textbook figure; modern morphometry gives a much wider range (~270–790 million). Restated as a range, not a false-precision number. |
| Liver regrowth | Your liver can regrow a large part of itself after injury, replacing lost tissue over just weeks. | A liver can regrow most of its lost size within weeks after surgery, but repeated damage, such as alcohol, scars it permanently instead. | Missing the stated condition: regrowth follows *acute* loss; *repeated/chronic* damage scars instead of regrowing — and that's the part AQA actually teaches (alcohol → liver disease). |
| Bacterial ratio | The bacterial cells living on and in your body are thought to roughly equal your number of human cells. | You carry roughly as many bacterial cells as human cells, yet they are so much smaller that together they weigh only about 200 grams. | Original correctly avoided repeating the debunked "10:1" myth, but pass 2 found it had no GCSE anchor and the surprise was invisible to a reader who'd never heard the old claim. Adding the mass gives it both. |
| Breathing rate | An average adult breathes in and out roughly 20,000 times a day without ever thinking about it. | At a resting 12 to 20 breaths a minute, you take somewhere between 17,000 and 29,000 breaths a day, mostly without thinking about it. | Two defects: "without ever thinking about it" is false (breathing has conscious control too); and the arithmetic didn't close — 12–20/min implies 17,000–29,000/day, and "roughly 20,000" was the low end dressed as the middle. |
| Egg cell | A human egg cell is the largest single cell in the body, just visible to the naked eye. | The human egg cell is about 0.1 mm across, big enough to see, just, without a microscope. Most cells are ten times smaller. | **Two-round fix.** "Largest single cell" is vulnerable to motor-neurone length; pass 1's fix to "largest by volume" was WORSE (a 1 m axon is ~80× an egg cell's volume). Pass 2 dropped the superlative entirely. |
| Skin turnover | Your skin is the largest organ in your body, and most of its surface layer is replaced within about a month. | Skin is your largest organ, and its outer layer is completely replaced roughly every month or two as dead cells flake away. | "Within about a month" sat at the optimistic end of a 28–56 day literature range. |

#### Chemistry

| Draft | Before | After (shipped) | Why |
|---|---|---|---|
| Empty atom | An atom is almost entirely empty space: if its nucleus were the size of a marble, the nearest electron would be roughly a kilometre away. | An atom is mostly empty space: scale the nucleus up to a marble and the whole atom would be longer than a football pitch. | **Two-round fix, and pass 1's own fix was wrong.** Original: "nearest electron" is actually about atomic *radius*, and the ratio gave the wrong order of magnitude next to what AQA teaches. Pass 1's rewrite ("hundreds of metres") undershot: the arithmetic (1.5 cm marble × AQA's taught ≥10,000:1 ratio) gives ~150 m, and pass 2 showed a diameter framing is both correct and a safe floor across any plausible ratio. |
| Table salt | Table salt is made of two dangerous elements on their own, sodium metal and chlorine gas, that become harmless once bonded together as ions. | Sodium reacts violently with water; chlorine is a toxic gas; bonded together as ions they make table salt, which we eat. | "Harmless" is false — salt is a genuine dietary hazard in quantity. Pass 1 fixed the chemistry but left an ambiguous three-item list; pass 2 restructured the sentence so it can't be misread as a third ingredient. |
| Glass myth | Glass is a solid, not a liquid — old windowpanes are sometimes thicker at the bottom simply because of how they were made, not because the glass has flowed. | Glass is a solid, not a slow-flowing liquid: old windowpanes are sometimes thicker at the bottom because of how they were made, not flow. | Original never named the specific myth ("slow-flowing liquid") it was correcting, so a skimming reader could miss the correction and supply the myth themselves. |

#### Physics

| Draft | Before | After (shipped) | Why |
|---|---|---|---|
| Vacuum sound | Sound cannot travel through the vacuum of space at all, because there are no particles there to carry the vibration. | Sound cannot travel through space: it needs particles to pass the vibration on, and space is far too empty to carry it. | "No particles there" is literally false (interstellar/interplanetary space has sparse particles); the honest reason is density far too low, not true vacuum. |
| Hammer/feather | If you dropped a hammer and a feather in a vacuum, with no air resistance, they would hit the ground at the same time. | Dropped together from the same height in a vacuum, a hammer and a feather land at the same moment. | **Two-round fix.** Pass 1 named "in a vacuum" but left "same height, released together" unstated; pass 2 made the release condition explicit rather than leaving "fall together" to carry two jobs at once. |
| Rainbow | A rainbow forms because water droplets split white light into its different wavelengths and reflect each one at a slightly different angle. | Sunlight refracts entering a raindrop, reflects off the back, then refracts again leaving, each colour bending by a slightly different amount. | **Two-round fix.** Dispersion happens by refraction, not by wavelength-dependent reflection — pass 1's rewrite kept the wrong mechanism; pass 2 restored the correct three-step refract/reflect/refract sequence. |
| Eclipse coincidence | A total solar eclipse is possible because the Sun is both about 400 times wider than the Moon and about 400 times further away. | On average the Sun is about 400 times wider than the Moon and 390 times further away, so both look almost the same size. | Rounding BOTH ratios to "400" manufactures a false exact coincidence — the real ratios are ~400.4 (diameter) and ~389 (distance), and the ~3% gap is physically the reason annular eclipses exist at all. Pass 2 added "on average", since the Moon's elliptical orbit swings the true ratio 368–420. |
| Glow in the dark | Glow-in-the-dark objects work by absorbing light energy and re-releasing it slowly, not by producing genuinely new light of their own. | Glow-in-the-dark objects absorb light energy first, then release it slowly as light, which is why they must be charged in bright light. | "Not... genuinely new light of their own" was false — the object does emit new, longer-wavelength photons; what it lacks is its own energy source. |
| Falling object | An object falling freely near Earth's surface gains about 10 metres per second of speed for every second it keeps falling. | Ignoring air resistance, a falling object near Earth's surface gains about 9.8 metres per second of speed every second it falls. | AQA's own exam data sheet gives g = 9.8 N/kg, not 10 — a revision site should match the value students are handed in the exam. |

## 8. How to add a fact

1. Open `shared/science-facts.js`. Read its header comment (rules 1–9
   above, restated there, including the round-2 50/50 pitch ruling)
   before writing anything.
2. Append `{ subject: 'biology' | 'chemistry' | 'physics', text: '…' }`
   anywhere in the `window.MRB_SCIENCE_FACTS` array — order doesn't
   matter, the rotator shuffles its own draw order at runtime.
3. Ask yourself honestly whether it's spec-facing or wow-shaped, and
   check the current balance in §6 before adding another of whichever
   the list already has more of.
4. Check the word count by hand (under 25) and re-read rules 1–7 against
   the exact sentence you wrote, not a looser version of it in your head.
5. Get a second, independent read on it — the same two-pass Opus-examiner
   pattern this batch used (a subject-specialist pass, then a second
   specialist cross-checking the first pass's verdict without having
   written it) — before it ships. **Do not skip the second pass even if
   the first pass says KEEP or gives what looks like a clean REWRITE**:
   in this batch alone, three facts (biology's egg cell, chemistry's
   atom-scale marble analogy, physics's rainbow mechanism) had a pass-1
   rewrite that *introduced* a new error the second pass had to catch. A
   fact that reads true to its own author, or to the examiner who just
   fixed it, is exactly the failure mode two independent passes exist to
   stop.
6. Run `python3 build_all.py` — `science-facts.js` gets cache-bust
   stamped automatically like every other `shared/*.js` file, no
   generator change needed for content-only edits.
7. **Re-run the browser verification if the longest fact changes.** The
   fact panel's reserved height is set by the browser from whichever
   fact is longest at render time (see §9) — a new longest fact should be
   checked against the four widths (1280/820/390/360) and the two mobile
   fold checks (390×844, 360×740), not assumed safe because the word
   count is still under 25.
8. No gate currently re-verifies fact TEXT (truth is a human/examiner
   judgement, not a mechanical one) — `ks4_chrome_tells` and
   `ks4_chrome_drive` watch `shared/science-facts.js` and
   `shared/k4-facts.js` structurally (Design's sample-content bans, the
   chrome walk) but do not mark science content. Mide's own read remains
   the actual content gate, per the Autonomy Contract's "science or
   content accuracy is Mide's sole gate" rule — as this very round-2
   revision demonstrates.

## 9. Implementation notes (for whoever next touches the panel)

- **Zero layout shift** is achieved by rendering *every* fact into
  `#k4-facts-stage` at once, stacked with CSS `grid-area: 1 / 1` — the
  same technique `.k4-stars-slides` already uses for the GCSE hub's Top
  Stars crossfade. Because every fact contributes to the grid track's
  sizing even while invisible (`opacity: 0`), the box is sized to the
  tallest fact automatically and can never change again as the active
  fact rotates. This was re-verified after round 2's fact-list rewrite
  by measuring the headline's `getBoundingClientRect()` across 6 forced
  fact changes against the new 76-fact list and confirming byte-identical
  JSON (see the PR/commit report for the exact numbers).
- **Deck**: a Fisher-Yates shuffle per pass, reshuffled when exhausted,
  with a boundary check that swaps the new pass's first two entries if
  the first would repeat the fact just shown. Re-verified after round 2
  by advancing the deck through more than two full 76-fact passes via
  the debug hook `window.__MRB_FACTS_DEBUG` and confirming every
  consecutive 76-fact window is a full permutation with no adjacent
  repeat anywhere.
- **Accessibility**: `#k4-facts-stage` is `aria-hidden="true"` and has no
  `aria-live` region — a screen-reader user is never interrupted by the
  rotation. `#k4-facts-sr` is a single visually-hidden `<p>`, populated
  once at load with one randomly-chosen fact, and never rewritten.
- **Reduced motion**: checked once at boot via
  `window.matchMedia('(prefers-reduced-motion: reduce)')`. If it
  matches, the deck still runs once (to pick which single fact shows)
  but no `setInterval` is ever started — re-verified after round 2 by
  emulating the media feature via CDP and confirming the shown fact is
  unchanged after 20 real seconds.
- **Mobile**: the panel is a `.k4-band-side` sibling of `.k4-band-copy`
  inside the existing `.k4-band` flex row. `.k4-band`'s own
  `flex-wrap: wrap` puts the panel under the lede on narrow screens with
  no extra ordering CSS. Re-verified after round 2: the first
  `.k4-door` card's top stays above the fold at both 390×844 and
  360×740.
- **Colour tokens**: the "KS3 studio design system" instruction is
  satisfied through the `--k4-*` custom properties this chrome file
  already carries — the literal `--ks3-*` custom properties only resolve
  under `.rd[data-mode="ks3"]` (see `shared/tokens.css`), which the KS4
  chrome page does not carry. Subject dot colours are `#1D6FB8` /
  `#B02342` / `#237A3B` — `generate_site_v5.py`'s `PHYSICS_COLOR` /
  `CHEMISTRY_COLOR` / `BIOLOGY_COLOR`, the same hexes the door cards and
  subject picker already render, not the older teal/pink/green pair in
  CLAUDE.md's subject-colour note (superseded by the MRB-46 Phase 3
  swap).
