/* Authored exam content — properties-ionic-compounds
   Source: ~/Documents/mrb-authoring/phase2-exam/properties-ionic-compounds.html (MRB-136 Phase 2A, approved 24 Jul 2026)
   Net-new authored content. Never written into the 8 frozen fields.
   Misconception slugs are verbatim join keys to the MRB-135 MCQ banks — do not rename. */
(function () {
  'use strict';
  var C = (window.MrbExamContent = window.MrbExamContent || {});

  C['properties-ionic-compounds'] = {
    page: 'properties-ionic-compounds',
    title: 'Properties of Ionic Compounds',
    spec: '5.2.2.3',

    misconceptions: [
      { slug: 'electrons-carry-ionic-current',
        statement: '"Ionic solutions conduct because electrons flow through them, like in a metal." / "Molten ionic compounds conduct using delocalised electrons."',
        source: 'common_mistake; quiz Q2 distractor' },
      { slug: 'ionic-conducts-when-solid',
        statement: '"It contains charged ions, so it should conduct even when solid."',
        source: 'common_mistake; quiz Q1/Q9' },
      { slug: 'melting-creates-ions',
        statement: '"Melting or dissolving creates ions that were not there in the solid."',
        source: 'quiz Q2 distractor' },
      { slug: 'no-ions-in-solid',
        statement: '"The solid contains no ions / only neutral molecules / the ions have lost their charge."',
        source: 'quiz Q9 distractors' },
      { slug: 'water-carries-current',
        statement: '"Only when dissolved — the water is what carries the current."',
        source: 'quiz Q1 distractor' },
      { slug: 'covalent-bonds-in-ionic',
        statement: '"Strong covalent bonds throughout the lattice must be broken / the covalent bonds snap."',
        source: 'quiz Q3/Q4 distractors' },
      { slug: 'crystal-size-sets-mp',
        statement: '"The crystals are large, so more heat is needed."',
        source: 'quiz Q3 distractor' },
      { slug: 'ion-mass-sets-mp',
        statement: '"The ions are very heavy and resist heating."',
        source: 'quiz Q3 distractor' },
      { slug: 'ions-melt-on-impact',
        statement: '"The ions melt at the point of impact" (for shattering).',
        source: 'quiz Q4 distractor' },
      { slug: 'delocalised-electrons-in-ionic',
        statement: '"The delocalised electrons are knocked out of place."',
        source: 'quiz Q4 distractor' },
      { slug: 'higher-charge-repels',
        statement: '"Higher charges repel, so melting point decreases as charge rises."',
        source: 'quiz Q10 distractor' },
      { slug: 'ionic-is-molecule',
        statement: '"A small molecule of a few ions held weakly together."',
        source: 'quiz Q5 distractor' }
    ],

    writeThenMark: [
      {
        id: 'pic-1a',
        label: '1A',
        heading: 'THE 6-MARKER (banker)',
        stem: 'Sodium chloride is an ionic compound. Explain, in terms of its structure and bonding, why sodium chloride has a high melting point, and why it conducts electricity when molten or dissolved but not when solid. [6 marks]',
        tariff: 6,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: true,
        note: 'Indicative content — award any 6. Two strands; a Level-3 answer links both back to structure (see §2 levels).',
        markingPoints: [
          { id: 'mp1',
            text: 'Sodium chloride has a giant ionic lattice / giant structure of (many) ions.',
            strand: 'Melting-point strand',
            essential: true },
          { id: 'mp2',
            text: 'There are strong electrostatic forces of attraction between the oppositely charged ions.',
            strand: 'Melting-point strand',
            essential: true },
          { id: 'mp3',
            text: 'These forces act in all directions throughout the lattice / there are many such attractions.',
            strand: 'Melting-point strand',
            essential: false },
          { id: 'mp4',
            text: 'A large amount of energy is needed to overcome/break these forces, so the melting point is high.',
            strand: 'Melting-point strand',
            essential: true },
          { id: 'mp5',
            text: 'When solid, the ions are held in fixed positions / cannot move (so cannot carry charge).',
            strand: 'Conduction strand',
            essential: true },
          { id: 'mp6',
            text: 'When molten or dissolved, the ions are free to move.',
            strand: 'Conduction strand',
            essential: true },
          { id: 'mp7',
            text: 'The (mobile) ions carry the charge / current.',
            strand: 'Conduction strand',
            essential: true }
        ],
        allow: [
          '"electrostatic attraction between + and − ions" for MP2',
          '"bonds" for the electrostatic forces at Foundation',
          '"current" for charge',
          '"the ions can move about" for "free to move"',
          '"when melted OR when dissolved in water" either freeing route'
        ],
        doNotAccept: [
          { text: 'electrons / delocalised electrons flow or carry the charge', slug: 'electrons-carry-ionic-current' },
          { text: '"melting makes/creates the ions"', slug: 'melting-creates-ions' },
          { text: '"there are no ions in the solid"', slug: 'no-ions-in-solid' },
          { text: '"covalent bonds break/snap"', slug: 'covalent-bonds-in-ionic' },
          { text: '"the water carries the current"', slug: 'water-carries-current' },
          { text: '"molecules"' }
        ],
        tierNotes: {
          foundation: 'giant lattice → strong forces between oppositely charged ions → lots of energy to melt; solid = ions fixed/can\'t move; molten/dissolved = ions free to move and carry charge. The linked chain at basic level earns full marks here.',
          higher: 'use precise language ("electrostatic forces of attraction between oppositely charged ions", not "strong bonds"); and in any comparative variant, bring in charge-magnitude reasoning (see 1D); explicitly distinguish ion-conduction from electron-conduction if the stem contrasts with a metal.'
        },
        levels: [
          { level: 3, marks: [5, 6],
            descriptor: 'You explain both the melting point and the conduction, and every property is linked back to the structure. The chain is joined up: giant lattice → strong forces between oppositely charged ions → lots of energy to melt; and solid ions fixed → can\'t move → don\'t conduct, molten/dissolved ions free → carry charge. You say why, not just what.' },
          { level: 2, marks: [3, 4],
            descriptor: 'You explain one strand well but the other is thin or has a broken link. E.g. melting point fully explained, but conduction is just "it conducts when molten" with no mention of ions being free to move; or conduction explained but the melting point is blamed on "big crystals". Several correct points, partial linking.' },
          { level: 1, marks: [1, 2],
            descriptor: 'Isolated correct statements with no links, or you describe the properties without explaining them from the structure ("high melting point, conducts when molten"). True but not joined to the lattice.' },
          { level: 0, levelLabel: '—', marks: [0, 0],
            descriptor: 'Nothing relevant, or only misconceptions.' }
        ],
        capFailures: [
          'saying electrons carry the current — this shows the ionic model isn\'t understood, so the whole conduction strand scores nothing and you can\'t reach Level 3.',
          'Listing properties without linking them to structure — stays Level 1 however many properties you name.',
          'Conflating ionic with metallic ("delocalised electrons", "sea of electrons") — caps at Level 1–2.',
          'Saying melting creates the ions — loses the solid-state marks and signals a model error.'
        ]
      },

      {
        id: 'pic-1b',
        label: '1B',
        heading: 'Explain conduction (shorter)',
        stem: 'Explain why ionic compounds conduct electricity when molten or dissolved, but not when solid. [4 marks]',
        tariff: 4,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q2)',
        markingPoints: [
          { id: 'mp1', text: 'In the solid the ions are in fixed positions / held in the lattice.', essential: true },
          { id: 'mp2', text: 'so the ions cannot move (to carry charge).', essential: true },
          { id: 'mp3', text: 'when molten or dissolved the ions are free to move.', essential: true },
          { id: 'mp4', text: 'the moving ions carry the charge / current.', essential: true }
        ],
        allow: [
          'MP3+MP4 combined as "the ions are then free to move and carry charge" (still both marks if both ideas present).'
        ],
        doNotAccept: [
          { text: 'electrons/delocalised electrons', slug: 'electrons-carry-ionic-current' },
          { text: '"melting creates the ions"', slug: 'melting-creates-ions' },
          { text: '"the solid has no charged particles"', slug: 'no-ions-in-solid' }
        ],
        tierNotes: {
          foundation: 'Foundation-safe.',
          higher: 'Higher answer should pre-empt the misconception by noting the ions already exist in the solid and are freed, not created.'
        }
      },

      {
        id: 'pic-1c',
        label: '1C',
        heading: 'Explain high melting point',
        stem: 'Explain why ionic compounds have high melting and boiling points. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q3)',
        markingPoints: [
          { id: 'mp1', text: 'giant ionic lattice / many ions.', essential: true },
          { id: 'mp2', text: 'strong electrostatic forces of attraction between oppositely charged ions.', essential: true },
          { id: 'mp3', text: 'a large amount of energy is needed to overcome them.', essential: true }
        ],
        doNotAccept: [
          { text: '"large crystals need more heat"', slug: 'crystal-size-sets-mp' },
          { text: '"ions are heavy"', slug: 'ion-mass-sets-mp' },
          { text: '"covalent bonds"', slug: 'covalent-bonds-in-ionic' }
        ],
        tierNotes: {
          foundation: 'Foundation-safe.'
        }
      },

      {
        id: 'pic-1d',
        label: '1D',
        heading: 'Explain brittleness',
        stem: 'Ionic compounds are hard but brittle. Explain why a crystal shatters when it is struck. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q4)',
        markingPoints: [
          { id: 'mp1', text: 'the force shifts a layer of ions (by one position).', essential: true },
          { id: 'mp2', text: 'ions of the same charge become aligned / next to each other.', essential: true },
          { id: 'mp3', text: 'like charges repel, so the crystal splits / shatters.', essential: true }
        ],
        allow: [
          '"same charges line up and push apart"'
        ],
        doNotAccept: [
          { text: '"covalent bonds snap"', slug: 'covalent-bonds-in-ionic' },
          { text: '"ions melt at the impact point"', slug: 'ions-melt-on-impact' },
          { text: '"delocalised electrons displaced"', slug: 'delocalised-electrons-in-ionic' }
        ],
        tierNotes: {
          foundation: 'Foundation-safe.'
        }
      },

      {
        id: 'pic-1e',
        label: '1E',
        heading: '[HIGHER] Compare melting points by charge',
        stem: 'Magnesium oxide (MgO) has a higher melting point than sodium chloride (NaCl). Explain why. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q)',
        markingPoints: [
          { id: 'mp1', text: 'MgO ions carry larger charges (Mg²⁺ and O²⁻ = 2+/2−) than NaCl ions (Na⁺/Cl⁻ = 1+/1−).', essential: true },
          { id: 'mp2', text: 'so there are stronger electrostatic forces of attraction between the ions.', essential: true },
          { id: 'mp3', text: 'more energy is needed to overcome the forces / to melt.', essential: true }
        ],
        allow: [
          '"double the charge"',
          'force is proportional to the product of the charges (MP2).'
        ],
        check: true,
        checkNote: 'AQA accepts either the qualitative "greater charge → stronger attraction" or the proportionality; Foundation would only need the qualitative version.',
        doNotAccept: [
          { text: '"MgO is bigger / larger crystal"', slug: 'crystal-size-sets-mp' },
          { text: '"magnesium is heavier"', slug: 'ion-mass-sets-mp' },
          { text: '"more ions"' }
        ],
        tierNotes: {
          higher: 'Higher-only. This is the grade 8/9 charge-magnitude reasoning. Transfer variants: Na₂O vs NaCl (frozen Higher), CaO vs KCl (MRB-135 exemplar PIC-11), Al₂O₃ vs NaCl (frozen Triple-Higher — 3+/2− is the strongest case).'
        }
      }
    ],

    beTheExaminer: [
      {
        id: 'pic-be1',
        label: '4A',
        targetItemId: 'pic-1a',
        heading: 'Partially right (earns marks)',
        studentAnswer: 'Sodium chloride has a high melting point because it has strong bonds that need a lot of energy to break. It conducts electricity when it is dissolved in water because the electrons are then free to flow through the solution and carry the current. It doesn\'t conduct when solid because the electrons can\'t move.',
        officialMark: 2,
        outOf: 6,
        pointsHit: ['mp2', 'mp4'],
        pointsHitNote: 'MP2/MP4 — "strong bonds… a lot of energy to break" gets the strong-attraction + energy idea (2 marks), even though "lattice" and "oppositely charged ions" are not named.',
        pointsMissed: ['mp1', 'mp5', 'mp6', 'mp7'],
        pointsMissedNote: 'the whole conduction strand — the student attributes conduction to electrons (electrons-carry-ionic-current). Ionic compounds have no free electrons; it is the ions that move. No mention of ions being free to move, so MP5–MP7 score nothing. Caps at Level 1–2.',
        misconceptionsShown: ['electrons-carry-ionic-current'],
        examinerLine: "The melting-point half is on the right lines. But your conduction is built on the wrong particle — swap every 'electron' for 'ion' and you'd have earned three more marks.",
        partiallyRight: true
      },
      {
        id: 'pic-be2',
        label: '4B',
        targetItemId: 'pic-1b',
        heading: 'Low but instructive',
        studentAnswer: 'When you melt sodium chloride the heat gives it energy and this makes new ions that can move around, and the moving ions let electricity flow. In the solid there aren\'t any ions yet, so it can\'t conduct.',
        note: '(to: Explain why molten NaCl conducts but solid does not. [4 marks])',
        officialMark: 2,
        outOf: 4,
        pointsHit: ['mp3', 'mp4'],
        pointsHitNote: 'MP3+MP4 — "moving ions… let electricity flow" (ions free to move + carry charge, 2 marks).',
        pointsMissed: ['mp1', 'mp2'],
        pointsMissedNote: '"makes new ions" / "there aren\'t any ions in the solid" is the melting-creates-ions + no-ions-in-solid misconception. The ions already exist in the solid lattice; melting frees them, it does not create them. Loses both solid-state marks (MP1/MP2).',
        misconceptionsShown: ['melting-creates-ions', 'no-ions-in-solid'],
        examinerLine: "The molten half is spot on. But the ions are already there in the solid, locked in the lattice — melting just sets them free. 'The solid has no ions' throws away two easy marks.",
        partiallyRight: false
      }
    ],

    chains: [
      {
        id: 'pic-chainA',
        label: 'Chain A',
        title: 'Why NaCl conducts when molten/dissolved but not solid',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Sodium chloride is a giant lattice of oppositely charged ions.', role: 'essential' },
          { id: 'l2', text: 'In the solid, the ions are held in fixed positions.', role: 'essential' },
          { id: 'l3', text: 'So in the solid the ions cannot move to carry charge.', role: 'essential' },
          { id: 'l4', text: 'When melted or dissolved, the ions become free to move.', role: 'essential' },
          { id: 'l5', text: 'The moving ions carry the charge, so it conducts.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Delocalised electrons carry the current.', slug: 'electrons-carry-ionic-current' },
          { id: 'h2', text: 'Melting creates ions that were not there before.', slug: 'melting-creates-ions' },
          { id: 'h3', text: 'The water carries the current.', slug: 'water-carries-current' },
          { id: 'h4', text: 'In the solid there are no charged particles at all.', slug: 'no-ions-in-solid' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          optional: ['l1'],
          interchangeable: [['l2', 'l3']],
          mustPrecede: [['l4', 'l5']]
        },
        orderingNote: 'links 2 and 3 may be placed as a single block in either internal order (fixed-position ↔ can\'t-move are the same idea); 4 must precede 5. Do not mark a chain wrong if 1 is omitted but 2→5 are correct — 1 is scene-setting.'
      },
      {
        id: 'pic-chainB',
        label: 'Chain B',
        title: 'Why NaCl has a high melting point',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Giant ionic lattice containing many ions.', role: 'essential' },
          { id: 'l2', text: 'Strong electrostatic forces of attraction between oppositely charged ions.', role: 'essential' },
          { id: 'l3', text: 'Acting in all directions throughout the lattice.', role: 'creditworthy' },
          { id: 'l4', text: 'A large amount of energy is needed to overcome these forces.', role: 'essential' },
          { id: 'l5', text: 'So the melting point is high.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Strong covalent bonds must be broken.', slug: 'covalent-bonds-in-ionic' },
          { id: 'h2', text: 'The crystals are large, so more heat is needed.', slug: 'crystal-size-sets-mp' },
          { id: 'h3', text: 'The ions are heavy and resist heating.', slug: 'ion-mass-sets-mp' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          optional: ['l3']
        },
        orderingNote: 'link 3 may sit anywhere between 2 and 4, or be omitted, without breaking the chain.'
      },
      {
        id: 'pic-chainC',
        label: 'Chain C',
        title: 'Why an ionic crystal shatters (brittleness)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'A force shifts a layer of ions.', role: 'essential' },
          { id: 'l2', text: 'Ions of the same charge become aligned next to each other.', role: 'essential' },
          { id: 'l3', text: 'Like charges repel.', role: 'essential' },
          { id: 'l4', text: 'The repulsion pushes the layers apart and the crystal shatters.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The covalent bonds snap.', slug: 'covalent-bonds-in-ionic' },
          { id: 'h2', text: 'The ions melt at the point of impact.', slug: 'ions-melt-on-impact' },
          { id: 'h3', text: 'The delocalised electrons are knocked out of place.', slug: 'delocalised-electrons-in-ionic' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: 'strict 1→2→3→4; no alternative orderings (each link causes the next).'
      }
    ],

    checkIndex: [
      '1E — whether AQA credits the proportionality "force ∝ product of charges" at GCSE or only the qualitative "greater charge → stronger attraction".',
      'MgO melting point 2852 °C and NaCl 801 °C are quoted from the frozen theory; standard AQA data-book values, treated as correct.',
      'Tariff of 1A as 6 marks: this banker is a real AQA 6-mark levels item (properties of ionic compounds from structure) — confident.',
      'FormulaDeducer is not on this page (no formula construction examinable here) — it lives on ionic-bonding; noted as a deliberate scope call.'
    ]
  };
})();
