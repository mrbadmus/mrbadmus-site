/* Authored exam content — giant-covalent-structures
   Source: ~/Documents/mrb-authoring/phase2-exam/giant-covalent-structures.html (MRB-136 Phase 2A, approved 24 Jul 2026)
   Net-new authored content. Never written into the 8 frozen fields.
   Misconception slugs are verbatim join keys to the MRB-135 MCQ banks — do not rename. */
(function () {
  'use strict';
  var C = (window.MrbExamContent = window.MrbExamContent || {});

  C['giant-covalent-structures'] = {
    page: 'giant-covalent-structures',
    title: 'Giant Covalent Structures',
    spec: '5.2.2.6',
    specNote: 'Spec 5.2.2.6 (+ 5.2.3 graphene/fullerenes)',
    badge: '6-MARK BANKER №2',

    /* Tier-tagging note carried verbatim from the authored file's flag box. */
    tierFlag: 'Tier-tagging note (frozen-content defect, carried from Gate 0): graphene, fullerenes and carbon nanotubes are NOT Higher-only in AQA Trilogy 5.2.3.3, yet the frozen page places them in an HT-only box. Any transfer item on graphene/C₆₀/nanotubes below is therefore tagged Foundation-accessible, not Higher-only. Flagged, not fixed — see summary.rtf.',

    /* [CHECK] index for this page — page-level, verbatim. */
    checkIndex: [
      'graphene/fullerenes/nanotubes tier — I have tagged transfer items on these as Foundation-accessible because AQA 5.2.3.3 carries no HT marker; this contradicts the frozen HT-only box (Gate 0 defect). Confirm before build tags them Higher.',
      '1A tariff of 6 marks — diamond-vs-graphite compare is a genuine AQA levels banker; confident.',
      '"weak intermolecular forces between layers" vs "weak forces between layers" — both credited; allow both.',
      'SiO₂ melting point not quoted anywhere in frozen content, so no accept-value asserted — 1E/Chain C use it qualitatively only.'
    ],

    misconceptions: [
      { slug: 'graphite-is-metallic',
        statement: '"Graphite conducts because it has metallic bonding (and diamond has ionic bonding)."',
        source: 'quiz Q1 distractor' },
      { slug: 'more-atoms-more-conduction',
        statement: '"Graphite packs more atoms per layer, and more atoms means better conductivity."',
        source: 'quiz Q1 distractor' },
      { slug: 'transparency-conducts',
        statement: '"Diamond is transparent, so charge passes through as light."',
        source: 'quiz Q1 distractor' },
      { slug: 'graphite-smooth-surface',
        statement: '"Graphite is slippery because its surface is so smooth there are no atoms to catch on."',
        source: 'quiz Q2 distractor' },
      { slug: 'graphite-dissolves-lubricant',
        statement: '"It dissolves in water between surfaces to make a slippery solution."',
        source: 'quiz Q2 distractor' },
      { slug: 'hard-makes-slippery',
        statement: '"It is as hard as diamond, and hard materials make surfaces slippery."',
        source: 'quiz Q2 distractor' },
      { slug: 'giant-covalent-is-molecular',
        statement: '"Its separate molecules are held by unusually strong intermolecular forces."',
        source: 'quiz Q3 distractor' },
      { slug: 'covalent-lattice-is-ionic',
        statement: '"Strong ionic bonds between oppositely charged carbon ions."',
        source: 'quiz Q3 distractor' },
      { slug: 'diamond-has-electron-sea',
        statement: '"Delocalised electrons form a sea that holds the carbon atoms in place."',
        source: 'quiz Q3 distractor' },
      { slug: 'allotropes-different-elements',
        statement: '"Diamond and graphite contain different elements."',
        source: 'quiz Q5 distractor' },
      { slug: 'diamond-graphite-metal-nonmetal',
        statement: '"One is a metal and the other a non-metal."',
        source: 'quiz Q5 distractor' },
      { slug: 'soft-means-low-mp',
        statement: '"Graphite\'s layers slide easily, so it must melt at a low temperature."',
        source: 'built on Higher Q + examiner tip' }
    ],

    writeThenMark: [
      {
        id: 'gcs-1a',
        label: '1A',
        heading: 'THE 6-MARKER (banker)',
        stem: 'Diamond and graphite are both forms of carbon, but they have very different properties. Compare the structure and bonding of diamond and graphite, and explain why diamond is hard and does not conduct electricity, while graphite is soft and does conduct electricity.',
        tariff: 6,
        command: 'Compare/Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: true,
        note: 'Award any 6. A Level-3 answer covers both substances and links every property to the bond count / electrons (see §2).',
        markingPoints: [
          { id: 'mp1', text: 'Each carbon atom is bonded to 4 other carbon atoms.', strand: 'Diamond', essential: true },
          { id: 'mp2', text: 'by strong covalent bonds, in a giant rigid 3D lattice.', strand: 'Diamond', essential: true },
          { id: 'mp3', text: 'all 4 outer electrons are used in bonds → no free (delocalised) electrons → does not conduct.', strand: 'Diamond', essential: true },
          { id: 'mp4', text: 'the rigid 3D network of many strong bonds makes it hard (and gives a very high melting point).', strand: 'Diamond', essential: true },
          { id: 'mp5', text: 'Each carbon atom is bonded to 3 other carbon atoms, in layers / hexagonal sheets.', strand: 'Graphite', essential: true },
          { id: 'mp6', text: 'the 4th outer electron of each carbon is delocalised → free to move → carries charge → conducts.', strand: 'Graphite', essential: true },
          { id: 'mp7', text: 'the layers are held by weak forces between them → layers slide over each other → soft / slippery.', strand: 'Graphite', essential: true }
        ],
        allow: [
          '"bonded to 4/3 others"',
          '"spare/free electron" for the 4th delocalised electron',
          '"layers slide over each other" for soft',
          '"weak forces between layers" OR "weak intermolecular forces between layers" for MP7'
        ],
        doNotAccept: [
          { text: 'graphite conducts because it is metallic/ionic', slug: 'graphite-is-metallic' },
          { text: '"more atoms conduct better"', slug: 'more-atoms-more-conduction' },
          { text: 'diamond has free/delocalised electrons' },
          { text: '"covalent bonds between the layers" (there are none — the interlayer forces are weak)' },
          { text: '"different elements"', slug: 'allotropes-different-elements' }
        ],
        tierNotes: {
          foundation: 'diamond = 4 bonds, rigid 3D, all electrons used → hard, no conduction; graphite = 3 bonds, layers, 4th electron delocalised → conducts, layers slide → soft. Both substances, each property linked.',
          higher: 'precise naming of the interlayer forces as weak (not "no bonds"), and that the within-layer covalent bonds stay strong (this is why graphite\'s MP stays high — see 1D); transfer to graphene/SiO₂ if asked.'
        },
        levels: [
          { level: 3, marks: [5, 6], descriptor: 'You cover both diamond and graphite AND link every property to the bonding: hard ← rigid 3D of 4 strong bonds; no conduction ← all 4 electrons used; conducts ← 3 bonds leave a delocalised electron; soft ← weak forces between layers let them slide. Structure and property are joined every time.' },
          { level: 2, marks: [3, 4], descriptor: 'Both structures described and some properties linked, but a link is missing or one substance is thin. E.g. graphite fully explained, but diamond is only "it\'s hard because strong" without the 4-bonds/all-electrons detail; or you explain the structures but leave one property (usually "soft") unexplained.' },
          { level: 1, marks: [1, 2], descriptor: 'Isolated facts — you state properties or structures but don\'t link them. "Diamond is hard, graphite is soft, both are carbon" with no mechanism.' },
          { level: 0, marks: [0, 0], descriptor: 'Nothing relevant, or only misconceptions.' }
        ],
        capFailures: [
          'Describing properties without linking to bonding — the classic Level-1 trap; the compare-cards on the page give you the facts, but marks come from the because.',
          'Conflating the models — "graphite is metallic / diamond is ionic" — the bonding model is wrong, so those marks are gone.',
          'Only doing one substance — a full diamond answer with no graphite (or vice versa) caps at Level 2.',
          'Saying there are "covalent bonds between the layers" — there aren\'t; that misunderstands why graphite is soft.'
        ]
      },

      {
        id: 'gcs-1b',
        label: '1B',
        heading: 'Explain conduction contrast',
        stem: 'Explain why graphite conducts electricity but diamond does not.',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q1)',
        markingPoints: [
          { id: 'mp1', text: 'in graphite each carbon bonds to only 3 others, leaving 1 delocalised (free) electron per carbon.', essential: true },
          { id: 'mp2', text: 'these electrons are free to move and carry charge.', essential: true },
          { id: 'mp3', text: 'in diamond each carbon bonds to 4 others, using all 4 outer electrons, so there are no free electrons to carry charge.', essential: true }
        ],
        allow: [],
        doNotAccept: [
          { text: 'metallic/ionic bonding', slug: 'graphite-is-metallic' },
          { text: '"more atoms"', slug: 'more-atoms-more-conduction' },
          { text: 'transparency', slug: 'transparency-conducts' }
        ],
        tierNote: 'Foundation-safe.'
      },

      {
        id: 'gcs-1c',
        label: '1C',
        heading: 'Explain lubrication',
        stem: 'Explain why graphite is used as a lubricant.',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q2)',
        markingPoints: [
          { id: 'mp1', text: 'graphite is made of layers of carbon atoms.', essential: true },
          { id: 'mp2', text: 'the layers are held together by weak forces (between layers).', essential: true },
          { id: 'mp3', text: 'so the layers can slide over each other easily.', essential: true }
        ],
        allow: [],
        doNotAccept: [
          { text: 'smooth/atom-free surface', slug: 'graphite-smooth-surface' },
          { text: 'dissolves', slug: 'graphite-dissolves-lubricant' },
          { text: '"hard like diamond"', slug: 'hard-makes-slippery' }
        ],
        tierNote: 'Foundation-safe.'
      },

      {
        id: 'gcs-1d',
        label: '1D',
        heading: 'The discrimination question',
        stem: 'Explain why graphite has a high melting point even though its layers can slide over each other easily.',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q — the council\'s "best question")',
        markingPoints: [
          { id: 'mp1', text: 'within each layer, each carbon is joined to 3 others by strong covalent bonds.', essential: true },
          { id: 'mp2', text: 'melting requires breaking these strong covalent bonds, which needs a large amount of energy → high melting point.', essential: true },
          { id: 'mp3', text: 'the easy sliding is due to the weak forces between layers — a different set of forces, which sliding overcomes without breaking the covalent bonds.', essential: true }
        ],
        allow: [
          'the explicit within-layer (strong covalent) vs between-layer (weak) distinction for MP3'
        ],
        doNotAccept: [
          { text: '"soft means low melting point"', slug: 'soft-means-low-mp' },
          { text: '"giant structures always melt high" as the sole reason (unexplained rule)' }
        ],
        tierNote: 'Higher-only. Tests whether the student can hold two force types apart. Grade 8/9 discriminator.'
      },

      {
        id: 'gcs-1e',
        label: '1E',
        heading: 'Explain diamond hardness/MP',
        stem: 'Explain why diamond is very hard and has a very high melting point.',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q3)',
        markingPoints: [
          { id: 'mp1', text: 'every carbon is joined to 4 others by strong covalent bonds.', essential: true },
          { id: 'mp2', text: 'in a giant rigid 3D lattice, throughout the structure.', essential: true },
          { id: 'mp3', text: 'a lot of energy is needed to break the many strong covalent bonds (→ high MP); the rigid network → hard.', essential: true }
        ],
        allow: [],
        doNotAccept: [
          { text: 'intermolecular forces', slug: 'giant-covalent-is-molecular' },
          { text: 'ionic bonds', slug: 'covalent-lattice-is-ionic' },
          { text: 'electron sea', slug: 'diamond-has-electron-sea' }
        ],
        tierNote: 'Foundation-safe.',
        transferNote: 'SiO₂ is the direct transfer (frozen Higher Q "why SiO₂ has a very high MP") — same MPs, different substance.'
      }
    ],

    beTheExaminer: [
      {
        id: 'gcs-be1',
        label: '4A',
        targetItemId: 'gcs-1a',
        heading: 'Partially right (earns marks)',
        studentAnswer: '"Diamond is hard because it has really strong bonds all through it and every carbon is joined to four others. Graphite is soft and slippery, which is why it\'s used in pencils. Graphite conducts electricity but diamond can\'t, because graphite is a metal and metals conduct."',
        officialMark: 3,
        outOf: 6,
        pointsHit: ['mp1', 'mp2', 'mp4'],
        pointsHitNote: 'MP1 (4 bonds), MP2 (strong covalent, throughout), MP4 (hard from the strong-bond network) — the diamond strand is exam-ready (3 marks).',
        pointsMissed: ['mp3', 'mp5', 'mp6', 'mp7'],
        pointsMissedNote: 'graphite side — "soft and slippery" is stated, not explained (no layers / weak forces / sliding → no soft marks, a Level-1 trap); conduction wrongly pinned on "graphite is a metal" (graphite-is-metallic), so the delocalised-electron mechanism is absent → no conduction marks.',
        misconceptionsShown: ['graphite-is-metallic'],
        examinerLine: '"Your diamond half is full marks. Graphite let you down — you named the properties but not the reasons. Add \'3 bonds, spare electron delocalised, weak forces between layers\' and they\'re yours. And graphite is not a metal."',
        partiallyRight: true
      },
      {
        id: 'gcs-be2',
        label: '4B',
        targetItemId: 'gcs-1d',
        heading: 'Low but instructive',
        studentAnswer: '"Graphite\'s layers slide over each other really easily because the forces between them are weak, so it doesn\'t take much energy to move them. Even so it has a high melting point because graphite is a giant structure and giant structures always have high melting points."',
        officialMark: 1,
        outOf: 3,
        pointsHit: ['mp3'],
        pointsHitNote: 'partial — identifies the weak forces between layers (background credit toward MP3\'s distinction).',
        pointsMissed: ['mp1', 'mp2'],
        pointsMissedNote: 'the high MP is attributed to an unexplained rule ("giant structures always do"), not to the strong covalent bonds within each layer that melting must break (MP1/MP2). The student never distinguishes the two force types — the exact discrimination the question tests (soft-means-low-mp avoided but not resolved).',
        misconceptionsShown: [],
        misconceptionsAvoided: ['soft-means-low-mp'],
        examinerLine: '"You spotted the weak forces — good. But you dodged the question: the high melting point comes from the strong covalent bonds WITHIN each layer that melting has to break. \'Giant structures always melt high\' isn\'t an explanation."',
        partiallyRight: false
      }
    ],

    chains: [
      {
        id: 'gcs-chainA',
        label: 'Chain A',
        title: 'Why graphite conducts (diamond doesn\'t)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'In graphite each carbon atom bonds to only 3 others.', role: 'essential' },
          { id: 'l2', text: 'This leaves one outer electron per carbon not used in bonding.', role: 'essential' },
          { id: 'l3', text: 'These electrons are delocalised / free to move.', role: 'essential' },
          { id: 'l4', text: 'The moving electrons carry charge, so graphite conducts.', role: 'essential' },
          { id: 'l5', text: 'In diamond all 4 electrons are used in bonds, so there are none free to conduct.', role: 'creditworthy', roleLabel: 'creditworthy (contrast)' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Graphite conducts because it has metallic bonding.', slug: 'graphite-is-metallic' },
          { id: 'h2', text: 'More atoms per layer means better conduction.', slug: 'more-atoms-more-conduction' },
          { id: 'h3', text: 'Diamond is transparent, so charge passes through it as light.', slug: 'transparency-conducts' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          optional: ['l5'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: '1→2→3→4 strict; link 5 (contrast) may be placed at the end or omitted.'
      },
      {
        id: 'gcs-chainB',
        label: 'Chain B',
        title: 'Why graphite is soft / a lubricant',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Graphite is made of layers of carbon atoms (hexagonal sheets).', role: 'essential' },
          { id: 'l2', text: 'The layers are held together by weak forces between them.', role: 'essential' },
          { id: 'l3', text: 'The layers can slide over each other.', role: 'essential' },
          { id: 'l4', text: 'So graphite is soft / slippery / a good lubricant.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Its surface is so smooth there are no atoms to catch on.', slug: 'graphite-smooth-surface' },
          { id: 'h2', text: 'It dissolves to form a slippery solution.', slug: 'graphite-dissolves-lubricant' },
          { id: 'h3', text: 'It is as hard as diamond, and hard things are slippery.', slug: 'hard-makes-slippery' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: 'strict 1→2→3→4.'
      },
      {
        id: 'gcs-chainC',
        label: 'Chain C',
        title: 'Why diamond is hard + high MP',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Every carbon is bonded to 4 others.', role: 'essential' },
          { id: 'l2', text: 'by strong covalent bonds.', role: 'essential' },
          { id: 'l3', text: 'in a giant rigid 3D lattice throughout the structure.', role: 'creditworthy' },
          { id: 'l4', text: 'Many strong covalent bonds must be broken to melt → high MP; the rigid network → very hard.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Its molecules are held by strong intermolecular forces.', slug: 'giant-covalent-is-molecular' },
          { id: 'h2', text: 'Strong ionic bonds hold the carbon ions together.', slug: 'covalent-lattice-is-ionic' },
          { id: 'h3', text: 'A sea of delocalised electrons holds the atoms in place.', slug: 'diamond-has-electron-sea' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          interchangeable: [['l2', 'l3']],
          mustPrecede: [['l1', 'l2'], ['l1', 'l3'], ['l2', 'l4'], ['l3', 'l4']]
        },
        orderingNote: '1→2 together; 3 may sit before or after 2; 4 last. This chain also serves SiO₂ (swap "carbon" → "silicon and oxygen atoms").'
      }
    ]
  };
})();
