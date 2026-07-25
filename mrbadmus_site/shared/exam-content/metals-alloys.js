/* Authored exam content — metals-alloys
   Source: ~/Documents/mrb-authoring/phase2-exam/metals-alloys.html (MRB-136 Phase 2A, approved 24 Jul 2026)
   Net-new authored content. Never written into the 8 frozen fields.
   Misconception slugs are verbatim join keys to the MRB-135 MCQ banks — do not rename. */
(function () {
  'use strict';
  var C = (window.MrbExamContent = window.MrbExamContent || {});

  C['metals-alloys'] = {
    page: 'metals-alloys',
    title: 'Metals and Alloys',
    spec: '5.2.2.7–5.2.2.8',

    misconceptions: [
      { slug: 'alloy-is-compound',
        statement: '"An alloy is a compound of a metal and another element." (It is a mixture.)',
        source: 'quiz Q7 distractor' },
      { slug: 'alloy-is-purer',
        statement: '"Brass has been purified, and pure metals are always harder."',
        source: 'quiz Q2 distractor' },
      { slug: 'more-bonds-harder',
        statement: '"Brass has more metallic bonds than copper, and more bonds means harder."',
        source: 'quiz Q2 distractor' },
      { slug: 'added-metal-own-hardness',
        statement: '"Zinc is a harder metal, so mixing it in makes the product hard."',
        source: 'quiz Q2 distractor' },
      { slug: 'metal-must-melt-to-conduct',
        statement: '"Metals must melt first to conduct, like ionic compounds."',
        source: 'common_mistake; quiz Q1' },
      { slug: 'ions-carry-heat',
        statement: '"The positive ions carry the heat as they move around."',
        source: 'quiz Q3 distractor' },
      { slug: 'water-spreads-heat',
        statement: '"Metals contain water that spreads the heat."',
        source: 'quiz Q3 distractor' },
      { slug: 'covalent-in-metal',
        statement: '"The covalent bonds pass the heat along." / metals bend because covalent bonds bend.',
        source: 'quiz Q3 distractor' },
      { slug: 'alloy-only-atoms',
        statement: '"A pure metal contains ions but an alloy contains only atoms."',
        source: 'quiz Q4 distractor' },
      { slug: 'pure-metal-no-bonding',
        statement: '"Pure metals contain no metallic bonds, so they fall apart / are soft."',
        source: 'quiz Q4/Q5 distractors' },
      { slug: 'metal-is-molecular',
        statement: '"A pure metal is molecular but an alloy is a giant lattice."',
        source: 'quiz Q4 distractor' },
      { slug: 'size-lets-metal-conduct',
        statement: '"Metal atoms are smaller than ions, so they move more easily."',
        source: 'quiz Q1 distractor' },
      { slug: 'protons-conduct',
        statement: '"Metals have more protons, which makes them better at conducting."',
        source: 'quiz Q1 distractor' }
    ],

    writeThenMark: [
      {
        id: 'ma-1a',
        label: '1A',
        heading: 'THE 6-MARKER (banker)',
        stem: 'Steel is an alloy of iron and carbon. It is used to build bridges instead of pure iron. Explain, in terms of structure and bonding, why pure metals can be bent into shape (are malleable), and why steel is harder than pure iron. [6 marks]',
        tariff: 6,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: true,
        check: true,
        checkNote: '1A tariff (6 marks) — I composed the banker from two frozen strands (malleability + alloy hardness). AQA sets 6-mark items on metallic properties and on alloys; this composite is plausible and coherent, but it is a constructed 6-marker, not lifted from a specific past paper — Mide to confirm the pairing reads as one question.',
        note: 'Award any 6. Two strands sharing one idea — the sliding of layers. A Level-3 answer links both (see §2).',
        markingPoints: [
          { id: 'mp1',
            text: 'A metal is a giant structure — a regular lattice of positive metal ions.',
            strand: 'Malleability strand (pure metal)',
            essential: true },
          { id: 'mp2',
            text: 'surrounded by a sea of delocalised electrons (metallic bonding).',
            strand: 'Malleability strand (pure metal)',
            essential: false,
            tag: '(context; creditworthy)' },
          { id: 'mp3',
            text: 'the layers of ions are all the same size, so they can slide over each other when a force is applied.',
            strand: 'Malleability strand (pure metal)',
            essential: true },
          { id: 'mp4',
            text: 'the metal changes shape without breaking → malleable.',
            strand: 'Malleability strand (pure metal)',
            essential: true },
          { id: 'mp5',
            text: 'an alloy (steel) contains atoms of a different size (carbon) mixed into the iron.',
            strand: 'Alloy-hardness strand',
            essential: true },
          { id: 'mp6',
            text: 'the different-sized atoms distort / disrupt the regular layers.',
            strand: 'Alloy-hardness strand',
            essential: true },
          { id: 'mp7',
            text: 'so the layers can no longer slide over each other easily → steel is harder.',
            strand: 'Alloy-hardness strand',
            essential: true }
        ],
        allow: [
          '"layers of atoms" for layers of ions',
          '"the different-sized atoms get in the way"',
          '"the layers can\'t slide as easily"',
          '"distort/disrupt/break up the regular arrangement"'
        ],
        doNotAccept: [
          { text: '"alloy has more bonds"', slug: 'more-bonds-harder' },
          { text: '"the added atom is just harder"', slug: 'added-metal-own-hardness' },
          { text: '"alloy is purer"', slug: 'alloy-is-purer' },
          { text: '"steel is a compound" — steel is a MIXTURE.', slug: 'alloy-is-compound' }
        ],
        tierNotes: {
          foundation: 'same-size layers slide → soft/malleable; different-sized atoms in the alloy stop the layers sliding → harder.',
          higher: 'name delocalised electrons / metallic bonding precisely, and say why sliding doesn\'t break the metal (the non-directional metallic bonding / electron sea re-accommodates the ions in their new positions); handle the malleable-vs-brittle contrast with ionic (1D).'
        },
        levels: [
          { level: 3, marks: [5, 6],
            descriptor: 'You explain both the malleability of the pure metal and the extra hardness of the alloy, and each is linked to the layers: same-size layers slide → soft/malleable; different-sized atoms distort the layers → can\'t slide → harder. The two strands share one mechanism and you show it.' },
          { level: 2, marks: [3, 4],
            descriptor: 'One strand explained well, the other thin or a link missing. E.g. alloy hardness fully explained but malleability is just "metals are bendy" with no sliding-layers reason; or the structure named but a property left unlinked.' },
          { level: 1, marks: [1, 2],
            descriptor: 'Isolated facts — "metals are malleable, alloys are harder" with no mechanism, or the structure described without linking it to the property.' },
          { level: 0, marks: [0, 0],
            descriptor: 'Nothing relevant, or only misconceptions.' }
        ],
        capFailures: [
          '"An alloy is a compound" — this is the model-level error the page exists to kill; it undermines the whole alloy strand, because the hardening comes from mixing different-sized atoms, not from forming a compound.',
          '"More bonds = harder" — wrong mechanism; the alloy strand scores nothing.',
          'Listing properties without the sliding-layers idea — stays Level 1.',
          'Explaining hardness as "the added atoms bond tightly and hold it together" — backwards; they get in the way of sliding, they don\'t glue it.'
        ]
      },
      {
        id: 'ma-1b',
        label: '1B',
        heading: 'Explain alloy hardness (shorter)',
        stem: 'Explain why brass (copper mixed with zinc) is harder than pure copper. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q2)',
        markingPoints: [
          { id: 'mp1', text: 'the zinc atoms are a different size to the copper atoms.', essential: true },
          { id: 'mp2', text: 'so they distort / disrupt the regular lattice (layers).', essential: true },
          { id: 'mp3', text: 'this stops the layers of atoms sliding over each other → harder.', essential: true }
        ],
        doNotAccept: [
          { text: 'more bonds', slug: 'more-bonds-harder' },
          { text: 'zinc\'s own hardness', slug: 'added-metal-own-hardness' },
          { text: 'purer', slug: 'alloy-is-purer' }
        ],
        tierNote: 'Foundation-safe.'
      },
      {
        id: 'ma-1c',
        label: '1C',
        heading: 'Explain solid-state conduction',
        stem: 'Explain why metals can conduct electricity in the solid state, but ionic compounds cannot. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q1)',
        markingPoints: [
          { id: 'mp1', text: 'metals have delocalised electrons that are free to move, even when solid.', essential: true },
          { id: 'mp2', text: 'these moving electrons carry the charge.', essential: true },
          { id: 'mp3', text: 'in an ionic solid the charge carriers are ions, which are held in fixed positions and cannot move.', essential: true }
        ],
        doNotAccept: [
          { text: '"metals must melt first"', slug: 'metal-must-melt-to-conduct' },
          { text: 'atom size', slug: 'size-lets-metal-conduct' },
          { text: 'protons', slug: 'protons-conduct' }
        ],
        tierNote: 'Foundation-safe. Cross-page: this is also frozen Q on properties-ionic-compounds ("metal vs molten NaCl" Higher).'
      },
      {
        id: 'ma-1d',
        label: '1D',
        heading: 'Malleable vs brittle contrast',
        stem: 'Explain why metals are malleable but ionic compounds are brittle, in terms of what happens when the layers move. [4 marks]',
        tariff: 4,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q)',
        markingPoints: [
          { id: 'mp1', text: 'in a metal, layers of ions can slide over each other.', essential: true },
          { id: 'mp2', text: 'the delocalised electrons / non-directional metallic bonding hold the structure together as it slides → it bends, not breaks (malleable).', essential: true },
          { id: 'mp3', text: 'in an ionic compound, when a layer shifts, like-charged ions line up next to each other.', essential: true },
          { id: 'mp4', text: 'the like charges repel and the crystal shatters (brittle).', essential: true }
        ],
        doNotAccept: [
          { text: 'metals have covalent bonds', slug: 'covalent-in-metal' },
          { text: 'ionic compound "melts" on impact' }
        ],
        tierNote: 'Higher-only. Two-structure contrast; the malleability half needs the "electron sea holds it together" idea, which is the grade-8/9 detail.'
      }
    ],

    beTheExaminer: [
      {
        id: 'ma-be1',
        label: '4A',
        targetItemId: 'ma-1a',
        heading: 'Partially right (earns marks)',
        headingNote: 'marks the 6-marker (1A)',
        studentAnswer: 'Metals are malleable because the atoms can slide over each other when you hit them. Steel is harder than iron because steel is a compound of iron and carbon, and compounds are stronger than pure elements. The carbon atoms bond tightly to the iron and hold everything together.',
        officialMark: 2,
        outOf: 6,
        pointsHit: ['mp3', 'mp4'],
        pointsHitNote: 'MP3/MP4 — "atoms slide over each other → malleable" (the sliding-layers idea, 1–2 marks; the electron sea isn\'t named but the mechanism is there).',
        pointsMissed: ['mp1', 'mp2', 'mp5', 'mp6', 'mp7'],
        pointsMissedNote: 'the whole alloy strand is built on alloy-is-compound — steel is a mixture, not a compound. "Carbon bonds tightly and holds everything together" reverses the real mechanism: different-sized atoms distort the layers so they can\'t slide, they don\'t glue the metal. No alloy marks.',
        misconceptionsShown: ['alloy-is-compound'],
        examinerLine: 'Malleability is on track. But steel is a mixture, not a compound, and alloys are harder because the different-sized atoms get in the way of the sliding layers — not because they \'bond tightly\'. Fix those two and you double your marks.',
        partiallyRight: true
      },
      {
        id: 'ma-be2',
        label: '4B',
        targetItemId: 'ma-1c',
        heading: 'Low but instructive',
        headingNote: 'marks the conduction question (1C)',
        studentAnswer: 'Metals conduct electricity when solid because they have delocalised electrons that are free to move and carry the charge. Ionic compounds can\'t conduct when solid because they have to be melted first before anything can move, the same as all solids.',
        note: '(to 1C, [3 marks])',
        officialMark: 2,
        outOf: 3,
        pointsHit: ['mp1', 'mp2'],
        pointsHitNote: 'MP1+MP2 — delocalised electrons free to move and carry charge (2 marks).',
        pointsMissed: ['mp3'],
        pointsMissedNote: 'MP3 — "all solids must melt first" contradicts the student\'s own first sentence (metals are solids and DO conduct). The real reason is that the ionic charge carriers are ions held in fixed positions (metal-must-melt-to-conduct, half-corrected).',
        misconceptionsShown: ['metal-must-melt-to-conduct'],
        examinerLine: 'Two marks banked. But metals are solids and they conduct — so \'all solids must melt\' can\'t be right. Say ionic compounds don\'t conduct as solids because their charge carriers are ions locked in place.',
        partiallyRight: true
      }
    ],

    chains: [
      {
        id: 'ma-chainA',
        label: 'Chain A',
        title: 'Why an alloy is harder than the pure metal',
        tier: 'any',
        links: [
          { id: 'l1', text: 'A pure metal has layers of atoms that are all the same size.', role: 'essential' },
          { id: 'l2', text: 'These same-size layers can slide over each other easily (so the pure metal is soft).', role: 'essential' },
          { id: 'l3', text: 'An alloy has atoms of a different size mixed in.', role: 'essential' },
          { id: 'l4', text: 'The different-sized atoms distort the regular layers.', role: 'essential' },
          { id: 'l5', text: 'So the layers can no longer slide easily → the alloy is harder.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The alloy has more metallic bonds, and more bonds means harder.', slug: 'more-bonds-harder' },
          { id: 'h2', text: 'The added metal is harder, so the mixture is harder.', slug: 'added-metal-own-hardness' },
          { id: 'h3', text: 'The alloy is purer than the metal, and pure metals are harder.', slug: 'alloy-is-purer' },
          { id: 'h4', text: 'An alloy is a compound, and compounds are harder than metals.', slug: 'alloy-is-compound' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          interchangeable: [['l1', 'l2']],
          mustPrecede: [['l1', 'l3'], ['l2', 'l3'], ['l3', 'l4'], ['l4', 'l5']]
        },
        orderingNote: '1→2 (pure metal) then 3→4→5 (alloy); the two blocks must stay in that order, but 1 and 2 can swap internally.'
      },
      {
        id: 'ma-chainB',
        label: 'Chain B',
        title: 'Why metals conduct (electricity & heat)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'A metal is a lattice of positive ions in a sea of delocalised electrons.', role: 'essential' },
          { id: 'l2', text: 'The delocalised electrons are free to move through the structure, even when solid.', role: 'essential' },
          { id: 'l3', text: 'They drift when a voltage is applied → carry charge (conducts electricity); they also transfer energy → conduct heat.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The positive ions move around and carry the charge/heat.', slug: 'ions-carry-heat' },
          { id: 'h2', text: 'The metal must melt first, like an ionic compound.', slug: 'metal-must-melt-to-conduct' },
          { id: 'h3', text: 'Metals contain water that spreads the heat.', slug: 'water-spreads-heat' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3']]
        },
        orderingNote: 'strict 1→2→3.'
      },
      {
        id: 'ma-chainC',
        label: 'Chain C',
        title: 'Why metals are malleable (contrast with ionic brittle)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'In a metal the layers of ions can slide over each other.', role: 'essential' },
          { id: 'l2', text: 'The delocalised electrons hold the structure together as the ions move (the bonds are not directional).', role: 'essential' },
          { id: 'l3', text: 'So the metal changes shape without breaking → malleable.', role: 'essential' },
          { id: 'l4', text: '(Contrast) In an ionic solid, sliding a layer brings like charges together, they repel, and it shatters.', role: 'creditworthy', roleNote: 'creditworthy (contrast)' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Metals have covalent bonds that bend without breaking.', slug: 'covalent-in-metal' },
          { id: 'h2', text: 'Pure metals have no bonding, which is why they are soft.', slug: 'pure-metal-no-bonding' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          optional: ['l4'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: '1→2→3; link 4 (contrast) at the end or omitted.'
      }
    ],

    checkIndex: [
      '1A tariff (6 marks) — I composed the banker from two frozen strands (malleability + alloy hardness). AQA sets 6-mark items on metallic properties and on alloys; this composite is plausible and coherent, but it is a constructed 6-marker, not lifted from a specific past paper — Mide to confirm the pairing reads as one question.',
      'Steel = iron + 0.1–2% carbon (from frozen theory) — standard.',
      '"layers of ions" vs "layers of atoms" — AQA credits both for metals; allow stated.',
      'FormulaDeducer not applicable to this page (no ionic-formula construction) — deliberate scope call.'
    ]
  };
})();
