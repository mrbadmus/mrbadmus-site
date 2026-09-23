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
     9. PITCH: a mix of things a pupil meets at AQA GCSE (combined and
        triple, spec 8461/8462/8463) and "wow" facts a 12–16 year old
        would repeat to a friend. Not a first-year-undergrad claim, not a
        KS1 one.

   ── SHAPE ──────────────────────────────────────────────────────────────
   One object per fact: { subject: 'biology' | 'chemistry' | 'physics',
   text: '…' }. Nothing else is read — no id, no tier, no difficulty. The
   rotator (shared/k4-facts.js) reads window.MRB_SCIENCE_FACTS as a flat
   array and doesn't care about ordering; it shuffles its own draw order
   at runtime, so new entries can be appended anywhere in the array below.
   ═══════════════════════════════════════════════════════════════════════ */

window.MRB_SCIENCE_FACTS = [
  // ── Biology ──────────────────────────────────────────────────────────
  { subject: 'biology', text: 'A red blood cell has no nucleus, which leaves more room to carry oxygen around your body.' },
  { subject: 'biology', text: "Mitochondria are nicknamed the cell's powerhouse: they are where aerobic respiration transfers energy from glucose." },
  { subject: 'biology', text: 'An adult human is estimated to have about 37 trillion cells, though nobody has ever counted them one by one.' },
  { subject: 'biology', text: 'In diffusion, particles spread out, moving overall from a higher to a lower concentration, with no energy needed from the cell.' },
  { subject: 'biology', text: "The small intestine's lining is folded into villi, giving it a huge surface area for absorbing digested food." },
  { subject: 'biology', text: 'Enzymes are biological catalysts: each one speeds up one particular reaction without being used up itself.' },
  { subject: 'biology', text: 'The DNA inside one human body cell would stretch about 2 metres if you unwound it all.' },
  { subject: 'biology', text: 'Plants make glucose from carbon dioxide and water using light energy, in a reaction called photosynthesis.' },
  { subject: 'biology', text: "In most plants, stomata sit mainly on the leaf's underside; guard cells open and close them, controlling gas exchange and water loss." },
  { subject: 'biology', text: 'A human heart has four chambers and beats roughly 100,000 times a day without you thinking about it once.' },
  { subject: 'biology', text: 'White blood cells called phagocytes can engulf and digest invading bacteria.' },
  { subject: 'biology', text: 'Many vaccines contain a weakened or inactive pathogen, training your immune system to recognise it without you catching the disease.' },
  { subject: 'biology', text: 'Antibiotics kill bacteria but do nothing against viruses, which is why they cannot treat a cold.' },
  { subject: 'biology', text: 'Homeostasis keeps conditions inside your body steady, such as temperature and blood glucose concentration.' },
  { subject: 'biology', text: 'Insulin is a hormone released by the pancreas that lowers blood glucose concentration.' },
  { subject: 'biology', text: 'A synapse is the tiny gap between two neurones, crossed by chemical messengers called neurotransmitters.' },
  { subject: 'biology', text: 'Alleles are different versions of the same gene; for most genes you inherit one copy from each parent.' },
  { subject: 'biology', text: 'Meiosis produces gametes with half the chromosome number of the cell that made them.' },
  { subject: 'biology', text: "A dominant allele's characteristic shows up in an organism even if only one copy of it is present." },
  { subject: 'biology', text: 'In a food chain, energy is lost at every stage, much of it as heat from respiration and in waste materials.' },
  { subject: 'biology', text: 'Decomposers break down dead material, returning nutrients such as nitrogen compounds to the soil.' },
  { subject: 'biology', text: "Biodiversity is the variety of species in an ecosystem; greater biodiversity reduces each species' dependence on others for food and shelter." },
  { subject: 'biology', text: 'Xylem tissue carries water up a plant, while phloem carries dissolved sugars both up and down it.' },
  { subject: 'biology', text: 'Bone is a living tissue: your skeleton is constantly being broken down and rebuilt throughout your life.' },
  { subject: 'biology', text: 'Yeast is a single-celled fungus that can respire without oxygen to produce ethanol and carbon dioxide.' },
  { subject: 'biology', text: 'Your body cells each hold 46 chromosomes: two copies of the human genome, which is about 3 billion DNA base pairs long.' },
  { subject: 'biology', text: 'Capillary walls are just one cell thick, so oxygen and nutrients diffuse quickly into the surrounding tissue.' },

  // ── Chemistry ────────────────────────────────────────────────────────
  { subject: 'chemistry', text: "An atom's radius is about 0.1 nanometres, and a nanometre is one billionth of a metre." },
  { subject: 'chemistry', text: "An atom's nucleus holds its protons and any neutrons, yet takes up a tiny fraction of the atom's volume." },
  { subject: 'chemistry', text: "An element's atomic number tells you how many protons are in one atom of that element." },
  { subject: 'chemistry', text: 'Isotopes of an element have the same number of protons but different numbers of neutrons.' },
  { subject: 'chemistry', text: 'When a metal reacts with a non-metal, electrons transfer from metal to non-metal atoms, forming oppositely charged ions that attract.' },
  { subject: 'chemistry', text: 'In covalent bonding, atoms share pairs of electrons so each atom fills its outer shell.' },
  { subject: 'chemistry', text: 'Metals conduct electricity because the delocalised electrons in their structure are free to move.' },
  { subject: 'chemistry', text: 'The Group 1 metals are called the alkali metals, and they get more reactive as you go down the group.' },
  { subject: 'chemistry', text: 'The Group 7 elements are called the halogens, and they get less reactive as you go down the group.' },
  { subject: 'chemistry', text: 'The noble gases in Group 0 have a full outer shell of electrons, which makes them very unreactive.' },
  { subject: 'chemistry', text: 'The law of conservation of mass says the total mass of reactants equals the total mass of products.' },
  { subject: 'chemistry', text: 'One mole of any substance contains about 6.02 × 10²³ particles, a number called the Avogadro constant.' },
  { subject: 'chemistry', text: 'Electrolysis uses electrical energy to break down a molten ionic compound into its elements.' },
  { subject: 'chemistry', text: 'Electroplating uses electrolysis to coat an object with a thin layer of metal, such as the silver on plated cutlery.' },
  { subject: 'chemistry', text: 'An exothermic reaction transfers energy to the surroundings, so the surrounding temperature rises.' },
  { subject: 'chemistry', text: 'An endothermic reaction takes in energy from the surroundings, so the surrounding temperature falls.' },
  { subject: 'chemistry', text: 'A catalyst speeds up a reaction without being used up, by opening a pathway with lower activation energy.' },
  { subject: 'chemistry', text: 'Raising the temperature speeds up a reaction because particles collide more often and with more energy.' },
  { subject: 'chemistry', text: 'In a reversible reaction at equilibrium, the forward and backward reactions occur at the same rate.' },
  { subject: 'chemistry', text: 'Crude oil is a mixture of hydrocarbons, separated into fractions by fractional distillation.' },
  { subject: 'chemistry', text: 'Alkanes are saturated hydrocarbons: every bond is a single covalent bond, so each carbon holds as many hydrogens as possible.' },
  { subject: 'chemistry', text: 'Complete combustion of a hydrocarbon in plenty of oxygen produces carbon dioxide and water.' },
  { subject: 'chemistry', text: "Earth's early atmosphere is thought to have been mostly carbon dioxide, with almost no oxygen in it." },
  { subject: 'chemistry', text: "Today's atmosphere is roughly four-fifths nitrogen and about one-fifth oxygen by volume." },
  { subject: 'chemistry', text: 'Limewater turns cloudy when carbon dioxide is bubbled through it, a standard test for the gas.' },
  { subject: 'chemistry', text: 'In chemistry, a pure substance melts and boils at fixed temperatures; a mixture melts over a range of temperatures.' },
  { subject: 'chemistry', text: 'Chromatography separates a mixture because its substances move at different speeds as a solvent carries them through the paper.' },

  // ── Physics ──────────────────────────────────────────────────────────
  { subject: 'physics', text: 'Speed is distance travelled divided by time taken, usually measured in metres per second.' },
  { subject: 'physics', text: 'Acceleration is the rate of change of velocity, measured in metres per second squared.' },
  { subject: 'physics', text: "Newton's second law states that resultant force equals mass multiplied by acceleration." },
  { subject: 'physics', text: 'A resultant force of zero means an object is either stationary or moving at a constant velocity.' },
  { subject: 'physics', text: 'Momentum is mass multiplied by velocity, and it is conserved whenever objects collide in a closed system.' },
  { subject: 'physics', text: 'Energy cannot be created or destroyed, only transferred from one store to another.' },
  { subject: 'physics', text: "Gravitational potential energy depends on an object's mass, the gravitational field strength, and its height above the ground." },
  { subject: 'physics', text: "Kinetic energy rises with the square of an object's speed, not in direct proportion to it." },
  { subject: 'physics', text: 'Power is the rate of energy transfer, measured in watts, where one watt equals one joule per second.' },
  { subject: 'physics', text: 'Electric current is the rate of flow of charge, measured in amperes.' },
  { subject: 'physics', text: 'In a series circuit the current is the same everywhere, but the potential difference is shared between components.' },
  { subject: 'physics', text: 'In a parallel circuit the potential difference across each branch is equal, but the current splits between them.' },
  { subject: 'physics', text: "A wire's resistance increases as its length increases, if the material, cross-sectional area and temperature stay the same." },
  { subject: 'physics', text: 'Static electricity builds up when electrons transfer between two insulating materials rubbed together.' },
  { subject: 'physics', text: 'A transformer changes the size of an alternating voltage using two coils linked by a changing magnetic field.' },
  { subject: 'physics', text: 'Every object above absolute zero emits infrared radiation.' },
  { subject: 'physics', text: 'Sound waves are longitudinal, so the particles vibrate parallel to the direction the wave travels.' },
  { subject: 'physics', text: 'Light waves are transverse, so their vibrations are at right angles to the direction of travel.' },
  { subject: 'physics', text: 'The wave equation states that wave speed equals frequency multiplied by wavelength.' },
  { subject: 'physics', text: 'In a vacuum, every type of electromagnetic wave travels at about 300 million metres per second.' },
  { subject: 'physics', text: 'Radioactive decay is random, but the half-life is the time taken for half the nuclei of a radioactive isotope in a sample to decay.' },
  { subject: 'physics', text: 'Alpha radiation is the most strongly ionising type, yet a single sheet of paper can stop it.' },
  { subject: 'physics', text: 'Density is mass divided by volume, usually measured in kilograms per cubic metre.' },
  { subject: 'physics', text: "A magnetic field is strongest at a magnet's poles, shown by field lines drawn closest together there." },
  { subject: 'physics', text: "Earth's magnetic field is generated deep inside the planet and helps shield us from the Sun's charged particles." },
  { subject: 'physics', text: "The Moon's atmosphere is far too thin to carry sound, so astronauts standing on its surface cannot hear each other speak." },
];
