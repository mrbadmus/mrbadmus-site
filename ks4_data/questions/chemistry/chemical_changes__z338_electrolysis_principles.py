"""Chemistry · Chemical changes — the MRB-338 expansion for `electrolysis-principles`.

The vocabulary first, because everything downstream depends on it: electrolyte,
electrode, cathode, anode, cation, anion, and which of them is negative. The
single biggest source of lost marks is the sign of the cathode, so it is asked
from several sides — from the terminal it is joined to, from the ion that
travels to it, and from the electron transfer that happens there.

The rest is the condition for conduction. A solid ionic lattice holds its ions
still, a melt or a solution frees them, and a covalent substance has none to
free, so melting sugar changes nothing. Inert against reactive electrodes rounds
the leaf off, with the copper anode as the worked case. Specific products belong
to the molten, aqueous and extraction leaves; half equations are written in
their own.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-electrolysis-principles-e05',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what electrolysis does to a compound.',
        "options": [
            'It joins two compounds into a larger one',
            'It dissolves the compound in warm water',
            'It breaks the compound down using electrical energy',
            'It melts the compound without changing it in any way',
        ],
        "correct_index": 2,
        "why": 'Electrolysis is decomposition driven by an electric current, so '
               'the compound is split into simpler substances.',
    },
    {
        "id": 'ks4-electrolysis-principles-e06',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the positive electrode.',
        "options": [
            'The cathode',
            'The anion',
            'The anode',
            'The cation, which is the positive plate',
        ],
        "correct_index": 2,
        "why": 'The anode is joined to the positive terminal of the supply, '
               'which is why negative ions travel towards it.',
    },
    {
        "id": 'ks4-electrolysis-principles-e07',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the name given to a positively charged ion.',
        "options": [
            'An anion',
            'An isotope',
            'An electron',
            'A cation',
        ],
        "correct_index": 3,
        "why": 'Cations carry a positive charge, and it is the cathode they are '
               'drawn towards.',
    },
    {
        "id": 'ks4-electrolysis-principles-e08',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why solid sodium chloride does not conduct electricity.',
        "options": [
            'It contains no ions until it has been melted',
            'Its ions have lost their charge in the solid',
            'Its ions are held in place and cannot move',
            'It is a covalent compound in the solid state',
        ],
        "correct_index": 2,
        "why": 'Conduction needs charged particles free to move, and a solid '
               'lattice holds every ion in a fixed position.',
    },
    {
        "id": 'ks4-electrolysis-principles-e09',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens at the anode in terms of electrons.',
        "options": [
            'Electrons are gained by the ions arriving there',
            'Electrons are destroyed as the current passes',
            'Electrons are shared between the two electrodes',
            'Electrons are lost by the ions arriving there',
        ],
        "correct_index": 3,
        "why": 'Anions give up electrons to the positive anode, which makes the '
               'anode the site of oxidation.',
    },
    {
        "id": 'ks4-electrolysis-principles-e10',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the two states in which an ionic compound can be '
                'electrolysed.',
        "options": [
            'Solid or gaseous, but not molten',
            'Molten or dissolved',
            'Solid or dissolved',
            'Gaseous or molten',
        ],
        "correct_index": 1,
        "why": 'Melting or dissolving the compound releases the ions from the '
               'lattice so they are free to carry charge.',
    },
    {
        "id": 'ks4-electrolysis-principles-e11',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify a use of electrolysis in industry.',
        "options": [
            'Separating a mixture of two liquids',
            'Extracting aluminium from its ore',
            'Slowing the rusting of a steel beam',
            'Testing a solution for chloride ions',
        ],
        "correct_index": 1,
        "why": 'Metals above carbon in the reactivity series are obtained by '
               'electrolysis rather than by reduction with carbon.',
    },
    {
        "id": 'ks4-electrolysis-principles-e12',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the name for the reaction in which a particle gains '
                'electrons.',
        "options": [
            'Oxidation',
            'Reduction',
            'Neutralisation',
            'Displacement',
        ],
        "correct_index": 1,
        "why": 'Gain of electrons is reduction, which is why the cathode is the '
               'electrode where reduction happens.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-electrolysis-principles-s05',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why molten lead bromide conducts electricity while the '
                'solid does not.',
        "options": [
            'Melting gives the compound a charge it did not have before',
            'Melting turns the ions into free electrons that can drift',
            'Melting frees the ions so they can move through the liquid',
            'Melting splits the compound before any current is passed',
        ],
        "correct_index": 2,
        "why": 'Charge is carried through an electrolyte by moving ions, and '
               'only a melt or a solution lets them move.',
    },
    {
        "id": 'ks4-electrolysis-principles-s06',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what carries the charge through the wires of the external '
                'circuit.',
        "options": [
            'Ions from the electrolyte',
            'Molecules of the solvent',
            'Atoms of the electrode metal',
            'Electrons from the supply',
        ],
        "correct_index": 3,
        "why": 'Ions move only within the electrolyte; in the metal wires the '
               'current is a flow of electrons.',
    },
    {
        "id": 'ks4-electrolysis-principles-s07',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why chloride ions move towards the anode.',
        "options": [
            'They are negative, and opposite charges attract',
            'They are heavier than the metal ions in the melt',
            'They are pushed there by the flow of electrons',
            'They are negative, and like charges attract',
        ],
        "correct_index": 0,
        "why": 'A chloride ion carries a negative charge, so it is pulled '
               'towards the positively charged anode.',
    },
    {
        "id": 'ks4-electrolysis-principles-s08',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what would be seen at the cathode when a metal is '
                'being deposited.',
        "options": [
            'A gas bubbling steadily off the surface',
            'The electrode slowly wearing away and thinning',
            'A solid coating building up on the electrode',
            'A coloured solution forming in a ring around the electrode',
        ],
        "correct_index": 2,
        "why": 'Metal ions reaching the cathode gain electrons and become metal '
               'atoms, which build up as a layer.',
    },
    {
        "id": 'ks4-electrolysis-principles-s09',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the two electrodes must not be allowed to touch each '
                'other.',
        "options": [
            'The current would short-circuit instead of passing through',
            'The electrodes would stick together permanently',
            'The electrolyte would be heated up far too quickly and boil',
            'The ions would stop moving through the liquid altogether',
        ],
        "correct_index": 0,
        "why": 'If they touch, the current takes the easy path between them and '
               'no ions are discharged.',
    },
    {
        "id": 'ks4-electrolysis-principles-s10',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why copper metal conducts electricity without being '
                'decomposed.',
        "options": [
            'It is too good a conductor for decomposition to occur',
            'Its ions are too tightly packed to be pulled apart',
            'It is an element, so there is nothing to decompose',
            'Its delocalised electrons carry the charge, not its ions',
        ],
        "correct_index": 3,
        "why": 'In a metal the current is a flow of electrons through a fixed '
               'lattice, so no substance is broken down.',
    },
    {
        "id": 'ks4-electrolysis-principles-s11',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what happens to the mass of product formed if the '
                'current is left running for twice as long.',
        "options": [
            'It roughly doubles',
            'It stays the same',
            'It roughly halves',
            'It falls to zero',
        ],
        "correct_index": 0,
        "why": 'Twice the time passes twice the charge, so about twice as many '
               'ions are discharged at each electrode.',
    },
    {
        "id": 'ks4-electrolysis-principles-s12',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify which substance could not act as an electrolyte.',
        "options": [
            'Molten potassium iodide',
            'Copper sulfate solution',
            'Sodium chloride solution',
            'Molten candle wax',
        ],
        "correct_index": 3,
        "why": 'Wax is covalent and holds no ions, so melting it gives nothing '
               'that can carry charge.',
    },
    {
        "id": 'ks4-electrolysis-principles-s13',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the name of the electrode at which oxidation takes place.',
        "options": [
            'The cathode',
            'The anode',
            'Both electrodes equally',
            'Neither electrode',
        ],
        "correct_index": 1,
        "why": 'Oxidation is loss of electrons, and it is at the anode that '
               'ions give their electrons up.',
    },
    {
        "id": 'ks4-electrolysis-principles-s14',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why graphite is chosen for the electrodes in a school '
                'electrolysis.',
        "options": [
            'It has a very low melting point, so it is easy to shape',
            'It dissolves slowly and replaces the ions that are used up',
            'It conducts electricity and does not react with the electrolyte',
            'It attracts both kinds of ion equally towards its surface',
        ],
        "correct_index": 2,
        "why": 'Graphite carries the current because of its delocalised '
               'electrons, and it takes no part in the reaction itself.',
    },
    {
        "id": 'ks4-electrolysis-principles-s15',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what is meant by a reactive electrode.',
        "options": [
            'One that is made of a non-metal rather than a metal',
            'One that reacts with the air above the electrolyte',
            'One that must be replaced after every single use',
            'One that takes part in the reaction at its surface',
        ],
        "correct_index": 3,
        "why": 'A reactive electrode is itself changed — a copper anode, for '
               'instance, dissolves as the current passes.',
    },
    {
        "id": 'ks4-electrolysis-principles-s16',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the direction in which magnesium ions travel in molten '
                'magnesium chloride.',
        "options": [
            'Towards the anode, which is positive',
            'Towards the cathode, which is negative',
            'Towards whichever electrode is nearer',
            'They stay still while the chloride ions move',
        ],
        "correct_index": 1,
        "why": 'A magnesium ion carries a 2+ charge, so it is attracted to the '
               'negative electrode.',
    },
    {
        "id": 'ks4-electrolysis-principles-s17',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a lamp in the circuit lights only once the solid '
                'ionic compound has melted.',
        "options": [
            'The melt lets ions move, so the circuit is completed',
            'The melt is hotter, so the wires conduct more easily',
            'The melt is a metal, and metals conduct electricity',
            'The melt has a lower resistance than the hot wires',
        ],
        "correct_index": 0,
        "why": 'Until the ions can move there is no path for charge through the '
               'compound, so no current flows anywhere in the circuit.',
    },
    {
        "id": 'ks4-electrolysis-principles-s18',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the electrons that leave the anode.',
        "options": [
            'They pass through the electrolyte to the cathode',
            'They stay on the anode and build up a charge',
            'They travel round the circuit to the cathode',
            'They are used up and do not go anywhere',
        ],
        "correct_index": 2,
        "why": 'The external circuit carries them from anode to supply and on to '
               'the cathode, where other ions collect them.',
    },
    {
        "id": 'ks4-electrolysis-principles-s19',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electrolysis of a molten compound needs a great '
                'deal of energy.',
        "options": [
            'The current has to pass through a solid before the melt',
            'The ions must be created from atoms before they can move',
            'The electrodes must be heated separately from the melt',
            'The compound must be kept molten as well as being decomposed',
        ],
        "correct_index": 3,
        "why": 'Energy goes both into holding the compound above its melting '
               'point and into driving the decomposition itself.',
    },
    {
        "id": 'ks4-electrolysis-principles-s20',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the electrode that gains mass when a spoon is being '
                'electroplated.',
        "options": [
            'The anode',
            'The cathode',
            'Both of them, by the same amount',
            'Neither of them',
        ],
        "correct_index": 1,
        "why": 'The object being plated is the cathode, and metal ions are '
               'deposited on it as they gain electrons.',
    },
    {
        "id": 'ks4-electrolysis-principles-s21',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what happens to a bromide ion when it reaches the '
                'anode.',
        "options": [
            'It gains an electron and becomes a bromine atom',
            'It loses an electron and becomes a bromine atom',
            'It keeps its charge and joins to the electrode',
            'It gains a proton and becomes hydrogen bromide',
        ],
        "correct_index": 1,
        "why": 'The extra electron that made it an ion is handed to the anode, '
               'leaving a neutral atom that pairs up into a molecule.',
    },
    {
        "id": 'ks4-electrolysis-principles-s22',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why platinum is sometimes used instead of graphite for '
                'electrodes.',
        "options": [
            'It is cheaper to buy than graphite of the same size',
            'It is unreactive and does not crumble as graphite can',
            'It reacts with the electrolyte and speeds the process',
            'It conducts heat better, so the melt stays warmer',
        ],
        "correct_index": 1,
        "why": 'Platinum is inert and mechanically strong, though its cost keeps '
               'graphite as the usual school choice.',
    },
    {
        "id": 'ks4-electrolysis-principles-s23',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what happens to the current if the power supply is '
                'switched from 6 V to 12 V.',
        "options": [
            'It rises, so the products form more quickly',
            'It falls, so the products form more slowly',
            'It stays the same, because the ions are unchanged',
            'It drops to zero, because the voltage is too high',
        ],
        "correct_index": 0,
        "why": 'A larger potential difference drives a larger current, so more '
               'ions are discharged in a given time.',
    },
    {
        "id": 'ks4-electrolysis-principles-s24',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what the word electrolyte means when applied to a car '
                'battery.',
        "options": [
            'The metal plates that carry the current',
            'The liquid whose ions carry the current',
            'The casing that holds the whole cell together',
            'The wire joining the battery to the engine',
        ],
        "correct_index": 1,
        "why": 'An electrolyte is always the ionic conductor, whether it is a '
               'melt, a salt solution or the acid in a cell.',
    },
    {
        "id": 'ks4-electrolysis-principles-s25',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why no products form if the supply is disconnected, '
                'even though the ions are still free to move.',
        "options": [
            'The ions recombine into the original solid at once',
            'The electrodes lose their ability to conduct charge',
            'The electrolyte cools and the ions stop moving',
            'There is no charge on the electrodes to attract the ions',
        ],
        "correct_index": 3,
        "why": 'Without a potential difference the ions simply drift at random '
               'and nothing is discharged at either electrode.',
    },
    {
        "id": 'ks4-electrolysis-principles-s26',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the type of particle that is discharged at the cathode.',
        "options": [
            'A negative ion',
            'A positive ion',
            'A neutral atom',
            'A free electron',
        ],
        "correct_index": 1,
        "why": 'Positive ions are drawn to the negative cathode, where they '
               'collect electrons and become neutral.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-electrolysis-principles-h05',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why an aluminium ion needs three electrons at the '
                'cathode while a sodium ion needs one.',
        "options": [
            'The aluminium ion is larger, so it holds more electrons',
            'The aluminium ion carries a 3+ charge and sodium only 1+',
            'Aluminium is lower in the reactivity series than sodium',
            'Aluminium atoms are heavier, so they need more charge',
        ],
        "correct_index": 1,
        "why": 'The number of electrons gained must cancel the charge on the '
               'ion exactly, leaving a neutral atom.',
    },
    {
        "id": 'ks4-electrolysis-principles-h06',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student connects the electrodes the wrong way round. Predict '
                'what happens to the products.',
        "options": [
            'No products form, because the current cannot flow at all',
            'The same products form, but at the opposite electrodes',
            'The same products form at exactly the same electrodes',
            'Both products form at whichever electrode is nearer',
        ],
        "correct_index": 1,
        "why": 'Swapping the terminals swaps which electrode is positive, so the '
               'ions swap destinations while the chemistry is unchanged.',
    },
    {
        "id": 'ks4-electrolysis-principles-h07',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what happens to a graphite cathode and to a copper '
                'cathode in copper sulfate solution.',
        "options": [
            'Both dissolve, because a cathode always loses material',
            'Only the graphite one gains mass, since copper cannot coat copper',
            'Only the copper one gains mass, because like attracts like',
            'Both gain copper, because deposition does not depend on the metal',
        ],
        "correct_index": 3,
        "why": 'Copper ions are reduced on whatever surface is made negative, so '
               'both cathodes take on a copper layer.',
    },
    {
        "id": 'ks4-electrolysis-principles-h08',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electrolysis of a solution can be carried out '
                'at room temperature but that of a melt cannot.',
        "options": [
            'A solution conducts by electrons rather than by moving ions',
            'A solution contains far more ions than a melt of the same salt',
            'A solution needs no heating to free its ions from the lattice',
            'A solution has already been decomposed before the current flows',
        ],
        "correct_index": 2,
        "why": 'Dissolving separates the ions at ordinary temperatures, while '
               'melting the same compound may need hundreds of degrees.',
    },
    {
        "id": 'ks4-electrolysis-principles-h09',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which statement about a cation is correct.',
        "options": [
            'It has more electrons than protons and moves to the anode',
            'It has fewer electrons than protons and moves to the cathode',
            'It has equal electrons and protons and moves to the cathode',
            'It has fewer protons than electrons and moves to the cathode',
        ],
        "correct_index": 1,
        "why": 'Losing electrons leaves an excess of protons, giving the '
               'positive charge that draws the ion to the negative electrode.',
    },
    {
        "id": 'ks4-electrolysis-principles-h10',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the electrolyte is stirred in some industrial '
                'cells.',
        "options": [
            'To bring fresh ions to the electrodes as they are used up',
            'To stop the two electrodes from touching each other',
            'To keep the temperature of the cell from rising',
            'To mix the two products together before collection',
        ],
        "correct_index": 0,
        "why": 'The liquid next to an electrode is depleted first, so stirring '
               'keeps the supply of ions at the surface high.',
    },
    {
        "id": 'ks4-electrolysis-principles-h11',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why electrolysis is described as a redox process.',
        "options": [
            'Oxygen is added at one electrode and removed at the other',
            'Reduction happens at the cathode and oxidation at the anode',
            'The electrodes are alternately oxidised and then reduced',
            'The electrolyte is reduced while the electrodes are oxidised',
        ],
        "correct_index": 1,
        "why": 'Electrons lost at one electrode are exactly the electrons gained '
               'at the other, so the two half-changes happen together.',
    },
    {
        "id": 'ks4-electrolysis-principles-h12',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A cell is set up with pure water between two graphite '
                'electrodes and almost no current flows. Explain why.',
        "options": [
            'Graphite will not conduct unless it is in contact with a metal',
            'Water is too cold for its ions to be able to move about',
            'Water is covalent and contains very few ions to carry charge',
            'Water has already been decomposed by the air above it',
        ],
        "correct_index": 2,
        "why": 'Only a tiny fraction of water molecules are ionised at any '
               'moment, so there are almost no charge carriers present.',
    },
    {
        "id": 'ks4-electrolysis-principles-h13',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict the effect on the current of dissolving more salt in '
                'the solution being electrolysed.',
        "options": [
            'The current falls, because the ions crowd together and slow down',
            'The current falls, because the solution becomes thicker',
            'The current is unchanged, because the voltage is fixed',
            'The current rises, because more ions can carry charge',
        ],
        "correct_index": 3,
        "why": 'More dissolved ions means more charge carriers between the '
               'electrodes, so more charge flows each second.',
    },
    {
        "id": 'ks4-electrolysis-principles-h14',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that the cathode is positive because it '
                'attracts positive ions.',
        "options": [
            'Correct, since an electrode must share the charge it attracts',
            'Correct, because cations would be repelled by a negative plate',
            'Wrong, because the cathode is negative and attracts cations',
            'Wrong, because the cathode attracts anions rather than cations',
        ],
        "correct_index": 2,
        "why": 'Opposite charges attract, so it is precisely because the cathode '
               'is negative that positive ions travel to it.',
    },
    {
        "id": 'ks4-electrolysis-principles-h15',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine how many electrons pass round the circuit for every '
                'one calcium ion discharged at the cathode.',
        "options": [
            'One electron',
            'Two electrons',
            'Three electrons',
            'Four electrons',
        ],
        "correct_index": 1,
        "why": 'A calcium ion carries a 2+ charge, so two electrons are needed '
               'to turn it into a neutral calcium atom.',
    },
    {
        "id": 'ks4-electrolysis-principles-h16',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the products of an electrolysis are often kept '
                'apart once they have formed.',
        "options": [
            'They would make the electrodes conduct less well over time',
            'They would dissolve back into the electrolyte and be lost',
            'They would react together again and undo the decomposition',
            'They would cool the cell and slow the current down',
        ],
        "correct_index": 2,
        "why": 'The elements made were combined to begin with, so allowing them '
               'to meet simply reverses the change.',
    },
    {
        "id": 'ks4-electrolysis-principles-h17',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the total charge passed when the same current runs for '
                '10 minutes and for 30 minutes.',
        "options": [
            'The same in each case, since the current is the same',
            'Three times as much in the longer run',
            'Twice as much in the longer run',
            'Nine times as much, because the rate rises as well',
        ],
        "correct_index": 1,
        "why": 'Charge is current multiplied by time, so tripling the time '
               'triples the charge and roughly triples the product.',
    },
    {
        "id": 'ks4-electrolysis-principles-h18',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a solution of glucose does not conduct even though '
                'the glucose has dissolved.',
        "options": [
            'Glucose molecules are far too large to move in water',
            'Glucose is an acid, and acids conduct only when concentrated',
            'Glucose reacts with the water and destroys its ions',
            'Glucose dissolves as molecules, so no ions are released',
        ],
        "correct_index": 3,
        "why": 'Dissolving a covalent substance separates molecules, not ions, '
               'so nothing charged is free to move.',
    },
    {
        "id": 'ks4-electrolysis-principles-h19',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce what would happen to the mass of a silver anode used to '
                'plate a ring with silver.',
        "options": [
            'It gains mass as silver is deposited on it',
            'It stays the same, because silver is far too unreactive to dissolve',
            'It loses mass as silver goes into the solution',
            'It gains mass at first and then loses it again',
        ],
        "correct_index": 2,
        "why": 'The anode dissolves to replace the silver ions taken out of '
               'solution at the ring, so its mass falls.',
    },
    {
        "id": 'ks4-electrolysis-principles-h20',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a d.c. supply is described as giving each electrode '
                'a fixed identity.',
        "options": [
            'One terminal stays positive, so one electrode is always the anode',
            'The current is larger, so the electrodes cannot change over',
            'Direct current flows only in the electrolyte, not in the wires',
            'Direct current heats one electrode and cools the other',
        ],
        "correct_index": 0,
        "why": 'Because the polarity never reverses, each ion always travels to '
               'the same electrode and the products stay separated.',
    },
    {
        "id": 'ks4-electrolysis-principles-h21',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why an industrial cell uses electrodes with a very '
                'large surface area.',
        "options": [
            'More surface keeps the electrolyte from evaporating',
            'More surface lowers the voltage the cell needs to run',
            'More surface lets more ions be discharged each second',
            'More surface stops the products from mixing together',
        ],
        "correct_index": 2,
        "why": 'Discharge happens only where an ion meets an electrode, so a '
               'bigger area lets a bigger current be carried.',
    },
    {
        "id": 'ks4-electrolysis-principles-h22',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student says that electrons travel through the electrolyte '
                'from one electrode to the other. Identify the error.',
        "options": [
            'Electrons do cross, but only when the solution is concentrated',
            'No charge crosses the electrolyte, so no reaction takes place',
            'Electrons cross the electrolyte but in the opposite direction',
            'Charge crosses the electrolyte on moving ions, not on electrons',
        ],
        "correct_index": 3,
        "why": 'Electrons travel only in the external wires; inside the liquid '
               'it is the ions that move and carry the charge.',
    },
    {
        "id": 'ks4-electrolysis-principles-h23',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the concentration of an electrolyte falls during '
                'electrolysis with inert electrodes.',
        "options": [
            'Ions are removed as they are discharged into products',
            'Water is added continuously to keep the cell topped up',
            'The electrodes absorb ions and hold them at the surface',
            'The ions combine into larger ions that do not conduct',
        ],
        "correct_index": 0,
        "why": 'Every ion discharged leaves the solution as a product, so the '
               'number of ions left behind steadily falls.',
    },
    {
        "id": 'ks4-electrolysis-principles-h24',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the energy cost of extracting a metal by electrolysis '
                'with that of reducing its oxide using carbon.',
        "options": [
            'Electrolysis is cheaper, because no fuel is burnt in it',
            'They cost about the same, since both require strong heating',
            'Electrolysis costs more, because heating and current are both needed',
            'Carbon reduction costs more, because carbon is scarce',
        ],
        "correct_index": 2,
        "why": 'An electrolytic cell must be kept molten and supplied with '
               'electricity, which is why carbon reduction is used wherever it works.',
    },
    {
        "id": 'ks4-electrolysis-principles-h25',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which pair of substances would both conduct when molten '
                'and both be decomposed.',
        "options": [
            'Sodium chloride and potassium bromide',
            'Sodium chloride and solid sulfur',
            'Copper metal and potassium bromide',
            'Candle wax and copper metal',
        ],
        "correct_index": 0,
        "why": 'Both are ionic, so melting frees their ions and passing a '
               'current splits each into its elements.',
    },
    {
        "id": 'ks4-electrolysis-principles-h26',
        "subtopic_slug": 'electrolysis-principles',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the same cell gives a larger current when the '
                'electrodes are pushed closer together.',
        "options": [
            'The ions are squeezed, so each one carries more charge',
            'The electrodes become more strongly charged as they approach',
            'The electrolyte becomes more concentrated between them',
            'The ions have a shorter distance to travel through the liquid',
        ],
        "correct_index": 3,
        "why": 'A shorter path through the electrolyte means less resistance, so '
               'the same voltage drives a larger current.',
    },
]
