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
})();
