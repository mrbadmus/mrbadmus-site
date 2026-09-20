"""Chemistry · Chemical changes — the MRB-338 expansion for `extraction-of-metals`.

The whole leaf turns on one decision: does the metal sit above or below CARBON in
the reactivity series. Below it, the oxide is reduced by heating with carbon (iron
from haematite, zinc from zinc oxide, copper from malachite); above it, no furnace
temperature will do and electrolysis of a molten compound is the only route.

The weight therefore falls on that rule and on the two places it is applied — the
blast furnace, where the reducing agent is the carbon monoxide rather than the coke
itself, and the alternative routes for ore too poor to smelt. Phytomining and
bioleaching carry the evaluation rows: what each uses, what each produces, and how
speed, cost, ore grade and environmental damage compare with traditional mining.
Data rows work in tonnes of ore, tonnes of iron and kilograms of crop ash, and the
aluminium cell's own apparatus is deliberately left to `electrolysis-extraction`.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-extraction-of-metals-e05',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what a rock must contain before it is called an ore.',
        "options": [
            'Enough of a metal compound to make extracting the metal worthwhile',
            'A metal that has already been melted down, cast into bars and stamped with its purity',
            'Two or more different metals mixed together to give it better properties',
            'A metal held in place by an electric current running through it',
        ],
        "correct_index": 0,
        "why": 'An ore is rock containing a metal compound in a high enough '
               'proportion for extraction to be worth the cost.',
    },
    {
        "id": 'ks4-extraction-of-metals-e06',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the industrial process in which a metal oxide is heated with '
                'carbon to give the metal.',
        "options": [
            'Electroplating',
            'Smelting',
            'Cracking',
            'Distillation',
        ],
        "correct_index": 1,
        "why": 'Smelting is the name given to reducing a metal oxide by heating it '
               'with carbon.',
    },
    {
        "id": 'ks4-extraction-of-metals-e07',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is meant by a high-grade ore.',
        "options": [
            'A rock that has been crushed and washed ready for the furnace',
            'A rock in which the metal is present as the uncombined element, not as a compound',
            'A rock with a high percentage of the metal compound in it',
            'A rock that yields more than one metal when it is smelted',
        ],
        "correct_index": 2,
        "why": 'Grade describes how rich the rock is, so a high-grade ore holds a '
               'large proportion of the metal compound.',
    },
    {
        "id": 'ks4-extraction-of-metals-e08',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is grown on low-grade ore in phytomining.',
        "options": [
            'Fungi in sealed tanks',
            'Algae in shallow ponds',
            'Plants',
            'Moulds on damp paper',
        ],
        "correct_index": 2,
        "why": 'Phytomining grows plants on the low-grade ore so that their roots '
               'take up the metal compounds.',
    },
    {
        "id": 'ks4-extraction-of-metals-e09',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the type of living organism used in bioleaching.',
        "options": [
            'Earthworms',
            'Willow trees',
            'Yeast cells',
            'Bacteria',
        ],
        "correct_index": 3,
        "why": 'Bioleaching uses bacteria, which feed on the low-grade ore and put '
               'the metal compounds into solution.',
    },
    {
        "id": 'ks4-extraction-of-metals-e10',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is done with the crop once it has been harvested in '
                'phytomining.',
        "options": [
            'It is burned, and the ash holds the metal compounds',
            'It is pressed, and the juice is bottled and sold on',
            'It is buried again so the metal goes back into the soil',
            'It is fed to livestock so that the metal builds up in the meat and can be recovered',
        ],
        "correct_index": 0,
        "why": 'The harvested crop is burned, and the ash that is left contains the '
               'metal compounds in a much higher concentration.',
    },
    {
        "id": 'ks4-extraction-of-metals-e11',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the chemical name of the compound that makes up most of '
                'haematite.',
        "options": [
            'Iron(II) sulfate',
            'Iron(III) oxide',
            'Iron(III) carbonate',
            'Iron(II) sulfide',
        ],
        "correct_index": 1,
        "why": 'Haematite is largely iron(III) oxide, Fe2O3, which is why the '
               'furnace has to remove oxygen from it.',
    },
    {
        "id": 'ks4-extraction-of-metals-e12',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the three kinds of compound that a metal is usually present '
                'as in its ore.',
        "options": [
            'A nitrate, a phosphide or a nitride',
            'A hydroxide, a nitride or a hydride',
            'An oxide, a sulfide or a carbonate',
            'An alloy, an amalgam or a solution',
        ],
        "correct_index": 2,
        "why": 'Ores nearly all hold the metal as an oxide, a sulfide or a '
               'carbonate rather than as the element.',
    },
    {
        "id": 'ks4-extraction-of-metals-s05',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a metal lying above carbon in the reactivity series '
                'cannot be obtained by heating its oxide with carbon.',
        "options": [
            'Carbon burns away completely before it can touch the oxide',
            'Carbon is less reactive than the metal, so it cannot take the oxygen away',
            'The oxide melts before the carbon becomes hot enough to react',
            'Carbon attacks sulfide ores, so an oxide ore is left unchanged',
        ],
        "correct_index": 1,
        "why": 'Reduction by carbon works only when carbon is the more reactive of '
               'the two, so a metal above carbon keeps its oxygen.',
    },
    {
        "id": 'ks4-extraction-of-metals-s06',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A metal is obtained industrially by passing a current through its '
                'molten chloride. Deduce what that tells you about the metal.',
        "options": [
            'It lies below carbon, because only a metal below carbon melts cleanly enough to flow',
            'It lies above carbon, so carbon cannot reduce its compounds',
            'It lies below hydrogen, because a current releases hydrogen first',
            'Its position cannot be worked out from the method used to get it',
        ],
        "correct_index": 1,
        "why": 'Electrolysis is used precisely because carbon reduction fails, and '
               'that happens for metals above carbon.',
    },
    {
        "id": 'ks4-extraction-of-metals-s07',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why mining companies are now interested in rock holding '
                'a very small percentage of copper.',
        "options": [
            'The richest copper ores are running out, so poorer rock is what is left',
            'Poorer rock is softer, so much less machinery is needed to crush it up',
            'Copper separates out more easily when there is less of it present',
            'Poorer rock holds copper as the element, so no reduction is needed',
        ],
        "correct_index": 0,
        "why": 'Demand has stayed high while the high-grade deposits have been used '
               'up, so low-grade rock is now worth working.',
    },
    {
        "id": 'ks4-extraction-of-metals-s08',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student writes ZnO + C → Zn + CO2 for the extraction of zinc. '
                'Explain what is wrong with the equation.',
        "options": [
            'The oxygen does not balance: it should read 2ZnO + C → 2Zn + CO2',
            'Carbon should be written as carbon monoxide, because a solid is unable to reduce anything',
            'Zinc is above carbon, so no equation of this kind is possible at all',
            'The products are reversed: zinc oxide is made rather than broken down',
        ],
        "correct_index": 0,
        "why": 'One ZnO supplies a single oxygen atom, but CO2 needs two, so two '
               'formula units of zinc oxide are required.',
    },
    {
        "id": 'ks4-extraction-of-metals-s09',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why very hot air is blasted in at the base of the furnace '
                'used to extract iron.',
        "options": [
            'It cools the liquid metal so that it has set hard by the time it is tapped off',
            'It blows the powdered ore upwards so that it mixes with the charge',
            'It supplies oxygen that burns the coke and releases the heat needed',
            'It supplies nitrogen, which joins with the metal and hardens it',
        ],
        "correct_index": 2,
        "why": 'Burning coke in the blasted air is an exothermic reaction and is '
               'what raises the furnace to working temperature.',
    },
    {
        "id": 'ks4-extraction-of-metals-s10',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why liquid iron gathers at the base of the furnace while '
                'the waste slag rests on top of it.',
        "options": [
            'The slag is magnetic, so it is held up against the furnace walls',
            'Iron is the denser of the two liquids, so it sinks below the slag',
            'Iron is still solid there, so it drops through the liquid slag',
            'Iron is pulled down by the current that passes through the charge',
        ],
        "correct_index": 1,
        "why": 'Both are liquid at that temperature and the metal is much denser, so '
               'it settles underneath and can be tapped off.',
    },
    {
        "id": 'ks4-extraction-of-metals-s11',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the percentage by mass of iron in Fe2O3, taking Mr of '
                'Fe2O3 as 160 and Ar of Fe as 56.',
        "options": [
            '35%',
            '30%',
            '56%',
            '70%',
        ],
        "correct_index": 3,
        "why": 'Two iron atoms give 2 x 56 = 112, and 112 / 160 x 100 = 70%.',
    },
    {
        "id": 'ks4-extraction-of-metals-s12',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In a furnace, 160 tonnes of Fe2O3 is fully reduced. Calculate the '
                'mass of iron this produces, given Ar of Fe = 56 and Mr of Fe2O3 = 160.',
        "options": [
            '56 tonnes',
            '320 tonnes',
            '112 tonnes',
            '160 tonnes',
        ],
        "correct_index": 2,
        "why": '160 tonnes is one formula mass of Fe2O3, which holds 2 x 56 = 112 '
               'tonnes of iron.',
    },
    {
        "id": 'ks4-extraction-of-metals-s13',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how copper compounds get from low-grade ore into the ash of a '
                'phytomining crop.',
        "options": [
            'They settle on the leaves as dust, and burning the crop fixes that dust into the ash',
            'The plants build new copper compounds out of the gases they take in',
            'The roots change the compounds to metal, which stays behind on burning',
            'The roots take the compounds up, and burning leaves them in the ash',
        ],
        "correct_index": 3,
        "why": 'The plants absorb the metal compounds through their roots, and '
               'burning the crop leaves those compounds concentrated in the ash.',
    },
    {
        "id": 'ks4-extraction-of-metals-s14',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the ash from a phytomining crop is stirred into acid '
                'before the copper is recovered.',
        "options": [
            'The acid kills off any bacteria left in the ash so that they cannot spoil the metal',
            'It brings the copper compounds into solution so they can then be treated',
            'The acid burns off the rest of the plant matter, leaving copper behind',
            'It turns the copper compounds into copper oxide, which carbon can reduce',
        ],
        "correct_index": 1,
        "why": 'The copper in the ash is present as compounds, so the ash is '
               'dissolved to give a solution that can then be processed.',
    },
    {
        "id": 'ks4-extraction-of-metals-s15',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State how copper metal is recovered from the leachate that '
                'bioleaching produces.',
        "options": [
            'By heating the leachate with coke in a furnace until the liquid metal runs out',
            'By filtering the leachate through a bed of fine washed sand',
            'By displacement with scrap iron, or by electrolysis of the solution',
            'By standing the leachate in open tanks until the water has gone',
        ],
        "correct_index": 2,
        "why": 'The dissolved copper is either displaced by a more reactive metal '
               'such as scrap iron, or released by electrolysing the solution.',
    },
    {
        "id": 'ks4-extraction-of-metals-s16',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest one advantage that phytomining has over digging a new '
                'open-cast mine.',
        "options": [
            'It does not scar the landscape with a huge pit or waste heaps',
            'It gives far more metal from the same area of ground each year',
            'It delivers the metal ready to use, so that no later processing stage is needed',
            'It suits rich rock as well as poor rock, and finishes much faster',
        ],
        "correct_index": 0,
        "why": 'Growing a crop leaves the ground largely intact, so none of the '
               'quarrying, spoil heaps, noise and dust of open-cast mining arise.',
    },
    {
        "id": 'ks4-extraction-of-metals-s17',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why phytomining is a slow way of obtaining a metal.',
        "options": [
            'The ore has to be ground down to a fine powder by hand before the crop can be sown',
            'Plants absorb metals in darkness, so the process stops each morning',
            'A whole crop has to grow to maturity before any metal is recovered',
            'The ash has to be left to cool for some months before it can be used',
        ],
        "correct_index": 2,
        "why": 'Each harvest takes a full growing season, so the metal arrives at '
               'the rate the plants grow rather than the rate a furnace works.',
    },
    {
        "id": 'ks4-extraction-of-metals-s18',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what phytomining and bioleaching each use to free the metal '
                'compounds held in low-grade ore.',
        "options": [
            'Phytomining uses growing plants, and bioleaching uses bacteria',
            'Phytomining uses bacteria living in the soil, and bioleaching uses the roots of plants',
            'Both use bacteria, but bioleaching also needs an electric current',
            'Both use plants, but phytomining burns them and bioleaching does not',
        ],
        "correct_index": 0,
        "why": 'Phytomining works through a crop of plants; bioleaching works '
               'through bacteria that feed on the ore.',
    },
    {
        "id": 'ks4-extraction-of-metals-s19',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student says that phytomining produces pure copper. Explain why that '
                'is wrong.',
        "options": [
            'The plants give copper oxide, and copper oxide counts as the pure metal already',
            'The ash holds no copper at all, because it burns off with the plant',
            'The ash holds copper compounds, which still have to be processed',
            'The copper is pure but is mixed with so much soil that it is useless',
        ],
        "correct_index": 2,
        "why": 'Burning the crop leaves an ash of copper compounds, so a reduction '
               'or electrolysis stage is still needed to get the metal.',
    },
    {
        "id": 'ks4-extraction-of-metals-s20',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student says iron has to be extracted electrically because iron '
                'is a reactive metal. Explain the error.',
        "options": [
            'Iron is unreactive, so it is dug straight out of the ground as metal',
            'Iron does need a current, but that is because its ore is a sulfide and not an oxide',
            'Iron is reactive, but a current works on solutions and not on hot ores',
            'Iron sits below carbon, so heating its oxide with carbon is enough',
        ],
        "correct_index": 3,
        "why": 'Iron is reactive enough to be found combined, but it lies below '
               'carbon, so carbon reduction removes the oxygen for it.',
    },
    {
        "id": 'ks4-extraction-of-metals-s21',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why heating aluminium oxide with carbon gives no aluminium, '
                'however far the temperature is raised.',
        "options": [
            'Aluminium oxide is a covalent compound, so it holds no oxygen for carbon to remove',
            'Aluminium oxide boils off before the carbon can begin to react with it',
            'Aluminium is above carbon, so carbon cannot strip the oxygen from it',
            'Aluminium is too light to settle out, so it is carried away as dust',
        ],
        "correct_index": 2,
        "why": 'Aluminium is more reactive than carbon, so it holds its oxygen more '
               'strongly than carbon can and no temperature changes that order.',
    },
    {
        "id": 'ks4-extraction-of-metals-s22',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Four metals are offered: potassium, calcium, lead and aluminium. '
                'Identify the one obtained by reduction with carbon.',
        "options": [
            'Potassium',
            'Lead',
            'Calcium',
            'Aluminium',
        ],
        "correct_index": 1,
        "why": 'Lead is the only one of the four that lies below carbon, so only '
               'its oxide can be reduced by heating with carbon.',
    },
    {
        "id": 'ks4-extraction-of-metals-s23',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Malachite is an ore holding copper carbonate. Describe the two '
                'stages by which copper is obtained from it.',
        "options": [
            'Heat it to leave copper oxide, then heat that oxide with carbon',
            'Dissolve it in water, then leave the solution in a warm place to crystallise',
            'Melt it, then blow air through the liquid to burn off the carbon',
            'Roast it with sulfur, then wash the copper out of the residue',
        ],
        "correct_index": 0,
        "why": 'Heating decomposes the carbonate to copper oxide, and the oxide is '
               'then reduced by carbon because copper lies below carbon.',
    },
    {
        "id": 'ks4-extraction-of-metals-s24',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a copper mine may be shut down while copper compounds '
                'remain in the rock.',
        "options": [
            'Once the richest rock has gone, the compounds left stop reacting',
            'What is left is too poor in copper to pay for the cost of extraction',
            'The law forbids a mine from taking more than half of the ore present',
            'Compounds lying deeper down are ones that carbon is unable to reduce',
        ],
        "correct_index": 1,
        "why": 'Extraction has to pay for itself, so a deposit is abandoned once '
               'its grade falls below the level that covers the cost.',
    },
    {
        "id": 'ks4-extraction-of-metals-s25',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why carbon monoxide, rather than the lumps of coke, does '
                'most of the reducing inside a blast furnace.',
        "options": [
            'Coke is used up before the ore has travelled down to it',
            'Ore and coke are kept in separate parts of the furnace',
            'A gas reaches the surface of every lump of ore throughout the furnace',
            'The coke holds the charge up, so it is not free to react',
        ],
        "correct_index": 2,
        "why": 'Solid coke touches the ore only where lumps happen to meet, while '
               'the gas flows around and into every piece of ore.',
    },
    {
        "id": 'ks4-extraction-of-metals-s26',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe one environmental problem caused by mining a metal ore '
                'and one caused by smelting it.',
        "options": [
            'Mining uses up the oxygen held in the rock, and smelting cools the soil nearby',
            'Mining lifts the water table, and smelting locks carbon in slag',
            'Mining scars the landscape, and smelting releases polluting gases',
            'Mining takes carbon dioxide from the air, and smelting adds nitrogen',
        ],
        "correct_index": 2,
        "why": 'Digging and tipping ore destroys habitat and leaves spoil heaps, '
               'while smelting gives out carbon dioxide and other waste gases.',
    },
    {
        "id": 'ks4-extraction-of-metals-h05',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A furnace is charged with 800 tonnes of ore containing 80% Fe2O3 by '
                'mass. Calculate the maximum mass of iron this charge could yield. '
                '(Mr of Fe2O3 = 160, Ar of Fe = 56)',
        "options": [
            '224 tonnes',
            '448 tonnes',
            '560 tonnes',
            '640 tonnes',
        ],
        "correct_index": 1,
        "why": '800 x 0.80 = 640 tonnes of Fe2O3, and 640 x 112 / 160 = 448 tonnes '
               'of iron.',
    },
    {
        "id": 'ks4-extraction-of-metals-h06',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper and iron both lie below carbon in the reactivity series, yet '
                'copper was worked thousands of years before iron. Suggest why.',
        "options": [
            'Copper oxide is reduced at a far lower temperature than iron oxide is',
            'Iron ore is far rarer near the surface, so it was not found until much later',
            'Copper is a much commoner element in the Earth than iron, so its ores were found first',
            'Iron ore needed a current, and no source of electricity then existed',
        ],
        "correct_index": 0,
        "why": 'A simple charcoal fire is hot enough to reduce copper oxide, whereas '
               'iron oxide needs the much higher temperature of a blast furnace.',
    },
    {
        "id": 'ks4-extraction-of-metals-h07',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'The reduction step follows Fe2O3 + 3CO → 2Fe + 3CO2. Calculate the '
                'mass of carbon monoxide needed for 160 tonnes of Fe2O3, taking Mr '
                'of CO as 28.',
        "options": [
            '28 tonnes',
            '56 tonnes',
            '84 tonnes',
            '168 tonnes',
        ],
        "correct_index": 2,
        "why": '160 tonnes is one formula mass of Fe2O3, so three formula masses of '
               'CO are needed: 3 x 28 = 84 tonnes.',
    },
    {
        "id": 'ks4-extraction-of-metals-h08',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the mass of carbon dioxide given off when 320 tonnes of '
                'Fe2O3 is reduced, taking Mr of CO2 as 44 and Mr of Fe2O3 as 160.',
        "options": [
            '88 tonnes',
            '132 tonnes',
            '176 tonnes',
            '264 tonnes',
        ],
        "correct_index": 3,
        "why": '320 / 160 = 2 formula masses, each giving 3 CO2, so 2 x 3 x 44 = 264 '
               'tonnes.',
    },
    {
        "id": 'ks4-extraction-of-metals-h09',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A rock contains 0.4% copper by mass. Calculate the mass of rock '
                'that has to be worked to recover one tonne of copper.',
        "options": [
            '40 tonnes',
            '250 tonnes',
            '400 tonnes',
            '2500 tonnes',
        ],
        "correct_index": 1,
        "why": '0.4% is 0.004 as a decimal, and 1 / 0.004 = 250 tonnes of rock per '
               'tonne of copper.',
    },
    {
        "id": 'ks4-extraction-of-metals-h10',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'One phytomining harvest leaves 40 kg of ash, and the ash is 3% '
                'copper by mass. Calculate the mass of copper the harvest yielded.',
        "options": [
            '0.12 kg',
            '13.3 kg',
            '1.2 kg',
            '12 kg',
        ],
        "correct_index": 2,
        "why": '3% of 40 kg is 0.03 x 40 = 1.2 kg of copper.',
    },
    {
        "id": 'ks4-extraction-of-metals-h11',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Zinc oxide, ZnO, is heated with carbon to give zinc. Calculate the '
                'mass of zinc from 810 tonnes of zinc oxide, taking Mr of ZnO as 81 '
                'and Ar of Zn as 65.',
        "options": [
            '325 tonnes',
            '810 tonnes',
            '1300 tonnes',
            '650 tonnes',
        ],
        "correct_index": 3,
        "why": '810 / 81 = 10 formula masses of ZnO, which give 10 formula masses of '
               'zinc: 10 x 65 = 650 tonnes.',
    },
    {
        "id": 'ks4-extraction-of-metals-h12',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A 500 tonne batch of low-grade ore yields 3 tonnes of copper. Determine '
                'the percentage of copper in that batch.',
        "options": [
            '0.06%',
            '6%',
            '1.7%',
            '0.6%',
        ],
        "correct_index": 3,
        "why": '3 / 500 x 100 = 0.6% copper by mass.',
    },
    {
        "id": 'ks4-extraction-of-metals-h13',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the energy needed to extract a metal lying above carbon in '
                'the reactivity series with one lying below it.',
        "options": [
            'The metal above carbon needs far more, as its compound has to be melted and a large current driven through it',
            'The metal below carbon needs far more, as a furnace has to be held at working heat for days on end',
            'Both need the same, as the same amount of oxygen has to be taken from each of the oxides',
            'The metal above carbon needs less, as its compounds are the ones that fall apart on heating',
        ],
        "correct_index": 0,
        "why": 'A metal below carbon needs only a hot furnace and coke, while one '
               'above carbon needs its compound molten and a large current as well.',
    },
    {
        "id": 'ks4-extraction-of-metals-h14',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron tapped from a blast furnace is about 96% iron by mass. '
                'Calculate the mass of iron in a 250 tonne tapping.',
        "options": [
            '2400 tonnes',
            '260 tonnes',
            '240 tonnes',
            '10 tonnes',
        ],
        "correct_index": 2,
        "why": '96% of 250 tonnes is 0.96 x 250 = 240 tonnes of iron, the remaining '
               '10 tonnes being impurities carried over from the charge.',
    },
    {
        "id": 'ks4-extraction-of-metals-h15',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why bioleaching and phytomining are being developed even '
                'though both work more slowly than traditional mining.',
        "options": [
            'They give a purer metal, so there is no further processing stage needed afterwards',
            'They can work rock too poor in metal for traditional mining to pay',
            'They leave the rock exactly as it was, so the same ground can be worked again',
            'They need no land, so a whole plant fits inside one small building',
        ],
        "correct_index": 1,
        "why": 'Traditional mining of very low-grade rock costs more than the metal '
               'is worth, and these routes make such deposits usable.',
    },
    {
        "id": 'ks4-extraction-of-metals-h16',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that phytomining does no environmental harm '
                'because no quarry has to be dug.',
        "options": [
            'The claim holds: growing a crop and then burning it puts nothing at all into the surroundings around the site',
            'The claim fails outright: phytomining damages a far larger area of land than any open-cast mine would do',
            'The claim holds: the crop puts back the metal that it took, so the soil is left exactly as it was beforehand',
            'The claim goes too far: land is still taken, the ash needs acid treatment and energy is used, though the harm is less than quarrying',
        ],
        "correct_index": 3,
        "why": 'Phytomining is gentler than quarrying but not harmless: it occupies '
               'land for whole seasons, and the ash still has to be processed.',
    },
    {
        "id": 'ks4-extraction-of-metals-h17',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student states that carbon reduces any metal oxide provided the '
                'furnace is hot enough. Evaluate the statement.',
        "options": [
            'It is right: an oxide gives up its oxygen once the heat is high enough',
            'It is wrong: no temperature lets carbon take oxygen from a metal above it',
            'It is wrong: carbon reduces a metal oxide, but cannot do so unless the oxide is molten',
            'It is right for oxides, but heat makes no difference to a carbonate ore',
        ],
        "correct_index": 1,
        "why": 'Whether carbon can take the oxygen is set by the order of reactivity, '
               'not by temperature, so a metal above carbon is never reduced by it.',
    },
    {
        "id": 'ks4-extraction-of-metals-h18',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A company owns a large, rich copper deposit and must choose between '
                'a smelter and bioleaching. Justify a choice.',
        "options": [
            'Bioleaching: bacteria work through a heap faster than a furnace can',
            'The smelter: bioleaching works on iron ores and not on copper ores',
            'The smelter: rich rock makes smelting pay, and it delivers metal faster',
            'Bioleaching: rich rock is the one kind of rock that the bacteria are able to attack',
        ],
        "correct_index": 2,
        "why": 'Bioleaching earns its place on rock too poor to smelt; with a rich '
               'deposit the faster, established route is the better choice.',
    },
    {
        "id": 'ks4-extraction-of-metals-h19',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why copper obtained by phytomining can cost more per tonne than '
                'copper from a conventional mine, though the low-grade ore is worthless.',
        "options": [
            'The plants take the copper up as the pure metal, and pure metal is taxed at a higher rate',
            'The ash itself is worth more than the metal, so the copper has to be sold off at a loss',
            'A phytomining crop has to be raised under glass, and a glasshouse costs more than a mine does',
            'Each crop takes a season and yields only a little metal, so land, labour and processing costs are spread thinly',
        ],
        "correct_index": 3,
        "why": 'The cost of a season of land, tending, harvesting, burning and '
               'processing is set against a small mass of metal per crop.',
    },
    {
        "id": 'ks4-extraction-of-metals-h20',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the carbon dioxide released by smelting an ore with the '
                'carbon dioxide balance of phytomining.',
        "options": [
            'Smelting releases it from the coke, while a crop takes it in as it grows and returns it on burning',
            'Both release exactly the same amount of it, because burning plant matter and burning coke give identical products',
            'Smelting takes it into the slag, while phytomining drives it out of the soil around the crop',
            'Neither releases any, because the carbon stays locked inside the metal along both of the routes',
        ],
        "correct_index": 0,
        "why": 'Smelting adds carbon dioxide from fossil coke, whereas the crop '
               'absorbs the same gas while growing and gives it back when burned.',
    },
    {
        "id": 'ks4-extraction-of-metals-h21',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Many copper ores are sulfides. Suggest why such an ore is roasted '
                'in air first, and name the gas that then has to be removed.',
        "options": [
            'Roasting dries the ore out, and the steam produced has to be removed',
            'Roasting turns the sulfide to an oxide, and sulfur dioxide is removed',
            'Roasting turns the sulfide into a carbonate, and the carbon dioxide is then removed',
            'Roasting melts the sulfur out, and hydrogen sulfide is removed',
        ],
        "correct_index": 1,
        "why": 'Roasting converts the sulfide to an oxide that carbon can reduce, '
               'and the sulfur leaves as sulfur dioxide, which must be trapped.',
    },
    {
        "id": 'ks4-extraction-of-metals-h22',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A poor deposit lies 200 m underground. Evaluate which of '
                'phytomining and bioleaching suits it better.',
        "options": [
            'Phytomining: roots grow towards metal compounds and follow them to any depth',
            'Phytomining: the deeper the rock, the richer the ash left when the crop burns',
            'Bioleaching: bacteria can be circulated through the rock, while roots never reach so deep',
            'Neither: both methods work only on rock that has already been through a furnace',
        ],
        "correct_index": 2,
        "why": 'Plant roots reach only the top of the soil, while a bacterial '
               'solution can be pumped down and circulated through the deposit.',
    },
    {
        "id": 'ks4-extraction-of-metals-h23',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Limestone is tipped into a blast furnace along with the ore and the '
                'coke. Explain what it is there to do.',
        "options": [
            'It adds the extra carbon monoxide that strips oxygen out of the ore',
            'It keeps the charge dry so the coke catches light lower down',
            'It lowers the melting point of the metal, so that it can be tapped off',
            'It reacts with acidic impurities in the ore to give a slag that runs off',
        ],
        "correct_index": 3,
        "why": 'Limestone decomposes and the calcium oxide formed reacts with acidic '
               'impurities such as silica, carrying them off as molten slag.',
    },
    {
        "id": 'ks4-extraction-of-metals-h24',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why rock holding 30% of a metal compound may be worth '
                'working in one country and not in another.',
        "options": [
            'Energy, labour and transport cost different amounts, and those costs decide whether extraction pays',
            'A metal grows less reactive nearer the equator, so extraction is easier there',
            'Rock counts as an ore only above sea level, and that differs from country to country',
            'The proportion of metal in a deposit drops over time, faster in a warm climate',
        ],
        "correct_index": 0,
        "why": 'Whether a deposit is an ore is an economic judgement, so the same '
               'grade of rock can be profitable in one place and not in another.',
    },
    {
        "id": 'ks4-extraction-of-metals-h25',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student suggests bioleaching is a clean process because no furnace '
                'is involved. Evaluate the suggestion.',
        "options": [
            'It is only partly right: the leachate is acidic and toxic, and processing it still takes energy',
            'It is fully right: the bacteria break the rock down and let nothing harmful into the ground',
            'It is wrong: bioleaching burns more fuel than smelting, because the bacteria must be kept warm',
            'It is wrong: a furnace is used at the end, to melt the copper out of the leached heap',
        ],
        "correct_index": 0,
        "why": 'Avoiding a furnace saves fuel and waste gas, but the acidic leachate '
               'can pollute water and still has to be processed.',
    },
    {
        "id": 'ks4-extraction-of-metals-h26',
        "subtopic_slug": 'extraction-of-metals',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Bacteria are used to recover copper from the waste heaps of an old mine. '
                'Suggest an advantage over opening a fresh mine.',
        "options": [
            'The waste is richer in copper than fresh rock, so bacteria work faster',
            'The leachate needs no processing, as the copper comes out as the metal',
            'The heaps hold copper as the element, so no chemical change is needed',
            'The rock is already broken and at the surface, so none has to be dug or blasted',
        ],
        "correct_index": 3,
        "why": 'The heaps are crushed waste lying in the open, so the digging, '
               'blasting and new land take of a fresh mine are all avoided.',
    },
]
