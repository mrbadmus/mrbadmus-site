"""Chemistry · Chemical changes — the MRB-338 expansion for `half-equations`.

Higher tier, and the leaf turns on two things balancing at once: the atoms and
the charge. The weight therefore falls on the electron COUNT rather than on the
products — a pupil who can name what forms at each electrode still writes
`Cl- → Cl2 + e-` unless the diatomic molecule and the charge are both checked.

The twelve shipped rows already own hydrogen at the cathode, aluminium at the
cathode, sodium at the cathode, the oxide and hydroxide anode equations, the
bromine-equation error and the dilute-sulfuric-acid combination, so none of
those is asked again here. The new rows take the metals those leave free — zinc,
potassium, silver, copper, lead, iron, magnesium, calcium — the electron-count
questions the shipped rows never ask, and the harder band's real work, which is
making two half equations agree on electrons before combining them. A named
electrolyte appears only as the SETTING for an equation, never as a bare product
prediction. Every equation below balances for atoms and for charge.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-half-equations-e05',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what a half equation shows.',
        "options": [
            'The change at one electrode',
            'The overall change happening in the whole cell',
            'The formula of the electrolyte being broken down',
            'The mass of each product that collects on the two electrodes',
        ],
        "correct_index": 0,
        "why": 'A half equation describes one electrode only, which is why the '
               'electrons appear in it as reactants or as products.',
    },
    {
        "id": 'ks4-half-equations-e06',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the half equation showing reduction.',
        "options": [
            'Cu → Cu2+ + 2e-',
            '4OH- → O2 + 2H2O + 4e-',
            '2Cl- → Cl2 + 2e-',
            'Cu2+ + 2e- → Cu',
        ],
        "correct_index": 3,
        "why": 'Reduction is gain of electrons, so the electrons sit on the left '
               'with the copper ion that takes them.',
    },
    {
        "id": 'ks4-half-equations-e07',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Zinc is deposited at a cathode. Give the equation.',
        "options": [
            'Zn2+ → Zn + 2e-',
            'Zn+ + e- → Zn',
            'Zn2+ + 2e- → Zn',
            'Zn → Zn2+ + 2e-',
        ],
        "correct_index": 2,
        "why": 'The zinc ion carries a 2+ charge, so it gains two electrons at the '
               'cathode and is deposited as zinc metal.',
    },
    {
        "id": 'ks4-half-equations-e08',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State how many electrons an aluminium ion gains when it is reduced.',
        "options": [
            'One, because one atom forms',
            'Three, because the ion carries a 3+ charge',
            'Two, as for every metal ion',
            'Six, because Al2O3 holds two ions',
        ],
        "correct_index": 1,
        "why": 'The 3+ charge has to be cancelled, so three electrons are needed, '
               'giving Al3+ + 3e- → Al.',
    },
    {
        "id": 'ks4-half-equations-e09',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'An oxidation is taking place. State where the electrons are written.',
        "options": [
            'On the left, because the ion here is the reactant overall',
            'On the left, because electrons are being gained',
            'On the right, because they have been lost',
            'On the right, because the charge has to increase',
        ],
        "correct_index": 2,
        "why": 'Oxidation is loss of electrons, so the electrons leave the species '
               'and are written among the products.',
    },
    {
        "id": 'ks4-half-equations-e10',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Which equation shows chlorine forming at an anode?',
        "options": [
            'Cl- → Cl2 + e-',
            '2Cl- + 2e- → Cl2',
            'Cl2 + 2e- → 2Cl-',
            '2Cl- → Cl2 + 2e-',
        ],
        "correct_index": 3,
        "why": 'Two chloride ions are needed to build one Cl2 molecule, and each '
               'loses a single electron.',
    },
    {
        "id": 'ks4-half-equations-e11',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Potassium metal collects at a cathode. Give the equation.',
        "options": [
            '2K+ → K2 + 2e-',
            'K+ + 2e- → K',
            'K → K+ + e-',
            'K+ + e- → K',
        ],
        "correct_index": 3,
        "why": 'A potassium ion carries a single positive charge, so one electron is '
               'enough to reduce it to a potassium atom.',
    },
    {
        "id": 'ks4-half-equations-e12',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Electrons appear among the products of a half equation. Name the '
                'electrode it describes.',
        "options": [
            'The cathode, where ions take in electrons',
            'The anode, where the ions hand their electrons over',
            'Either one, as electrons pass through both',
            'Neither, as electrons are left out entirely',
        ],
        "correct_index": 1,
        "why": 'Electrons among the products means they have been lost, and loss of '
               'electrons happens at the anode.',
    },
    {
        "id": 'ks4-half-equations-e13',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Silver plates onto a cathode. Give the equation.',
        "options": [
            'Ag2+ + 2e- → Ag',
            'Ag → Ag+ + e-',
            'Ag+ + e- → Ag',
            'Ag+ → Ag + e-',
        ],
        "correct_index": 2,
        "why": 'The silver ion is Ag+, so a single electron reduces it to a silver '
               'atom on the cathode surface.',
    },
    {
        "id": 'ks4-half-equations-e14',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State how many electrons a 2+ metal ion takes in at a cathode.',
        "options": [
            'One, since a single atom is produced',
            'Four, because two pairs are needed',
            'Three, as for most metal ions',
            'Two, matching its 2+ charge',
        ],
        "correct_index": 3,
        "why": 'The number of electrons equals the size of the charge, so a 2+ ion '
               'needs exactly two of them.',
    },
    {
        "id": 'ks4-half-equations-e15',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why two chloride ions, rather than one, appear when '
                'chlorine is made.',
        "options": [
            'Every chloride ion carries two units of negative charge',
            'Chlorine gas exists as Cl2 molecules',
            'An anode reaction has to give up two electrons for each molecule made',
            'A chloride ion has to lose its outer electron twice over',
        ],
        "correct_index": 1,
        "why": 'The product is the diatomic molecule Cl2, so two ions are needed to '
               'supply its two atoms.',
    },
    {
        "id": 'ks4-half-equations-e16',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A cathode becomes coated with copper. Give the equation.',
        "options": [
            'Cu2+ + 2e- → Cu',
            'Cu → Cu2+ + 2e-',
            'Cu2+ → Cu + 2e-',
            'Cu+ + e- → Cu',
        ],
        "correct_index": 0,
        "why": 'The copper(II) ion takes two electrons at the cathode, which cancels '
               'its 2+ charge and deposits copper metal.',
    },
    {
        "id": 'ks4-half-equations-e17',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Lead metal appears on a cathode. Give the equation.',
        "options": [
            'Pb → Pb2+ + 2e-',
            'Pb2+ → Pb + 2e-',
            'Pb2+ + 2e- → Pb',
            'Pb2+ + e- → Pb',
        ],
        "correct_index": 2,
        "why": 'A lead(II) ion carries a 2+ charge, so it gains two electrons to '
               'become a neutral lead atom.',
    },
    {
        "id": 'ks4-half-equations-e18',
        "subtopic_slug": 'half-equations',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A half equation has two electrons written on the left. State '
                'whether it shows oxidation or reduction.',
        "options": [
            'Reduction, because electrons are gained',
            'Oxidation, because the charge falls',
            'Oxidation, because electrons are shown',
            'Neither, because the side does not matter here',
        ],
        "correct_index": 0,
        "why": 'Electrons on the left have been taken in by the species, and gain of '
               'electrons is reduction.',
    },

    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-half-equations-s05',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Molten magnesium chloride is electrolysed. Give the equation at the '
                'negative electrode.',
        "options": [
            'Mg → Mg2+ + 2e-',
            'Mg2+ + e- → Mg',
            'Mg2+ + 2e- → Mg',
            '2Cl- → Cl2 + 2e-',
        ],
        "correct_index": 2,
        "why": 'Magnesium ions carry a 2+ charge and are attracted to the negative '
               'electrode, where they each gain two electrons.',
    },
    {
        "id": 'ks4-half-equations-s06',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Chlorine bubbles off the positive electrode of a molten zinc '
                'chloride cell. Determine how many electrons two chloride ions '
                'release.',
        "options": [
            'One electron between the two ions',
            'Two electrons, one from each ion',
            'Four electrons, two from each ion',
            'None, because chloride ions gain electrons here',
        ],
        "correct_index": 1,
        "why": 'Each chloride ion loses the single electron that gave it its 1- '
               'charge, so the pair releases two altogether.',
    },
    {
        "id": 'ks4-half-equations-s07',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Iron(II) ions are reduced to iron metal at a cathode. Write the '
                'equation for that change.',
        "options": [
            'Fe2O3 + 6e- → 2Fe + 3O2',
            'Fe3+ + 3e- → Fe',
            'Fe2+ + 2e- → Fe',
            'Fe2+ + e- → Fe',
        ],
        "correct_index": 2,
        "why": 'An iron(II) ion carries a 2+ charge, so two electrons reduce it to a '
               'neutral iron atom.',
    },
    {
        "id": 'ks4-half-equations-s08',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A cathode reaction takes 2 electrons and an anode reaction releases '
                '4. Determine how many times the cathode reaction must happen.',
        "options": [
            'Once, because one anode reaction is enough',
            'Four times, one for each electron released',
            'Three times, so that six electrons are used',
            'Twice, so that all four electrons are used',
        ],
        "correct_index": 3,
        "why": 'Four electrons are released and each cathode reaction consumes two, '
               'so the cathode reaction runs twice.',
    },
    {
        "id": 'ks4-half-equations-s09',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine how many hydroxide ions must be oxidised in order to '
                'release 4 electrons.',
        "options": [
            'Four, one electron from each ion',
            'Two, because oxygen is diatomic',
            'One, because it carries a 1- charge',
            'Eight, two ions for every electron',
        ],
        "correct_index": 0,
        "why": 'Each hydroxide ion carries a single negative charge and gives up one '
               'electron, so four ions supply four electrons.',
    },
    {
        "id": 'ks4-half-equations-s10',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'An oxidation may be written as Fe2+ - e- → Fe3+. Explain what this '
                'form is saying.',
        "options": [
            'One electron is being taken away from the iron ion',
            'One electron is being added on to the iron ion',
            'The iron ion is ending up with one fewer proton',
            'The reaction is running backwards, from iron(III) to iron(II)',
        ],
        "correct_index": 0,
        "why": 'Subtracting an electron on the left says the same thing as adding it '
               'on the right, so this is Fe2+ → Fe3+ + e-.',
    },
    {
        "id": 'ks4-half-equations-s11',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Dilute sulfuric acid is electrolysed. Determine the moles of '
                'electrons needed to make 1 mol of hydrogen.',
        "options": [
            '1 mol, one electron for each molecule',
            '0.5 mol, as the two ions share a pair',
            '2 mol, as two hydrogen ions are reduced',
            '4 mol, because the acid is dibasic',
        ],
        "correct_index": 2,
        "why": 'Two hydrogen ions and two electrons make one H2 molecule, so 1 mol '
               'of hydrogen needs 2 mol of electrons.',
    },
    {
        "id": 'ks4-half-equations-s12',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'During the purification of copper the impure anode loses mass. '
                'Write the equation for what happens to it.',
        "options": [
            'Cu → Cu2+ + 2e-',
            'Cu2+ + 2e- → Cu',
            'Cu + 2e- → Cu2-',
            '2H+ + 2e- → H2',
        ],
        "correct_index": 0,
        "why": 'Copper atoms in the anode each lose two electrons and enter the '
               'solution as Cu2+ ions, so the anode wears away.',
    },
    {
        "id": 'ks4-half-equations-s13',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A pupil writes Cu2+ + e- → Cu for a cathode. Identify the error.',
        "options": [
            'The electron is on the wrong side',
            'One electron too few for the 2+ copper ion',
            'Copper is not deposited at a cathode',
            'The copper should be written Cu2',
        ],
        "correct_index": 1,
        "why": 'A 2+ ion needs two electrons, so as written the charges do not '
               'balance: the left comes to 1+ and the right to 0.',
    },
    {
        "id": 'ks4-half-equations-s14',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Iodine is produced when potassium iodide solution is electrolysed. '
                'Write the equation for its formation.',
        "options": [
            'I- → I2 + e-',
            '2I- + 2e- → I2',
            'K+ + e- → K',
            '2I- → I2 + 2e-',
        ],
        "correct_index": 3,
        "why": 'Iodide is a halide ion, so iodine forms at the anode and two iodide '
               'ions release two electrons between them.',
    },
    {
        "id": 'ks4-half-equations-s15',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Zinc displaces copper from copper sulfate solution. Write the '
                'equation for the zinc.',
        "options": [
            'Zn2+ + 2e- → Zn',
            'Zn → Zn2+ + e-',
            'Zn + 2e- → Zn2-',
            'Zn → Zn2+ + 2e-',
        ],
        "correct_index": 3,
        "why": 'Zinc atoms lose two electrons each to become Zn2+ ions, so the zinc '
               'is oxidised while the copper ions are reduced.',
    },
    {
        "id": 'ks4-half-equations-s16',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why the electron counts in two half equations are made '
                'equal before they are combined.',
        "options": [
            'Every electron lost at one electrode is gained at the other',
            'The two electrodes are the same size',
            'A metal ion has the same charge as a halide ion',
            'The gases formed occupy equal volumes',
        ],
        "correct_index": 0,
        "why": 'Electrons are neither created nor destroyed, so the number released '
               'at the anode must match the number taken up at the cathode.',
    },
    {
        "id": 'ks4-half-equations-s17',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calcium is obtained by electrolysing its molten oxide. Write the '
                'cathode reaction.',
        "options": [
            'Ca2+ + 2e- → Ca',
            'Ca → Ca2+ + 2e-',
            'CaO + 2e- → Ca + O2',
            'Ca2+ + e- → Ca',
        ],
        "correct_index": 0,
        "why": 'The calcium ion is Ca2+, so two electrons reduce it to calcium metal '
               'at the negative electrode.',
    },
    {
        "id": 'ks4-half-equations-s18',
        "subtopic_slug": 'half-equations',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Hydrogen rather than sodium is produced when sodium chloride '
                'solution is electrolysed. Write the cathode reaction.',
        "options": [
            'Na+ + e- → Na',
            'H+ + 2e- → H2',
            '2H+ + 2e- → H2',
            '2H+ → H2 + 2e-',
        ],
        "correct_index": 2,
        "why": 'Sodium is more reactive than hydrogen, so the hydrogen ions from the '
               'water are reduced instead, two at a time.',
    },

    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-half-equations-h05',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'One electrode reaction takes 2 electrons and the other releases 3. '
                'Determine the smallest number of electrons that lets both balance.',
        "options": [
            'Five, from adding two and three',
            'Six, the lowest common multiple of 2 and 3',
            'Two, the smaller of the two numbers',
            'Three, the larger of the two numbers',
        ],
        "correct_index": 1,
        "why": 'Six is the smallest number that both 2 and 3 divide into, so the '
               'first reaction runs three times and the second twice.',
    },
    {
        "id": 'ks4-half-equations-h06',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine the balanced overall equation for electrolysing molten '
                'aluminium oxide.',
        "options": [
            'Al2O3 → 2Al + 3O2',
            'Al2O3 → 2Al + O2',
            '2Al2O3 → 4Al + 3O2',
            '4Al2O3 → 8Al + 3O2',
        ],
        "correct_index": 2,
        "why": 'Two Al2O3 units supply four aluminium atoms and six oxide ions, and '
               'six oxide ions make three O2 molecules.',
    },
    {
        "id": 'ks4-half-equations-h07',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A molten metal chloride is reduced at the cathode by '
                'X2+ + 2e- → X. Deduce the formula of that chloride.',
        "options": [
            'XCl, since one chloride ion is enough to balance it',
            'XCl2, since two chloride ions balance a 2+ ion',
            'X2Cl, since the metal carries the charge of two chloride ions',
            'X2Cl3, since the two charges cross over as 2 and 3',
        ],
        "correct_index": 1,
        "why": 'A 2+ ion needs two 1- chloride ions for the compound to have no '
               'overall charge, so the formula is XCl2.',
    },
    {
        "id": 'ks4-half-equations-h08',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the number of moles of electrons released when 2 mol of '
                'bromide ions are oxidised.',
        "options": [
            '1 mol, since the two ions share a single electron pair',
            '0.5 mol, since only one Br2 molecule is formed',
            '4 mol, since bromine is diatomic and so doubles it',
            '2 mol, since each bromide ion loses one electron',
        ],
        "correct_index": 3,
        "why": 'Each bromide ion loses a single electron as it is oxidised, so 2 mol '
               'of ions release 2 mol of electrons.',
    },
    {
        "id": 'ks4-half-equations-h09',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Sodium sulfate solution is electrolysed with inert electrodes. '
                'Deduce how many hydrogen molecules form for each oxygen molecule.',
        "options": [
            'Two hydrogen molecules for each oxygen molecule',
            'One hydrogen molecule for each oxygen molecule',
            'Half a hydrogen molecule for each oxygen molecule',
            'Four hydrogen molecules for each oxygen molecule',
        ],
        "correct_index": 0,
        "why": 'Making one O2 molecule releases four electrons, and every two '
               'electrons make one H2, so two H2 form for each O2.',
    },
    {
        "id": 'ks4-half-equations-h10',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why the change from chloride ions to chlorine gas at an '
                'anode counts as an oxidation.',
        "options": [
            'The ions have lost electrons to the electrode',
            'The ions have gained electrons from the electrode',
            'Oxygen is given off alongside the chlorine molecule formed',
            'The chlorine molecule ends up negatively charged',
        ],
        "correct_index": 0,
        "why": 'Oxidation is loss of electrons, and each chloride ion gives up the '
               'electron that gave it its negative charge.',
    },
    {
        "id": 'ks4-half-equations-h11',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'An iron(III) ion becomes an iron(II) ion. Deduce the equation for '
                'that change.',
        "options": [
            'Fe3+ → Fe2+ + e-',
            'Fe3+ + 3e- → Fe2+',
            'Fe2+ + e- → Fe3+',
            'Fe3+ + e- → Fe2+',
        ],
        "correct_index": 3,
        "why": 'The charge falls from 3+ to 2+, which means one electron has been '
               'gained, so the change is a reduction.',
    },
    {
        "id": 'ks4-half-equations-h12',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Molten lead bromide breaks down during electrolysis. Determine how '
                'many bromine molecules form for each lead atom.',
        "options": [
            'Two bromine molecules for each lead atom',
            'Three bromine molecules for every two lead atoms',
            'Half a bromine molecule for each lead atom',
            'One bromine molecule for each lead atom',
        ],
        "correct_index": 3,
        "why": 'Depositing one lead atom takes two electrons and making one Br2 '
               'molecule releases two, so the two happen one for one.',
    },
    {
        "id": 'ks4-half-equations-h13',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '6 electrons pass through molten aluminium chloride during '
                'electrolysis. Deduce how many aluminium atoms and chlorine '
                'molecules that produces.',
        "options": [
            '3 aluminium atoms and 2 chlorine molecules',
            '6 aluminium atoms and 6 chlorine molecules',
            '2 aluminium atoms and 3 chlorine molecules',
            '2 aluminium atoms and 6 chlorine molecules',
        ],
        "correct_index": 2,
        "why": 'Each aluminium ion takes three electrons and each Cl2 molecule '
               'releases two, so six electrons give two atoms and three molecules.',
    },
    {
        "id": 'ks4-half-equations-h14',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A pupil offers 2O2- + 4e- → O2 as an anode equation. Evaluate it.',
        "options": [
            'Correct, because four electrons balance the two 2- charges',
            'Wrong, because the electrons belong among the products',
            'Wrong, because three oxide ions are needed to make each O2 molecule',
            'Wrong, because an anode is where oxide ions are reduced',
        ],
        "correct_index": 1,
        "why": 'Oxide ions are oxidised at an anode and therefore lose electrons, so '
               'the electrons must be written on the right.',
    },
    {
        "id": 'ks4-half-equations-h15',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A pure copper anode loses 6.4 g during the electrolysis of copper '
                'sulfate solution. Predict the mass gained by the cathode.',
        "options": [
            '3.2 g, because two electrons are involved',
            '12.8 g, since the charge doubles it',
            '6.4 g, the same mass as the anode lost',
            'Nothing, because the copper stays in solution as ions',
        ],
        "correct_index": 2,
        "why": 'The anode releases one Cu2+ ion for every copper atom the cathode '
               'deposits, so the mass transfers across unchanged.',
    },
    {
        "id": 'ks4-half-equations-h16',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Magnesium sulfate solution is electrolysed and no magnesium is '
                'deposited. Deduce the cathode equation and the reason.',
        "options": [
            'Mg2+ + 2e- → Mg, as the ion carries a 2+ charge',
            '2H+ + 2e- → H2, as magnesium is more reactive than hydrogen',
            '2H+ + 2e- → H2, as sulfate ions block the metal',
            'Mg2+ + 2e- → Mg, as water gives no hydrogen ions',
        ],
        "correct_index": 1,
        "why": 'When the metal is more reactive than hydrogen its ions stay in '
               'solution and the hydrogen ions from the water are reduced.',
    },
    {
        "id": 'ks4-half-equations-h17',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Calculate the moles of electrons that must pass to make 1 mol of '
                'chlorine gas.',
        "options": [
            '1 mol, one electron for each molecule that forms',
            '4 mol, because chlorine molecules form in pairs of pairs',
            '0.5 mol, because the two ions share the loss',
            '2 mol, one from each of the two chloride ions',
        ],
        "correct_index": 3,
        "why": 'One Cl2 molecule is built from two chloride ions, each of which '
               'releases one electron, so 1 mol of Cl2 needs 2 mol of electrons.',
    },
    {
        "id": 'ks4-half-equations-h18',
        "subtopic_slug": 'half-equations',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Write the overall ionic equation for the electrolysis of molten '
                'sodium chloride.',
        "options": [
            'Na+ + Cl- → Na + Cl',
            '2Na+ + Cl2 → 2Na + 2Cl-',
            'Na+ + 2Cl- → Na + Cl2',
            '2Na+ + 2Cl- → 2Na + Cl2',
        ],
        "correct_index": 3,
        "why": 'Two sodium ions take the two electrons that two chloride ions '
               'release, so the electrons cancel and the charges balance at zero.',
    },
]
