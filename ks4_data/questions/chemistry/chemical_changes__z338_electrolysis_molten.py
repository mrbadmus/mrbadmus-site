"""Chemistry · Chemical changes — the MRB-338 expansion for `electrolysis-molten`.

A melt holds only the ions of the compound itself, so the prediction is a
two-line rule: the metal at the cathode, the non-metal at the anode. The leaf
spends most of its weight making that rule portable — potassium bromide,
calcium chloride, lithium chloride, magnesium oxide, sodium iodide — rather than
repeating the one demonstration.

Lead(II) bromide carries the practical: the solid that will not conduct until it
melts, the grey bead under the negative electrode, the red-brown vapour at the
positive one and the fume cupboard that goes with it. The rest is the cost of
the route — melting points in the hundreds of degrees, and why that expense is
accepted only for metals that carbon cannot reduce. Aqueous solutions, where
water joins in, belong to their own leaf.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-electrolysis-molten-e05',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State which ions are present in a molten ionic compound.',
        "options": [
            'Only the negative ions, since metals stay as atoms',
            'Those from the compound plus hydrogen ions',
            'Those from the compound plus hydroxide ions from water',
            'Only those that came from the compound itself',
        ],
        "correct_index": 3,
        "why": 'There is no water in a melt, so nothing is present except the '
               'compound broken into its own ions.',
    },
    {
        "id": 'ks4-electrolysis-molten-e06',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Molten sodium chloride is electrolysed. Name the element '
                'given off as a gas.',
        "options": [
            'Sodium',
            'Chlorine',
            'Hydrogen',
            'Oxygen',
        ],
        "correct_index": 1,
        "why": 'Chloride ions are negative, so they travel to the anode and lose '
               'electrons to become chlorine gas.',
    },
    {
        "id": 'ks4-electrolysis-molten-e07',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the colour of chlorine gas.',
        "options": [
            'Yellow-green',
            'Red-brown',
            'Deep purple',
            'Bright blue',
        ],
        "correct_index": 0,
        "why": 'Chlorine is a pale yellow-green gas, which is how it is told '
               'apart from brown bromine vapour.',
    },
    {
        "id": 'ks4-electrolysis-molten-e08',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what must be done to solid lead(II) bromide before any '
                'current will pass through it.',
        "options": [
            'It must be dissolved in a little cold water',
            'It must be melted so that its ions can move',
            'It must be ground into a very fine powder',
            'It must be pressed hard against both of the electrodes',
        ],
        "correct_index": 1,
        "why": 'The ions are locked in the lattice while the compound is solid, '
               'and only melting sets them free to carry charge.',
    },
    {
        "id": 'ks4-electrolysis-molten-e09',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Molten aluminium oxide is electrolysed. Name the substance '
                'that collects at the cathode.',
        "options": [
            'Oxygen',
            'Aluminium oxide',
            'Aluminium',
            'Hydrogen',
        ],
        "correct_index": 2,
        "why": 'Aluminium ions are positive, so they are attracted to the '
               'cathode and gain electrons to form the metal.',
    },
    {
        "id": 'ks4-electrolysis-molten-e10',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the approximate melting point of sodium chloride.',
        "options": [
            'About 80 degrees C',
            'About 250 degrees C',
            'About 800 degrees C',
            'About 8000 degrees C',
        ],
        "correct_index": 2,
        "why": 'Sodium chloride melts at about 801 degrees C, which is why '
               'melting it is such an expensive first step.',
    },
    {
        "id": 'ks4-electrolysis-molten-e11',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is seen at the negative electrode during the '
                'electrolysis of molten lead bromide.',
        "options": [
            'A stream of colourless bubbles rising',
            'A silvery bead of molten metal forming',
            'A brown vapour spreading upwards',
            'A white solid crust building up all over the surface',
        ],
        "correct_index": 1,
        "why": 'Lead ions gain electrons there, and at that temperature the lead '
               'that forms is a molten silvery bead.',
    },
    {
        "id": 'ks4-electrolysis-molten-e12',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the compound that could be electrolysed when molten.',
        "options": [
            'Potassium bromide',
            'Solid iodine',
            'Paraffin wax',
            'Liquid ethanol',
        ],
        "correct_index": 0,
        "why": 'Only an ionic compound has ions to free on melting; the other '
               'three are covalent and give none.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-electrolysis-molten-s05',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict the two products of electrolysing molten calcium '
                'chloride.',
        "options": [
            'Calcium at the anode and chlorine at the cathode',
            'Calcium at the cathode and chlorine at the anode',
            'Hydrogen at the cathode and chlorine at the anode',
            'Calcium at the cathode and oxygen at the anode',
        ],
        "correct_index": 1,
        "why": 'The metal ion is positive and goes to the cathode; the chloride '
               'ion is negative and goes to the anode.',
    },
    {
        "id": 'ks4-electrolysis-molten-s06',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the test that would confirm the gas collected at the '
                'anode is chlorine.',
        "options": [
            'It relights a glowing splint held in the gas',
            'It bleaches damp litmus paper held in the gas',
            'It turns limewater a milky white colour',
            'It gives a squeaky pop with a lit splint',
        ],
        "correct_index": 1,
        "why": 'Chlorine bleaches moist indicator paper, which no other common '
               'laboratory gas does.',
    },
    {
        "id": 'ks4-electrolysis-molten-s07',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why no oxygen is produced when molten sodium chloride '
                'is electrolysed.',
        "options": [
            'Oxygen can only be released from a solution, not a melt',
            'Oxygen is produced but dissolves back into the melt',
            'Sodium reacts with any oxygen as soon as it forms',
            'There is no oxide or hydroxide ion in the melt at all',
        ],
        "correct_index": 3,
        "why": 'A melt holds only sodium and chloride ions, so there is no '
               'source of oxygen at either electrode.',
    },
    {
        "id": 'ks4-electrolysis-molten-s08',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict the products of electrolysing molten lithium chloride.',
        "options": [
            'Lithium chloride and hydrogen',
            'Lithium and oxygen',
            'Hydrogen and chlorine',
            'Lithium and chlorine',
        ],
        "correct_index": 3,
        "why": 'Only lithium ions and chloride ions are present, so the '
               'compound simply splits into its two elements.',
    },
    {
        "id": 'ks4-electrolysis-molten-s09',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the lead bromide is held in a crucible rather than '
                'a glass beaker.',
        "options": [
            'The crucible withstands the temperature needed to melt it',
            'The crucible conducts the current into the melt from below',
            'The crucible keeps bromine vapour from escaping upwards',
            'The crucible reacts with the bromine and makes it safe',
        ],
        "correct_index": 0,
        "why": 'Lead bromide melts at a few hundred degrees, which glass could '
               'not be heated to without cracking.',
    },
    {
        "id": 'ks4-electrolysis-molten-s10',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how the mass of an inert anode changes during the '
                'electrolysis of a molten salt.',
        "options": [
            'It rises, because the non-metal collects on its surface',
            'It falls at first and then returns to its starting value',
            'It falls, because the anode dissolves into the melt',
            'It stays the same, because the anode takes no part',
        ],
        "correct_index": 3,
        "why": 'An inert electrode only provides a surface for discharge, so '
               'nothing is added to it or taken from it.',
    },
    {
        "id": 'ks4-electrolysis-molten-s11',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the products must be kept apart once molten sodium '
                'chloride has been electrolysed.',
        "options": [
            'Chlorine would freeze onto the surface of the sodium',
            'Sodium would dissolve into the chlorine gas above it',
            'Sodium and chlorine would react and re-form the salt',
            'The two products would block the flow of the current',
        ],
        "correct_index": 2,
        "why": 'The two elements are highly reactive towards one another, so '
               'letting them meet simply undoes the decomposition.',
    },
    {
        "id": 'ks4-electrolysis-molten-s12',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the metal produced at the cathode is often a '
                'liquid rather than a solid.',
        "options": [
            'The current passing through keeps the metal soft',
            'Metals are always liquid when they are first made',
            'The cell is above the melting point of the metal formed',
            'The metal dissolves in the melt and looks like a liquid',
        ],
        "correct_index": 2,
        "why": 'The compound has to be kept molten, and that temperature is '
               'usually above the melting point of the metal itself.',
    },
    {
        "id": 'ks4-electrolysis-molten-s13',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what is produced at the anode when molten sodium oxide '
                'is electrolysed.',
        "options": [
            'Sodium',
            'Oxygen',
            'Hydrogen',
            'Water vapour',
        ],
        "correct_index": 1,
        "why": 'Oxide ions carry a negative charge, so they move to the anode '
               'and are oxidised to oxygen gas.',
    },
    {
        "id": 'ks4-electrolysis-molten-s14',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why electrolysis, rather than heating with carbon, is '
                'used to obtain potassium.',
        "options": [
            'Potassium melts before the carbon becomes hot enough',
            'Potassium compounds are too cheap to be worth reducing',
            'Carbon would contaminate the potassium with soot',
            'Potassium is above carbon in the reactivity series',
        ],
        "correct_index": 3,
        "why": 'Carbon can only displace a metal below itself in the series, so '
               'a more reactive metal has to be won by electrolysis.',
    },
    {
        "id": 'ks4-electrolysis-molten-s15',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what happens to the bromide ions during the '
                'electrolysis of molten lead bromide.',
        "options": [
            'They gain electrons at the cathode and form bromine',
            'They lose electrons at the anode and form bromine',
            'They stay in the melt and take no part in the change',
            'They join the lead ions and leave as lead bromide vapour',
        ],
        "correct_index": 1,
        "why": 'A bromide ion is negative, so it travels to the anode and is '
               'oxidised there by losing its extra electron.',
    },
    {
        "id": 'ks4-electrolysis-molten-s16',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electrolysis of a molten compound is an '
                'expensive way to obtain a metal.',
        "options": [
            'Only a very small amount of metal can be made at once',
            'The electrodes have to be made of a precious metal',
            'The metal produced has to be purified a second time',
            'Energy is needed to melt the compound and to pass the current',
        ],
        "correct_index": 3,
        "why": 'Both the heating and the electricity are large running costs, '
               'and neither can be avoided.',
    },
    {
        "id": 'ks4-electrolysis-molten-s17',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the ions in the lattice as the compound '
                'melts.',
        "options": [
            'They break apart into atoms that can move freely',
            'They lose their charges and become neutral particles',
            'They keep their charges but are now free to move',
            'They combine into larger groups that carry more charge',
        ],
        "correct_index": 2,
        "why": 'Melting overcomes the forces holding the lattice together '
               'without changing the ions themselves.',
    },
    {
        "id": 'ks4-electrolysis-molten-s18',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict the products of electrolysing molten calcium oxide.',
        "options": [
            'Hydrogen at the cathode and oxygen at the anode',
            'Calcium at the anode and oxygen at the cathode',
            'Calcium carbonate at the cathode and oxygen at the anode',
            'Calcium at the cathode and oxygen at the anode',
        ],
        "correct_index": 3,
        "why": 'The calcium ion is positive and the oxide ion negative, so each '
               'goes to the electrode of opposite sign.',
    },
    {
        "id": 'ks4-electrolysis-molten-s19',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why gloves and a face shield are used when a hot melt is '
                'being electrolysed.',
        "options": [
            'The melt gives off a gas that smells unpleasant',
            'The melt would stain the skin a permanent colour',
            'The melt is hot enough to cause a serious burn',
            'The melt conducts, so it could give an electric shock',
        ],
        "correct_index": 2,
        "why": 'A splash of a liquid at several hundred degrees is the main '
               'hazard, alongside the toxic vapour above it.',
    },
    {
        "id": 'ks4-electrolysis-molten-s20',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a bulb in the circuit glows more brightly as more '
                'of the lead bromide melts.',
        "options": [
            'The bromine produced conducts better than the melt does',
            'The melt becomes hotter, which raises the voltage supplied',
            'The electrodes move closer together as the solid collapses',
            'More ions are free to move, so a larger current flows',
        ],
        "correct_index": 3,
        "why": 'Current through an electrolyte depends on how many ions can '
               'move, and melting steadily frees more of them.',
    },
    {
        "id": 'ks4-electrolysis-molten-s21',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the type of reaction that takes place at the cathode of a '
                'molten salt cell.',
        "options": [
            'Oxidation, because electrons are lost there',
            'Reduction, because electrons are gained there',
            'Neutralisation, because charges are cancelled there',
            'Displacement, because one metal replaces another',
        ],
        "correct_index": 1,
        "why": 'Metal ions collect electrons at the cathode, and gain of '
               'electrons is reduction.',
    },
    {
        "id": 'ks4-electrolysis-molten-s22',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why molten magnesium oxide needs a much higher '
                'temperature than molten sodium chloride.',
        "options": [
            'Its ions carry larger charges, so the lattice is stronger',
            'Its ions are much heavier and so move more slowly',
            'It contains oxygen, which resists being heated',
            'It is a covalent compound rather than an ionic one',
        ],
        "correct_index": 0,
        "why": 'Magnesium is 2+ and oxide is 2-, so the electrostatic '
               'attractions are far stronger than between 1+ and 1- ions.',
    },
    {
        "id": 'ks4-electrolysis-molten-s23',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what would happen if the melt were allowed to cool '
                'and solidify part-way through.',
        "options": [
            'The products would swap over to the opposite electrodes',
            'The current would rise, because the solid is a better conductor',
            'The current would stop, because the ions could no longer move',
            'The reaction would carry on exactly as it was before',
        ],
        "correct_index": 2,
        "why": 'A solid lattice holds the ions in place, so there is nothing '
               'left to carry charge through the compound.',
    },
    {
        "id": 'ks4-electrolysis-molten-s24',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Molten sodium iodide is electrolysed. Name the element '
                'deposited at the negative electrode.',
        "options": [
            'Iodine',
            'Sodium',
            'Hydrogen',
            'Sodium iodide',
        ],
        "correct_index": 1,
        "why": 'The sodium ion is the positive one, so it is drawn to the '
               'cathode and reduced to sodium metal.',
    },
    {
        "id": 'ks4-electrolysis-molten-s25',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the sodium made from molten sodium chloride is '
                'stored under oil.',
        "options": [
            'Oil stops it conducting electricity in storage',
            'Oil keeps it molten so that it can be poured out',
            'Oil keeps it from reacting with air and moisture',
            'Oil dissolves any chlorine still clinging to it',
        ],
        "correct_index": 2,
        "why": 'Sodium is reactive enough to attack water vapour and oxygen, so '
               'it is sealed away from both.',
    },
    {
        "id": 'ks4-electrolysis-molten-s26',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why graphite rather than copper is used for the '
                'electrodes in a molten salt cell.',
        "options": [
            'Graphite melts at the same temperature as the salt does',
            'Graphite conducts better than any metal at high temperature',
            'Graphite survives the temperature and does not react',
            'Graphite attracts the metal ions more strongly than copper',
        ],
        "correct_index": 2,
        "why": 'Graphite stays solid and inert in a melt that would attack or '
               'melt most metals.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-electrolysis-molten-h05',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the ratio of aluminium atoms to oxygen molecules '
                'made when molten aluminium oxide is electrolysed.',
        "options": [
            '2 : 3',
            '4 : 3',
            '1 : 1',
            '3 : 2',
        ],
        "correct_index": 1,
        "why": 'Twelve electrons make four aluminium atoms from 3+ ions and '
               'three oxygen molecules from 2- oxide ions.',
    },
    {
        "id": 'ks4-electrolysis-molten-h06',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the products of electrolysing molten potassium bromide '
                'with those of electrolysing molten potassium oxide.',
        "options": [
            'Both give potassium at the cathode, with bromine or oxygen at the anode',
            'Both give potassium at the anode, with bromine or oxygen at the cathode',
            'The bromide gives potassium but the oxide gives hydrogen instead',
            'Both give the same two products, since the metal is the same',
        ],
        "correct_index": 0,
        "why": 'The cathode product depends on the metal ion and the anode '
               'product on whichever non-metal ion the compound holds.',
    },
    {
        "id": 'ks4-electrolysis-molten-h07',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the same two products are formed whether the '
                'current passed is large or small.',
        "options": [
            'A larger current would also release hydrogen from the melt',
            'A small current leaves the compound whole instead of splitting it up',
            'The ions present decide the products; the current sets only the rate',
            'The size of the current decides which electrode each ion goes to',
        ],
        "correct_index": 2,
        "why": 'Only two kinds of ion are available to discharge, so a bigger '
               'current simply discharges more of them each second.',
    },
    {
        "id": 'ks4-electrolysis-molten-h08',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the electrolysis of molten lead bromide is shown as '
                'a demonstration rather than a class practical.',
        "options": [
            'The lead produced would be sold on rather than thrown away',
            'The apparatus is too costly for a whole class to be given one',
            'The reaction is too slow to be seen in a single lesson',
            'The bromine vapour is toxic and the melt is dangerously hot',
        ],
        "correct_index": 3,
        "why": 'A hot melt and a toxic brown vapour together make it a fume '
               'cupboard job with one careful operator.',
    },
    {
        "id": 'ks4-electrolysis-molten-h09',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine how many chloride ions must be discharged for every '
                'aluminium ion discharged in molten aluminium chloride.',
        "options": [
            'One',
            'Two',
            'Three',
            'Six',
        ],
        "correct_index": 2,
        "why": 'Each aluminium ion takes three electrons, and each chloride ion '
               'supplies one, so three are needed to balance it.',
    },
    {
        "id": 'ks4-electrolysis-molten-h10',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student predicts that molten silicon dioxide would give '
                'silicon and oxygen. Evaluate the prediction.',
        "options": [
            'Correct, because every oxide can be split by a current',
            'Correct, but only once the melt has been cooled a little',
            'Wrong, because silicon dioxide is covalent and has no ions',
            'Wrong, because silicon is below carbon in the reactivity series',
        ],
        "correct_index": 2,
        "why": 'Electrolysis needs mobile ions, and a giant covalent structure '
               'provides none however hot it is made.',
    },
    {
        "id": 'ks4-electrolysis-molten-h11',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the same total charge produces twice as many '
                'sodium atoms as calcium atoms.',
        "options": [
            'Calcium ions travel to the cathode half as quickly as sodium ions',
            'A sodium atom is half the mass of a calcium atom',
            'Sodium is higher in the reactivity series than calcium is',
            'A sodium ion needs one electron and a calcium ion needs two',
        ],
        "correct_index": 3,
        "why": 'The same number of electrons goes twice as far when each ion '
               'being neutralised needs only one of them.',
    },
    {
        "id": 'ks4-electrolysis-molten-h12',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the crucible in a lead bromide demonstration is '
                'stood on a heatproof mat inside a tray.',
        "options": [
            'The tray reflects heat back and keeps the melt liquid',
            'The tray stops the current earthing through the bench',
            'The tray catches the melt if the hot crucible cracks',
            'The tray absorbs the bromine vapour as it drifts down',
        ],
        "correct_index": 2,
        "why": 'Molten lead bromide escaping onto a bench would be both a burn '
               'and a toxic spill, so it is contained.',
    },
    {
        "id": 'ks4-electrolysis-molten-h13',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce the formula of the compound if electrolysing it gives '
                'magnesium and bromine in a 1 : 1 atom-to-molecule ratio.',
        "options": [
            'MgBr',
            'MgBr2',
            'Mg2Br',
            'Mg2Br3',
        ],
        "correct_index": 1,
        "why": 'One magnesium ion at 2+ needs two bromide ions at 1-, and those '
               'two bromides make one bromine molecule.',
    },
    {
        "id": 'ks4-electrolysis-molten-h14',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why electrolysing a molten compound made of just two '
                'elements gives exactly two products at inert electrodes.',
        "options": [
            'Only one kind of ion can reach each of the two electrodes',
            'The compound holds one metal ion and one non-metal ion',
            'Two electrodes must always give two separate products',
            'The current splits evenly between the two halves of the cell',
        ],
        "correct_index": 1,
        "why": 'A binary ionic melt contains just two kinds of ion, so each '
               'electrode has only one candidate to discharge.',
    },
    {
        "id": 'ks4-electrolysis-molten-h15',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the mass lost by the melt with the mass of the two '
                'products collected.',
        "options": [
            'The products weigh more, because gas takes up more space',
            'The products weigh less, because some mass is destroyed',
            'Some mass is lost as energy, so the products weigh less',
            'The two are equal, because mass is conserved overall',
        ],
        "correct_index": 3,
        "why": 'Decomposition rearranges atoms without creating or destroying '
               'any, so the totals match.',
    },
    {
        "id": 'ks4-electrolysis-molten-h16',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why industry electrolyses molten sodium chloride in a '
                'cell that keeps the two electrode compartments apart.',
        "options": [
            'To make sure each electrode receives an equal current',
            'To let each compartment be kept at a different temperature',
            'To stop the sodium and the chlorine meeting and reacting',
            'To allow one product to be made without the other',
        ],
        "correct_index": 2,
        "why": 'Separating the compartments preserves both products, which '
               'would otherwise recombine into the salt they came from.',
    },
    {
        "id": 'ks4-electrolysis-molten-h17',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which molten compound would give a brown vapour at the '
                'anode.',
        "options": [
            'Sodium chloride',
            'Magnesium bromide',
            'Calcium oxide',
            'Potassium iodide',
        ],
        "correct_index": 1,
        "why": 'Only a bromide releases bromine, and bromine vapour is brown; '
               'chlorine is yellow-green and iodine vapour is violet.',
    },
    {
        "id": 'ks4-electrolysis-molten-h18',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the current through the cell falls slowly over a '
                'long run even before the compound runs out.',
        "options": [
            'The products dissolve and block the path of the ions',
            'The electrodes become coated and stop conducting',
            'The melt cools because the reaction takes heat in',
            'Fewer ions are left in the melt as they are discharged',
        ],
        "correct_index": 3,
        "why": 'Every ion discharged leaves the melt as a product, so the number '
               'of charge carriers steadily drops.',
    },
    {
        "id": 'ks4-electrolysis-molten-h19',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a molten compound is sometimes mixed with a second '
                'salt before it is electrolysed.',
        "options": [
            'The mixture melts at a lower temperature, saving energy',
            'The second salt reacts and releases the metal directly',
            'The mixture conducts by electrons rather than by ions',
            'The second salt raises the melting point and steadies the cell',
        ],
        "correct_index": 0,
        "why": 'A mixture of ionic compounds usually melts below either on its '
               'own, which is why cryolite is used with aluminium oxide.',
    },
    {
        "id": 'ks4-electrolysis-molten-h20',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would be seen at each electrode if molten '
                'potassium chloride were electrolysed behind a safety screen.',
        "options": [
            'A pale green gas at the anode and a molten metal at the cathode',
            'A brown vapour at the anode and a grey solid at the cathode',
            'A colourless gas at both of the electrodes at once',
            'A purple vapour at the anode and no change at the cathode',
        ],
        "correct_index": 0,
        "why": 'Chlorine is the yellow-green gas at the anode, and potassium '
               'melts at 63 degrees C so it forms as a liquid.',
    },
    {
        "id": 'ks4-electrolysis-molten-h21',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electrolysis of a melt is described as the '
                'reverse of the reaction that formed the compound.',
        "options": [
            'The elements are put back together rather than split apart',
            'The compound is turned into a different compound altogether',
            'The energy released when it formed is now given out once more',
            'The elements that combined to make it are released again',
        ],
        "correct_index": 3,
        "why": 'Forming the salt released energy as the elements combined, and '
               'electrolysis supplies energy to take them apart again.',
    },
    {
        "id": 'ks4-electrolysis-molten-h22',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the number of electrons transferred in total when '
                'one formula unit of molten calcium chloride is decomposed.',
        "options": [
            'One',
            'Two',
            'Four',
            'Six',
        ],
        "correct_index": 1,
        "why": 'The calcium ion takes two electrons at the cathode, and the two '
               'chloride ions release those same two at the anode.',
    },
    {
        "id": 'ks4-electrolysis-molten-h23',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that a compound which conducts when molten '
                'must be ionic.',
        "options": [
            'Wrong, because some covalent liquids conduct electricity well',
            'Wrong, because melting can create ions in a covalent compound',
            'Correct, because conduction in a melt needs mobile ions',
            'Correct, but only if the compound also dissolves in water',
        ],
        "correct_index": 2,
        "why": 'A melt has no delocalised electrons, so the only way it can '
               'carry charge is with ions that were there already.',
    },
    {
        "id": 'ks4-electrolysis-molten-h24',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the anode gas is piped away rather than allowed to '
                'escape into the room.',
        "options": [
            'The gas would react with the cathode product in the air',
            'The gas would cool the cell down as it rose out of it',
            'The gas is toxic and is often worth collecting and selling',
            'Letting it escape would make the room too humid to work in',
        ],
        "correct_index": 2,
        "why": 'Chlorine and bromine are both harmful to breathe and both are '
               'valuable industrial chemicals.',
    },
    {
        "id": 'ks4-electrolysis-molten-h25',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the temperature needed to electrolyse sodium chloride '
                'as a melt with that needed for a solution of it.',
        "options": [
            'The solution needs the higher temperature of the two',
            'Both need about the same temperature to work properly',
            'The melt needs about 800 degrees C; the solution works cold',
            'Neither needs any heating, because the current warms them',
        ],
        "correct_index": 2,
        "why": 'Dissolving frees the ions at room temperature, while melting the '
               'same salt demands several hundred degrees.',
    },
    {
        "id": 'ks4-electrolysis-molten-h26',
        "subtopic_slug": 'electrolysis-molten',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce what would happen if molten lead bromide were '
                'electrolysed with a lead anode instead of a graphite one.',
        "options": [
            'Bromine would form at the cathode rather than the anode',
            'The anode would stay unchanged, exactly as graphite does',
            'The anode would dissolve, adding lead ions to the melt',
            'No reaction would take place at either of the electrodes',
        ],
        "correct_index": 2,
        "why": 'A reactive electrode takes part itself, so lead atoms lose '
               'electrons and enter the melt as ions.',
    },
]
