"""Chemistry · Chemical changes — the MRB-338 expansion for `reactivity-series`.

The order itself is only four rows' worth of recall, so the weight falls where
the AQA specification puts it: on the EVIDENCE for the order. Reaction vigour
with cold water, with steam, with dilute acid and with oxygen carries the
easier and standard bands, using the metals the course names by name, and
displacement in salt solution carries most of the harder band.

Reactivity as the tendency to form a positive ion is the thread that ties the
three kinds of evidence together, and it gets its own rows rather than being
assumed. The unreactive metals (silver, gold, platinum) are asked through what
they do NOT do and through why that is useful. Extraction is deliberately
absent: it belongs to `extraction-of-metals`, and the electron definition of
oxidation belongs to `oxidation-reduction`.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-reactivity-series-e05',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State which of these four metals is the least reactive: sodium, zinc, '
                'silver, calcium.',
        "options": [
            'Sodium',
            'Zinc',
            'Silver',
            'Calcium',
        ],
        "correct_index": 2,
        "why": 'Silver lies near the bottom of the reactivity series, below copper, while '
               'sodium and calcium are near the top and zinc is in the middle.',
    },
    {
        "id": 'ks4-reactivity-series-e06',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the two products formed when lithium reacts with cold water.',
        "options": [
            'Lithium hydroxide and hydrogen',
            'Lithium oxide and hydrogen gas',
            'Lithium hydroxide and oxygen',
            'Lithium hydride and water',
        ],
        "correct_index": 0,
        "why": 'A metal that reacts with water gives a metal hydroxide and hydrogen, so '
               'lithium + water → lithium hydroxide + hydrogen.',
    },
    {
        "id": 'ks4-reactivity-series-e07',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": "State what a metal's reactivity is a measure of.",
        "options": [
            'How easily it can be bent or scratched',
            'How well it carries an electric current',
            'How high a temperature it melts at',
            'How readily it forms a positive ion',
        ],
        "correct_index": 3,
        "why": 'Reactivity is how readily a metal loses electrons to form a positive ion, '
               'which is why one order predicts water, acid and displacement behaviour alike.',
    },
    {
        "id": 'ks4-reactivity-series-e08',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the general name of the compound formed when a metal reacts with '
                'oxygen.',
        "options": [
            'A metal hydroxide',
            'A metal oxide',
            'A metal carbonate',
            'A metal hydride',
        ],
        "correct_index": 1,
        "why": 'Metal + oxygen → metal oxide, and how fiercely a metal burns in oxygen is one '
               'of the three kinds of evidence for the reactivity order.',
    },
    {
        "id": 'ks4-reactivity-series-e09',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the metal in this list that lies below hydrogen in the reactivity '
                'series: magnesium, zinc, copper, iron.',
        "options": [
            'Magnesium',
            'Zinc',
            'Copper',
            'Iron',
        ],
        "correct_index": 2,
        "why": 'Copper is the only one of the four below hydrogen, which is why it gives no '
               'hydrogen with dilute acid while the other three do.',
    },
    {
        "id": 'ks4-reactivity-series-e10',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the metal that stays bright and untarnished after years in the open '
                'air.',
        "options": [
            'Iron',
            'Gold',
            'Sodium',
            'Magnesium',
        ],
        "correct_index": 1,
        "why": 'Gold is so unreactive that it does not combine with the oxygen or water in '
               'air, whereas iron rusts, magnesium dulls and sodium reacts in seconds.',
    },
    {
        "id": 'ks4-reactivity-series-e11',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens in a displacement reaction between a metal and a salt '
                'solution.',
        "options": [
            'A more reactive metal takes the place of a less reactive one in the compound',
            'Two dissolved compounds swap partners so that an insoluble solid settles out',
            'A compound is broken apart into its elements by a current passed through it',
            'A thin layer of one metal is coated onto another by a current in a solution',
        ],
        "correct_index": 0,
        "why": 'Displacement follows the reactivity order: the metal that forms its positive '
               'ion more readily ends up in the solution.',
    },
    {
        "id": 'ks4-reactivity-series-e12',
        "subtopic_slug": 'reactivity-series',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what is seen when a small piece of sodium is dropped onto cold '
                'water.',
        "options": [
            'It sinks to the bottom and slowly dulls over an hour or so, giving off no '
            'bubbles at all',
            'It stays unchanged until the water is heated close to boiling point',
            'It burns with a bright white flame and leaves a white powder behind',
            'It melts into a ball and fizzes quickly as it moves over the surface',
        ],
        "correct_index": 3,
        "why": 'Sodium is high in the series, so its reaction with cold water is fast enough '
               'to melt the metal and release hydrogen rapidly.',
    },
    {
        "id": 'ks4-reactivity-series-s05',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A clean zinc strip is left in blue copper(II) sulfate solution for an hour. '
                'Describe what is observed.',
        "options": [
            'The blue colour deepens steadily, because the zinc releases more copper ions '
            'into it',
            'The blue colour fades and a brown coating builds up on the strip',
            'A white solid forms and the strip slowly rises to the surface',
            'No change, because zinc is the lower of the two in the series',
        ],
        "correct_index": 1,
        "why": 'Zinc is above copper, so it displaces copper from the solution: copper ions '
               'leave the solution as copper metal and the blue colour fades.',
    },
    {
        "id": 'ks4-reactivity-series-s06',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A copper wire is left standing in colourless silver nitrate solution. '
                'Predict what is observed.',
        "options": [
            'The wire dissolves and the solution stays completely colourless',
            'A black layer of silver oxide coats the wire and no metal forms',
            'No change at all, because silver is the more reactive metal of the two and keeps '
            'its nitrate',
            'Grey crystals of silver grow on the wire and the solution turns blue',
        ],
        "correct_index": 3,
        "why": 'Copper is above silver, so copper displaces it: silver is deposited as metal '
               'while blue copper ions pass into the solution.',
    },
    {
        "id": 'ks4-reactivity-series-s07',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A silver spoon is left standing in copper(II) sulfate solution for a day. '
                'Explain what happens to it.',
        "options": [
            'Nothing at all, because silver is below copper in the reactivity series',
            'The silver displaces the copper, which coats the spoon as a brown-pink layer of '
            'metal',
            'The silver dissolves, since every metal dissolves in a salt solution',
            'The silver turns into silver sulfate and no solid metal is deposited',
        ],
        "correct_index": 0,
        "why": 'Displacement needs the added metal to be the more reactive one, and silver is '
               'below copper, so the spoon is unchanged.',
    },
    {
        "id": 'ks4-reactivity-series-s08',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An iron nail is placed in lead(II) nitrate solution. Predict the products.',
        "options": [
            'Hydrogen gas and iron(II) nitrate solution, with all of the lead left in '
            'solution',
            'Iron(III) oxide on the nail, with the nitrate left unchanged',
            'Iron(II) nitrate solution and grey lead deposited on the nail',
            'No products, because iron cannot displace a metal from a nitrate',
        ],
        "correct_index": 2,
        "why": 'Iron is above lead, so iron takes the place of lead in the salt: iron(II) '
               'nitrate forms in solution and lead appears as a grey solid.',
    },
    {
        "id": 'ks4-reactivity-series-s09',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Three 0.5 g metal samples are each added to excess dilute hydrochloric acid. '
                'P gives 60 cm3 of hydrogen in 20 s, Q gives 60 cm3 in 200 s, and R gives '
                'none in 200 s. Determine the order from most to least reactive.',
        "options": [
            'Q, P, R',
            'R, Q, P',
            'P, R, Q',
            'P, Q, R',
        ],
        "correct_index": 3,
        "why": 'The faster the hydrogen comes off, the more reactive the metal, so P is above '
               'Q, and R gives none at all because it lies below hydrogen.',
    },
    {
        "id": 'ks4-reactivity-series-s10',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why sodium is stored under oil.',
        "options": [
            'Oil stops the sodium from melting, since sodium melts at a temperature below '
            'that of a warm room',
            'Oil dissolves away the oxide layer that would otherwise stop the sodium reacting '
            'with water',
            'Oil stops the sodium reacting with the nitrogen that makes up most of the air '
            'around it',
            'Oil keeps away the air and the water vapour in it, both of which a metal that '
            'high in the series reacts with quickly',
        ],
        "correct_index": 3,
        "why": 'Sodium is high in the reactivity series, so it reacts rapidly with both '
               'oxygen and water vapour and has to be kept out of contact with air.',
    },
    {
        "id": 'ks4-reactivity-series-s11',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why copper, rather than magnesium, is used for the cold water pipes '
                'in a house.',
        "options": [
            'Magnesium is much denser than copper, so pipes made of magnesium would be far '
            'too heavy for the walls of a house to carry',
            'Copper does not react with water, whereas magnesium is above it in the series '
            'and would slowly be eaten away',
            'Copper is the more reactive of the two, so it seals its own surface',
            'Magnesium carries heat away too quickly, so the water would cool',
        ],
        "correct_index": 1,
        "why": 'Copper is below hydrogen and does not react with water at all, so a copper '
               'pipe is not attacked by the water it carries.',
    },
    {
        "id": 'ks4-reactivity-series-s12',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium hardly reacts with cold water but reacts well with steam, while '
                'calcium bubbles in cold water. Explain what this shows about the two metals.',
        "options": [
            'Magnesium is the higher of the two, because it needs the hotter steam, and '
            'needing more heat means being more reactive',
            'They are equally reactive, since both of them react with water somehow',
            'Calcium is the higher of the two, because it reacts with the gentler of the two '
            'forms of water',
            'Neither can be placed, because only a displacement test can order any two metals',
        ],
        "correct_index": 2,
        "why": 'The less vigorous the conditions a metal needs, the more reactive it is, so '
               'reacting with cold water places calcium above magnesium.',
    },
    {
        "id": 'ks4-reactivity-series-s13',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Aluminium sits above zinc in the reactivity series, yet an aluminium pan is '
                'not visibly attacked by water. Suggest why.',
        "options": [
            'Aluminium is in fact below copper in the reactivity series, so the order printed '
            'in most textbooks is wrong',
            'A pan is made of an alloy, and no alloy takes part in any reaction',
            'Aluminium only reacts once it has been heated red hot in a flame',
            'A tough oxide layer forms on the surface and keeps the water away from the '
            'aluminium underneath',
        ],
        "correct_index": 3,
        "why": 'Aluminium really is reactive, but the unreactive oxide layer it forms sticks '
               'to the surface and protects the metal beneath it.',
    },
    {
        "id": 'ks4-reactivity-series-s14',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why gold is used for the contacts inside an electrical plug on '
                'expensive equipment.',
        "options": [
            'Gold is so unreactive that the contact does not corrode, so it keeps conducting '
            'for the life of the equipment',
            'Gold is the best conductor of heat of any metal, so a contact made of gold '
            'cannot overheat',
            'Gold is the softest metal there is, so a contact made of gold moulds '
            'itself to any wire',
            'Gold reacts with the oxygen in the air to form a coat of gold oxide that '
            'conducts well',
        ],
        "correct_index": 0,
        "why": 'A corroded contact conducts badly, and gold is low enough in the reactivity '
               'series that it does not combine with oxygen or water.',
    },
    {
        "id": 'ks4-reactivity-series-s15',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": "A student writes that the fiercer a metal's reaction with water, the lower "
                'down the reactivity series it must be. Explain the error.',
        "options": [
            'The vigour tells you nothing at all, because temperature sets the rate',
            'Only the gas given off matters, and hydrogen is the gas that the metals lower '
            'down give off',
            'It is the wrong way round: the fiercer the reaction, the higher up the metal is',
            'Vigour depends only on how much metal is used, so the order cannot be judged from it',
        ],
        "correct_index": 2,
        "why": 'Reaction vigour is the evidence for the order, and the most vigorous metals '
               'with water, such as potassium and sodium, sit at the top of the series.',
    },
    {
        "id": 'ks4-reactivity-series-s16',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the correctly balanced equation for sodium reacting with cold '
                'water.',
        "options": [
            'Na + H2O → NaOH + H2',
            '2Na + 2H2O → 2NaOH + H2',
            '2Na + 2H2O → 2NaOH + 2H2',
            'Na + 2H2O → Na(OH)2 + H2',
        ],
        "correct_index": 1,
        "why": 'Two sodium atoms and two water molecules give two NaOH units and one H2 '
               'molecule, which balances 2 Na, 4 H and 2 O on each side.',
    },
    {
        "id": 'ks4-reactivity-series-s17',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Lithium burns in oxygen to form lithium oxide, Li2O. Identify the balanced '
                'equation.',
        "options": [
            '4Li + O2 → 2Li2O',
            'Li + O2 → Li2O',
            '2Li + O2 → 2Li2O',
            '4Li + 2O2 → 2Li2O',
        ],
        "correct_index": 0,
        "why": 'Four lithium atoms and one O2 molecule give two Li2O units, balancing 4 Li '
               'and 2 O on each side.',
    },
    {
        "id": 'ks4-reactivity-series-s18',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the equation for the reaction that happens when magnesium is added '
                'to iron(II) sulfate solution.',
        "options": [
            'Fe + MgSO4 → FeSO4 + Mg',
            'Mg + FeSO4 → MgSO4 + Fe',
            '2Mg + FeSO4 → 2MgSO4 + Fe',
            'Mg + FeSO4 → MgSO4 + Fe2',
        ],
        "correct_index": 1,
        "why": 'Magnesium is above iron, so it takes the place of iron in the sulfate, and '
               'the equation already balances one-to-one.',
    },
    {
        "id": 'ks4-reactivity-series-s19',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium fizzes much faster than iron in dilute hydrochloric acid of the '
                'same concentration. Explain what this difference is caused by.',
        "options": [
            'Magnesium is the softer of the two metals, so the acid can cut into its surface '
            'more quickly',
            'Magnesium forms its positive ion more readily than iron does, so it releases '
            'hydrogen from the acid faster',
            'Magnesium is the denser of the two metals, so more of it touches the acid at '
            'once',
            'Magnesium has the lower melting point, so the acid warms its surface more easily',
        ],
        "correct_index": 1,
        "why": 'Reactivity is the tendency to form a positive ion, and magnesium lies above '
               'iron, so its reaction with the same acid is faster.',
    },
    {
        "id": 'ks4-reactivity-series-s20',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Lead shot is stirred into zinc nitrate solution and left. Predict the '
                'outcome.',
        "options": [
            'Zinc coats the lead, because a nitrate always gives up its metal',
            'Lead nitrate forms in the solution and zinc metal settles at the bottom of the '
            'beaker',
            'No reaction, because lead is below zinc in the reactivity series',
            'Both metals dissolve, leaving a colourless mixture of two nitrates',
        ],
        "correct_index": 2,
        "why": 'Lead is the less reactive of the two, so it cannot take the place of zinc in '
               'the salt and nothing happens.',
    },
    {
        "id": 'ks4-reactivity-series-s21',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Tin granules are added to copper(II) sulfate solution. Predict whether a '
                'reaction takes place and name any metal formed.',
        "options": [
            'No reaction, because tin lies below copper in the series',
            'A reaction takes place, and the metal formed is tin, deposited as grey granules',
            'A reaction takes place, and the metal deposited is copper',
            'No reaction, because both metals lie below hydrogen in the series',
        ],
        "correct_index": 2,
        "why": 'Tin is above copper, so tin displaces copper: copper metal is deposited and '
               'tin sulfate is left in solution.',
    },
    {
        "id": 'ks4-reactivity-series-s22',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'When an iron nail is left in copper(II) sulfate solution the liquid changes '
                'from blue to pale green. Explain the change in colour.',
        "options": [
            'Iron ions have replaced the copper ions, and iron(II) sulfate is pale green',
            'The copper sulfate has been diluted by water given out in the reaction',
            'A pale green gas is dissolving in the water as the reaction goes on',
            'Rust from the nail is mixing into the blue solution and is turning it green',
        ],
        "correct_index": 0,
        "why": 'Displacement swaps the metal in solution: blue copper ions are removed as '
               'copper metal and pale green iron(II) ions take their place.',
    },
    {
        "id": 'ks4-reactivity-series-s23',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Zinc granules are stirred into pale green iron(II) sulfate solution. Predict '
                'what happens and name the solution left behind.',
        "options": [
            'Nothing happens, and the iron(II) sulfate solution is left as it was',
            'The zinc dissolves and hydrogen is given off, leaving zinc sulfate',
            'Iron coats the zinc, and a pale green solution of zinc sulfate is left in the '
            'tube',
            'Dark grey iron is deposited, and colourless zinc sulfate is left',
        ],
        "correct_index": 3,
        "why": 'Zinc is above iron, so zinc displaces it: iron is deposited as a dark solid '
               'and the zinc goes into solution as zinc sulfate.',
    },
    {
        "id": 'ks4-reactivity-series-s24',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Four metals are available: zinc, calcium, lead and copper. Identify which '
                'one reacts with cold water, and justify the choice.',
        "options": [
            'Zinc, because it is the only one of the four above hydrogen',
            'Calcium, because it is high in the series, above magnesium',
            'Copper, because it is the heaviest of the four and sinks into the water',
            'Lead, because it is the softest of the four and a soft metal is attacked first',
        ],
        "correct_index": 1,
        "why": 'Only metals above magnesium react at a noticeable rate with cold water, and '
               'of these four only calcium is that high in the series.',
    },
    {
        "id": 'ks4-reactivity-series-s25',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A technician needs a supply of hydrogen and has strips of copper and of '
                'zinc, plus dilute acid. Determine which metal to use and why.',
        "options": [
            'Copper, because a metal below hydrogen releases it most easily',
            'Either metal, because any metal and any acid will give off hydrogen',
            'Copper, because it is unreactive and so will not be used up itself',
            'Zinc, because it is above hydrogen and so displaces it from the acid',
        ],
        "correct_index": 3,
        "why": 'Only a metal above hydrogen in the series can take hydrogen out of an acid, '
               'and zinc is above it while copper is below.',
    },
    {
        "id": 'ks4-reactivity-series-s26',
        "subtopic_slug": 'reactivity-series',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A freshly cut piece of sodium and a freshly cut piece of lead are left on a '
                'bench. The sodium dulls within seconds and the lead over many days. Explain '
                'why.',
        "options": [
            'Sodium is far higher in the series, so it combines with oxygen much faster',
            'Sodium is by far the softer metal, so its surface is scratched away by the air '
            'moving past it',
            'Lead is the heavier metal, so the oxygen in the air cannot lift its surface '
            'layer',
            'Sodium is warmer when it is cut, and a warmer surface always dulls more quickly',
        ],
        "correct_index": 0,
        "why": 'How quickly a freshly cut surface tarnishes is evidence of how readily the '
               'metal reacts with oxygen, and sodium is far above lead in the series.',
    },
    {
        "id": 'ks4-reactivity-series-h05',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Metal X displaces metal Y from Y sulfate solution. Metal Z displaces metal X '
                'from X sulfate solution. Metal Y displaces neither of the others. Determine '
                'the order from most to least reactive.',
        "options": [
            'X, Y, Z',
            'Y, Z, X',
            'X, Z, Y',
            'Z, X, Y',
        ],
        "correct_index": 3,
        "why": 'A metal only displaces one below it, so Z is above X and X is above Y, giving '
               'Z, X, Y.',
    },
    {
        "id": 'ks4-reactivity-series-h06',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Metal J gives no bubbles with dilute hydrochloric acid, but it does displace '
                'silver from silver nitrate solution. Deduce which of platinum, copper, zinc '
                'and magnesium J could be.',
        "options": [
            'Magnesium',
            'Copper',
            'Zinc',
            'Platinum',
        ],
        "correct_index": 1,
        "why": 'No bubbles with acid places J below hydrogen, and displacing silver places it '
               'above silver, and copper is the only one of the four in that gap.',
    },
    {
        "id": 'ks4-reactivity-series-h07',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Lead is added to copper(II) sulfate solution in one beaker and to zinc '
                'sulfate solution in another. Predict which beaker shows a reaction.',
        "options": [
            'Both of them show a reaction',
            'Neither of them shows a reaction',
            'The copper sulfate only',
            'The zinc sulfate only',
        ],
        "correct_index": 2,
        "why": 'Lead is above copper but below zinc, so it displaces copper from its solution '
               'and leaves the zinc solution untouched.',
    },
    {
        "id": 'ks4-reactivity-series-h08',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student argues that platinum must be a very reactive metal, because a '
                'catalytic converter containing it makes exhaust gases react quickly. '
                'Evaluate the argument.',
        "options": [
            'It is wrong: a catalyst speeds a reaction up without being changed itself, and '
            'it is exactly because platinum is unreactive that it survives the hot exhaust',
            'It is wrong, because platinum is not a metal at all, and reactivity is a '
            'property that belongs to metals and to nothing else',
            'It is right, because a substance can only speed a reaction up by taking part in '
            'it and being used up as the reaction goes on',
            'It is right, because the platinum inside a converter is used up quickly and has '
            'to be replaced every few months of driving',
        ],
        "correct_index": 0,
        "why": 'A catalyst is left unchanged at the end, so a converter needs a metal that '
               'does not corrode in hot gases, which is why unreactive platinum is chosen.',
    },
    {
        "id": 'ks4-reactivity-series-h09',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Equal masses of four metals are each added to 25 cm3 of copper(II) sulfate '
                'solution. The temperature rises by 21 degrees C for W, 2 degrees C for X, 11 '
                'degrees C for Y and 0 degrees C for Z. Determine the order from most to '
                'least reactive.',
        "options": [
            'W, X, Y, Z',
            'Z, X, Y, W',
            'Y, W, X, Z',
            'W, Y, X, Z',
        ],
        "correct_index": 3,
        "why": 'The bigger the temperature rise, the more vigorous the displacement, so the '
               'order follows the rises 21, 11, 2 and 0 degrees C.',
    },
    {
        "id": 'ks4-reactivity-series-h10',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An iron nail of mass 4.00 g is left in copper(II) sulfate solution. It is '
                'then washed, dried and found to weigh 4.15 g, with the coating still '
                'attached. Explain the increase in mass.',
        "options": [
            'Water has been absorbed into the surface of the metal while the reaction was '
            'going on',
            'The sulfate ions from the solution have stuck to the outside of the nail',
            'Each iron atom that dissolved has been replaced by a heavier copper atom',
            'Iron gains mass whenever it reacts, because reacting always adds oxygen',
        ],
        "correct_index": 2,
        "why": 'Iron dissolves as iron ions and copper is deposited in its place, and a '
               'copper atom has more mass than an iron atom, so the coated nail weighs more.',
    },
    {
        "id": 'ks4-reactivity-series-h11',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In the same dilute acid, metal A releases 48 cm3 of hydrogen in 30 s and '
                'metal B releases 48 cm3 in 120 s. Calculate how many times faster A reacts.',
        "options": [
            '4 times faster',
            '2 times faster',
            '90 times faster',
            '0.25 times faster',
        ],
        "correct_index": 0,
        "why": 'Both give the same volume, so comparing the times gives 120 s divided by 30 '
               's, which is 4, and the faster metal is the more reactive.',
    },
    {
        "id": 'ks4-reactivity-series-h12',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium powder is heated with copper(II) oxide in one crucible, and copper '
                'powder is heated with magnesium oxide in another. Predict which mixture '
                'reacts.',
        "options": [
            'Both mixtures react',
            'Neither mixture reacts in either crucible',
            'The copper and magnesium oxide',
            'The magnesium and copper oxide',
        ],
        "correct_index": 3,
        "why": 'The more reactive metal takes the oxygen, and magnesium is above copper, so '
               'magnesium removes oxygen from copper oxide but copper cannot do the reverse.',
    },
    {
        "id": 'ks4-reactivity-series-h13',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student sees that both zinc and iron give off bubbles in dilute '
                'hydrochloric acid and concludes that the two metals are equally reactive. '
                'Evaluate the conclusion.',
        "options": [
            'It is sound, because two metals that both give off bubbles in the same dilute '
            'acid are equally reactive',
            'It is unsound, because the bubbles given off by the iron are carbon dioxide and '
            'not hydrogen',
            'It is unsound: both are above hydrogen, but the rates differ, and zinc bubbles '
            'faster than iron, which places zinc higher',
            'It is sound, provided that the same mass of each metal was added to the same '
            'acid',
        ],
        "correct_index": 2,
        "why": 'Reacting at all only shows both metals are above hydrogen; it is the '
               'difference in rate that separates them, and zinc reacts faster than iron.',
    },
    {
        "id": 'ks4-reactivity-series-h14',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a metal keeps the same position in the reactivity series whether '
                'it is judged by its reaction with water, its reaction with acid, or '
                'displacement.',
        "options": [
            'Because water, acid and salt solutions are all liquids that behave alike',
            'Because all three tests are carried out at exactly the same temperature, and '
            'temperature is what decides the order',
            'Because each of the three depends on the same thing: how readily the metal gives '
            'up electrons to form a positive ion',
            'Because the order was fixed by displacement first, and the other two tests are '
            'only ever used to confirm it',
        ],
        "correct_index": 2,
        "why": 'All three reactions require the metal atom to become a positive ion, so one '
               'property sets the order in every case.',
    },
    {
        "id": 'ks4-reactivity-series-h15',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Silver is described as an unreactive metal, yet a silver chain slowly turns '
                'black over several years. Explain whether this contradicts the description.',
        "options": [
            'Yes, because a metal described as unreactive takes part in no reaction of any '
            'kind, whatever it is left in contact with',
            'Yes, because the blackening shows that silver is above hydrogen after all, and '
            'so it cannot be called unreactive',
            'No, because the black layer is dirt picked up from skin and clothing rather than '
            'a new compound formed by a reaction',
            'No, because unreactive here means no reaction with water or dilute acid, and the '
            'blackening is a very slow reaction with traces of gases in the air',
        ],
        "correct_index": 3,
        "why": 'Silver sits below hydrogen and is not attacked by water or dilute acid, and a '
               'reaction slow enough to take years does not move it up the series.',
    },
    {
        "id": 'ks4-reactivity-series-h16',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why reaction with water is of no use for placing copper, silver and '
                'gold in order, and state what is used instead.',
        "options": [
            'None of the three reacts with water at all, so displacement from salt solutions is used',
            'All three react with water at the same rate, so their oxides are compared '
            'instead',
            'Water would dissolve all three metals completely, so their melting points are '
            'compared instead',
            'Each of the three reacts with water far too quickly to be timed, so the reaction '
            'with oxygen is used instead',
        ],
        "correct_index": 0,
        "why": 'Metals below hydrogen give no reaction with water, so there is nothing to '
               'compare, and their order is found by seeing which displaces which from '
               'solution.',
    },
    {
        "id": 'ks4-reactivity-series-h17',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Metal T lies below aluminium but above hydrogen, and does not react with '
                'cold water. Deduce which of sodium, zinc, copper and calcium T could be.',
        "options": [
            'Copper',
            'Zinc',
            'Sodium',
            'Calcium',
        ],
        "correct_index": 1,
        "why": 'Copper is below hydrogen, while sodium and calcium both react with cold '
               'water, so zinc is the only one left that fits all three clues.',
    },
    {
        "id": 'ks4-reactivity-series-h18',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A zinc strip is dipped into three separate solutions: magnesium sulfate, '
                'copper(II) sulfate and iron(II) sulfate. Determine in which of them zinc '
                'reacts.',
        "options": [
            'The copper sulfate and the iron sulfate',
            'The magnesium sulfate and the iron sulfate',
            'The magnesium sulfate and the copper sulfate',
            'All three of the solutions',
        ],
        "correct_index": 0,
        "why": 'Zinc is above both copper and iron, so it displaces each of them, but it is '
               'below magnesium and cannot displace that.',
    },
    {
        "id": 'ks4-reactivity-series-h19',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two metals are compared by timing the bubbles given off in dilute acid, but '
                'one is added as a fine powder and the other as a single lump. Explain why '
                'the comparison cannot settle which metal is more reactive.',
        "options": [
            'Because a powder and a lump of the same metal behave as two chemically different '
            'substances in acid',
            'Because a lump always reacts faster than a powder, so the result is bound to '
            'come out the wrong way round',
            'Because the powder has a far larger surface area, so any difference in rate may '
            'be caused by that rather than by reactivity',
            'Because bubbles cannot be counted accurately enough to compare any two metals '
            'fairly',
        ],
        "correct_index": 2,
        "why": 'Surface area changes the rate on its own, so it has to be kept the same if '
               'the rate is to be evidence about reactivity.',
    },
    {
        "id": 'ks4-reactivity-series-h20',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student puts copper in dilute sulfuric acid, sees no bubbles, and '
                'concludes that copper is the least reactive metal there is. Evaluate the '
                'conclusion.',
        "options": [
            'It is sound, because a metal that will not even react with a dilute acid can '
            'have nothing else at all that is able to attack it',
            'It is unsound, because copper does react with dilute sulfuric acid, only slowly',
            'It is sound, provided the acid was warmed before the copper was added to it',
            'It is unsound: no bubbles only places copper below hydrogen, and silver, gold '
            'and platinum are lower still',
        ],
        "correct_index": 3,
        "why": 'The test separates metals above hydrogen from those below it, and copper, '
               'silver, gold and platinum are all below, so it cannot rank them against each '
               'other.',
    },
    {
        "id": 'ks4-reactivity-series-h21',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium gives 30 cm3 of hydrogen in 5 minutes with cold water, and 30 cm3 '
                'in 10 seconds with steam. Determine what this shows about the position of '
                'magnesium in the reactivity series.',
        "options": [
            'Nothing about its position: the two runs differ in temperature, and a position '
            'is only fixed by comparing metals under the same conditions',
            'That magnesium holds two positions in the series at once, one for its reaction '
            'with cold water and one for its reaction with steam',
            'That magnesium is above calcium, because a metal that reacts with steam is '
            'always above one that reacts with cold water',
            'That magnesium is below copper, because a metal that needs steam must be below '
            'one that needs no heating at all',
        ],
        "correct_index": 0,
        "why": 'Raising the temperature speeds up a reaction without changing the metal, so '
               'these two results compare conditions rather than metals.',
    },
    {
        "id": 'ks4-reactivity-series-h22',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Four metals are available: iron, magnesium, tin and copper. Determine which '
                'one would displace all of the other three from their sulfate solutions.',
        "options": [
            'Iron',
            'Tin',
            'Magnesium',
            'Copper',
        ],
        "correct_index": 2,
        "why": 'Only a metal above all of the others can displace each of them, and magnesium '
               'is the highest of the four in the reactivity series.',
    },
    {
        "id": 'ks4-reactivity-series-h23',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A gold ring and an iron nail are each left in dilute hydrochloric acid for a '
                'week. Predict and explain what is seen in each case.',
        "options": [
            'Both are eaten away, because a week is long enough for any metal to dissolve',
            'The nail slowly bubbles and is partly eaten away; the ring is not attacked at all',
            'The ring is eaten away and the nail is unchanged, because gold is attacked by acid '
            'more easily',
            'Neither changes, because dilute acid is far too weak to attack any solid metal',
        ],
        "correct_index": 1,
        "why": 'Iron lies above hydrogen so it reacts with the acid and releases hydrogen, '
               'while gold lies well below hydrogen and is not attacked at all.',
    },
    {
        "id": 'ks4-reactivity-series-h24',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Potassium reacts more violently with cold water than lithium does. Explain '
                'this difference in terms of what the metal atoms do.',
        "options": [
            'Potassium atoms are heavier than lithium atoms, so they hit the water surface '
            'harder',
            'Potassium atoms have more outer electrons than lithium atoms to give away to the '
            'water',
            'Potassium atoms gain electrons from the water far more easily than lithium atoms '
            'do',
            'Potassium atoms lose an outer electron more readily, so form positive ions '
            'faster',
        ],
        "correct_index": 3,
        "why": 'Reactivity is the tendency to form a positive ion, and potassium loses its '
               'outer electron more readily than lithium, which puts it above lithium in the '
               'series.',
    },
    {
        "id": 'ks4-reactivity-series-h25',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Zinc is stirred into silver nitrate solution, and silver is stirred into '
                'zinc nitrate solution. Determine which mixture reacts and name the metal '
                'deposited.',
        "options": [
            'The zinc in silver nitrate, depositing silver',
            'The silver in zinc nitrate, depositing zinc',
            'Both mixtures react, and a metal is deposited in each of them',
            'Neither mixture reacts, and both metals are left unchanged',
        ],
        "correct_index": 0,
        "why": 'Zinc is the more reactive of the two, so it takes the place of silver in the '
               'nitrate and silver metal is deposited; the reverse cannot happen.',
    },
    {
        "id": 'ks4-reactivity-series-h26',
        "subtopic_slug": 'reactivity-series',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An iron nail is left in copper(II) sulfate solution for two days. Copper '
                'stops being deposited even though most of the nail is still there. Explain '
                'what has been used up.',
        "options": [
            'The copper ions in the solution, every one of which has now been displaced',
            'The sulfate ions in the solution, which carry the copper across to the surface '
            'of the nail',
            'The water, which must be present before the two metals can change places',
            'The iron in the nail, which has all passed into the solution as iron(II) sulfate',
        ],
        "correct_index": 0,
        "why": 'Displacement stops when one reactant runs out, and here the copper ions have '
               'all been turned into copper metal while plenty of iron remains.',
    },
]
