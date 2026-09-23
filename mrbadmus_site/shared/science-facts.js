/* ═══════════════════════════════════════════════════════════════════════
   science-facts.js — the landing page's rotating "did you know" facts
   (MRB-342.2 Part 4)

   Consumed by shared/k4-facts.js on the landing hero (index.html) only.
   A plain global, like every other shared/*.js file on this site — there
   is no module system and no build step.

   ── RULES A NEW FACT MUST MEET ────────────────────────────────────────
   Every entry here went through two independent Opus examiner passes
   (subject specialist, then a second specialist cross-checking the first
   pass's verdicts and rewrites) before it shipped. Read
   docs/landing/science-facts.md for the full record — what was kept,
   cut, and rewritten, and why — before adding to this file. A new fact
   should go through the same two-pass check, not just this list:

     1. TRUE AS STATED. Not true-with-an-asterisk unless the asterisk is
        written into the sentence.
     2. UK/SI units only — metres, kilograms, seconds, joules, °C,
        newtons, m/s. No imperial, ever.
     3. NO MYTHS. If it's one of the usual suspects (glass is a slow
        liquid, 10% of your brain, blood is blue in your veins, 5 senses,
        goldfish memory, tongue maps, lightning never strikes twice,
        radioactive bananas, swallowed spiders, hair/nails growing after
        death, exactly 5 litres of blood, a dropped penny is lethal, the
        Great Wall from space) — it does not belong here, full stop.
     4. NOTHING THAT WILL DATE. No "most recently discovered", no "the
        largest ever found", no counts that change (element counts,
        exoplanet counts, world records). A fact that was true in 2026 and
        false in 2030 is a fact this file cannot hold.
     5. NOTHING UNSAFE. No fact that reads as an invitation to try
        something at home — mixing chemicals, heating a sealed container,
        looking at the Sun, handling mercury, anything electrical, eating
        or drinking something to test it.
     6. HONEST ROUNDING. Say "about" or "roughly" when a number is
        approximate, and make sure the rounding doesn't do misleading
        work (78%/21% air rounded to "four-fifths"/"one-fifth" is honest;
        rounding away a real caveat is not).
     7. STATE THE CONDITION. If a fact is only true under some unstated
        condition (closed system, molten not aqueous, "most plants" not
        "all plants"), either state the condition or don't ship the fact.
     8. UNDER 25 WORDS. Every entry below is checked mechanically —
        `python3 -c "print(len(open('shared/science-facts.js').read()...))"`
        won't do it for you; count the sentence, not the file.
     9. PITCH: roughly HALF spec-facing (things a pupil meets at AQA GCSE,
        combined and triple, spec 8461/8462/8463) and HALF "wow" facts a
        12-16 year old would repeat to a friend — not a first-year-
        undergrad claim, not a KS1 one, and ideally a wow fact hangs off
        something the pupil will meet at GCSE rather than being pure
        trivia. This 50/50 split is a deliberate ruling (Mide, MRB-342.2):
        the first draft was ~94% bare spec-recall definitions, which reads
        as a textbook rather than an invitation to read the next one, so a
        second round of drafting and two more Opus passes rebalanced it.

   ── SHAPE ──────────────────────────────────────────────────────────────
   One object per fact: { subject: 'biology' | 'chemistry' | 'physics',
   text: '…' }. Nothing else is read — no id, no tier, no difficulty. The
   rotator (shared/k4-facts.js) reads window.MRB_SCIENCE_FACTS as a flat
   array and doesn't care about ordering; it shuffles its own draw order
   at runtime, so new entries can be appended anywhere in the array below.
   ═══════════════════════════════════════════════════════════════════════ */

window.MRB_SCIENCE_FACTS = [
  // ── Biology (28) ──
  { subject: 'biology', text: 'A red blood cell has no nucleus, which leaves more room to carry oxygen around your body.' },
  { subject: 'biology', text: 'Mitochondria are nicknamed the cell\'s powerhouse: they are where aerobic respiration transfers energy from glucose.' },
  { subject: 'biology', text: 'An adult human is estimated to have about 37 trillion cells, though nobody has ever counted them one by one.' },
  { subject: 'biology', text: 'The small intestine\'s lining is folded into villi, giving it a huge surface area for absorbing digested food.' },
  { subject: 'biology', text: 'The DNA inside one human body cell would stretch about 2 metres if you unwound it all.' },
  { subject: 'biology', text: 'Plants make glucose from carbon dioxide and water using light energy, in a reaction called photosynthesis.' },
  { subject: 'biology', text: 'A human heart has four chambers and beats roughly 100,000 times a day without you thinking about it once.' },
  { subject: 'biology', text: 'White blood cells called phagocytes can engulf and digest invading bacteria.' },
  { subject: 'biology', text: 'Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease.' },
  { subject: 'biology', text: 'Antibiotics kill bacteria but do nothing against viruses, which is why they cannot treat a cold.' },
  { subject: 'biology', text: 'Alleles are different versions of the same gene; for most genes you inherit one copy from each parent.' },
  { subject: 'biology', text: 'Bone is a living tissue: your skeleton is constantly being broken down and rebuilt throughout your life.' },
  { subject: 'biology', text: 'Yeast is a single-celled fungus that can respire without oxygen to produce ethanol and carbon dioxide.' },
  { subject: 'biology', text: 'Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long.' },
  { subject: 'biology', text: 'Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue.' },
  { subject: 'biology', text: 'Your bone marrow makes an estimated 2 million new red blood cells every second, for your entire life.' },
  { subject: 'biology', text: 'The fastest nerve impulses in your body travel at around 100 metres per second, the length of a football pitch in about a second.' },
  { subject: 'biology', text: 'Your stomach lining is replaced every few days; without it and its mucus, the acid and protein-digesting enzymes inside would start digesting you.' },
  { subject: 'biology', text: 'Your lungs hold hundreds of millions of microscopic air sacs called alveoli, giving a gas exchange surface area of tens of square metres.' },
  { subject: 'biology', text: 'A liver can regrow most of its lost size within weeks after surgery, but repeated damage, such as alcohol, scars it permanently instead.' },
  { subject: 'biology', text: 'Water makes up roughly 60% of an adult human body by mass, more than any other single substance.' },
  { subject: 'biology', text: 'Bacteria can reproduce by splitting in two roughly every 20 minutes under ideal conditions, doubling their numbers each time.' },
  { subject: 'biology', text: 'You carry roughly as many bacterial cells as human cells, yet they are so much smaller that together they weigh only about 200 grams.' },
  { subject: 'biology', text: 'At a resting 12 to 20 breaths a minute, you take somewhere between 17,000 and 29,000 breaths a day, mostly without thinking about it.' },
  { subject: 'biology', text: 'The human egg cell is about 0.1 mm across, big enough to see, just, without a microscope. Most cells are ten times smaller.' },
  { subject: 'biology', text: 'Skin is your largest organ, and its outer layer is completely replaced roughly every month or two as dead cells flake away.' },
  { subject: 'biology', text: 'The oxygen you are breathing right now is waste: essentially all of Earth\'s oxygen was dumped into the air by photosynthesis.' },
  { subject: 'biology', text: 'Your heart produces a tiny electrical signal every time it beats; a doctor\'s ECG machine is built to detect exactly that signal.' },
  // ── Chemistry (25) ──
  { subject: 'chemistry', text: 'An atom\'s radius is about 0.1 nanometres, and a nanometre is one billionth of a metre.' },
  { subject: 'chemistry', text: 'An atom\'s nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom\'s volume.' },
  { subject: 'chemistry', text: 'When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract.' },
  { subject: 'chemistry', text: 'The Group 1 metals are called the alkali metals, and they get more reactive as you go down the group.' },
  { subject: 'chemistry', text: 'The law of conservation of mass says the total mass of reactants equals the total mass of products.' },
  { subject: 'chemistry', text: 'One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant.' },
  { subject: 'chemistry', text: 'Electrolysis uses electrical energy to break down a molten ionic compound into its elements.' },
  { subject: 'chemistry', text: 'Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery.' },
  { subject: 'chemistry', text: 'A catalyst speeds up a reaction without being used up, by opening a pathway with lower activation energy.' },
  { subject: 'chemistry', text: 'Crude oil is a mixture of hydrocarbons, separated into fractions by fractional distillation.' },
  { subject: 'chemistry', text: 'Complete combustion of a hydrocarbon in plenty of oxygen produces carbon dioxide and water.' },
  { subject: 'chemistry', text: 'Earth\'s early atmosphere is thought to have been mostly carbon dioxide, with almost no oxygen in it.' },
  { subject: 'chemistry', text: 'Today\'s atmosphere is roughly four-fifths nitrogen and about one-fifth oxygen by volume.' },
  { subject: 'chemistry', text: 'Limewater turns cloudy when carbon dioxide is bubbled through it, a standard test for the gas.' },
  { subject: 'chemistry', text: 'In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures.' },
  { subject: 'chemistry', text: 'Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper.' },
  { subject: 'chemistry', text: 'An atom is mostly empty space: scale the nucleus up to a marble and the whole atom would be longer than a football pitch.' },
  { subject: 'chemistry', text: 'Diamond and the graphite in a pencil are both made of pure carbon, just with the atoms arranged differently.' },
  { subject: 'chemistry', text: 'Helium is so unreactive that it forms no stable compounds under normal conditions, despite being the second most common element in the universe.' },
  { subject: 'chemistry', text: 'Water is one of very few common substances that expands when it freezes, which is why ice floats.' },
  { subject: 'chemistry', text: 'Rust forms when iron reacts with both oxygen and water at once; dry iron in dry air barely rusts at all.' },
  { subject: 'chemistry', text: 'Sodium reacts violently with water; chlorine is a toxic gas; bonded together as ions they make table salt, which we eat.' },
  { subject: 'chemistry', text: 'Gold is so malleable that it can be beaten into a sheet thin enough for faint light to pass through it.' },
  { subject: 'chemistry', text: 'Glass is a solid, not a slow-flowing liquid: old windowpanes are sometimes thicker at the bottom because of how they were made, not flow.' },
  { subject: 'chemistry', text: 'Dry ice, solid carbon dioxide, turns straight to gas at normal pressure, never melting; the white fog is water vapour condensing from the air.' },
  // ── Physics (23) ──
  { subject: 'physics', text: 'Newton\'s second law states that resultant force equals mass multiplied by acceleration.' },
  { subject: 'physics', text: 'Momentum is mass multiplied by velocity, and it is conserved whenever objects collide in a closed system.' },
  { subject: 'physics', text: 'Energy cannot be created or destroyed, only transferred from one store to another.' },
  { subject: 'physics', text: 'Gravitational potential energy depends on an object\'s mass, the gravitational field strength, and its height above the ground.' },
  { subject: 'physics', text: 'Kinetic energy rises with the square of an object\'s speed, not in direct proportion to it.' },
  { subject: 'physics', text: 'Static electricity builds up when electrons transfer between two insulating materials rubbed together.' },
  { subject: 'physics', text: 'Every object above absolute zero emits infrared radiation.' },
  { subject: 'physics', text: 'The wave equation states that wave speed equals frequency multiplied by wavelength.' },
  { subject: 'physics', text: 'In a vacuum, every type of electromagnetic wave travels at about 300 million metres per second.' },
  { subject: 'physics', text: 'Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay.' },
  { subject: 'physics', text: 'Alpha radiation is the most strongly ionising type, yet a single sheet of paper can stop it.' },
  { subject: 'physics', text: 'Earth\'s magnetic field is generated deep inside the planet and helps shield us from the Sun\'s charged particles.' },
  { subject: 'physics', text: 'The Moon\'s atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak.' },
  { subject: 'physics', text: 'Sound cannot travel through space: it needs particles to pass the vibration on, and space is far too empty to carry it.' },
  { subject: 'physics', text: 'A radio still works in space because radio waves are electromagnetic waves, which need no medium to travel through.' },
  { subject: 'physics', text: 'Dropped together from the same height in a vacuum, a hammer and a feather land at the same moment.' },
  { subject: 'physics', text: 'Standing still on Earth, you are already travelling at roughly 30 kilometres per second around the Sun.' },
  { subject: 'physics', text: 'Lightning is a giant static discharge, the same effect that gives you a small shock after walking on carpet, just vastly bigger.' },
  { subject: 'physics', text: 'Sunlight refracts entering a raindrop, reflects off the back, then refracts again leaving, each colour bending by a slightly different amount.' },
  { subject: 'physics', text: 'On the Moon you would weigh about a sixth as much, but your mass, the amount of matter in you, would not change.' },
  { subject: 'physics', text: 'On average the Sun is about 400 times wider than the Moon and 390 times further away, so both look almost the same size.' },
  { subject: 'physics', text: 'Glow-in-the-dark objects absorb light energy first, then release it slowly as light, which is why they must be charged in bright light.' },
  { subject: 'physics', text: 'Ignoring air resistance, a falling object near Earth\'s surface gains about 9.8 metres per second of speed every second it falls.' },
];
