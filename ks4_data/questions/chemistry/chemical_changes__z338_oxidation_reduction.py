"""Chemistry · Chemical changes — the MRB-338 expansion for `oxidation-reduction`.

Two definitions of the same pair of changes, and the weight falls on holding
both at once: oxidation as gain of oxygen and as loss of electrons, reduction as
loss of oxygen and as gain of electrons. The oxygen definition carries the
metal-oxide rows (copper oxide with hydrogen, iron oxide with carbon monoxide,
zinc and lead oxides with carbon); the electron definition carries the rows
where no oxygen is present at all — magnesium in chlorine, a halogen displacing
a halide, a metal displacing another metal from its solution.

The heaviest single point is the counterintuitive one the lesson names as the
common mistake: an oxidising agent is itself reduced, a reducing agent is itself
oxidised. It is asked from several sides — define the agent, identify it in a
stated equation, correct a wrong statement about it, and deduce it in an
unfamiliar reaction such as magnesium burning in carbon dioxide. Named real
oxidising and reducing agents (hydrogen, carbon, carbon monoxide, oxygen,
chlorine, hydrogen peroxide, potassium manganate(VII)) and the everyday redox
contexts (rusting, combustion, respiration, photosynthesis, tarnishing,
water treatment) supply the applied and harder rows, with mass and
electron-counting data giving the arithmetic. No half equations are written and
no electrode is named — both belong to other subtopics.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-oxidation-reduction-e05',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A metal oxide loses its oxygen during a reaction. Name the type of '
                'change the metal oxide has undergone.',
        "options": [
            'Reduction',
            'Oxidation',
            'Neutralisation',
            'Precipitation',
        ],
        "correct_index": 0,
        "why": 'Loss of oxygen is reduction, so the oxide has been reduced by whatever '
               'took its oxygen away.',
    },
    {
        "id": 'ks4-oxidation-reduction-e06',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'OIL RIG is used to remember the electron definitions of oxidation and '
                'reduction. State what the letters OIL stand for.',
        "options": [
            'Oxidation Is Loss of oxygen, so a substance that burns has been reduced',
            'Oxidation Is Loss of electrons',
            'Oxygen Is Lost, not electrons',
            'Oxidation Is Loss of protons',
        ],
        "correct_index": 1,
        "why": 'OIL RIG is about electrons only: Oxidation Is Loss and Reduction Is '
               'Gain of electrons.',
    },
    {
        "id": 'ks4-oxidation-reduction-e07',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the change that is described as reduction in terms of '
                'electrons.',
        "options": [
            'Loss of electrons by a substance',
            'Sharing of a pair of electrons between two atoms that react together',
            'Gain of electrons by a substance',
            'Movement of electrons in a wire',
        ],
        "correct_index": 2,
        "why": 'Reduction Is Gain of electrons, which is the RIG half of OIL RIG.',
    },
    {
        "id": 'ks4-oxidation-reduction-e08',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what an oxidising agent does in a reaction.',
        "options": [
            'It gives electrons to another substance, or takes its oxygen',
            'It lowers the energy needed before the reaction can start',
            'It stays unchanged while making another substance react faster',
            'It takes electrons from another substance, or gives oxygen to it',
        ],
        "correct_index": 3,
        "why": 'An oxidising agent causes oxidation in something else, by taking its '
               'electrons or handing it oxygen.',
    },
    {
        "id": 'ks4-oxidation-reduction-e09',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the substance from this list that is commonly used as a '
                'reducing agent.',
        "options": [
            'Carbon monoxide',
            'Chlorine',
            'Hydrogen peroxide',
            'Oxygen',
        ],
        "correct_index": 0,
        "why": 'Carbon monoxide donates electrons and removes oxygen, which is what a '
               'reducing agent does; the other three are oxidising agents.',
    },
    {
        "id": 'ks4-oxidation-reduction-e10',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what the term redox tells you about a reaction.',
        "options": [
            'Only reduction takes place in it',
            'Oxidation and reduction both take place in it',
            'It can be reversed again by adding water, because every redox reaction is two-way',
            'It gives out heat to the surroundings as it proceeds',
        ],
        "correct_index": 1,
        "why": 'Redox is short for reduction and oxidation, and the two changes always '
               'happen together in the same reaction.',
    },
    {
        "id": 'ks4-oxidation-reduction-e11',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium ribbon is burned in air and the white powder formed has a '
                'greater mass than the ribbon. Name the change the magnesium has '
                'undergone.',
        "options": [
            'Reduction, because the magnesium lost electrons',
            'Neutralisation, because a white solid formed',
            'Oxidation, because the magnesium has gained oxygen',
            'Thermal decomposition, because the heat has broken the ribbon down',
        ],
        "correct_index": 2,
        "why": 'The extra mass is the oxygen that has joined the magnesium, and gain '
               'of oxygen is oxidation.',
    },
    {
        "id": 'ks4-oxidation-reduction-e12',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A potassium atom changes into a potassium ion, K+. State whether the '
                'potassium has been oxidised or reduced.',
        "options": [
            'Reduced, because it has lost one electron',
            'Oxidised, because it has gained a proton, and gaining a particle is oxidation',
            'Reduced, because its overall charge has become positive',
            'Oxidised, because it has lost one electron',
        ],
        "correct_index": 3,
        "why": 'A neutral atom becoming a 1+ ion must have lost one electron, and loss '
               'of electrons is oxidation.',
    },
    {
        "id": 'ks4-oxidation-reduction-s05',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Hydrogen is passed over hot copper(II) oxide: CuO + H2 → Cu + H2O. '
                'Identify the substance that has been reduced.',
        "options": [
            'The copper(II) oxide, because it has lost its oxygen',
            'The hydrogen, because it has joined up with the oxygen',
            'The water, because it is the new substance that forms',
            'The copper, because it has been heated strongly in the tube',
        ],
        "correct_index": 0,
        "why": 'The copper(II) oxide ends as copper, so it has lost oxygen, and loss of '
               'oxygen is reduction.',
    },
    {
        "id": 'ks4-oxidation-reduction-s06',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron(III) oxide is heated with carbon monoxide: Fe2O3 + 3CO → 2Fe + '
                '3CO2. State what happens to the carbon monoxide in terms of oxygen.',
        "options": [
            'It is reduced, because its job is to reduce the iron oxide',
            'It is oxidised, because each molecule gains an oxygen atom',
            'It is unchanged, because it merely carries the iron away',
            'It is reduced, because it ends up as carbon dioxide gas',
        ],
        "correct_index": 1,
        "why": 'Each CO molecule picks up one oxygen atom to become CO2, and gain of '
               'oxygen is oxidation.',
    },
    {
        "id": 'ks4-oxidation-reduction-s07',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A black mixture of copper(II) oxide and carbon is heated, and a '
                'pink-brown metal appears. State which substance in the mixture is the '
                'reducing agent.',
        "options": [
            'The copper(II) oxide, because it hands its own oxygen over',
            'The carbon dioxide, because it forms as the reaction finishes off',
            'The carbon, because it removes oxygen from the copper(II) oxide',
            'The copper, because it is the metal that is set free here',
        ],
        "correct_index": 2,
        "why": 'The carbon takes the oxygen from the copper(II) oxide, so it causes the '
               'reduction and is the reducing agent.',
    },
    {
        "id": 'ks4-oxidation-reduction-s08',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why hydrogen is called a reducing agent even though the '
                'hydrogen itself is oxidised.',
        "options": [
            'Because hydrogen is oxidised first and is then reduced again by the end of the reaction',
            'Because the name describes the reduction in hydrogen\'s own mass',
            'Because the words oxidised and reduced mean the same thing for a gas',
            'Because an agent is named after what it does to the other substance',
        ],
        "correct_index": 3,
        "why": 'An agent is named for the change it causes, not the change it suffers, '
               'so a reducing agent reduces something else and is oxidised itself.',
    },
    {
        "id": 'ks4-oxidation-reduction-s09',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium burns in chlorine: Mg + Cl2 → MgCl2. Explain why this is '
                'still called a redox reaction when no oxygen is involved.',
        "options": [
            'Because electrons are transferred: magnesium loses them and chlorine gains them',
            'Because chlorine behaves in just the same way as oxygen does in every reaction',
            'Because two elements react together, and that is always called redox',
            'Because the magnesium is broken down into much smaller particles',
        ],
        "correct_index": 0,
        "why": 'The electron definition does not need oxygen: magnesium is oxidised as '
               'it loses electrons and chlorine is reduced as it gains them.',
    },
    {
        "id": 'ks4-oxidation-reduction-s10',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium is put into copper(II) sulfate solution: Mg + CuSO4 → MgSO4 '
                '+ Cu. Identify the substance that has been oxidised.',
        "options": [
            'The copper(II) sulfate, because the copper leaves the solution behind',
            'The magnesium, because each atom gives away two electrons',
            'The sulfate ions, because they move across from one metal to the other',
            'The copper, because it appears as a fresh brown solid on the metal',
        ],
        "correct_index": 1,
        "why": 'Each magnesium atom loses two electrons to become Mg2+, and loss of '
               'electrons is oxidation.',
    },
    {
        "id": 'ks4-oxidation-reduction-s11',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron filings are stirred into copper(II) sulfate solution. State what '
                'happens to the sulfate ions during the reaction.',
        "options": [
            'They are oxidised, because they change partner from copper to iron',
            'They are reduced, because they gain electrons from the iron filings',
            'They are neither oxidised nor reduced, because they are unchanged',
            'They are oxidised, because the solution loses its blue colour as they react',
        ],
        "correct_index": 2,
        "why": 'The sulfate ions are spectator ions: they are 2- before and after, so '
               'they neither gain nor lose electrons.',
    },
    {
        "id": 'ks4-oxidation-reduction-s12',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Bromine solution is added to potassium iodide solution: Br2 + 2KI → '
                '2KBr + I2. Identify the species that has been reduced.',
        "options": [
            'The iodide ions, because they lose their charge',
            'The potassium ions, because they end up with a brand new partner',
            'The iodine, because it colours the solution',
            'The bromine, because each atom gains an electron',
        ],
        "correct_index": 3,
        "why": 'Each bromine atom gains one electron to become a bromide ion, and gain '
               'of electrons is reduction.',
    },
    {
        "id": 'ks4-oxidation-reduction-s13',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Rusting is a redox reaction. State what happens to the oxygen from the '
                'air as an iron gate rusts.',
        "options": [
            'It is reduced, because it gains electrons from the iron',
            'It is oxidised, because it joins a new compound',
            'It is unchanged, because it simply sticks to the surface of the iron',
            'It is oxidised, because rust is named after oxygen',
        ],
        "correct_index": 0,
        "why": 'The oxygen takes electrons from the iron to become oxide ions, so the '
               'oxygen is reduced while the iron is oxidised.',
    },
    {
        "id": 'ks4-oxidation-reduction-s14',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In respiration, glucose reacts with oxygen to form carbon dioxide and '
                'water. State which substance has been oxidised.',
        "options": [
            'The water, because it contains oxygen atoms',
            'The glucose, because it gains oxygen during the reaction',
            'The carbon dioxide, because it is the substance left holding the oxygen',
            'The oxygen, because the word oxidised is named after it, so the oxygen must be the part oxidised',
        ],
        "correct_index": 1,
        "why": 'The glucose gains oxygen as it is converted to carbon dioxide and '
               'water, and gain of oxygen is oxidation.',
    },
    {
        "id": 'ks4-oxidation-reduction-s15',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In photosynthesis, carbon dioxide is converted into glucose. State '
                'what has happened to the carbon dioxide.',
        "options": [
            'It has been oxidised, because it is built into a much larger molecule',
            'It has been neutralised, because carbon dioxide is an acidic gas',
            'It has been reduced, because oxygen has been taken away from it',
            'It has been oxidised, because sunlight adds energy to the molecule',
        ],
        "correct_index": 2,
        "why": 'Glucose holds less oxygen per carbon atom than carbon dioxide does, so '
               'the carbon dioxide has lost oxygen and been reduced.',
    },
    {
        "id": 'ks4-oxidation-reduction-s16',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student says copper(II) oxide is reduced because its mass falls when '
                'it is heated with carbon. Explain why the word reduction does not mean '
                'this.',
        "options": [
            'Reduction means the solid becomes a fine powder rather than staying as one single lump',
            'Reduction means the temperature of the mixture falls as it reacts',
            'Reduction means the amount of the substance present becomes smaller',
            'Reduction means losing oxygen or gaining electrons, not losing mass',
        ],
        "correct_index": 3,
        "why": 'The mass does fall, but that is a consequence: reduction is defined as '
               'loss of oxygen or gain of electrons.',
    },
    {
        "id": 'ks4-oxidation-reduction-s17',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the number of electrons lost in a redox reaction must '
                'equal the number gained.',
        "options": [
            'Because electrons cannot be created or destroyed, so each one lost has to be gained elsewhere',
            'Because the two substances must start with the same number of electrons',
            'Because each substance has to end the reaction with no overall charge',
            'Because oxidation happens first and reduction then copies it exactly',
        ],
        "correct_index": 0,
        "why": 'Electrons are only passed from one substance to another, so the number '
               'lost by one is exactly the number gained by the other.',
    },
    {
        "id": 'ks4-oxidation-reduction-s18',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium burns in oxygen: 2Mg + O2 → 2MgO. Determine the total number '
                'of electrons transferred.',
        "options": [
            'Two electrons',
            'Four electrons',
            'Six electrons',
            'Eight electrons',
        ],
        "correct_index": 1,
        "why": 'Two magnesium atoms each lose two electrons, so four electrons in total '
               'pass to the two oxygen atoms.',
    },
    {
        "id": 'ks4-oxidation-reduction-s19',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In the reaction SnO2 + 2H2 → Sn + 2H2O, identify the oxidising agent.',
        "options": [
            'The hydrogen, because it supplies the electrons',
            'The water, because it holds the oxygen at the end',
            'The tin(IV) oxide, because it gives its oxygen to the hydrogen',
            'The tin, because it is the metal in the reaction',
        ],
        "correct_index": 2,
        "why": 'The tin(IV) oxide hands its oxygen to the hydrogen, so it causes the '
               'oxidation and is itself reduced to tin.',
    },
    {
        "id": 'ks4-oxidation-reduction-s20',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Chlorine is bubbled through colourless potassium bromide solution and '
                'the solution turns orange. State the role of the chlorine.',
        "options": [
            'It is the reducing agent, because it releases the bromine in the salt',
            'It is a catalyst, because it speeds the colour change up',
            'It is the solvent, because the bromine formed dissolves in it',
            'It is the oxidising agent, because it takes electrons from bromide ions',
        ],
        "correct_index": 3,
        "why": 'The chlorine takes an electron from each bromide ion, so the bromide is '
               'oxidised to bromine and the chlorine is the oxidising agent.',
    },
    {
        "id": 'ks4-oxidation-reduction-s21',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper is placed in silver nitrate solution and silver coats the '
                'copper: Cu + 2AgNO3 → Cu(NO3)2 + 2Ag. State what has happened to the '
                'silver ions.',
        "options": [
            'They have been reduced, because each one has gained an electron',
            'They have been oxidised, because they have come out of the solution',
            'They have been neither oxidised nor reduced, because it is only the nitrate that has moved about',
            'They have been oxidised, because a solid holds more oxygen than a solution',
        ],
        "correct_index": 0,
        "why": 'Each Ag+ ion gains one electron from the copper to become a silver '
               'atom, and gain of electrons is reduction.',
    },
    {
        "id": 'ks4-oxidation-reduction-s22',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electron definition of oxidation is more useful than '
                'the oxygen definition.',
        "options": [
            'Because electrons are easier to follow in a reaction than oxygen is',
            'Because it also covers redox reactions in which no oxygen takes part',
            'Because oxygen takes no part in any reaction met in school',
            'Because the oxygen definition applies only to metal oxides',
        ],
        "correct_index": 1,
        "why": 'Reactions such as sodium with chlorine transfer electrons with no '
               'oxygen present, so only the electron definition describes them.',
    },
    {
        "id": 'ks4-oxidation-reduction-s23',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A silver spoon slowly darkens in air as silver sulfide forms on its '
                'surface. Suggest why the silver has been oxidised.',
        "options": [
            'Because the silver has gained electrons from the sulfur in the air',
            'Because oxidation means any change of colour on a metal surface',
            'Because the silver atoms have lost electrons to form silver ions',
            'Because the spoon has gained mass, and a gain in mass is the definition of oxidation',
        ],
        "correct_index": 2,
        "why": 'Silver atoms lose electrons to become Ag+ ions in silver sulfide, and '
               'loss of electrons is oxidation even though no oxygen is involved.',
    },
    {
        "id": 'ks4-oxidation-reduction-s24',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In the reaction 2ZnO + C → 2Zn + CO2, determine which substance has '
                'been reduced and which has been oxidised.',
        "options": [
            'Carbon is reduced and zinc oxide is oxidised',
            'Both the zinc oxide and the carbon are reduced',
            'Zinc oxide is reduced and carbon dioxide is oxidised',
            'Zinc oxide is reduced and carbon is oxidised',
        ],
        "correct_index": 3,
        "why": 'The zinc oxide loses its oxygen so it is reduced, and the carbon gains '
               'that oxygen so it is oxidised.',
    },
    {
        "id": 'ks4-oxidation-reduction-s25',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'No change is seen when a piece of copper is left in zinc sulfate '
                'solution. State what this shows about electron transfer.',
        "options": [
            'No electrons have been transferred, so no redox reaction has happened',
            'Electrons have moved from the copper to the zinc ions, but too slowly to see',
            'Electrons have moved from the zinc ions onto the copper, leaving it unchanged',
            'Electrons have been shared between the copper and the sulfate ions',
        ],
        "correct_index": 0,
        "why": 'Nothing is oxidised and nothing is reduced, so no electrons have passed '
               'between the copper and the zinc ions.',
    },
    {
        "id": 'ks4-oxidation-reduction-s26',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Purple potassium manganate(VII) solution loses its colour as it '
                'oxidises another substance. State what the manganate ions have done in '
                'terms of electrons.',
        "options": [
            'They have lost electrons, because an oxidising agent gives electrons away',
            'They have gained electrons, so they have been reduced',
            'They have kept all of their electrons, because the colour change is physical',
            'They have gained oxygen, because an oxidising agent takes in oxygen',
        ],
        "correct_index": 1,
        "why": 'To oxidise something else the manganate ions must take its electrons, '
               'so they gain electrons and are reduced.',
    },
    {
        "id": 'ks4-oxidation-reduction-h05',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In a teacher demonstration, burning magnesium goes on burning inside a '
                'jar of carbon dioxide: 2Mg + CO2 → 2MgO + C. Deduce which substance '
                'acts as the oxidising agent.',
        "options": [
            'The magnesium, because it is the substance that is burning, and burning is always oxidation',
            'The carbon, because it is set free from the compound as a black solid',
            'The carbon dioxide, because it gives its oxygen to the magnesium',
            'The magnesium oxide, because it holds the oxygen at the end',
        ],
        "correct_index": 2,
        "why": 'The carbon dioxide hands its oxygen to the magnesium, so it oxidises '
               'the magnesium and is itself reduced to carbon.',
    },
    {
        "id": 'ks4-oxidation-reduction-h06',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Steam passed over very hot iron gives hydrogen: 3Fe + 4H2O → Fe3O4 + '
                '4H2. Deduce which species has been reduced.',
        "options": [
            'The iron, because it becomes part of a compound for the first time',
            'The Fe3O4, because it is the product that contains the oxygen',
            'The oxygen in the steam, because it ends up joined to the iron',
            'The hydrogen in the steam, because it loses the oxygen it was joined to',
        ],
        "correct_index": 3,
        "why": 'The hydrogen starts combined with oxygen in water and ends as H2, so it '
               'has lost oxygen and been reduced while the iron was oxidised.',
    },
    {
        "id": 'ks4-oxidation-reduction-h07',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the electron transfer when magnesium reacts with oxygen and '
                'when magnesium reacts with chlorine.',
        "options": [
            'Magnesium loses two electrons in both reactions',
            'Magnesium loses two electrons with oxygen but gains two with chlorine',
            'Magnesium loses two electrons with oxygen and only one with chlorine',
            'Magnesium shares its electrons with chlorine but loses them to oxygen',
        ],
        "correct_index": 0,
        "why": 'Magnesium forms Mg2+ in both MgO and MgCl2, so it loses two electrons '
               'each time and is oxidised in both.',
    },
    {
        "id": 'ks4-oxidation-reduction-h08',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student states that an oxidising agent must contain oxygen. Evaluate '
                'this statement.',
        "options": [
            'Correct, because oxidation is defined by the transfer of oxygen',
            'Incorrect, because chlorine holds no oxygen yet it takes electrons from metals',
            'Correct, because every oxidising agent met in school contains oxygen',
            'Incorrect, because an oxidising agent gives its electrons away instead',
        ],
        "correct_index": 1,
        "why": 'An oxidising agent only has to accept electrons, so chlorine oxidises '
               'metals and bromide ions without any oxygen being present.',
    },
    {
        "id": 'ks4-oxidation-reduction-h09',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Aluminium reacts with chlorine: 2Al + 3Cl2 → 2AlCl3. Determine the '
                'total number of electrons transferred.',
        "options": [
            'Three electrons',
            'Four electrons',
            'Six electrons',
            'Twelve electrons',
        ],
        "correct_index": 2,
        "why": 'Each aluminium atom loses three electrons to form Al3+, so two atoms '
               'release six, which the six chlorine atoms take one each.',
    },
    {
        "id": 'ks4-oxidation-reduction-h10',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron powder is heated in oxygen: 4Fe + 3O2 → 2Fe2O3. Determine the '
                'number of electrons transferred for each unit of Fe2O3 formed.',
        "options": [
            'Three electrons',
            'Nine electrons',
            'Twelve electrons',
            'Six electrons',
        ],
        "correct_index": 3,
        "why": 'Each iron atom loses three electrons to form Fe3+, and one Fe2O3 unit '
               'contains two iron atoms, so six electrons move per unit.',
    },
    {
        "id": 'ks4-oxidation-reduction-h11',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A strip of magnesium left in iron(II) sulfate solution becomes coated '
                'with a dark grey solid. Predict which species has been reduced and '
                'justify the prediction.',
        "options": [
            'The iron(II) ions, because they gain electrons to form iron atoms',
            'The magnesium, because it becomes covered by the new solid',
            'The sulfate ions, because they must take up the spare electrons',
            'The magnesium ions, because they enter the solution as it reacts',
        ],
        "correct_index": 0,
        "why": 'The grey coating is iron, so Fe2+ ions have each gained two electrons '
               'from the magnesium, and gain of electrons is reduction.',
    },
    {
        "id": 'ks4-oxidation-reduction-h12',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'When copper is heated in air it slowly forms black copper(II) oxide. '
                'Explain how the copper can be described as the reducing agent here.',
        "options": [
            'Because it takes oxygen out of the air, which reduces the amount of air',
            'Because it gives electrons to the oxygen, and so reduces the oxygen',
            'Because it turns black, and a darker colour is a sure sign that a metal has been reduced',
            'Because it is reduced itself while the oxygen around it is oxidised',
        ],
        "correct_index": 1,
        "why": 'The copper donates electrons to the oxygen, so the oxygen is reduced to '
               'oxide ions; the copper is the reducing agent and is itself oxidised.',
    },
    {
        "id": 'ks4-oxidation-reduction-h13',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two reactions are 2Ca + O2 → 2CaO and 2K + Br2 → 2KBr. Determine which '
                'of them can be described as redox using the oxygen definition.',
        "options": [
            'The potassium reaction only, because bromine behaves just like oxygen',
            'Both reactions, because a metal reacts with a non-metal in each case',
            'The calcium reaction only, because the potassium reaction has no oxygen',
            'Neither reaction, because the oxygen definition cannot be used for metals',
        ],
        "correct_index": 2,
        "why": 'Only the calcium reaction involves oxygen; the potassium reaction is '
               'redox but needs the electron definition to show it.',
    },
    {
        "id": 'ks4-oxidation-reduction-h14',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In the thermite reaction, Fe2O3 + 2Al → 2Fe + Al2O3. Determine the '
                'reducing agent and what it becomes.',
        "options": [
            'Iron(III) oxide, which becomes iron metal',
            'Iron, which becomes iron(III) oxide',
            'Aluminium oxide, which becomes aluminium',
            'Aluminium, which becomes aluminium oxide',
        ],
        "correct_index": 3,
        "why": 'The aluminium takes the oxygen from the iron(III) oxide, so it is the '
               'reducing agent and ends up oxidised to aluminium oxide.',
    },
    {
        "id": 'ks4-oxidation-reduction-h15',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student heats copper in air and the mass rises; the black product is '
                'then heated with carbon and the mass falls back. Explain both mass '
                'changes.',
        "options": [
            'Copper is oxidised as oxygen is added, then the oxide is reduced as carbon takes the oxygen away',
            'Copper is reduced as it is heated, and then oxidised again by the carbon',
            'Copper gains carbon in the first step and loses it again in the second',
            'Copper melts in the first step and turns solid again in the second',
        ],
        "correct_index": 0,
        "why": 'The mass rises because oxygen joins the copper, and falls because the '
               'carbon removes that oxygen again, reducing the oxide back to copper.',
    },
    {
        "id": 'ks4-oxidation-reduction-h16',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Hydrogen peroxide removes a stain by oxidising the coloured compound '
                'in it. Deduce what happens to the hydrogen peroxide.',
        "options": [
            'It is oxidised, because it is the oxidising agent in the reaction',
            'It is reduced, because it takes electrons from the coloured compound',
            'It is unchanged, because it lifts the colour away physically',
            'It is neutralised, because removing a colour neutralises the stain',
        ],
        "correct_index": 1,
        "why": 'An oxidising agent accepts electrons from the substance it oxidises, so '
               'the hydrogen peroxide is itself reduced.',
    },
    {
        "id": 'ks4-oxidation-reduction-h17',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A magnesium ribbon of mass 0.36 g is burned completely and the white '
                'product has a mass of 0.60 g. Calculate the mass of oxygen that has '
                'combined with the magnesium.',
        "options": [
            '0.36 g',
            '0.60 g',
            '0.24 g',
            '0.96 g',
        ],
        "correct_index": 2,
        "why": 'The gain in mass is the oxygen added: 0.60 g - 0.36 g = 0.24 g.',
    },
    {
        "id": 'ks4-oxidation-reduction-h18',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Hydrogen reduces 2.00 g of copper(II) oxide and 1.60 g of copper is '
                'left. Calculate the mass of oxygen removed from the copper(II) oxide.',
        "options": [
            '0.20 g',
            '1.60 g',
            '3.60 g',
            '0.40 g',
        ],
        "correct_index": 3,
        "why": 'The oxygen lost is the fall in mass of the solid: 2.00 g - 1.60 g = '
               '0.40 g.',
    },
    {
        "id": 'ks4-oxidation-reduction-h19',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what the reducing agent becomes when copper(II) oxide is '
                'reduced by hydrogen with what it becomes when iron(III) oxide is '
                'reduced by carbon monoxide.',
        "options": [
            'Hydrogen becomes water and carbon monoxide becomes carbon dioxide',
            'Hydrogen becomes water and carbon monoxide becomes carbon',
            'Hydrogen becomes hydrogen ions and carbon monoxide becomes solid carbon',
            'Both of the reducing agents are left unchanged at the end of the reaction',
        ],
        "correct_index": 0,
        "why": 'Each reducing agent is oxidised by the oxygen it removes, so hydrogen '
               'gains oxygen to form water and carbon monoxide forms carbon dioxide.',
    },
    {
        "id": 'ks4-oxidation-reduction-h20',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An aluminium window frame does not corrode away, because a thin layer '
                'of aluminium oxide forms on it. Explain this in terms of oxidation.',
        "options": [
            'The surface aluminium is reduced, and a reduced metal cannot be attacked again',
            'The surface aluminium is oxidised, and the oxide layer keeps oxygen from the metal below',
            'Aluminium cannot be oxidised at all, which is why it is chosen for frames',
            'The oxide layer is oxidised further each day, which is why it stays thin',
        ],
        "correct_index": 1,
        "why": 'The outermost aluminium atoms are oxidised to aluminium oxide, and that '
               'unreactive layer then stops oxygen reaching the aluminium underneath.',
    },
    {
        "id": 'ks4-oxidation-reduction-h21',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what happens to carbon in respiration with what happens to '
                'carbon in photosynthesis.',
        "options": [
            'It is reduced in respiration and oxidised in photosynthesis',
            'It is oxidised in both, because carbon dioxide is formed in each',
            'It is oxidised in respiration and reduced in photosynthesis',
            'It is reduced in both, because carbon is the same element in each',
        ],
        "correct_index": 2,
        "why": 'Respiration turns glucose into carbon dioxide, gaining oxygen, while '
               'photosynthesis turns carbon dioxide into glucose, losing oxygen.',
    },
    {
        "id": 'ks4-oxidation-reduction-h22',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Chlorine kills bacteria in drinking water by oxidising substances '
                'inside their cells. Deduce what happens to the chlorine atoms as it '
                'does so.',
        "options": [
            'They lose electrons and are oxidised to chloride ions',
            'They stay as chlorine molecules, because they act as a catalyst',
            'They join up with the water molecules around them and are oxidised, giving off oxygen gas',
            'They gain electrons and are reduced to chloride ions',
        ],
        "correct_index": 3,
        "why": 'To oxidise something the chlorine must accept electrons from it, so '
               'each chlorine atom is reduced to a chloride ion.',
    },
    {
        "id": 'ks4-oxidation-reduction-h23',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'For 2PbO + C → 2Pb + CO2, one student says the carbon is reduced and '
                'another says the lead(II) oxide is the oxidising agent. Determine '
                'which student is correct.',
        "options": [
            'Only the second student, because lead(II) oxide gives its oxygen away',
            'Only the first student, because carbon ends up combined with oxygen',
            'Both students, because carbon is reduced while the oxide oxidises it',
            'Neither student, because carbon and lead(II) oxide are both oxidised',
        ],
        "correct_index": 0,
        "why": 'The lead(II) oxide gives its oxygen to the carbon, so it is the '
               'oxidising agent, and the carbon is oxidised rather than reduced.',
    },
    {
        "id": 'ks4-oxidation-reduction-h24',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In a reaction between two elements, atoms of element X take electrons '
                'from atoms of element Y. Deduce which element is oxidised and which is '
                'the oxidising agent.',
        "options": [
            'X is oxidised and Y is the oxidising agent',
            'Y is oxidised and X is the oxidising agent',
            'Y is oxidised and Y is also the oxidising agent',
            'X is oxidised and X is also the oxidising agent',
        ],
        "correct_index": 1,
        "why": 'Y loses electrons so Y is oxidised, and X causes that by accepting the '
               'electrons, so X is the oxidising agent.',
    },
    {
        "id": 'ks4-oxidation-reduction-h25',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper(II) oxide is 80% copper by mass. Calculate the mass of copper '
                'obtained when 5.0 g of copper(II) oxide is completely reduced.',
        "options": [
            '0.80 g',
            '5.0 g',
            '4.0 g',
            '6.3 g',
        ],
        "correct_index": 2,
        "why": '80% of 5.0 g is 0.80 x 5.0 = 4.0 g of copper, the other 1.0 g being the '
               'oxygen removed.',
    },
    {
        "id": 'ks4-oxidation-reduction-h26',
        "subtopic_slug": 'oxidation-reduction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Chlorine displaces bromine from potassium bromide solution, but '
                'bromine does not displace chlorine from potassium chloride solution. '
                'Deduce which halogen is the better oxidising agent.',
        "options": [
            'Bromine, because it is displaced and so must hold its electrons more strongly',
            'Both are equally good, because each one is a halogen that forms ions',
            'Neither, because displacement depends on solubility and not on electrons',
            'Chlorine, because it takes electrons from bromide ions but bromine cannot take them from chloride ions',
        ],
        "correct_index": 3,
        "why": 'Chlorine can pull electrons off bromide ions while bromine cannot pull '
               'them off chloride ions, so chlorine is the stronger oxidising agent.',
    },
]
