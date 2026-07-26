/* Authored exam content — ionic-bonding
   Source: ~/Documents/mrb-authoring/phase2-exam/ionic-bonding.html (MRB-136 Phase 2A, approved 24 Jul 2026)
   Net-new authored content. Never written into the 8 frozen fields.
   Misconception slugs are verbatim join keys to the MRB-135 MCQ banks — do not rename. */
(function () {
  'use strict';
  var C = (window.MrbExamContent = window.MrbExamContent || {});

  C['ionic-bonding'] = {
    page: 'ionic-bonding',
    title: 'Ionic Bonding',
    spec: '5.2.1.2',
    badge: 'FORMULA DEDUCER HOME PAGE',
    subtitle: 'Spec 5.2.1.2 · FORMULA DEDUCER HOME PAGE · MRB-136 Phase 2A DRAFT · consumes: FormulaDeducer (primary), WriteThenMark, ChainBuilder, BeTheExaminer. PROCESS-family page — no 6-mark banker; the exam value is the transfer→ions→attraction chain, formula construction, and the "the bond is not the transfer" refutation.',

    /* §1 preamble, verbatim. */
    writeThenMarkNote: 'No 6-mark banker on this page (stated judgement). Ionic-bonding is a PROCESS page — AQA assesses it through 2–4 mark "describe/explain" items, formula deduction, and dot-and-cross drawing (drawing → DotCrossCanvas, Phase 4). So §2 Levels descriptors is intentionally N/A; the extended-response marking lives in the ChainBuilder chains (§3). Below are the WriteThenMark items.',

    /* §2 Levels descriptors — intentionally N/A on this page. Verbatim. */
    levelsNote: 'N/A — this page has no 6-mark levels item (see §1). Deliberately omitted rather than manufacturing a banker where AQA does not set one. The nearest extended demand is the transfer→ions→attraction chain, marked point-by-point in §1A/1D and orderable in §3 Chain A.',

    /* [CHECK] index for this page — page-level, verbatim. */
    checkIndex: [
      '5C polyatomic set — examinable but beyond this page\'s frozen monatomic content; Mide to decide whether it ships on ionic-bonding or is deferred to a formulae/equations page.',
      'Whether AQA credits the "cross-over/swap" method or requires the balance-to-zero reasoning shown when a question says "justify using ion charges" — I have written the reasoning column as balance-to-zero (the safer, always-creditworthy form).',
      'H7–H10 assume the transition-metal charge is given (Roman numeral / stated) — the engine must supply it, not expect recall.',
      'No 6-mark banker on this page — stated as a judgement, not an omission.'
    ],

    misconceptions: [
      { slug: 'transfer-is-the-bond',
        statement: '"The ionic bond IS the transfer of electrons." (The transfer only makes the ions; the bond is the attraction.)',
        source: 'common_mistake; examiner_tip; Higher Q' },
      { slug: 'sharing-vs-transfer-swapped',
        statement: '"Sodium and chlorine share a pair of electrons."',
        source: 'quiz Q6/Q10 distractors' },
      { slug: 'transfer-direction-reversed',
        statement: '"Chlorine loses an electron to sodium." (It gains.)',
        source: 'quiz Q6/Q10 distractors' },
      { slug: 'charge-equals-group-number',
        statement: '"Chlorine is Group 7, so its ion is 7−." / "Charge always equals the group number."',
        source: 'quiz Q3/Q5 distractors' },
      { slug: 'gain-lose-reversed',
        statement: '"Metals gain electrons and non-metals lose them."',
        source: 'quiz Q9 distractor' },
      { slug: 'one-of-each-ion',
        statement: '"One calcium ion bonds with one chloride ion → CaCl."',
        source: 'quiz Q8 distractor' },
      { slug: 'charges-swapped-to-subscripts',
        statement: '"Ca₂Cl — two calcium ions with one chloride." (Charges put on the wrong ion.)',
        source: 'quiz Q8 distractor' },
      { slug: 'charges-as-own-subscript',
        statement: '"Al³⁺ and O²⁻ → Al₃O₂" (each ion\'s own charge used as its subscript; cross-over done the wrong way).',
        source: 'built on Q8 + Higher Al₂O₃ Q' },
      { slug: 'electrons-destroyed',
        statement: '"The electrons transferred are destroyed, leaving neutral atoms."',
        source: 'quiz Q7 distractor' },
      { slug: 'charges-disappear',
        statement: '"The ions are held so tightly their charges disappear."',
        source: 'quiz Q7 distractor' },
      { slug: 'full-shell-neutral',
        slugs: ['full-shell-neutral', 'full-shell-is-the-bond'],
        statement: '"A full shell is uncharged" / "the compound is held together because both atoms have full shells."',
        source: 'quiz Q7 distractor; Be-the-Examiner' },
      { slug: 'mass-sets-charge',
        statement: '"Metals are heavier, so their nuclei pull electrons in and become positive."',
        source: 'quiz Q9 distractor' },
      { slug: 'metal-nonmetal-covalent',
        slugs: ['metal-nonmetal-covalent', 'compound-is-metallic', 'unreactive-pair'],
        statement: '"Metal + non-metal shares / is metallic / doesn\'t react."',
        source: 'quiz Q1 distractors' }
    ],

    writeThenMark: [
      {
        id: 'ib-1a',
        label: '1A',
        heading: 'Describe the electron transfer',
        stem: 'Sodium (2.8.1) reacts with chlorine (2.8.7) to form sodium chloride. Describe, in terms of electrons, what happens when the ions form. [3 marks]',
        tariff: 3,
        command: 'Describe',
        ao: 'AO1/AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q6)',
        markingPoints: [
          { id: 'mp1', text: 'sodium loses its 1 outer electron → becomes Na⁺ (2.8).', essential: true },
          { id: 'mp2', text: 'chlorine gains that electron → becomes Cl⁻ (2.8.8).', essential: true },
          { id: 'mp3', text: 'the oppositely charged ions attract (electrostatic attraction).', essential: true }
        ],
        allow: [
          '"sodium gives its electron to chlorine"',
          'electron configs 2.8 / 2.8.8 shown instead of stated.'
        ],
        doNotAccept: [
          { text: '"share a pair"', slug: 'sharing-vs-transfer-swapped' },
          { text: '"chlorine loses to sodium"', slug: 'transfer-direction-reversed' },
          { text: '"both lose into a pool" (metallic confusion)' }
        ],
        tierNotes: {
          foundation: 'Foundation-safe.',
          higher: 'Higher answers should name the attraction (MP3) as the bond itself.'
        }
      },
      {
        id: 'ib-1b',
        label: '1B',
        heading: 'Why the compound is neutral',
        stem: 'Explain why an ionic compound such as sodium chloride has no overall electrical charge. [2 marks]',
        tariff: 2,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q7)',
        markingPoints: [
          { id: 'mp1', text: 'electrons are transferred, not created or destroyed (charge is conserved).', essential: true },
          { id: 'mp2', text: 'the total positive charge on the metal ions equals the total negative charge on the non-metal ions (they balance to zero).', essential: true }
        ],
        doNotAccept: [
          { text: '"electrons destroyed"', slug: 'electrons-destroyed' },
          { text: '"charges disappear"', slug: 'charges-disappear' },
          { text: '"full shells are uncharged"', slug: 'full-shell-neutral' }
        ],
        tierNote: 'Foundation-safe.'
      },
      {
        id: 'ib-1c',
        label: '1C',
        heading: 'Why metals form + and non-metals form −',
        stem: 'Explain, in terms of electron arrangement, why metals form positive ions but non-metals form negative ions. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q9)',
        markingPoints: [
          { id: 'mp1', text: 'metals have few outer electrons and lose them, leaving more protons than electrons → positive ion.', essential: true },
          { id: 'mp2', text: 'non-metals have nearly full outer shells and gain electrons, giving more electrons than protons → negative ion.', essential: true },
          { id: 'mp3', text: 'both do this to achieve a full outer shell (stable, like a noble gas).', essential: true }
        ],
        doNotAccept: [
          { text: 'mass/heaviness', slug: 'mass-sets-charge' },
          { text: '"more protons makes it negative"' },
          { text: '"metals gain, non-metals lose"', slug: 'gain-lose-reversed' }
        ],
        tierNote: 'Foundation-safe.'
      },
      {
        id: 'ib-1d',
        label: '1D',
        heading: 'The bond is NOT the transfer (refutation)',
        stem: 'A student writes: "The ionic bond is the transfer of electrons from sodium to chlorine." Explain why this statement is not correct. [3 marks]',
        tariff: 3,
        command: 'Explain',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q — the page\'s marquee misconception)',
        markingPoints: [
          { id: 'mp1', text: 'the transfer of electrons only creates the ions (Na⁺ and Cl⁻) — it is a one-off event.', essential: true },
          { id: 'mp2', text: 'the ionic bond itself is the strong electrostatic attraction between the oppositely charged ions.', essential: true },
          { id: 'mp3', text: 'so the transfer forms the ions, but it is the attraction between them that is the bond.', essential: true }
        ],
        allow: [
          '"the transfer makes the ions; the bond is the attraction that holds them together".'
        ],
        doNotAccept: [
          { text: 'any answer that restates "the bond is the transfer"', slug: 'transfer-is-the-bond' },
          { text: '"held together because both have full shells"', slug: 'full-shell-is-the-bond' }
        ],
        tierNote: 'Higher-only. Directly examinable; the frozen examiner tip is built on it.'
      },
      {
        id: 'ib-1e',
        label: '1E',
        heading: 'Why Al₂O₃ (via electron transfer)',
        stem: 'Explain, in terms of electron transfer, why the formula of aluminium oxide is Al₂O₃. [3 marks]',
        tariff: 3,
        command: 'Explain/Deduce',
        ao: 'AO2',
        tier: 'higher',
        isLevels: false,
        note: '(frozen Higher Q — bridges to FormulaDeducer §5)',
        markingPoints: [
          { id: 'mp1', text: 'each aluminium atom loses 3 electrons → Al³⁺; each oxygen atom gains 2 electrons → O²⁻.', essential: true },
          { id: 'mp2', text: 'the total electrons lost must equal the total electrons gained.', essential: true },
          { id: 'mp3', text: '2 Al lose 6 electrons and 3 O gain 6 electrons → ratio 2 : 3 → Al₂O₃.', essential: true }
        ],
        allow: [
          'charge-balance form (2 × 3+ = 6+ balances 3 × 2− = 6−).'
        ],
        doNotAccept: [
          { text: '"one of each"', slug: 'one-of-each-ion' },
          { text: 'Al₃O₂', slug: 'charges-as-own-subscript' }
        ],
        tierNote: 'Higher-only.'
      },
      {
        id: 'ib-1f',
        label: '1F',
        heading: 'Describe the dot-and-cross',
        headingNote: '(drawing → DotCrossCanvas Phase 4; described-form MPs here)',
        stem: 'Describe how a dot-and-cross diagram represents the formation of the ions in sodium chloride. [3 marks]',
        tariff: 3,
        command: 'Describe',
        ao: 'AO1',
        tier: 'any',
        isLevels: false,
        note: '(frozen Q10)',
        markingPoints: [
          { id: 'mp1', text: 'electrons from one atom are drawn as dots, from the other as crosses.', essential: true },
          { id: 'mp2', text: 'the single outer electron is shown transferred from sodium to chlorine.', essential: true },
          { id: 'mp3', text: 'each ion is drawn with a full outer shell, with its charge shown (in brackets).', essential: true }
        ],
        doNotAccept: [
          { text: '"a shared pair drawn between them"', slug: 'sharing-vs-transfer-swapped', altSlugs: ['dot-cross-is-shared'] },
          { text: '"a sea of electrons"', slug: 'dot-cross-is-metallic' }
        ],
        tierNote: 'Foundation-safe.'
      }
    ],

    beTheExaminer: [
      {
        id: 'ib-be1',
        label: '4A',
        targetItemId: 'ib-1d',
        heading: 'Partially right (earns marks)',
        headingNote: 'marks the refutation (1D)',
        studentAnswer: 'The statement is not fully correct. The transfer of electrons makes sodium into Na⁺ and chlorine into Cl⁻. After that the two ions have opposite charges. So the transfer is what starts it off, but really the compound is held together because both atoms now have full outer shells.',
        note: '(to 1D, [3 marks])',
        officialMark: 1,
        outOf: 3,
        pointsHit: ['mp1'],
        pointsHitNote: 'MP1 — correctly separates the transfer from the bond and says it creates the ions (1 mark).',
        pointsMissed: ['mp2', 'mp3'],
        pointsMissedNote: 'MP2/MP3 — never names the electrostatic attraction between the oppositely charged ions as the bond. "Held together because both have full shells" is the full-shell-is-the-bond misconception — the full shell explains why the ions form, not what holds them together.',
        misconceptionsShown: ['full-shell-is-the-bond'],
        examinerLine: 'Good — you\'ve separated the transfer (which makes the ions) from the bond. But the step that scores is naming the bond: the strong electrostatic attraction between the opposite charges. The full shells aren\'t the glue.',
        partiallyRight: true
      },
      {
        id: 'ib-be2',
        label: '4B',
        targetItemId: null,
        targetPrompt: 'Deduce the formula of aluminium oxide from its ions. [2 marks] — 1 for balancing idea, 1 for the correct formula',
        heading: 'Low but instructive',
        headingNote: 'marks a formula deduction',
        studentAnswer: 'Aluminium is Al³⁺ and oxygen is O²⁻, so the formula is Al₃O₂ because you swap the charges over to get the little numbers.',
        note: '(to: Deduce the formula of aluminium oxide from its ions. [2 marks] — 1 for balancing idea, 1 for the correct formula)',
        officialMark: 1,
        outOf: 2,
        pointsHitNote: 'identifies the correct ions and charges and knows the charges must balance via a swap (1 mark).',
        pointsMissedNote: 'the swap was done the wrong way — the student used each ion\'s own charge as its own subscript (Al→3, O→2 → Al₃O₂ = 9+ and 4− = +5, not neutral). The subscript must come from the other ion\'s charge (charges-as-own-subscript). Correct: Al₂O₃.',
        misconceptionsShown: ['charges-as-own-subscript'],
        examinerLine: 'You knew the charges and the swap trick — but you swapped the wrong way. Aluminium takes oxygen\'s 2, oxygen takes aluminium\'s 3 → Al₂O₃. Always check it balances: 2 × 3+ = 6+, 3 × 2− = 6−. ✓',
        partiallyRight: false
      }
    ],

    chains: [
      {
        id: 'ib-chainA',
        label: 'Chain A',
        title: 'How the ionic bond in NaCl forms (transfer → ions → attraction)',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Sodium has 1 electron in its outer shell; chlorine has 7.', role: 'creditworthy', roleNote: 'creditworthy (scene-set)' },
          { id: 'l2', text: 'Sodium loses its 1 outer electron → becomes Na⁺ with a full outer shell.', role: 'essential' },
          { id: 'l3', text: 'Chlorine gains that electron → becomes Cl⁻ with a full outer shell.', role: 'essential' },
          { id: 'l4', text: 'The oppositely charged ions attract each other.', role: 'essential' },
          { id: 'l5', text: 'This strong electrostatic attraction is the ionic bond.', role: 'essential', roleNote: 'essential (kills transfer-is-the-bond)' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Sodium and chlorine share a pair of electrons.', slug: 'sharing-vs-transfer-swapped' },
          { id: 'h2', text: 'Chlorine loses an electron to sodium.', slug: 'transfer-direction-reversed' },
          { id: 'h3', text: 'The transfer of the electron is the ionic bond.', slug: 'transfer-is-the-bond' },
          { id: 'h4', text: 'Both atoms lose their electrons into a shared pool.', slug: 'metallic-confusion' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          optional: ['l1'],
          interchangeable: [['l2', 'l3']],
          mustPrecede: [['l4', 'l5']]
        },
        orderingNote: '2 and 3 may swap (the two atoms act at once); 4 must precede 5; link 1 may be omitted. The distinction between link 4 (attraction) and link 5 (that attraction IS the bond) is the whole point — do not let H3 substitute for 5.'
      },
      {
        id: 'ib-chainB',
        label: 'Chain B',
        title: 'Why metals form + ions and non-metals form − ions',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Metals have few electrons in their outer shell.', role: 'essential' },
          { id: 'l2', text: 'They lose these electrons to reach a full outer shell.', role: 'essential' },
          { id: 'l3', text: 'Losing negative electrons leaves more protons than electrons → a positive ion.', role: 'essential' },
          { id: 'l4', text: 'Non-metals have nearly full outer shells and gain electrons.', role: 'essential' },
          { id: 'l5', text: 'Gaining negative electrons gives more electrons than protons → a negative ion.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'Metals are heavier, so their nuclei pull electrons in.', slug: 'mass-sets-charge' },
          { id: 'h2', text: 'Non-metals have more protons, which makes them negative.', slug: 'protons-make-negative' },
          { id: 'h3', text: 'Metals gain electrons and non-metals lose them.', slug: 'gain-lose-reversed' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4', 'l5'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l4', 'l5']]
        },
        orderingNote: 'two parallel blocks (1→2→3 metals, 4→5 non-metals); either block may come first.'
      },
      {
        id: 'ib-chainC',
        label: 'Chain C',
        title: 'Why an ionic compound has no overall charge',
        tier: 'any',
        links: [
          { id: 'l1', text: 'Electrons are transferred from metal to non-metal, not created or destroyed.', role: 'essential' },
          { id: 'l2', text: 'The metal ions carry a total positive charge; the non-metal ions carry a total negative charge.', role: 'essential' },
          { id: 'l3', text: 'The formula has just enough of each ion so the total + equals the total −.', role: 'essential' },
          { id: 'l4', text: 'So the compound has no overall charge.', role: 'essential' }
        ],
        redHerrings: [
          { id: 'h1', text: 'The transferred electrons are destroyed.', slug: 'electrons-destroyed' },
          { id: 'h2', text: 'The ions are held so tightly their charges disappear.', slug: 'charges-disappear' },
          { id: 'h3', text: 'Full shells carry no charge.', slug: 'full-shell-neutral' }
        ],
        orderingRules: {
          canonical: ['l1', 'l2', 'l3', 'l4'],
          mustPrecede: [['l1', 'l2'], ['l2', 'l3'], ['l3', 'l4']]
        },
        orderingNote: 'strict 1→2→3→4.'
      }
    ],

    /* §5 FORMULA DEDUCER BANK — page-level notes, verbatim. */
    formulaNotes: {
      intro: 'Each item: the two ions with charges, the "balance to zero / lowest whole-number ratio" reasoning, the correct formula, and the common wrong formula(s) with the misconception each encodes. The live charge meter reads the running total (∑ = charge×count). Correct = meter reads 0 at the lowest whole-number ratio. Complements MRB-135\'s MCQ formula items (IB-14 used X³⁺/Y²⁻ → X₂Y₃; this bank uses fresh species so no overlap).',
      setTitles: {
        foundation: '5A · FOUNDATION set — Group 1/2 metals with Group 6/7 non-metals',
        higher: '5B · HIGHER set — 3+ and 3− ions, abstractions, given transition-metal charges',
        polyatomic: '5C · [CHECK] OPTIONAL — polyatomic-ion set (beyond this page\'s frozen content)'
      },
      foundation: 'Foundation scaffold: ions supplied with charges shown; the "predict the charge from the group" step (Group 1→1+, 2→2+, 6→2−, 7→1−) can be an optional pre-step for a fuller Foundation item. Progression: 1:1 (F1–2, 7–9) → 1:2 / 2:1 (F3–6, 10–12) → simplest-ratio trap (F7–8).',
      higher: 'Higher progression: named 3±-ion formulae (H1–4) → pure abstraction X/Y (H5–6, the exact grade-8/9 style) → transition-metal charges supplied so the student must use the given charge, not recall a default (H7–10, killing wrong-charge-used). H1 (Al₂O₃) is the worked round; H2–H10 fade the scaffold.',
      polyatomicFlag: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.'
    },

    formula: [
      /* ---- 5A · FOUNDATION set ---- */
      {
        id: 'F1',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Na', charge: 1 },
        anion: { symbol: 'Cl', charge: -1 },
        ratio: [1, 1],
        correctFormula: 'NaCl',
        correctFormulaDisplay: 'NaCl',
        reasoning: '1+ and 1− already balance → 1 : 1',
        chargeGiven: false,
        distractors: [],
        distractorNote: '(starter item, no trap)'
      },
      {
        id: 'F2',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'K', charge: 1 },
        anion: { symbol: 'Br', charge: -1 },
        ratio: [1, 1],
        correctFormula: 'KBr',
        correctFormulaDisplay: 'KBr',
        reasoning: '1+ / 1− → 1 : 1',
        chargeGiven: false,
        distractors: []
      },
      {
        id: 'F3',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Mg', charge: 2 },
        anion: { symbol: 'Cl', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'MgCl2',
        correctFormulaDisplay: 'MgCl₂',
        reasoning: 'one 2+ needs two 1− → 1 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'MgCl', display: 'MgCl', slug: 'one-of-each-ion', note: '(+1, not neutral)' },
          { formula: 'MgCl3', display: 'MgCl₃', slug: 'wrong-ratio' }
        ]
      },
      {
        id: 'F4',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Ca', charge: 2 },
        anion: { symbol: 'Cl', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'CaCl2',
        correctFormulaDisplay: 'CaCl₂',
        reasoning: 'one 2+ needs two 1− → 1 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'CaCl', display: 'CaCl', slug: 'one-of-each-ion' },
          { formula: 'Ca2Cl', display: 'Ca₂Cl', slug: 'charges-swapped-to-subscripts' },
          { formula: 'CaCl3', display: 'CaCl₃', slug: 'wrong-ratio' }
        ],
        distractorNote: '(all three are the frozen Q8 distractors)'
      },
      {
        id: 'F5',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Na', charge: 1 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [2, 1],
        correctFormula: 'Na2O',
        correctFormulaDisplay: 'Na₂O',
        reasoning: 'two 1+ balance one 2− → 2 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'NaO', display: 'NaO', slug: 'one-of-each-ion', note: '(−1)' },
          { formula: 'NaO2', display: 'NaO₂', slug: 'wrong-ratio' }
        ]
      },
      {
        id: 'F6',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'K', charge: 1 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [2, 1],
        correctFormula: 'K2O',
        correctFormulaDisplay: 'K₂O',
        reasoning: 'two 1+ balance one 2− → 2 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'KO', display: 'KO', slug: 'one-of-each-ion' }
        ],
        distractorNote: '(frozen Higher "predict K₂O")'
      },
      {
        id: 'F7',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Mg', charge: 2 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [1, 1],
        correctFormula: 'MgO',
        correctFormulaDisplay: 'MgO',
        reasoning: '2+ and 2− balance → 1 : 1 (simplest ratio)',
        chargeGiven: false,
        distractors: [
          { formula: 'Mg2O2', display: 'Mg₂O₂', slug: 'not-simplified', note: '(must give the simplest whole-number ratio)' }
        ]
      },
      {
        id: 'F8',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Ca', charge: 2 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [1, 1],
        correctFormula: 'CaO',
        correctFormulaDisplay: 'CaO',
        reasoning: '2+ / 2− → 1 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'Ca2O2', display: 'Ca₂O₂', slug: 'not-simplified' }
        ]
      },
      {
        id: 'F9',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Li', charge: 1 },
        anion: { symbol: 'F', charge: -1 },
        ratio: [1, 1],
        correctFormula: 'LiF',
        correctFormulaDisplay: 'LiF',
        reasoning: '1+ / 1− → 1 : 1',
        chargeGiven: false,
        distractors: []
      },
      {
        id: 'F10',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Mg', charge: 2 },
        anion: { symbol: 'F', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'MgF2',
        correctFormulaDisplay: 'MgF₂',
        reasoning: 'one 2+ needs two 1− → 1 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'MgF', display: 'MgF', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'F11',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Na', charge: 1 },
        anion: { symbol: 'S', charge: -2 },
        ratio: [2, 1],
        correctFormula: 'Na2S',
        correctFormulaDisplay: 'Na₂S',
        reasoning: 'two 1+ balance one 2− → 2 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'NaS', display: 'NaS', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'F12',
        set: 'foundation',
        tier: 'any',
        optional: false,
        check: false,
        cation: { symbol: 'Ca', charge: 2 },
        anion: { symbol: 'Br', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'CaBr2',
        correctFormulaDisplay: 'CaBr₂',
        reasoning: 'one 2+ needs two 1− → 1 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'CaBr', display: 'CaBr', slug: 'one-of-each-ion' }
        ]
      },

      /* ---- 5B · HIGHER set ---- */
      {
        id: 'H1',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Al', charge: 3 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [2, 3],
        correctFormula: 'Al2O3',
        correctFormulaDisplay: 'Al₂O₃',
        reasoning: 'LCM(3,2)=6 → two 3+ (6+) & three 2− (6−) → 2 : 3',
        chargeGiven: false,
        distractors: [
          { formula: 'AlO', display: 'AlO', slug: 'one-of-each-ion', note: '(+1)' },
          { formula: 'Al3O2', display: 'Al₃O₂', slug: 'charges-as-own-subscript', note: '(swap done wrong way, +5)' }
        ]
      },
      {
        id: 'H2',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Al', charge: 3 },
        anion: { symbol: 'Cl', charge: -1 },
        ratio: [1, 3],
        correctFormula: 'AlCl3',
        correctFormulaDisplay: 'AlCl₃',
        reasoning: 'LCM(3,1)=3 → one 3+ & three 1− → 1 : 3',
        chargeGiven: false,
        distractors: [
          { formula: 'AlCl', display: 'AlCl', slug: 'one-of-each-ion' },
          { formula: 'Al3Cl', display: 'Al₃Cl', slug: 'charges-as-own-subscript' }
        ]
      },
      {
        id: 'H3',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Mg', charge: 2 },
        anion: { symbol: 'N', charge: -3 },
        ratio: [3, 2],
        correctFormula: 'Mg3N2',
        correctFormulaDisplay: 'Mg₃N₂',
        reasoning: 'LCM(2,3)=6 → three 2+ (6+) & two 3− (6−) → 3 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'MgN', display: 'MgN', slug: 'one-of-each-ion' },
          { formula: 'Mg2N3', display: 'Mg₂N₃', slug: 'charges-as-own-subscript', note: '(4+/9−)' }
        ]
      },
      {
        id: 'H4',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Al', charge: 3 },
        anion: { symbol: 'S', charge: -2 },
        ratio: [2, 3],
        correctFormula: 'Al2S3',
        correctFormulaDisplay: 'Al₂S₃',
        reasoning: 'LCM(3,2)=6 → 2 : 3',
        chargeGiven: false,
        distractors: [
          { formula: 'AlS', display: 'AlS', slug: 'one-of-each-ion' },
          { formula: 'Al3S2', display: 'Al₃S₂', slug: 'charges-as-own-subscript' }
        ]
      },
      {
        id: 'H5',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        abstract: true,
        cation: { symbol: 'X', charge: 2 },
        anion: { symbol: 'Y', charge: -3 },
        ratio: [3, 2],
        correctFormula: 'X3Y2',
        correctFormulaDisplay: 'X₃Y₂',
        reasoning: 'LCM(2,3)=6 → three X²⁺ & two Y³⁻ → 3 : 2',
        chargeGiven: false,
        distractors: [
          { formula: 'XY', display: 'XY', slug: 'one-of-each-ion', note: '(−1)' },
          { formula: 'X2Y3', display: 'X₂Y₃', slug: 'charges-as-own-subscript', note: '(4+/9−)' }
        ],
        distractorNote: 'Complements MRB-135 IB-14 (X³⁺/Y²⁻→X₂Y₃).'
      },
      {
        id: 'H6',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        abstract: true,
        cation: { symbol: 'X', charge: 1 },
        anion: { symbol: 'Y', charge: -2 },
        ratio: [2, 1],
        correctFormula: 'X2Y',
        correctFormulaDisplay: 'X₂Y',
        reasoning: 'two X⁺ balance one Y²⁻ → 2 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'XY', display: 'XY', slug: 'one-of-each-ion' },
          { formula: 'XY2', display: 'XY₂', slug: 'charges-swapped-to-subscripts' }
        ]
      },
      {
        id: 'H7',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Fe', charge: 3 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [2, 3],
        correctFormula: 'Fe2O3',
        correctFormulaDisplay: 'Fe₂O₃',
        reasoning: 'LCM(3,2)=6 → 2 : 3',
        chargeGiven: true,
        distractors: [
          { formula: 'FeO', display: 'FeO', slug: 'wrong-charge-used', note: 'ignored the given 3+ (that is iron(II) oxide)' },
          { formula: 'Fe3O2', display: 'Fe₃O₂', slug: 'charges-as-own-subscript' }
        ]
      },
      {
        id: 'H8',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Fe', charge: 2 },
        anion: { symbol: 'Cl', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'FeCl2',
        correctFormulaDisplay: 'FeCl₂',
        reasoning: 'one 2+ needs two 1− → 1 : 2',
        chargeGiven: true,
        distractors: [
          { formula: 'FeCl3', display: 'FeCl₃', slug: 'wrong-charge-used', note: 'used Fe³⁺ instead' },
          { formula: 'FeCl', display: 'FeCl', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'H9',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Cu', charge: 2 },
        anion: { symbol: 'O', charge: -2 },
        ratio: [1, 1],
        correctFormula: 'CuO',
        correctFormulaDisplay: 'CuO',
        reasoning: '2+ / 2− → 1 : 1',
        chargeGiven: true,
        distractors: [
          { formula: 'Cu2O', display: 'Cu₂O', slug: 'wrong-charge-used', note: 'used Cu⁺ instead (that is copper(I) oxide)' }
        ]
      },
      {
        id: 'H10',
        set: 'higher',
        tier: 'higher',
        optional: false,
        check: false,
        cation: { symbol: 'Zn', charge: 2 },
        anion: { symbol: 'N', charge: -3 },
        ratio: [3, 2],
        correctFormula: 'Zn3N2',
        correctFormulaDisplay: 'Zn₃N₂',
        reasoning: 'LCM(2,3)=6 → three 2+ & two 3− → 3 : 2',
        chargeGiven: true,
        distractors: [
          { formula: 'ZnN', display: 'ZnN', slug: 'one-of-each-ion' },
          { formula: 'Zn2N3', display: 'Zn₂N₃', slug: 'charges-as-own-subscript' }
        ]
      },

      /* ---- 5C · [CHECK] OPTIONAL polyatomic-ion set ---- */
      {
        id: 'P1',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'Na', charge: 1 },
        anion: { symbol: 'OH', display: 'OH⁻', charge: -1 },
        ratio: [1, 1],
        correctFormula: 'NaOH',
        correctFormulaDisplay: 'NaOH',
        reasoning: '1+ / 1− → 1 : 1',
        chargeGiven: false,
        distractors: []
      },
      {
        id: 'P2',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'Ca', charge: 2 },
        anion: { symbol: 'OH', display: 'OH⁻', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'Ca(OH)2',
        correctFormulaDisplay: 'Ca(OH)₂',
        reasoning: 'one 2+ needs two OH⁻ → brackets round OH',
        chargeGiven: false,
        distractors: [
          { formula: 'CaOH2', display: 'CaOH₂', slug: 'missing-brackets', note: '(reads as one O, two H)' },
          { formula: 'CaOH', display: 'CaOH', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'P3',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'Na', charge: 1 },
        anion: { symbol: 'SO4', display: 'SO₄²⁻', charge: -2 },
        ratio: [2, 1],
        correctFormula: 'Na2SO4',
        correctFormulaDisplay: 'Na₂SO₄',
        reasoning: 'two 1+ balance one 2− → 2 : 1',
        chargeGiven: false,
        distractors: [
          { formula: 'NaSO4', display: 'NaSO₄', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'P4',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'Ca', charge: 2 },
        anion: { symbol: 'NO3', display: 'NO₃⁻', charge: -1 },
        ratio: [1, 2],
        correctFormula: 'Ca(NO3)2',
        correctFormulaDisplay: 'Ca(NO₃)₂',
        reasoning: 'one 2+ needs two NO₃⁻ → brackets',
        chargeGiven: false,
        distractors: [
          { formula: 'CaNO32', display: 'CaNO₃₂', slug: 'missing-brackets' },
          { formula: 'CaNO6', display: 'CaNO₆', slug: 'missing-brackets' }
        ]
      },
      {
        id: 'P5',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'NH4', display: 'NH₄⁺', charge: 1 },
        anion: { symbol: 'SO4', display: 'SO₄²⁻', charge: -2 },
        ratio: [2, 1],
        correctFormula: '(NH4)2SO4',
        correctFormulaDisplay: '(NH₄)₂SO₄',
        reasoning: 'two NH₄⁺ balance one SO₄²⁻ → brackets round NH₄',
        chargeGiven: false,
        distractors: [
          { formula: 'NH42SO4', display: 'NH₄₂SO₄', slug: 'missing-brackets' },
          { formula: 'NH4SO4', display: 'NH₄SO₄', slug: 'one-of-each-ion' }
        ]
      },
      {
        id: 'P6',
        set: 'polyatomic',
        tier: 'higher',
        optional: true,
        check: true,
        checkNote: 'Scope flag: the frozen ionic-bonding content covers only monatomic, group-derived ions. Formula construction with polyatomic ions (given in the AQA data sheet) IS examinable and encodes the high-value "forgot the brackets" misconception — but it is net-new relative to this page\'s frozen fields. Included as a separate opt-in set for Mide\'s decision, not folded into 5A/5B.',
        cation: { symbol: 'Al', charge: 3 },
        anion: { symbol: 'SO4', display: 'SO₄²⁻', charge: -2 },
        ratio: [2, 3],
        correctFormula: 'Al2(SO4)3',
        correctFormulaDisplay: 'Al₂(SO₄)₃',
        reasoning: 'LCM(3,2)=6 → two Al³⁺ & three SO₄²⁻ → brackets',
        chargeGiven: false,
        distractors: [
          { formula: 'Al2SO43', display: 'Al₂SO₄₃', slug: 'missing-brackets' },
          { formula: 'AlSO4', display: 'AlSO₄', slug: 'one-of-each-ion' }
        ]
      }
    ]
  };
})();
