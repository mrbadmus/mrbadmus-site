/* Authored exam content — properties-small-molecules
   Source: ~/Documents/mrb-authoring/phase2-exam/properties-small-molecules.html (MRB-136 Phase 2A, approved 24 Jul 2026)
   Net-new authored content. Never written into the 8 frozen fields.
   Misconception slugs are verbatim join keys to the MRB-135 MCQ banks — do not rename. */
(function () {
  'use strict';
  var C = (window.MrbExamContent = window.MrbExamContent || {});

  C['properties-small-molecules'] = {
    page: 'properties-small-molecules',
    title: 'Properties of Small Molecules',
    spec: '5.2.2.4',

    scopeNote: 'Scope judgement (stated, not hidden): the council names three 6-mark bankers (ionic properties, diamond-vs-graphite, alloys) — this page is not one of them. Its exam value is 2–4 mark "explain" items and the discrimination itself. I have still authored one composite 6-marker (§1A) so the WriteThenMark engine has a full-tariff item and levels descriptors to consume — framed as a structure-comparison (a real AQA extended-response style), but marked [CHECK] as a constructed item, not lifted from a past paper.',

    checkIndex: [
      '1A is a constructed composite 6-marker, not a named banker — confirm the diamond/CO₂ comparison reads cleanly at 6 marks (I kept CO₂ qualitative — "gas at room temperature" — deliberately, because CO₂ sublimes at ~−78 °C at 1 atm rather than melting, so no melting-point value is quoted).',
      '1B — GCSE does not require hydrogen bonding; "stronger intermolecular forces" is the ceiling, matching the frozen answer.',
      '4B mark is 1/3 borderline — flagged so Mide can set the house line on how generously to read "stronger bonds."'
    ],

    misconceptions: [
      { slug: 'covalent-is-weak',
        statement: '"Simple molecular substances melt easily because their covalent bonds are weak."',
        source: 'common_mistake; quiz Q3 distractor' },
      { slug: 'boiling-breaks-covalent',
        statement: '"The covalent bonds break (or half of them break) when it melts/boils."',
        source: 'examiner_tip; quiz Q4/Q10 distractors' },
      { slug: 'more-covalent-bonds-higher-bp',
        statement: '"Water has more covalent bonds, so it takes more energy to boil."',
        source: 'quiz Q1 distractor' },
      { slug: 'mass-alone-sets-bp',
        statement: '"Methane is lighter, so it simply evaporates faster."',
        source: 'quiz Q1 distractor' },
      { slug: 'oxygen-heavy',
        statement: '"Water contains oxygen, which makes the molecules too heavy to boil easily."',
        source: 'quiz Q1 distractor' },
      { slug: 'strong-bonds-block-conduction',
        statement: '"Their covalent bonds are too strong to let electrons move."',
        source: 'quiz Q2 distractor' },
      { slug: 'too-small-to-charge',
        statement: '"Their molecules are too small to hold a charge."',
        source: 'quiz Q2 distractor' },
      { slug: 'gases-never-conduct',
        statement: '"Simple molecules are always gases, and gases never conduct."',
        source: 'quiz Q2 distractor' },
      { slug: 'no-imf-at-all',
        statement: '"There are no forces at all between the molecules."',
        source: 'quiz Q3 distractor' },
      { slug: 'lose-electrons-on-warming',
        statement: '"The molecules lose electrons easily when warmed."',
        source: 'quiz Q3 distractor' },
      { slug: 'polymer-is-giant-covalent',
        statement: '"Polymers are giant covalent structures because the chains are so large."',
        source: 'polymers common_mistake (Higher transfer Q here)' }
    ],

    writeThenMark: [
      {
        id: 'psm-1a',
        label: '1A',
        heading: 'COMPOSITE 6-MARKER [CHECK]',
        stem: 'Diamond and carbon dioxide are both made of atoms joined by covalent bonds. Diamond has a very high melting point, but carbon dioxide is a gas at room temperature. Explain, in terms of structure and bonding, why their melting points are so different. [6 marks]',
        tariff: 6,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: true,
        check: true,
        checkNote: '1A is a constructed composite 6-marker, not a named banker — confirm the diamond/CO₂ comparison reads cleanly at 6 marks (I kept CO₂ qualitative — "gas at room temperature" — deliberately, because CO₂ sublimes at ~−78 °C at 1 atm rather than melting, so no melting-point value is quoted).',
        note: 'The purest test of the misconception — both substances are covalent, so a student can\'t hide behind "covalent = strong = high MP." Award any 6.',
        markingPoints: [
          { id: 'mp1',
            text: 'CO₂ is made of small, separate molecules.',
            strand: 'Carbon dioxide (simple molecular)',
            essential: true },
          { id: 'mp2',
            text: 'within each molecule the atoms are joined by strong covalent bonds.',
            strand: 'Carbon dioxide (simple molecular)',
            essential: true },
          { id: 'mp3',
            text: 'between the molecules there are only weak intermolecular forces.',
            strand: 'Carbon dioxide (simple molecular)',
            essential: true },
          { id: 'mp4',
            text: 'melting/boiling only overcomes the weak intermolecular forces — the covalent bonds do NOT break. (the discrimination mark)',
            strand: 'Carbon dioxide (simple molecular)',
            essential: true },
          { id: 'mp5',
            text: 'so only a little energy is needed → low melting point (gas at room temperature).',
            strand: 'Carbon dioxide (simple molecular)',
            essential: true },
          { id: 'mp6',
            text: 'diamond is a giant covalent structure — every carbon bonded to others by strong covalent bonds throughout.',
            strand: 'Diamond (giant covalent)',
            essential: true },
          { id: 'mp7',
            text: 'melting requires breaking many strong covalent bonds → a lot of energy → very high melting point.',
            strand: 'Diamond (giant covalent)',
            essential: true }
        ],
        allow: [
          '"forces between the molecules" for intermolecular forces',
          '"the bonds inside the molecule stay together" for MP4.'
        ],
        doNotAccept: [
          { text: '"CO₂\'s covalent bonds are weak"', slug: 'covalent-is-weak' },
          { text: '"the covalent bonds break when CO₂ boils"', slug: 'boiling-breaks-covalent' }
        ],
        tierNotes: {
          foundation: 'Foundation must produce: CO₂ = small molecules, weak forces between them, little energy → low MP; diamond = giant covalent, many strong bonds, lots of energy → high MP.',
          higher: 'Higher must add: the explicit discrimination (MP4) that the covalent bonds within CO₂ stay intact; precise "intermolecular forces"; and the larger-molecule → stronger-IMF nuance in size comparisons (1D).'
        },
        levels: [
          { level: 3, marks: [5, 6],
            descriptor: 'You explain both substances and make the key discrimination: in CO₂ only the weak forces between the molecules are overcome (the covalent bonds inside stay whole), while in diamond the covalent bonds themselves must break. Structure linked to melting point in both cases.' },
          { level: 2, marks: [3, 4],
            descriptor: 'Both structures described, but the discrimination is fuzzy. E.g. diamond explained well, and CO₂ said to "have weak bonds" without separating the weak forces between molecules from the strong covalent bonds within.' },
          { level: 1, marks: [1, 2],
            descriptor: 'Isolated statements — "CO₂ is a gas, diamond is hard," or "CO₂ has weak bonds and diamond has strong bonds" (the covalent-is-weak trap). True-sounding, but the models are conflated.' },
          { level: 0, levelLabel: '—', marks: [0, 0],
            descriptor: 'Nothing relevant, or only misconceptions.' }
        ],
        capFailuresHeading: 'Specific failures that cap your mark:',
        capFailures: [
          '"CO₂\'s covalent bonds are weak" — the defining error of this topic; it conflates the two force types, so the CO₂ side can\'t reach the top.',
          '"The covalent bonds break when CO₂ boils" — the discrimination is lost, so you can\'t reach Level 3.',
          'Describing without linking ("one\'s a gas, one\'s a solid") — Level 1.'
        ]
      },

      {
        id: 'psm-1b',
        label: '1B',
        heading: 'Explain the H₂O vs CH₄ difference',
        stem: 'Water (H₂O) boils at 100 °C but methane (CH₄) boils at −161 °C, although both are simple molecular. Explain why the difference is so large. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        check: true,
        checkNote: 'At GCSE, "stronger intermolecular forces" is the expected reason — students are NOT required to name hydrogen bonding; the frozen correct answer stops at "stronger intermolecular forces," which is right.',
        note: '(frozen Q1)',
        markingPoints: [
          { id: 'mp1', text: 'water molecules have stronger intermolecular forces than methane molecules.', essential: true },
          { id: 'mp2', text: 'so more energy is needed to overcome the forces / separate the molecules in water.', essential: true },
          { id: 'mp3', text: 'boiling does not break the covalent bonds, so the number of covalent bonds is not the reason.', essential: true }
        ],
        doNotAccept: [
          { text: '"water has more covalent bonds"', slug: 'more-covalent-bonds-higher-bp', note: 'water actually has fewer' },
          { text: '"methane is lighter and evaporates"', slug: 'mass-alone-sets-bp' },
          { text: '"oxygen is heavy"', slug: 'oxygen-heavy' }
        ],
        tierNotes: { foundation: 'Foundation-safe.' }
      },

      {
        id: 'psm-1c',
        label: '1C',
        heading: 'Explain low melting point',
        stem: 'Explain why simple molecular substances have low melting and boiling points. [2 marks]',
        tariff: 2,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q3)',
        markingPoints: [
          { id: 'mp1', text: 'the forces between the molecules (intermolecular forces) are weak.', essential: true },
          { id: 'mp2', text: 'only a little energy is needed to overcome them (the covalent bonds within are not broken).', essential: true }
        ],
        doNotAccept: [
          { text: '"covalent bonds are weak"', slug: 'covalent-is-weak' },
          { text: '"no forces at all"', slug: 'no-imf-at-all' }
        ],
        tierNotes: { foundation: 'Foundation-safe.' }
      },

      {
        id: 'psm-1d',
        label: '1D',
        heading: 'Explain non-conduction',
        stem: 'Explain why simple molecular substances do not conduct electricity. [2 marks]',
        tariff: 2,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q2)',
        markingPoints: [
          { id: 'mp1', text: 'the molecules have no overall charge.', essential: true },
          { id: 'mp2', text: 'there are no free electrons or ions to carry a current.', essential: true }
        ],
        doNotAccept: [
          { text: '"bonds too strong to let electrons move"', slug: 'strong-bonds-block-conduction' },
          { text: '"too small to hold a charge"', slug: 'too-small-to-charge' }
        ],
        tierNotes: { foundation: 'Foundation-safe.' }
      },

      {
        id: 'psm-1e',
        label: '1E',
        heading: '[HIGHER] Larger molecules → higher MP/BP',
        stem: 'Explain why larger molecules generally have higher melting and boiling points than smaller molecules. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q; transfer: Cl₂ gas vs I₂ solid)',
        markingPoints: [
          { id: 'mp1', text: 'larger molecules have more electrons / are bigger.', essential: true },
          { id: 'mp2', text: 'so the intermolecular forces between them are stronger.', essential: true },
          { id: 'mp3', text: 'more energy is needed to overcome these forces → higher melting/boiling point.', essential: true }
        ],
        doNotAccept: [
          { text: '"bigger molecules have more/stronger covalent bonds to break"', slug: 'boiling-breaks-covalent' }
        ],
        tierNotes: {
          higher: 'Higher-only. Direct transfer: "Chlorine (Cl₂) is a gas but iodine (I₂) is a solid — explain" (frozen Triple-Higher). I₂ is a larger molecule → stronger intermolecular forces → higher MP.'
        }
      },

      {
        id: 'psm-1f',
        label: '1F',
        heading: '[HIGHER] Polymers vs diamond',
        stem: 'Explain why polymers have much lower melting points than giant covalent structures such as diamond. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q)',
        markingPoints: [
          { id: 'mp1', text: 'in a polymer the chains are held to each other by weak intermolecular forces.', essential: true },
          { id: 'mp2', text: 'these need only a little energy to overcome.', essential: true },
          { id: 'mp3', text: 'in diamond, strong covalent bonds run throughout and must be broken → far more energy → much higher MP.', essential: true }
        ],
        doNotAccept: [
          { text: '"polymers are giant covalent structures"', slug: 'polymer-is-giant-covalent' }
        ],
        tierNotes: {
          higher: 'Higher-only. This is the polymer-vs-giant-covalent trap flagged in the examiner tip.'
        }
      }
    ],

    beTheExaminer: [
      {
        id: 'psm-be1',
        label: '4A',
        targetItemId: 'psm-1a',
        heading: 'Partially right (earns marks)',
        headingFull: '4A — Partially right (earns marks) · marks the 6-marker (1A)',
        studentAnswer: '"Carbon dioxide is a gas because its bonds are weak and don\'t take much energy to break. Diamond has a really high melting point because it\'s a giant structure where all the carbon atoms are joined by strong covalent bonds, so you need loads of energy to break them all."',
        officialMark: 3,
        outOf: 6,
        pointsHit: ['mp6', 'mp7'],
        pointsHitNote: 'MP6+MP7 (diamond) — giant covalent, strong bonds throughout, lots of energy to break (2–3 marks).',
        pointsMissed: ['mp3', 'mp4'],
        pointsMissedNote: 'the CO₂ side is the covalent-is-weak trap — "its bonds are weak" does not separate the weak forces between molecules from the strong covalent bonds within. No discrimination → MP3/MP4 lost.',
        misconceptionsShown: ['covalent-is-weak'],
        examinerLine: '"Diamond is exam-ready. But \'CO₂\'s bonds are weak\' is the classic slip — the covalent bonds inside CO₂ are strong; it\'s the forces BETWEEN the molecules that are weak, and only those are overcome when it boils. That distinction is the whole question."',
        partiallyRight: true
      },
      {
        id: 'psm-be2',
        label: '4B',
        targetItemId: 'psm-1b',
        heading: 'Low but instructive',
        headingFull: '4B — Low but instructive · marks the H₂O/CH₄ question (1B)',
        studentAnswer: '"Water boils at a much higher temperature because it has stronger bonds than methane. When you boil water you have to break these strong bonds, and that takes a lot of energy, but methane\'s bonds are weaker so it boils easily."',
        note: '(to 1B, [3 marks])',
        officialMark: 1,
        outOf: 3,
        markNote: '(borderline — an examiner could give 0)',
        pointsHit: ['mp1'],
        pointsHitNote: 'MP1, generously — "water has stronger [forces] than methane → more energy" is the right shape, so 1 mark for the comparative idea.',
        pointsMissed: ['mp2', 'mp3'],
        pointsMissedNote: '"you have to break these bonds when you boil water" is boiling-breaks-covalent — boiling does not break covalent bonds; it overcomes the weak intermolecular forces. The student never names intermolecular forces, so MP2/MP3 are gone and the mark is at risk.',
        misconceptionsShown: ['boiling-breaks-covalent'],
        examinerLine: '"You\'ve got \'stronger → more energy\', which is the right shape. But boiling never breaks the covalent bonds — it overcomes the weaker forces BETWEEN the molecules. Write \'intermolecular forces\' and the marks are safe."',
        partiallyRight: false
      }
    ],

    chains: [
      {
        id: 'psm-chainA',
        label: 'Chain A',
        title: 'Why a simple molecular substance has a low melting point (the discrimination chain)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'A simple molecular substance is made of small, separate molecules.', role: 'essential' },
          { id: 'l2', text: 'Within each molecule the atoms are joined by strong covalent bonds.', role: 'creditworthy', note: 'sets up the discrimination' },
          { id: 'l3', text: 'Between the molecules there are only weak intermolecular forces.', role: 'essential' },
          { id: 'l4', text: 'Melting/boiling overcomes the weak intermolecular forces — the covalent bonds do not break.', role: 'essential' },
          { id: 'l5', text: 'Only a little energy is needed → low melting/boiling point.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The covalent bonds inside the molecules are weak.', slug: 'covalent-is-weak' },
          { id: 'h2', text: 'The covalent bonds break when it melts.', slug: 'boiling-breaks-covalent' },
          { id: 'h3', text: 'There are no forces at all between the molecules.', slug: 'no-imf-at-all' },
          { id: 'h4', text: 'The molecules lose electrons when they are warmed.', slug: 'lose-electrons-on-warming' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          optional: ['l2'],
          interchangeable: [['l2', 'l3']],
          mustPrecede: [['l3', 'l4'], ['l4', 'l5']]
        },
        orderingNote: '2 and 3 may swap (they describe the two force types); 4 must follow 3; 5 last. Link 2 may be omitted without breaking the chain, but it is what makes the discrimination visible.'
      },
      {
        id: 'psm-chainB',
        label: 'Chain B',
        title: 'Why a simple molecular substance doesn\'t conduct',
        tier: 'any',
        links: [
          { id: 'l1', text: 'The molecules have no overall electric charge.', role: 'essential' },
          { id: 'l2', text: 'There are no free electrons or ions.', role: 'essential' },
          { id: 'l3', text: 'So there are no charged particles free to move and carry a current.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The covalent bonds are too strong to let electrons move.', slug: 'strong-bonds-block-conduction' },
          { id: 'h2', text: 'The molecules are too small to hold a charge.', slug: 'too-small-to-charge' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3'],
          interchangeable: [['l1', 'l2']],
          mustPrecede: [['l1', 'l3'], ['l2', 'l3']]
        },
        orderingNote: '1 and 2 may swap; 3 last.'
      },
      {
        id: 'psm-chainC',
        label: 'Chain C',
        title: 'Why larger molecules boil at higher temperatures',
        tier: 'higher',
        links: [
          { id: 'l1', text: 'Larger molecules have more electrons.', role: 'essential' },
          { id: 'l2', text: 'so the intermolecular forces between them are stronger.', role: 'essential' },
          { id: 'l3', text: 'more energy is needed to overcome these forces.', role: 'essential' },
          { id: 'l4', text: 'so the boiling point is higher.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Bigger molecules have more covalent bonds to break.', slug: 'boiling-breaks-covalent' },
          { id: 'h2', text: 'Heavier molecules just sink and can\'t evaporate.', slug: 'mass-alone-sets-bp' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: 'strict 1→2→3→4.'
      }
    ]
  };
})();
