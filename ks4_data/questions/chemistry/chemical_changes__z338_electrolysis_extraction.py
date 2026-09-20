"""Chemistry · Chemical changes — the MRB-338 expansion for `electrolysis-extraction`.

Two industrial cells and one workshop process, each asked for its reason rather
than its recipe. Aluminium carries the most weight: why carbon reduction is not
an option, what the cryolite is for, which electrode the molten metal collects
at, why the carbon anodes burn away and have to be replaced, and where the
running cost actually goes.

Copper purification is the mirror image — a reactive anode that dissolves, a
cathode that grows, an electrolyte whose concentration barely moves, and a
sludge of unreactive metals worth collecting. Electroplating closes the leaf
with the object as cathode and the plating metal as anode. The vocabulary of
electrodes and ion movement belongs to `electrolysis-principles`; half equations
are written in their own leaf.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-electrolysis-extraction-e05',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the compound that aluminium is extracted from.',
        "options": [
            'Aluminium carbonate',
            'Aluminium chloride',
            'Aluminium sulfate',
            'Aluminium oxide',
        ],
        "correct_index": 3,
        "why": 'The ore is refined to aluminium oxide, and it is that oxide '
               'which is melted and electrolysed.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e06',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the gas released at the anode during aluminium '
                'extraction.',
        "options": [
            'Hydrogen',
            'Oxygen',
            'Carbon monoxide',
            'Chlorine',
        ],
        "correct_index": 1,
        "why": 'Oxide ions travel to the anode and lose electrons there, so '
               'oxygen is the gas first released.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e07',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State which electrode the impure copper is used as during '
                'copper purification.',
        "options": [
            'The cathode, where the pure metal is deposited instead',
            'Neither, since it is simply dissolved in the acid',
            'The anode, where it dissolves into the solution',
            'Both, since two impure rods are used together',
        ],
        "correct_index": 2,
        "why": 'The impure rod is made positive so that its copper atoms lose '
               'electrons and enter the solution as ions.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e08',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the metal used to galvanise steel by electroplating.',
        "options": [
            'Zinc',
            'Tin',
            'Chromium',
            'Silver',
        ],
        "correct_index": 0,
        "why": 'A zinc coat protects the steel beneath it, and galvanising is '
               'the name given to that coating.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e09',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State where the molten aluminium collects in the cell.',
        "options": [
            'On the surface of the melt, where it is skimmed off',
            'At the bottom of the tank, where it is tapped off',
            'Around the graphite anodes that hang down from above',
            'In the pipework leading away from the tank',
        ],
        "correct_index": 1,
        "why": 'Molten aluminium is denser than the melt around it, so it sinks '
               'to the graphite lining and is drawn off there.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e10',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why aluminium cannot be extracted by heating its oxide '
                'with carbon.',
        "options": [
            'Aluminium oxide contains no oxygen for carbon to take',
            'Aluminium oxide will not melt at any workable temperature',
            'Carbon would make the aluminium far too brittle',
            'Aluminium is above carbon in the reactivity series',
        ],
        "correct_index": 3,
        "why": 'Carbon can only take oxygen from a metal less reactive than '
               'itself, and aluminium is more reactive.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e11',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the material that the anodes in the aluminium cell are '
                'made from.',
        "options": [
            'Steel',
            'Graphite',
            'Copper',
            'Cryolite, which is molten',
        ],
        "correct_index": 1,
        "why": 'Graphite conducts, withstands the temperature and is cheap '
               'enough to be replaced as it burns away.',
    },
    {
        "id": 'ks4-electrolysis-extraction-e12',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the purity of the copper obtained by electrolytic '
                'refining.',
        "options": [
            'About 50 per cent',
            'About 80 per cent',
            'Over 95 per cent',
            'Over 99 per cent',
        ],
        "correct_index": 3,
        "why": 'Only copper ions are discharged at the cathode, so the metal '
               'deposited is almost entirely copper.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-electrolysis-extraction-s05',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the graphite anodes in the aluminium cell have to '
                'be replaced regularly.',
        "options": [
            'They dissolve into the melt as aluminium is deposited',
            'They crack because the melt is cooler than the tank',
            'They become coated with a layer of pure aluminium metal',
            'They react with the oxygen made there and burn away',
        ],
        "correct_index": 3,
        "why": 'Hot carbon and the oxygen released at the same electrode react '
               'to make carbon dioxide, so the anode is steadily eaten away.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s06',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the cryolite once the aluminium has been '
                'tapped off.',
        "options": [
            'It is used up and has to be bought again each time',
            'It stays in the cell and is used again',
            'It is burnt off with the carbon anodes',
            'It leaves as a gas along with the oxygen',
        ],
        "correct_index": 1,
        "why": 'Cryolite is only a solvent, so it takes no part in the reaction '
               'and remains in the tank.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s07',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the concentration of copper ions in the electrolyte '
                'hardly changes during refining.',
        "options": [
            'The sulfate ions replace every copper ion that is used',
            'Copper enters the solution at the anode as fast as it leaves at the cathode',
            'The solution is topped up automatically from a tank above',
            'Copper ions are made by the power supply as the current runs',
        ],
        "correct_index": 1,
        "why": 'The reactive anode dissolves at the same rate as the cathode '
               'deposits, so the solution is left in balance.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s08',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how a steel fork is set up to be plated with silver.',
        "options": [
            'Fork as anode, silver as cathode, in silver nitrate solution',
            'Fork as cathode, silver as anode, in silver nitrate solution',
            'Fork as cathode, graphite as anode, in sodium chloride solution',
            'Fork and silver both as cathodes, in dilute sulfuric acid',
        ],
        "correct_index": 1,
        "why": 'Silver ions are deposited at the negative electrode, so the fork '
               'must be the cathode and the silver anode supplies the ions.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s09',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why aluminium is recycled rather than extracted afresh '
                'wherever possible.',
        "options": [
            'Recycling removes the need to melt the metal',
            'Recycled aluminium is stronger than newly extracted metal',
            'The ore has almost entirely run out right across the world',
            'Recycling uses far less energy than electrolysis does',
        ],
        "correct_index": 3,
        "why": 'Melting scrap needs a fraction of the electricity that running '
               'the electrolysis cell demands.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s10',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why copper for electrical cable must be almost pure.',
        "options": [
            'Impurities turn the copper a dull green colour over time',
            'Impurities make the copper melt at a much lower temperature',
            'Impurities make the copper attract moisture out of the air',
            'Impurities raise the resistance and waste energy as heat',
        ],
        "correct_index": 3,
        "why": 'Even small amounts of other metals interrupt the flow of '
               'electrons and lower the conductivity.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s11',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the gas that leaves the aluminium cell once the oxygen has '
                'attacked the hot anodes.',
        "options": [
            'Hydrogen',
            'Carbon monoxide',
            'Carbon dioxide',
            'Water vapour',
        ],
        "correct_index": 2,
        "why": 'The carbon of the anode burns in the oxygen released there, so '
               'carbon dioxide is given off.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s12',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the graphite lining of the steel tank acts as the '
                'cathode.',
        "options": [
            'It is the largest surface in the cell by area',
            'It is the coolest part of the whole tank',
            'It is in contact with the steel outside',
            'It is joined to the negative terminal of the supply',
        ],
        "correct_index": 3,
        "why": 'What makes an electrode a cathode is its connection to the '
               'negative terminal, not its position or size.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s13',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a chromium coating is put on steel taps.',
        "options": [
            'It makes the tap heavier and so harder to knock over accidentally',
            'It gives a hard, bright surface that resists corrosion',
            'It lets the tap conduct electricity to the water inside',
            'It allows the steel underneath to expand more freely',
        ],
        "correct_index": 1,
        "why": 'Electroplating puts a thin layer of a more useful metal over a '
               'cheaper, stronger one underneath.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s14',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the gold and silver present in crude '
                'copper during refining.',
        "options": [
            'They dissolve along with the copper and plate onto the cathode',
            'They are oxidised to their oxides and float on the electrolyte',
            'They stay as metals and settle below the anode',
            'They react with the sulfuric acid and are lost as a gas',
        ],
        "correct_index": 2,
        "why": 'Both are less reactive than copper, so they are not oxidised '
               'and simply drop away as the anode dissolves around them.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s15',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the aluminium cell has to run at about 950 degrees '
                'C rather than at room temperature.',
        "options": [
            'The current will not flow through a cold tank',
            'The aluminium must be hot before it will conduct',
            'The graphite only conducts once it has become red hot',
            'The mixture must be molten for its ions to move',
        ],
        "correct_index": 3,
        "why": 'Electrolysis needs mobile ions, and the oxide and cryolite '
               'mixture provides them only as a melt.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s16',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe the change in mass at the two electrodes when a '
                'nickel spoon is plated with silver.',
        "options": [
            'The silver anode loses mass and the spoon gains it',
            'The silver anode gains mass and the spoon loses it',
            'Both electrodes gain mass as silver is deposited',
            'Both electrodes lose mass into the electrolyte',
        ],
        "correct_index": 0,
        "why": 'Silver atoms leave the anode as ions and are deposited as atoms '
               'on the spoon, so mass moves from one to the other.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s17',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the electricity for an aluminium smelter is often '
                'bought from a hydroelectric station.',
        "options": [
            'Hydroelectric power gives a higher voltage than other sources',
            'Hydroelectric power delivers alternating current, which is needed',
            'Hydroelectric power can be switched on and off very quickly',
            'Hydroelectric power is usually the cheapest supply available',
        ],
        "correct_index": 3,
        "why": 'Electricity is the dominant running cost, so smelters are built '
               'wherever it is cheapest.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s18',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify which metal could be obtained by heating its oxide '
                'with carbon rather than by electrolysis.',
        "options": [
            'Potassium',
            'Calcium',
            'Iron',
            'Magnesium',
        ],
        "correct_index": 2,
        "why": 'Iron is below carbon in the reactivity series, so carbon can '
               'take the oxygen away from it.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s19',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is meant by the anode sludge in a copper refinery.',
        "options": [
            'The impure copper that has fallen off the anode',
            'The unreactive metals that drop below the anode',
            'The sulfate left behind as the acid is used up',
            'The oxide layer that forms on the cathode surface',
        ],
        "correct_index": 1,
        "why": 'Gold, silver and platinum are too unreactive to be oxidised at '
               'the anode, so they gather beneath it.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s20',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a thin plating layer is enough to protect a steel '
                'object.',
        "options": [
            'The coat makes the steel harder all the way through',
            'The coat makes the steel itself much less reactive',
            'The coat carries the current away from the steel beneath',
            'The coat keeps air and water away from the steel',
        ],
        "correct_index": 3,
        "why": 'Corrosion needs oxygen and water at the metal surface, and an '
               'unbroken coat keeps both of them off.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s21',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what would happen to the melting point of aluminium oxide '
                'if no cryolite were used.',
        "options": [
            'It would fall to about 660 degrees C',
            'It would stay at about 950 degrees C',
            'It would rise to about 2050 degrees C',
            'It would not have a melting point at all',
        ],
        "correct_index": 2,
        "why": 'Pure aluminium oxide melts at about 2050 degrees C, which is why '
               'dissolving it in cryolite matters so much.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s22',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what happens to a copper atom at the impure anode.',
        "options": [
            'It gains two electrons and stays put on the anode',
            'It loses two electrons and enters the solution',
            'It joins a sulfate ion and forms copper sulfate',
            'It is carried across to the cathode as a whole atom',
        ],
        "correct_index": 1,
        "why": 'Oxidation at the anode turns copper atoms into copper ions, '
               'which then move through the solution.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s23',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the anode sludge is collected rather than thrown '
                'away.',
        "options": [
            'It would block the drains if it were washed away',
            'It can be melted down and used as fresh anodes',
            'It contains precious metals that help pay for the process',
            'It is needed to keep the electrolyte at the right strength',
        ],
        "correct_index": 2,
        "why": 'Gold, silver and platinum recovered from the sludge offset part '
               'of the cost of refining.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s24',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the cathode in a copper refinery starts as a thin '
                'sheet of pure copper.',
        "options": [
            'It stops the electrolyte attacking the walls',
            'It supplies the copper ions that the solution needs',
            'It gives the depositing copper a clean surface to build on',
            'It is the only metal that conducts in the solution',
        ],
        "correct_index": 2,
        "why": 'Starting from pure copper means nothing else can contaminate '
               'the metal that grows on it.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s25',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the two main running costs of an aluminium smelter.',
        "options": [
            'The ore and the water used for cooling the tanks',
            'The electricity and the replacement anodes',
            'The cryolite and the steel used for the tanks',
            'The transport and the packaging of the metal',
        ],
        "correct_index": 1,
        "why": 'Current has to be supplied continuously and the carbon anodes '
               'are consumed, so both recur day after day.',
    },
    {
        "id": 'ks4-electrolysis-extraction-s26',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why aluminium is so plentiful in the ground yet was '
                'once more costly than gold.',
        "options": [
            'Its ore was almost impossible to find before modern mining',
            'It is common but very reactive, so it was hard to obtain',
            'It rusts quickly, so very little of it survived to be used',
            'It was found only in one country until the last century',
        ],
        "correct_index": 1,
        "why": 'Abundance in the crust says nothing about how easily a metal can '
               'be separated from its compound.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-electrolysis-extraction-h05',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A copper refining cell runs for a week. Determine how the total '
                'mass of the two electrodes together has changed.',
        "options": [
            'It has risen, because copper has been added at the cathode',
            'It has fallen, because copper has left the anode',
            'It is about unchanged, because one gains what the other loses',
            'It has fallen, because some copper is lost to the sludge',
        ],
        "correct_index": 2,
        "why": 'Copper simply moves from one electrode to the other through the '
               'solution, so the pair together stay much the same.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h06',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the aluminium cell cannot use an inert anode that '
                'never needs replacing.',
        "options": [
            'No cheap material yet resists oxygen at 950 degrees C',
            'An inert anode would not conduct the very large current',
            'An inert anode would stop the oxide ions from reaching it',
            'Aluminium would be made impure by an anode that never changed',
        ],
        "correct_index": 0,
        "why": 'Anything standing in hot oxygen at that temperature is attacked, '
               'and graphite is the cheapest material that lasts at all.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h07',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A silver anode loses 1.08 g while a bracelet is plated. '
                'Determine the mass of silver gained by the bracelet.',
        "options": [
            '0.54 g',
            '1.08 g',
            '2.16 g',
            '0.27 g',
        ],
        "correct_index": 1,
        "why": 'Every silver atom that leaves the anode as an ion is deposited '
               'again on the bracelet, so the masses match.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h08',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the electrolyte used for aluminium extraction with the '
                'one used for copper refining.',
        "options": [
            'Both are molten compounds that are kept at a high temperature',
            'Both are solutions of the metal salt in water',
            'Aluminium uses a molten mixture; copper uses a solution',
            'Aluminium uses a solution; copper uses a molten mixture',
        ],
        "correct_index": 2,
        "why": 'Aluminium is too reactive to be deposited from water, so its '
               'oxide is melted, while copper plates happily from solution.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h09',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a manufacturer plates a cheap metal with gold '
                'rather than making the whole object from gold.',
        "options": [
            'A plated object is heavier, which customers prefer',
            'Gold on its own is too soft for the job',
            'Gold cannot be melted and cast into any shape',
            'A thin coat gives the appearance at a fraction of the cost',
        ],
        "correct_index": 3,
        "why": 'Only the surface is seen and handled, so the expensive metal is '
               'needed only as a thin layer.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h10',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why zinc in crude copper ends up in the electrolyte '
                'rather than in the sludge.',
        "options": [
            'Zinc melts at the working temperature and runs away',
            'Zinc is denser than copper, so it sinks into the liquid',
            'Zinc is more reactive than copper, so it is oxidised too',
            'Zinc reacts with the sulfuric acid and dissolves',
        ],
        "correct_index": 2,
        "why": 'Metals above copper lose electrons at the anode and go into '
               'solution, but are not discharged again at the cathode.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h11',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would happen if the aluminium cell were run with '
                'solid aluminium oxide instead of a melt.',
        "options": [
            'The same products would form, but much more slowly',
            'Aluminium would form at the anode instead of the cathode',
            'Almost no current would flow, because the ions cannot move',
            'Oxygen alone would be released, leaving the metal behind',
        ],
        "correct_index": 2,
        "why": 'A solid lattice holds every ion fixed, so there is nothing to '
               'carry charge between the electrodes.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h12',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that the cryolite in the aluminium cell is a '
                'catalyst.',
        "options": [
            'Correct, because it is not used up during the process',
            'Correct, because it lowers the energy that the whole process needs',
            'Wrong, because it is a solvent rather than a rate-changer',
            'Wrong, because a catalyst would have to be a metal',
        ],
        "correct_index": 2,
        "why": 'It does survive unchanged, but its job is to dissolve the oxide '
               'at a workable temperature, not to speed a reaction up.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h13',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why an electroplating works stirs its solution gently '
                'and plates slowly.',
        "options": [
            'Stirring keeps both of the electrodes at the same temperature',
            'Stirring stops the object from floating up in the bath',
            'Slow plating lets the anode dissolve before the cathode grows',
            'A slow, even deposit sticks better than a rough, fast one',
        ],
        "correct_index": 3,
        "why": 'A layer built up slowly from a well-mixed solution is smooth and '
               'adheres, where a rushed one is powdery and flakes.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h14',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine how many electrons are needed at the cathode to make '
                'two aluminium atoms.',
        "options": [
            'Two',
            'Three',
            'Six',
            'Twelve',
        ],
        "correct_index": 2,
        "why": 'Each aluminium ion carries a 3+ charge and needs three '
               'electrons, so two atoms need six between them.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h15',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why copper refining needs far less energy per tonne '
                'than aluminium extraction.',
        "options": [
            'Copper ions carry a smaller charge than aluminium ions do',
            'Copper is refined from a cold solution, not a hot melt',
            'Copper is already a metal before the process begins',
            'Copper conducts electricity better than aluminium does',
        ],
        "correct_index": 1,
        "why": 'No part of the copper cell has to be held at several hundred '
               'degrees, which is where most of the aluminium energy goes.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h16',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the oxygen given off in the aluminium cell is not '
                'collected and sold.',
        "options": [
            'It would be contaminated by the aluminium dust that it carries up with it',
            'It is too dilute to be worth separating from the air',
            'It reacts with the carbon anodes before it can be piped away',
            'It escapes through the graphite lining at the bottom',
        ],
        "correct_index": 2,
        "why": 'The oxygen meets red-hot carbon the moment it is made, so what '
               'leaves the cell is largely carbon dioxide.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h17',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A silver plating bath and an aluminium cell each have an '
                'anode. State how the two anodes behave differently.',
        "options": [
            'Both anodes dissolve into the electrolyte as they work',
            'Both anodes stay unchanged, since both are inert',
            'The aluminium anode releases a gas; the silver anode dissolves',
            'The aluminium anode dissolves; the silver anode releases a gas',
        ],
        "correct_index": 2,
        "why": 'Graphite is inert and discharges oxide ions, while a silver '
               'anode is reactive and supplies fresh ions itself.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h18',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which of these metals must be obtained by electrolysis '
                'of a molten compound.',
        "options": [
            'Lead',
            'Tin',
            'Zinc',
            'Calcium',
        ],
        "correct_index": 3,
        "why": 'Calcium sits above carbon in the reactivity series, so carbon '
               'reduction cannot reach it while the other three are below.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h19',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the same total mass of copper is refined whether '
                'the current is doubled or the time is doubled.',
        "options": [
            'The anode can only dissolve at one fixed rate',
            'The electrolyte limits how much can ever be deposited',
            'Doubling the current halves the time automatically',
            'The charge passed is the same in each case',
        ],
        "correct_index": 3,
        "why": 'Charge is current multiplied by time, and it is charge that '
               'decides how many ions are discharged.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h20',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a smelter keeps its cells running continuously '
                'rather than shutting them down overnight.',
        "options": [
            'Reheating the solidified melt each morning would cost more',
            'The graphite anodes would crack apart as they cooled down',
            'The aluminium would react with air the moment it cooled',
            'The cryolite would evaporate away while the cell was off',
        ],
        "correct_index": 0,
        "why": 'Once a tank of oxide and cryolite freezes, bringing it back to '
               '950 degrees C costs far more than keeping it hot.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h21',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would be deposited at the cathode if the copper '
                'refining cell were run with sodium sulfate solution instead.',
        "options": [
            'Copper, taken from the impure anode as usual',
            'Sodium, since sodium ions are now the only metal ions',
            'Hydrogen, because sodium is far too reactive to be deposited',
            'Nothing, because a solution without copper cannot conduct',
        ],
        "correct_index": 2,
        "why": 'With copper ions absent at the start, the water supplies the '
               'hydrogen ions that are discharged in preference to sodium.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h22',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that electroplating always makes an object '
                'more resistant to corrosion.',
        "options": [
            'Correct, because every plating metal is unreactive',
            'Correct, provided the object underneath is a metal',
            'Wrong, because a broken coat can leave the metal exposed',
            'Wrong, because plating adds no protection of any kind',
        ],
        "correct_index": 2,
        "why": 'Protection depends on the layer staying unbroken; a scratch in a '
               'tin coat, for instance, lets the steel beneath corrode.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h23',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the aluminium tapped from the cell needs no '
                'further refining.',
        "options": [
            'Only aluminium ions are discharged at the cathode',
            'The cryolite filters out every other metal present',
            'The molten metal is skimmed before it is poured out',
            'Impurities burn away in the oxygen above the melt',
        ],
        "correct_index": 0,
        "why": 'The melt is a refined oxide dissolved in cryolite, so there is '
               'nothing else at the cathode to be reduced.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h24',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why recycling aluminium drink cans saves about 95 per '
                'cent of the energy of making new metal.',
        "options": [
            'The cans are already pure, so no ore has to be mined',
            'Recycled cans need no heating of any kind before reuse',
            'Melting the metal needs far less energy than electrolysis',
            'Recycling uses waste heat from other factories nearby',
        ],
        "correct_index": 2,
        "why": 'Aluminium melts at 660 degrees C, while extraction demands both '
               '950 degrees C and a continuous heavy current.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h25',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce what the electrolyte must contain if a spoon is to be '
                'plated with nickel.',
        "options": [
            'Only hydrogen and hydroxide ions',
            'Nickel atoms suspended in water',
            'Nickel ions in solution',
            'Nickel oxide melted to a liquid',
        ],
        "correct_index": 2,
        "why": 'The layer is built from ions discharged at the cathode, so the '
               'solution must supply ions of the plating metal.',
    },
    {
        "id": 'ks4-electrolysis-extraction-h26',
        "subtopic_slug": 'electrolysis-extraction',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the carbon dioxide leaving an aluminium smelter is '
                'counted against the metal as an environmental cost.',
        "options": [
            'It escapes from the cryolite as the cell heats up',
            'It is released by the ore as it is first dug out',
            'It comes from the anodes consumed in making the metal',
            'It is produced when the finished metal is cast into blocks',
        ],
        "correct_index": 2,
        "why": 'Every tonne of aluminium burns away a share of graphite anode, '
               'so that carbon dioxide belongs to the extraction itself.',
    },
]
