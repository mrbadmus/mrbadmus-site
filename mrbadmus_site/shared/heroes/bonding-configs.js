/* ============================================================
   MrBadmus Hero configs — BONDING unit (MRB-113)
   Data only. Content mirrors Design's Hero 10 (Diamond vs
   Graphite) spec and the giant-covalent-structures source in
   all_subtopics_chemistry.py. Keeping configs data-separate from
   the hero logic (two-state-compare.js) lets later units reuse
   the same archetype with their own config.

   Callout-rule colours (Mide, locked): each state's caption sits
   on a soft tint of that state's own accent —
     · diamond  → tone 'accent' (burnt-orange wash) — the rigid crystal
     · graphite → tone 'good'   (sage-green wash)   — it conducts
   so the two states read as an unmissable, colour-coded contrast,
   never plain cream.
============================================================ */
(function () {
  'use strict';
  var C = (window.MrbHeroConfigs = window.MrbHeroConfigs || {});
  var bonding = (C.bonding = C.bonding || {});

  bonding['giant-covalent-structures'] = {
    emoji: '💎', title: 'Diamond vs Graphite', subtitle: 'same carbon, opposite properties',
    strap: 'Same element — carbon. The properties come out opposite only because the giant covalent structure is arranged differently.',
    /* Phase 1a predict gate (MRB-133) — grounded in frozen theory: graphite's
       delocalised 4th electron vs diamond's four locked bonds. */
    predict: {
      question: 'Graphite is pure carbon, just like diamond. Will it conduct electricity?',
      options: ['Yes — it conducts', 'No — carbon never conducts'],
      correctIndex: 0,
      revealsOn: 'state:graphite',
    },
    states: [
      {
        key: 'diamond', label: '💎 Diamond', emoji: '💎', tone: 'accent',
        effectTitle: 'Rigid, very hard, and an electrical insulator',
        caption: 'Each carbon forms 4 covalent bonds to 4 other carbons in a giant 3-D tetrahedral lattice. To melt or scratch it you must break millions of strong bonds — so it is extremely hard with a very high melting point. Every outer electron is locked into a bond, leaving no free electrons, so diamond does NOT conduct electricity.',
        legend: '4 covalent bonds per carbon · rigid 3-D network · no free electrons',
        props: [
          { k: 'Bonds per carbon', v: '4', tone: 'neutral' },
          { k: 'Free electrons', v: 'None', tone: 'bad' },
          { k: 'Hardness', v: 'Very hard', tone: 'neutral' },
          { k: 'Melting point', v: 'Very high', tone: 'good' },
          { k: 'Conducts electricity', v: 'No ✕', tone: 'bad' },
        ],
        visual: { type: 'tetrahedral' },
      },
      {
        key: 'graphite', label: '✏️ Graphite', emoji: '✏️', tone: 'good',
        effectTitle: 'Soft & slippery, high melting point — and it conducts',
        caption: 'Each carbon forms only 3 covalent bonds, building flat hexagonal layers. The layers are held to each other by weak forces, so they slide over one another — making graphite soft and slippery. The spare 4th outer electron on every carbon is delocalised between the layers, so those free electrons carry charge and graphite DOES conduct. Strong bonds within each layer still give a very high melting point.',
        legend: '3 covalent bonds per carbon · weak forces between sliding layers · 1 free electron each',
        props: [
          { k: 'Bonds per carbon', v: '3', tone: 'neutral' },
          { k: 'Free electrons', v: '1 delocalised', tone: 'good' },
          { k: 'Between layers', v: 'Weak forces', tone: 'neutral' },
          { k: 'Melting point', v: 'Very high', tone: 'good' },
          { k: 'Conducts electricity', v: 'Yes ✓', tone: 'good' },
        ],
        visual: { type: 'hexLayers', delocalised: true, slide: true },
      },
    ],
  };

  /* ---- Categorise Bins (Hero 09) — replaces the old drag-match on
     the same page. Cards + correct mapping are copied VERBATIM from
     the `matching` block in all_subtopics_chemistry*.py (frozen
     science). Bin emoji, tint, prompt and the dark hint recap are
     presentation only and add no new fact. Diamond → warm, Graphite
     → cool: green stays reserved for the ✓ "correct" feedback. ---- */
  bonding['giant-covalent-structures-bins'] = {
    emoji: '💎', title: 'Diamond or Graphite?', subtitle: 'sort each property into the right structure',
    prompt: 'Tap a property, then tap a structure. Diamond and graphite are both pure carbon — the properties come out different only because the giant covalent structure is arranged differently. Tap a placed card to send it back.',
    trayLabel: 'PROPERTIES · tap one, then tap a structure',
    bins: [
      { key: 'diamond', label: 'Diamond', emoji: '💎', tint: 'warm' },
      { key: 'graphite', label: 'Graphite', emoji: '✏️', tint: 'cool' },
    ],
    cards: [
      { id: 'd-lattice', text: 'Each carbon bonded to 4 others in a 3D tetrahedral lattice — very hard', bin: 'diamond' },
      { id: 'g-layers',  text: 'Each carbon bonded to 3 others in flat hexagonal sheets — layers can slide', bin: 'graphite' },
      { id: 'g-conduct', text: 'Conducts electricity — 4th outer electron is delocalised between layers', bin: 'graphite' },
      { id: 'd-insulate', text: 'Does NOT conduct electricity — all 4 outer electrons are used in bonds', bin: 'diamond' },
      { id: 'g-uses',    text: 'Used as pencil lead and as electrodes in electrolysis', bin: 'graphite' },
      { id: 'd-uses',    text: 'Used for cutting tools and as a gemstone — hardest natural substance', bin: 'diamond' },
    ],
    hint: 'Both are pure carbon. Diamond: 4 bonds per carbon in a rigid 3-D lattice — very hard, no free electrons, does not conduct. Graphite: 3 bonds per carbon, layers slide, 1 delocalised electron per carbon carries charge — so it conducts.',
  };

  /* ---- chemical-bonds · Categorise Bins (Hero 09) — a 3-way category
     sort. Card text is copied VERBATIM from the `matching` block in
     all_subtopics_chemistry*.py (frozen science). Bin emoji/tint/prompt
     and the dark hint recap are presentation only and add no new fact.
     Green stays reserved for the ✓ "correct" mark, so the three bins use
     warm / cool / neutral tints. ---- */
  bonding['chemical-bonds-bins'] = {
    emoji: '🔗', title: 'Which bond type?', subtitle: 'sort each substance by how its atoms bond',
    prompt: 'Tap a substance, then tap a bond type. What the atoms ARE — metal or non-metal — decides the bond. Tap a placed card to send it back.',
    trayLabel: 'SUBSTANCES · tap one, then tap a bond type',
    bins: [
      { key: 'ionic',    label: 'Ionic',    emoji: '🧂', tint: 'warm' },
      { key: 'covalent', label: 'Covalent', emoji: '💧', tint: 'cool' },
      { key: 'metallic', label: 'Metallic', emoji: '🔩', tint: 'neutral' },
    ],
    cards: [
      { id: 'cb-nacl', text: 'Sodium chloride (NaCl) — metal Na transfers electron to non-metal Cl', bin: 'ionic' },
      { id: 'cb-h2o',  text: 'Water (H₂O) — two non-metals sharing electrons', bin: 'covalent' },
      { id: 'cb-cu',   text: 'Copper wire — metal atoms releasing electrons into a delocalised sea', bin: 'metallic' },
      { id: 'cb-mgo',  text: 'Magnesium oxide (MgO) — metal + non-metal, electron transfer', bin: 'ionic' },
      { id: 'cb-co2',  text: 'Carbon dioxide (CO₂) — two non-metals sharing electron pairs', bin: 'covalent' },
    ],
    hint: 'Metal + non-metal → ionic (electrons transferred). Non-metal + non-metal → covalent (electrons shared). A pure metal → metallic (electrons delocalised into a sea).',
  };

  /* ---- properties-small-molecules · Categorise Bins — a 2-way sort of
     properties into simple-molecular vs giant. Cards VERBATIM from the
     `matching` block; the "conducts when molten/dissolved" card is a giant
     IONIC property, so it maps to the giant bin. Presentation only. ---- */
  bonding['properties-small-molecules-bins'] = {
    emoji: '🧬', title: 'Simple molecular or giant?', subtitle: 'sort each property by structure type',
    prompt: 'Tap a property, then tap a structure type. Simple molecular = small separate molecules with weak forces between them; giant = strong bonds running throughout. Tap a placed card to send it back.',
    trayLabel: 'PROPERTIES · tap one, then tap a structure',
    bins: [
      { key: 'simple', label: 'Simple molecular', emoji: '💧', tint: 'cool' },
      { key: 'giant',  label: 'Giant structure',  emoji: '🧱', tint: 'warm' },
    ],
    cards: [
      { id: 'sm-lowmp',   text: 'Low melting point — weak intermolecular forces between molecules overcome easily', bin: 'simple' },
      { id: 'sm-highmp',  text: 'Very high melting point — many strong bonds throughout the entire structure', bin: 'giant' },
      { id: 'sm-gasliq',  text: 'Often gases or liquids at room temperature', bin: 'simple' },
      { id: 'sm-noconduct', text: 'Does not conduct electricity — no free ions or electrons', bin: 'simple' },
      { id: 'sm-molten',  text: 'Conducts when molten or dissolved — free ions carry charge', bin: 'giant' },
    ],
    hint: 'Simple molecular: small separate molecules, weak forces between them → low MP, no conduction. Giant structures: strong bonds throughout → very high MP; giant ionic ones conduct when molten or dissolved.',
  };

  /* ==========================================================
     B2 — metallic-bonding · Two-State Compare (electron-sea on/off)
     The bonding MODEL: with the delocalised sea, the metal conducts
     and its ion layers slide; imagine the electrons pinned to their
     atoms and neither works. Captions authored from the frozen
     `theory` + `common_mistake`. Colour = meaning via `tone`.
     ========================================================== */
  bonding['metallic-bonding'] = {
    emoji: '⚡', title: 'The Electron Sea', subtitle: 'what the delocalised electrons actually do',
    strap: 'Metallic bond = the strong electrostatic attraction between the positive metal ions and the sea of delocalised electrons — NOT an attraction between atoms.',
    /* Phase 1a predict gate — grounded in frozen theory: conduction needs
       delocalised (free-moving) electrons. */
    predict: {
      question: 'Imagine every outer electron stayed stuck to its own atom. Would the metal still conduct?',
      options: ['Yes — metals always conduct', 'No — nothing free to carry charge'],
      correctIndex: 1,
      revealsOn: 'state:off',
    },
    states: [
      {
        key: 'on', label: '🌊 Electron sea ON', emoji: '🌊', tone: 'good',
        effectTitle: 'Conducts electricity and heat — and the metal bends, not shatters',
        caption: 'The outer electrons are delocalised — free to move through the whole lattice of positive ions. They carry charge (electricity) and thermal energy (heat), and because the sea re-surrounds the ions wherever they go, layers of ions can slide past each other, so the metal is malleable and ductile.',
        legend: 'positive ions in a regular lattice · delocalised electrons drift freely',
        props: [
          { k: 'Melting point', v: 'High', tone: 'neutral' },
          { k: 'Conducts electricity', v: 'Yes ✓', tone: 'good' },
          { k: 'Conducts heat', v: 'Yes ✓', tone: 'good' },
          { k: 'Malleable / ductile', v: 'Yes', tone: 'neutral' },
        ],
        visual: { type: 'electronSea', free: true },
      },
      {
        key: 'off', label: '📍 Electrons pinned', emoji: '📍', tone: 'bad',
        effectTitle: 'No moving charge — and no metallic bond at all',
        caption: 'If every outer electron stayed stuck to its own atom, there would be no free charge to carry electricity or heat — and no shared sea to hold the positive ions together. The delocalised sea is exactly what makes a metal a metal. (This state is imaginary — a metal always has its sea.)',
        legend: 'electrons stuck to their atoms · nothing free to move',
        props: [
          { k: 'Conducts electricity', v: 'No ✕', tone: 'bad' },
          { k: 'Conducts heat', v: 'No ✕', tone: 'bad' },
          { k: 'Metallic bond', v: 'None', tone: 'bad' },
        ],
        visual: { type: 'electronSea', free: false },
      },
    ],
  };

  /* ==========================================================
     B2 — metals-alloys · Two-State Compare (metalLayers + force)
     STRUCTURE → PROPERTY: pure metal layers slide under force (soft),
     an alloy's different-sized atoms block the sliding (hard). The
     force button drives the shear; per-state `forced` overrides swap
     the caption. Conduction is owned by metallic-bonding, so it is a
     plain-fact prop here, not the interaction.
     ========================================================== */
  bonding['metals-alloys'] = {
    emoji: '🔩', title: 'Why Alloys Are Harder', subtitle: 'apply a force and watch the layers',
    strap: 'A metal is a giant lattice of positive ions in a sea of delocalised electrons. Pure metals are soft because the layers slide; alloys are harder because different-sized atoms stop the layers sliding.',
    force: { label: '🔨 Apply force', undoLabel: '↩ Release force' },
    /* Phase 1a predict gate — the council's wager (§4.11): commit before the
       first force press. Grounded in frozen theory: layer sliding vs disruption. */
    predict: {
      question: 'An alloy mixes different-sized atoms into the lattice. Under the same force, will it bend more or less than the pure metal?',
      options: ['More — the gaps make it floppier', 'Less — the layers can no longer slide'],
      correctIndex: 1,
      revealsOn: 'force',
    },
    states: [
      {
        key: 'pure', label: '⬜ Pure metal', emoji: '⬜', tone: 'neutral',
        effectTitle: 'Regular layers of one metal — soft and malleable',
        caption: 'Every ion is the same size, so they pack into neat, evenly-spaced layers. Apply a force to see what happens.',
        legend: 'identical ions · neat layers that can slide',
        forced: {
          tone: 'good',
          effectTitle: 'Layers slide → the metal bends ✓',
          caption: 'The layers slip over one another, so the metal changes shape without breaking — the electron sea just re-surrounds the ions in their new positions. This is why pure metals are soft and easily shaped.',
          legend: 'force applied · layers shear cleanly → bends',
        },
        props: [
          { k: 'Hardness', v: 'Soft', tone: 'neutral' },
          { k: 'Malleable', v: 'Yes', tone: 'neutral' },
          { k: 'Conducts (solid)', v: 'Yes ✓', tone: 'good' },
        ],
        visual: { type: 'metalLayers', alloy: false },
      },
      {
        key: 'alloy', label: '🔶 Alloy', emoji: '🔶', tone: 'neutral',
        effectTitle: 'Different-sized atoms mixed in — harder and stronger',
        caption: 'Atoms of another element (darker) sit among the main ions and distort the regular layers. Apply a force to compare.',
        legend: 'different-sized atoms · distorted layers',
        forced: {
          tone: 'accent',
          effectTitle: 'Sliding blocked → it resists ✕',
          caption: 'The odd-sized atoms stop the layers sliding cleanly, so the alloy keeps its shape under the force. That is why alloys such as steel, bronze and brass are harder and stronger than the pure metal.',
          legend: 'force applied · layers cannot slide → resists',
        },
        props: [
          { k: 'Hardness', v: 'Hard', tone: 'neutral' },
          { k: 'Malleable', v: 'Less', tone: 'neutral' },
          { k: 'Conducts (solid)', v: 'Yes ✓', tone: 'good' },
        ],
        visual: { type: 'metalLayers', alloy: true },
      },
    ],
  };

  /* ==========================================================
     B3 — ionic-bonding · Dot-and-Cross Stepper (transfer)
     Molecule picker: NaCl (1e), MgO (2e), MgCl₂ (2×1e, tri layout).
     Steps + configs authored from the frozen `theory` dot-and-cross
     summaries. dots (•) = electrons from the metal.
     ========================================================== */
  bonding['ionic-bonding'] = {
    emoji: '⚛️', title: 'Electron Transfer',
    /* Phase 1a predict gate — gates the NaCl transfer step (step index 2).
       Grounded in frozen theory: transfer, not sharing; distractors mirror the
       frozen quiz's transfer-vs-share confusion. */
    predict: {
      question: 'Sodium’s single outer electron is highlighted. What happens to it?',
      options: ['It is shared between Na and Cl', 'It transfers completely to chlorine'],
      correctIndex: 1,
      revealsOn: 'step:2',
    },
    molecules: [
      {
        name: 'NaCl', mode: 'transfer', layout: 'di',
        left:  { sym: 'Na', cfgBefore: '2.8.1', cfgAfter: '2.8', charge: '+', outer: 1, r: 74 },
        right: { sym: 'Cl', cfgBefore: '2.8.7', cfgAfter: '2.8.8', charge: '−', outer: 7, r: 74 },
        steps: [
          { phase: 'neutral', title: 'Two neutral atoms', caption: 'Na (2.8.1) has 1 outer electron. Cl (2.8.7) has 7 — one space left in its outer shell.' },
          { phase: 'focus', title: 'Spot the electron that moves', caption: 'Sodium’s single outer electron (•) is the one that will transfer — metals lose their outer electrons.' },
          { phase: 'moved', title: 'Transfer', caption: 'The electron moves into chlorine’s outer shell, filling the gap. Nothing is shared — it is given away.' },
          { phase: 'moved', title: 'Ions formed → the bond', caption: 'Na⁺ (2.8) and Cl⁻ (2.8.8) both have full outer shells. Opposite charges attract — that electrostatic attraction IS the ionic bond.' },
        ],
        result: 'Na⁺ + Cl⁻ → NaCl — the electrostatic attraction between the ions IS the ionic bond',
      },
      {
        name: 'MgO', mode: 'transfer', layout: 'di',
        left:  { sym: 'Mg', cfgBefore: '2.8.2', cfgAfter: '2.8', charge: '2+', outer: 2, r: 74 },
        right: { sym: 'O', cfgBefore: '2.6', cfgAfter: '2.8', charge: '2−', outer: 6, r: 74 },
        steps: [
          { phase: 'neutral', title: 'Two neutral atoms', caption: 'Mg (2.8.2) has 2 outer electrons. O (2.6) has 6 — it needs 2 more for a full shell.' },
          { phase: 'focus', title: 'Two electrons will move', caption: 'Both of magnesium’s outer electrons (•) transfer — a Group 2 metal loses 2 electrons.' },
          { phase: 'moved', title: 'Transfer', caption: 'Both electrons move into oxygen’s outer shell, completing it.' },
          { phase: 'moved', title: 'Ions formed → the bond', caption: 'Mg²⁺ and O²⁻ each have full shells. Double charges attract more strongly than in NaCl — MgO has a much higher melting point.' },
        ],
        result: 'Mg²⁺ + O²⁻ → MgO — double charges → stronger attraction → higher melting point',
      },
      {
        name: 'MgCl₂', mode: 'transfer', layout: 'tri',
        left:  { sym: 'Mg', cfgBefore: '2.8.2', cfgAfter: '2.8', charge: '2+', outer: 2, r: 58 },
        right: { sym: 'Cl', cfgBefore: '2.8.7', cfgAfter: '2.8.8', charge: '−', outer: 7, r: 58 },
        steps: [
          { phase: 'neutral', title: 'One metal, two non-metals', caption: 'Mg has 2 outer electrons to give. Each Cl needs just 1 — so it takes two chlorines to accept both.' },
          { phase: 'focus', title: 'One electron to each chlorine', caption: 'Magnesium’s two outer electrons (•) will go one to each chlorine atom.' },
          { phase: 'moved', title: 'Transfer', caption: 'Each Cl gains one electron and becomes Cl⁻; magnesium becomes Mg²⁺.' },
          { phase: 'moved', title: 'Charges balance', caption: 'One Mg²⁺ (2+) is balanced by two Cl⁻ (2 × 1−). Overall charge = 0, so the formula is MgCl₂.' },
        ],
        result: 'Mg²⁺ + 2 Cl⁻ → MgCl₂ — 2 chloride ions balance one Mg²⁺ (overall charge zero)',
      },
    ],
  };

  /* ==========================================================
     B3 — covalent-bonding · Dot-and-Cross Stepper (share)
     Diatomic-only picker: H₂, Cl₂, HCl (port map §6). Polyatomic
     molecules (H₂O, CH₄, NH₃, CO₂) appear as static feature-cards on
     the page, not in the hero. dots (•) = one atom, crosses (×) = the
     other; the overlap is the shared pair.
     ========================================================== */
  bonding['covalent-bonding'] = {
    emoji: '⚛️', title: 'Sharing a Pair',
    /* Phase 1a predict gate — gates the H₂ shared-pair step (step index 2).
       Grounded in frozen theory: non-metals share; neither can give away. */
    predict: {
      question: 'Two hydrogen atoms each need one more electron. How do both end up with a full shell?',
      options: ['One gives its electron to the other', 'They share a pair of electrons'],
      correctIndex: 1,
      revealsOn: 'step:2',
    },
    molecules: [
      {
        name: 'H₂', mode: 'share', layout: 'di',
        left:  { sym: 'H', cfgBefore: '1', cfgAfter: '2 (shared)', charge: '', outer: 1, r: 48 },
        right: { sym: 'H', cfgBefore: '1', cfgAfter: '2 (shared)', charge: '', outer: 1, r: 48 },
        steps: [
          { phase: 'neutral', title: 'Two non-metal atoms', caption: 'Each hydrogen has 1 electron and needs 1 more for a full shell (2). Neither can afford to give one away.' },
          { phase: 'focus', title: 'One electron from each', caption: 'Both hydrogens’ electrons are highlighted — they will pair up in the middle.' },
          { phase: 'moved', title: 'Shared pair = one bond', caption: 'One electron from each atom sits in the overlap. Both hydrogens now count a full shell of 2. One shared pair = one single covalent bond.' },
        ],
        result: 'H–H — one shared pair of electrons = one single covalent bond',
      },
      {
        name: 'Cl₂', mode: 'share', layout: 'di',
        left:  { sym: 'Cl', cfgBefore: '2.8.7', cfgAfter: '2.8.8 (shared)', charge: '', outer: 7, r: 74 },
        right: { sym: 'Cl', cfgBefore: '2.8.7', cfgAfter: '2.8.8 (shared)', charge: '', outer: 7, r: 74 },
        steps: [
          { phase: 'neutral', title: 'Two non-metal atoms', caption: 'Each chlorine has 7 outer electrons and needs just 1 more for a full shell of 8.' },
          { phase: 'focus', title: 'One electron from each', caption: 'Each chlorine offers one outer electron (•/×) to a shared pair.' },
          { phase: 'moved', title: 'Shared pair = one bond', caption: 'The shared pair sits between the two atoms, giving each chlorine a full shell of 8. One shared pair = one single covalent bond.' },
        ],
        result: 'Cl–Cl — one shared pair completes both shells (each Cl now has 8)',
      },
      {
        name: 'HCl', mode: 'share', layout: 'di',
        left:  { sym: 'H', cfgBefore: '1', cfgAfter: '2 (shared)', charge: '', outer: 1, r: 48 },
        right: { sym: 'Cl', cfgBefore: '2.8.7', cfgAfter: '2.8.8 (shared)', charge: '', outer: 7, r: 74 },
        steps: [
          { phase: 'neutral', title: 'Two non-metal atoms', caption: 'H needs 1 more electron; Cl needs 1 more. Neither gives one away — they share.' },
          { phase: 'focus', title: 'One electron from each', caption: 'Hydrogen’s electron (•) and one of chlorine’s (×) are highlighted — they will pair up.' },
          { phase: 'moved', title: 'Shared pair = one bond', caption: 'The shared pair gives H a full shell of 2 and Cl a full shell of 8. One shared pair = one single covalent bond.' },
        ],
        result: 'H–Cl — one shared pair of electrons = one single covalent bond',
      },
    ],
  };

  /* ==========================================================
     B3 — ionic-compounds · State Toggle Lab (NaCl)
     4 states (solid / molten / in solution / + force → shatter). The
     lattice conducts only when the ions are free to move; force shows
     brittleness (layers shift → like charges repel → shatter). Hints
     authored from the frozen `theory` + `common_mistake`.
     ========================================================== */
  bonding['ionic-compounds'] = {
    emoji: '🔬', title: 'Ionic Lattice Lab', subtitle: 'why can it conduct… and why does it shatter?',
    /* Phase 1a predict gate — gates the molten reveal. Grounded in frozen
       theory + wrong-exp bank: conduction = mobile IONS, never free electrons. */
    predict: {
      question: 'Solid sodium chloride does not conduct. What happens when it melts?',
      options: ['Still no conduction — same substance', 'Conducts — the ions are free to move', 'Conducts — melting frees electrons'],
      correctIndex: 1,
      revealsOn: 'state:molten',
    },
    ions: { pos: { glyph: '+' }, neg: { glyph: '−' } },
    grid: { cols: 7, rows: 5 },
    states: [
      { key: 'solid', label: '🧊 Solid', arrangement: 'lattice',
        verdict: { glow: false, title: 'No conduction ✕', sub: 'Ions are fixed in the lattice.' },
        hint: 'Solid lattice: ions locked in a regular 3-D pattern, alternating + and −. Strong forces in all directions → high melting point, and no conduction (the ions cannot move).' },
      { key: 'molten', label: '🔥 Molten', arrangement: 'jiggle',
        verdict: { glow: true, title: 'Conducts ✓', sub: 'Free-moving ions carry the charge.' },
        hint: 'Molten: enough energy has broken the lattice down, so the ions are now free to move and carry charge → it conducts.' },
      { key: 'solution', label: '💧 In solution', arrangement: 'dissolved',
        verdict: { glow: true, title: 'Conducts ✓', sub: 'Free-moving ions carry the charge.' },
        hint: 'Dissolved: water molecules surround the ions and pull them out of the lattice (hydration). The free-moving ions make the solution conduct.' },
      { key: 'shatter', label: '💥 Shattered', inToggle: false, arrangement: 'sheared',
        verdict: { glow: false, title: 'No conduction ✕', sub: 'Still a solid — ions still fixed.' },
        hint: 'A force shifted the layers → like charges (+ above +) now sit together and repel strongly → the crystal shatters instead of bending. This is why ionic solids are hard but brittle.' },
    ],
    force: { from: 'solid', to: 'shatter', label: '💥 Apply force (test brittleness)', undoLabel: '↩ Un-shatter' },
  };

  /* ==========================================================
     B5 — properties-ionic-compounds · Categorise Bins (Ionic / Metal / Both)
     Cards VERBATIM from the frozen `matching` (an ionic-vs-metal sort;
     the shared high-MP row → "Both"). Bin tint/emoji presentation only.
     ========================================================== */
  bonding['properties-ionic-compounds-bins'] = {
    emoji: '⚖️', title: 'Ionic compound, metal, or both?', subtitle: 'sort each property by structure',
    prompt: 'Tap a property, then tap a structure. Ionic compounds and metals share some properties (like high melting points) but differ in others. Tap a placed card to send it back.',
    trayLabel: 'PROPERTIES · tap one, then tap a structure',
    bins: [
      { key: 'ionic', label: 'Ionic compound', emoji: '🧂', tint: 'warm' },
      { key: 'metal', label: 'Metal', emoji: '🔩', tint: 'cool' },
      { key: 'both', label: 'Both', emoji: '🤝', tint: 'neutral' },
    ],
    cards: [
      { id: 'pic-brittle', text: 'Brittle — shatters when struck due to repulsion between like-charged ions', bin: 'ionic' },
      { id: 'pic-malleable', text: 'Malleable — layers of ions can slide without breaking the metallic bond', bin: 'metal' },
      { id: 'pic-molten', text: 'Conducts electricity when molten but not when solid', bin: 'ionic' },
      { id: 'pic-solid', text: 'Conducts electricity in solid state — delocalised electrons carry charge', bin: 'metal' },
      { id: 'pic-highmp', text: 'High melting points — strong electrostatic forces throughout the structure', bin: 'both' },
    ],
    hint: 'Ionic compounds: brittle, conduct only when molten/dissolved (mobile ions). Metals: malleable, conduct as solids (delocalised electrons). Both have high melting points — strong electrostatic forces throughout.',
  };
})();
