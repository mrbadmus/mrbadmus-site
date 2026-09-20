"""Chemistry · Chemical changes — the MRB-338 expansion for `salts-neutralisation`.

Three routes to a salt and the one question that picks between them: is the salt
soluble, and are the starting materials soluble too. Most of the weight sits on
the required practical — warm the acid, stir in excess insoluble base until no
more dissolves, filter, evaporate part of the water and leave the rest to
crystallise — because that is where the marks are lost, in the order of the
steps and the reason behind each one.

Precipitation carries the insoluble salts, with the wash-and-dry stage asked as
a reason rather than a recipe, and the solubility rules appear only where they
decide a method. Titration technique itself belongs to its own leaf and is
referred to here only as the route taken when both reactants dissolve; pH values
and indicator colours belong to `ph-scale`.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-salts-neutralisation-e05',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the piece of apparatus used to evaporate a salt solution '
                'over a water bath.',
        "options": [
            'A conical flask',
            'An evaporating basin',
            'A measuring cylinder, 100 cm3',
            'A volumetric flask',
        ],
        "correct_index": 1,
        "why": 'An evaporating basin is shallow and open, so water leaves the '
               'solution quickly over gentle heat.',
    },
    {
        "id": 'ks4-salts-neutralisation-e06',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why excess copper oxide is added to the sulfuric acid '
                'rather than an exact amount.',
        "options": [
            'To stop the copper oxide from settling to the bottom',
            'To make the reaction release more heat while it goes on',
            'To give a deeper blue colour to the final crystals formed',
            'To make sure that none of the acid is left unreacted',
        ],
        "correct_index": 3,
        "why": 'Any acid left over would end up in the crystals, so the base is '
               'added until it stops dissolving.',
    },
    {
        "id": 'ks4-salts-neutralisation-e07',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the colour of the copper sulfate crystals made from '
                'copper oxide and sulfuric acid.',
        "options": [
            'Black',
            'White',
            'Green',
            'Blue',
        ],
        "correct_index": 3,
        "why": 'Hydrated copper sulfate crystals are blue, which is why the '
               'solution is blue before the water is driven off.',
    },
    {
        "id": 'ks4-salts-neutralisation-e08',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the liquid used to wash a precipitate once it has been '
                'filtered.',
        "options": [
            'Dilute hydrochloric acid',
            'Distilled water',
            'Dilute sodium hydroxide',
            'Tap water from the sink',
        ],
        "correct_index": 1,
        "why": 'Distilled water carries no dissolved ions of its own, so it '
               'rinses the precipitate without leaving anything behind.',
    },
    {
        "id": 'ks4-salts-neutralisation-e09',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is meant by a precipitate.',
        "options": [
            'A gas released during a neutralisation reaction',
            'A liquid that passes through the filter paper',
            'An insoluble solid formed when two solutions are mixed',
            'A solution left behind after evaporation',
        ],
        "correct_index": 2,
        "why": 'A precipitate is a solid that will not dissolve, so it appears '
               'the moment the two solutions meet.',
    },
    {
        "id": 'ks4-salts-neutralisation-e10',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the salt that is insoluble in water.',
        "options": [
            'Sodium nitrate',
            'Potassium chloride',
            'Barium sulfate',
            'Copper sulfate',
        ],
        "correct_index": 2,
        "why": 'Sulfates are mostly soluble, but barium sulfate is one of the '
               'few that are not.',
    },
    {
        "id": 'ks4-salts-neutralisation-e11',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is left on the filter paper when the copper sulfate '
                'mixture is filtered.',
        "options": [
            'The blue copper sulfate solution',
            'The unreacted copper oxide powder',
            'The sulfuric acid that has not reacted',
            'The water driven out of the mixture',
        ],
        "correct_index": 1,
        "why": 'The salt is dissolved and passes through, so only the excess '
               'solid base is held back by the paper.',
    },
    {
        "id": 'ks4-salts-neutralisation-e12',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the general term for a substance that neutralises an acid '
                'to give a salt and water.',
        "options": [
            'A base',
            'A catalyst',
            'A solvent',
            'An indicator',
        ],
        "correct_index": 0,
        "why": 'Bases include metal oxides, metal hydroxides and carbonates, '
               'and each neutralises an acid.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-salts-neutralisation-s05',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Put the steps of the soluble-salt preparation in order: filter, '
                'add excess base, crystallise, evaporate part of the water.',
        "options": [
            'Filter, add excess base, evaporate, then crystallise',
            'Add excess base, filter, evaporate, crystallise',
            'Evaporate, add excess base, filter, then crystallise',
            'Add excess base, evaporate, filter, crystallise',
        ],
        "correct_index": 1,
        "why": 'The base must react before the leftover solid can be filtered '
               'off, and only then is the clear filtrate concentrated.',
    },
    {
        "id": 'ks4-salts-neutralisation-s06',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State how a student knows that enough copper oxide has been '
                'added to the warm acid.',
        "options": [
            'The mixture stops giving off any bubbles of gas',
            'The solution turns from blue back to colourless again',
            'The mixture becomes too hot to hold in a gloved hand',
            'Some copper oxide stays undissolved at the bottom',
        ],
        "correct_index": 3,
        "why": 'Once solid remains after stirring, the acid has all been used '
               'and the base is genuinely in excess.',
    },
    {
        "id": 'ks4-salts-neutralisation-s07',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the acid is warmed before the insoluble base is '
                'stirred into it.',
        "options": [
            'Warming speeds the reaction up so it finishes in a lesson',
            'Warming is the only way to make an insoluble base dissolve in acid',
            'Warming increases the mass of salt that can be produced',
            'Warming drives off water and concentrates the acid beforehand',
        ],
        "correct_index": 0,
        "why": 'Heating raises the rate of a slow reaction between a liquid and '
               'a solid without changing what is made.',
    },
    {
        "id": 'ks4-salts-neutralisation-s08',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the two solutions that could be mixed to precipitate '
                'silver chloride.',
        "options": [
            'Silver sulfate and sodium carbonate',
            'Silver chloride and sodium nitrate',
            'Silver nitrate and sodium sulfate solution',
            'Silver nitrate and sodium chloride',
        ],
        "correct_index": 3,
        "why": 'Both starting solutions must be soluble and between them supply '
               'the silver ion and the chloride ion.',
    },
    {
        "id": 'ks4-salts-neutralisation-s09',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how the crystals are dried once they have formed.',
        "options": [
            'Rinse them in dilute acid and then leave them on the bench',
            'Heat them strongly in a crucible until they glow',
            'Pat them between sheets of filter paper or leave them to air-dry',
            'Stir them back into warm water and evaporate a second time',
        ],
        "correct_index": 2,
        "why": 'Gentle drying removes surface liquid without driving the water '
               'of crystallisation out of the crystals.',
    },
    {
        "id": 'ks4-salts-neutralisation-s10',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the salt solution is not boiled dry in the '
                'evaporating basin.',
        "options": [
            'Boiling dry would turn the salt back into the acid and base again',
            'Boiling dry gives tiny crystals and can decompose the salt',
            'Boiling dry would leave the salt still slightly wet underneath',
            'The basin would crack and shatter under such strong heat',
        ],
        "correct_index": 1,
        "why": 'Slow crystallisation from a concentrated solution grows larger, '
               'purer crystals, and strong heating can break the salt down.',
    },
    {
        "id": 'ks4-salts-neutralisation-s11',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the correct method for making magnesium chloride '
                'crystals from magnesium carbonate.',
        "options": [
            'Mix it with sodium chloride solution and filter the precipitate',
            'Add excess carbonate to dilute hydrochloric acid, filter, evaporate',
            'Add excess carbonate to dilute sulfuric acid, filter, evaporate',
            'Electrolyse the molten carbonate and collect the crystals',
        ],
        "correct_index": 1,
        "why": 'Magnesium chloride is soluble and the carbonate is not, so the '
               'excess-solid route with hydrochloric acid gives it cleanly.',
    },
    {
        "id": 'ks4-salts-neutralisation-s12',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the ionic equation for the neutralisation of any acid by '
                'any alkali.',
        "options": [
            'H+ + Cl- -> HCl',
            'H2 + O2 -> H2O',
            'OH- + Na+ -> NaOH',
            'H+ + OH- -> H2O',
        ],
        "correct_index": 3,
        "why": 'Whatever the acid and alkali, the change that matters is a '
               'hydrogen ion joining a hydroxide ion to make water.',
    },
    {
        "id": 'ks4-salts-neutralisation-s13',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A precipitate of lead(II) iodide is filtered but not washed. '
                'Describe the effect on the dried solid.',
        "options": [
            'It weighs less, because some of it has dissolved into the wash water',
            'It is contaminated with the soluble salt left in the mixture',
            'It turns a paler colour as it dries out on the paper',
            'It stays exactly as pure as a properly washed sample would be',
        ],
        "correct_index": 1,
        "why": 'The liquid clinging to the solid carries dissolved ions, which '
               'are left behind as an impurity when it dries.',
    },
    {
        "id": 'ks4-salts-neutralisation-s14',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a titration, and not the excess-solid method, is '
                'used to make potassium nitrate.',
        "options": [
            'Potassium nitrate is insoluble, so it must be filtered off',
            'Both the alkali and the acid dissolve, so nothing can be filtered',
            'The reaction between them is far too slow for the other route to be used',
            'Potassium hydroxide would decompose if it were added in excess',
        ],
        "correct_index": 1,
        "why": 'The excess-solid method depends on filtering leftover solid, and '
               'a soluble alkali leaves none to filter.',
    },
    {
        "id": 'ks4-salts-neutralisation-s15',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the titration is repeated without indicator when a '
                'pure salt is wanted.',
        "options": [
            'The indicator would change the volume of acid needed',
            'The indicator would react with the acid and use some of it up',
            'The indicator would stop the salt from crystallising out',
            'The indicator would colour and contaminate the crystals',
        ],
        "correct_index": 3,
        "why": 'The known titre is used a second time with no indicator, so '
               'nothing but the salt is left when the water goes.',
    },
    {
        "id": 'ks4-salts-neutralisation-s16',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Choose the acid and the base needed to prepare zinc sulfate '
                'crystals by the excess-solid method.',
        "options": [
            'Sulfuric acid and zinc sulfate',
            'Hydrochloric acid and zinc oxide',
            'Sulfuric acid and zinc oxide',
            'Nitric acid and zinc carbonate',
        ],
        "correct_index": 2,
        "why": 'The sulfate must come from sulfuric acid and the zinc from an '
               'insoluble zinc compound that can be added in excess.',
    },
    {
        "id": 'ks4-salts-neutralisation-s17',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what is seen when barium chloride solution is added '
                'to sodium sulfate solution.',
        "options": [
            'The mixture fizzes and gives off a colourless gas',
            'A white solid appears and clouds the mixture',
            'The mixture warms and turns a deep yellow',
            'Nothing changes, because both salts are soluble',
        ],
        "correct_index": 1,
        "why": 'Barium sulfate is insoluble, so it forms straight away as a '
               'fine white precipitate.',
    },
    {
        "id": 'ks4-salts-neutralisation-s18',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Lead(II) iodide is precipitated by mixing lead nitrate '
                'solution with potassium iodide solution. Name the soluble salt '
                'left in the mixture.',
        "options": [
            'Potassium iodide',
            'Potassium nitrate',
            'Lead nitrate',
            'Potassium hydroxide',
        ],
        "correct_index": 1,
        "why": 'The lead leaves with the iodide as the precipitate, so the '
               'potassium and nitrate ions stay dissolved together.',
    },
    {
        "id": 'ks4-salts-neutralisation-s19',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the evaporating basin is heated over a water bath '
                'rather than directly in a flame.',
        "options": [
            'A water bath gives gentle, even heat below 100 degrees C',
            'A water bath heats the solution far faster than an open flame',
            'A water bath keeps the salt solution from turning acidic as it heats',
            'A water bath removes the need to wear eye protection at the bench',
        ],
        "correct_index": 0,
        "why": 'Gentle heating stops the solution spitting and stops the salt '
               'being decomposed by a fierce local temperature.',
    },
    {
        "id": 'ks4-salts-neutralisation-s20',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why filtering is not needed at any stage when an acid '
                'is neutralised by an alkali in a titration.',
        "options": [
            'The salt formed is insoluble and sinks to the bottom of the flask by itself',
            'The alkali is added in excess, so no solid can ever form',
            'The indicator removes any solid as soon as it appears',
            'Everything present stays dissolved, so there is no solid to remove',
        ],
        "correct_index": 3,
        "why": 'Acid, alkali and the salt made are all in solution, so the only '
               'separation needed is evaporation.',
    },
    {
        "id": 'ks4-salts-neutralisation-s21',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify which salt could not be made by adding an excess '
                'solid to an acid.',
        "options": [
            'Copper sulfate',
            'Zinc chloride',
            'Sodium chloride',
            'Magnesium nitrate',
        ],
        "correct_index": 2,
        "why": 'The sodium compounds that react with acid all dissolve, so no '
               'excess solid could be filtered out afterwards.',
    },
    {
        "id": 'ks4-salts-neutralisation-s22',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the volume of the solution while it sits '
                'on the windowsill to crystallise.',
        "options": [
            'It stays fixed, because the basin is kept covered',
            'It rises, because the crystals give out water as they grow',
            'It falls, because water slowly evaporates away',
            'It falls, because the salt soaks up the water as it forms',
        ],
        "correct_index": 2,
        "why": 'As water leaves, the remaining solution becomes saturated and '
               'the salt comes out of it as crystals.',
    },
    {
        "id": 'ks4-salts-neutralisation-s23',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how the precipitate is separated from the mixture '
                'once it has formed.',
        "options": [
            'Pour the mixture through filter paper in a funnel',
            'Evaporate the whole mixture over a strong flame',
            'Leave the mixture to settle and then boil the liquid',
            'Add more of one solution until the solid dissolves',
        ],
        "correct_index": 0,
        "why": 'The solid is held on the paper while the solution runs through, '
               'which is exactly what filtration is for.',
    },
    {
        "id": 'ks4-salts-neutralisation-s24',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why copper carbonate rather than copper metal is used to '
                'prepare copper sulfate.',
        "options": [
            'Copper metal would give a different salt from the carbonate',
            'Copper metal does not react with dilute acid',
            'Copper metal would dissolve too quickly to control',
            'Copper metal is more expensive than copper carbonate',
        ],
        "correct_index": 1,
        "why": 'Copper is below hydrogen in the reactivity series, so only a '
               'copper compound will neutralise the acid.',
    },
    {
        "id": 'ks4-salts-neutralisation-s25',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why safety glasses are worn throughout the salt '
                'preparation.',
        "options": [
            'Hot acid and hot salt solution can spit from the basin',
            'The crystals give off a vapour that stings the eyes badly',
            'Filter paper can tear and flick hot liquid up into the face',
            'The water bath produces a jet of steam that is under high pressure',
        ],
        "correct_index": 0,
        "why": 'Warm dilute acid is corrosive and a heated solution can spit, '
               'so the eyes are protected from start to finish.',
    },
    {
        "id": 'ks4-salts-neutralisation-s26',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the two products formed when copper oxide reacts with '
                'dilute sulfuric acid.',
        "options": [
            'Copper sulfate and hydrogen',
            'Copper sulfate and water',
            'Copper sulfide and water',
            'Copper hydroxide and water',
        ],
        "correct_index": 1,
        "why": 'A metal oxide is a base, so neutralising it with an acid gives '
               'the salt and water and nothing else.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-salts-neutralisation-h05',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student filters the mixture before all the copper oxide has '
                'reacted. Predict the effect on the crystals collected.',
        "options": [
            'They are contaminated with black copper oxide powder',
            'They are wet with acid and unsafe to handle',
            'Fewer crystals form, because some acid is filtered away unreacted',
            'The crystals are white rather than the usual blue',
        ],
        "correct_index": 2,
        "why": 'Acid that never met the base passes through with the filtrate '
               'and makes no salt, so the yield falls.',
    },
    {
        "id": 'ks4-salts-neutralisation-h06',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which pair of solutions would leave no precipitate at '
                'all when they are mixed.',
        "options": [
            'Barium chloride and sodium sulfate solution',
            'Sodium chloride and potassium nitrate',
            'Silver nitrate and potassium chloride solution',
            'Lead nitrate and sodium iodide solution',
        ],
        "correct_index": 1,
        "why": 'Every possible pairing there — sodium nitrate and potassium '
               'chloride — is soluble, so nothing can come out of solution.',
    },
    {
        "id": 'ks4-salts-neutralisation-h07',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the same mass of salt is obtained whether the acid '
                'is neutralised by copper oxide or by copper carbonate.',
        "options": [
            'Both of the bases have exactly the same formula mass as each other',
            'The excess solid dissolves into the acid and adds itself to the salt',
            'Both of the reactions release exactly the same volume of carbon dioxide',
            'The acid is the limiting reactant, and it fixes the salt made',
        ],
        "correct_index": 3,
        "why": 'With the base in excess, the amount of acid decides how much '
               'copper sulfate can form, whichever base supplies the copper.',
    },
    {
        "id": 'ks4-salts-neutralisation-h08',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A sample of copper sulfate crystals is heated strongly and '
                'turns white. Explain what has happened.',
        "options": [
            'The copper has been oxidised to a colourless compound',
            'The sulfate has broken away and left copper metal behind',
            'The water of crystallisation has been driven out',
            'The crystals have reacted with oxygen from the air',
        ],
        "correct_index": 2,
        "why": 'Blue copper sulfate is hydrated, and removing that water leaves '
               'the white anhydrous form.',
    },
    {
        "id": 'ks4-salts-neutralisation-h09',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the excess-solid route and the precipitation route in '
                'terms of what is kept at the filtration stage.',
        "options": [
            'The residue is kept in both, since the product is a solid in both',
            'The filtrate is kept in both, since the product dissolves in both',
            'The filtrate is kept in the excess-solid route and the residue in '
            'precipitation',
            'The residue is kept in the excess-solid route and the filtrate in '
            'precipitation',
        ],
        "correct_index": 2,
        "why": 'A soluble salt runs through with the liquid, while an insoluble '
               'one is the very solid held on the paper.',
    },
    {
        "id": 'ks4-salts-neutralisation-h10',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a chemist grinds the insoluble base to a fine '
                'powder before adding it to the acid.',
        "options": [
            'A powder increases the surface area, so it reacts faster',
            'A powder dissolves in the water rather than in the acid itself',
            'A powder produces a larger mass of salt from the same acid',
            'A powder prevents the mixture from boiling over the rim of the basin',
        ],
        "correct_index": 0,
        "why": 'More of the solid is exposed to the acid at once, so the '
               'reaction reaches completion inside a lesson.',
    },
    {
        "id": 'ks4-salts-neutralisation-h11',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would be collected if a student evaporated the '
                'mixture from a titration that still contained indicator.',
        "options": [
            'Pure white crystals, since the indicator burns away',
            'No crystals, because the indicator stops crystallisation',
            'Crystals stained by the indicator, so the salt is impure',
            'A solution that will not crystallise however long it stands',
        ],
        "correct_index": 2,
        "why": 'The indicator is a dissolved substance like any other, so it is '
               'left behind in the solid when the water goes.',
    },
    {
        "id": 'ks4-salts-neutralisation-h12',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the formula of the insoluble salt formed when lead '
                'nitrate solution meets potassium iodide solution.',
        "options": [
            'PbI',
            'PbI2',
            'Pb2I',
            'PbI3',
        ],
        "correct_index": 1,
        "why": 'A lead(II) ion carries a 2+ charge and each iodide ion a single '
               'negative charge, so two iodides balance one lead.',
    },
    {
        "id": 'ks4-salts-neutralisation-h13',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student uses tap water instead of distilled water to wash a '
                'precipitate. Evaluate the effect on the dried product.',
        "options": [
            'No effect, because plain water cannot change a solid that it does not dissolve',
            'The product is heavier, because tap water is denser than distilled',
            'The product dissolves away, because tap water is slightly acidic',
            'The product may be impure, because tap water leaves dissolved solids',
        ],
        "correct_index": 3,
        "why": 'Tap water carries dissolved ions that are deposited on the '
               'solid as the rinse water dries.',
    },
    {
        "id": 'ks4-salts-neutralisation-h14',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why calcium carbonate is a poor choice of base for '
                'preparing calcium sulfate from sulfuric acid.',
        "options": [
            'Calcium sulfate is barely soluble and coats the carbonate',
            'Calcium carbonate will not react with dilute sulfuric acid',
            'Calcium sulfate decomposes as soon as it is formed in the acid',
            'Calcium carbonate dissolves, so no excess could be filtered off',
        ],
        "correct_index": 0,
        "why": 'The calcium sulfate formed stays as a solid layer over the '
               'carbonate, so the reaction stalls before it is complete.',
    },
    {
        "id": 'ks4-salts-neutralisation-h15',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a student who leaves the filtrate uncovered for a '
                'fortnight finds large well-shaped crystals.',
        "options": [
            'The salt has reacted further with the air over that time',
            'Water left very slowly, so the crystals grew slowly and evenly',
            'The cold bench froze the solution into regular shapes',
            'Dust settling on the surface of the liquid gave the crystals their shape',
        ],
        "correct_index": 1,
        "why": 'Slow loss of solvent gives the particles time to settle into an '
               'ordered lattice, which is what makes large crystals.',
    },
    {
        "id": 'ks4-salts-neutralisation-h16',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce the two solutions a technician should mix to make a '
                'sample of calcium carbonate.',
        "options": [
            'Calcium chloride solution and sodium carbonate solution',
            'Calcium carbonate solution and sodium chloride solution together',
            'Calcium nitrate solution and sodium chloride solution',
            'Calcium hydroxide solution and sodium sulfate solution',
        ],
        "correct_index": 0,
        "why": 'Both starting solutions dissolve, and between them they supply '
               'the calcium and carbonate ions that form the insoluble solid.',
    },
    {
        "id": 'ks4-salts-neutralisation-h17',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the mass of salt collected is almost always less '
                'than the mass calculated from the acid used.',
        "options": [
            'The balance reads low once the basin has been heated',
            'Some of the salt evaporates along with the water',
            'Some of the acid evaporates as a gas before it can react with the base',
            'Some of the salt is lost on the filter paper and the glassware',
        ],
        "correct_index": 3,
        "why": 'Transfer losses at each stage mean not all of the product ever '
               'reaches the final sample.',
    },
    {
        "id": 'ks4-salts-neutralisation-h18',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A white precipitate forms when two colourless solutions meet, '
                'and the mixture still conducts electricity afterwards. Explain '
                'why it conducts.',
        "options": [
            'The precipitate itself carries the current through the liquid',
            'The remaining soluble salt leaves its ions in the solution',
            'Water alone conducts once a solid has been formed in it',
            'The precipitate slowly redissolves and restores the ions',
        ],
        "correct_index": 1,
        "why": 'Only two of the four ions leave as the precipitate; the other '
               'two stay dissolved and are free to move.',
    },
    {
        "id": 'ks4-salts-neutralisation-h19',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the purity of a salt made by the excess-solid route '
                'with one made by an indicator titration.',
        "options": [
            'The titration salt is the purer, because the volumes are measured exactly',
            'Both are equally pure, since both use the same acid',
            'The excess-solid salt is purer, because no indicator is present',
            'Neither can be pure, because water is always left behind',
        ],
        "correct_index": 2,
        "why": 'Filtering removes the only impurity in the excess-solid route, '
               'while an indicator left in a titration mixture colours the salt.',
    },
    {
        "id": 'ks4-salts-neutralisation-h20',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a precipitation reaction is used to remove lead '
                'ions from contaminated water.',
        "options": [
            'The lead evaporates once the second solution has been added',
            'The lead is neutralised by the added solution',
            'The lead is turned into an insoluble solid that can be filtered out',
            'The lead dissolves more completely and is then diluted away',
        ],
        "correct_index": 2,
        "why": 'Once the lead is locked into a solid that will not dissolve, '
               'filtration takes it out of the water altogether.',
    },
    {
        "id": 'ks4-salts-neutralisation-h21',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine which reagent is in excess if a solid is still '
                'visible after stirring dilute acid with a metal carbonate.',
        "options": [
            'The acid, because it is the liquid of the two',
            'The carbonate, because some of it is left unreacted',
            'Neither, because they are always used in equal amounts',
            'Both, because each is present in the beaker at the end',
        ],
        "correct_index": 1,
        "why": 'Solid remaining once the fizzing has stopped shows that the '
               'acid ran out first and the carbonate is in excess.',
    },
    {
        "id": 'ks4-salts-neutralisation-h22',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what a student would see on adding more sodium sulfate '
                'solution to a mixture in which barium sulfate has already '
                'stopped forming.',
        "options": [
            'More precipitate, because extra sulfate always makes more solid',
            'No further precipitate, because the barium ions are used up',
            'The precipitate dissolves again in the extra solution',
            'The mixture turns yellow as the excess sulfate builds up',
        ],
        "correct_index": 1,
        "why": 'Once every barium ion has been captured, adding more of the '
               'other reactant has nothing left to react with.',
    },
    {
        "id": 'ks4-salts-neutralisation-h23',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the same ionic equation describes the precipitation '
                'of silver chloride from several different pairs of solutions.',
        "options": [
            'All silver salts behave in exactly the same way in water',
            'Every one of the chloride solutions contains the same silver compound',
            'The spectator ions react first and are then replaced',
            'Only silver ions and chloride ions take part; the rest look on',
        ],
        "correct_index": 3,
        "why": 'Whatever brings the silver and the chloride, the change itself '
               'is those two ions joining into an insoluble solid.',
    },
    {
        "id": 'ks4-salts-neutralisation-h24',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student prepares nickel sulfate and reports a yield above '
                '100 per cent. Suggest the most likely reason.',
        "options": [
            'The reaction produced extra salt from the water present',
            'The crystals were still damp when they were weighed',
            'The balance was set to grams instead of kilograms',
            'Too much acid was used, so extra nickel dissolved',
        ],
        "correct_index": 1,
        "why": 'Water clinging to the crystals is weighed as though it were '
               'product, which pushes the apparent yield past 100 per cent.',
    },
    {
        "id": 'ks4-salts-neutralisation-h25',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that any salt can be made by mixing two '
                'solutions together.',
        "options": [
            'Correct, since mixing two solutions always makes a new salt',
            'Correct, provided one of the two solutions is an acid',
            'Wrong, because that route only works for an insoluble salt',
            'Wrong, because two solutions cannot react with one another',
        ],
        "correct_index": 2,
        "why": 'A soluble salt would simply stay dissolved among the other '
               'ions, so nothing could be separated out.',
    },
    {
        "id": 'ks4-salts-neutralisation-h26',
        "subtopic_slug": 'salts-neutralisation',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the filtrate rather than the residue is heated when '
                'copper chloride crystals are being prepared.',
        "options": [
            'The residue is the salt, and heating it would decompose it',
            'The residue holds the water that has to be evaporated away',
            'The filtrate contains the dissolved salt; the residue is leftover base',
            'The filtrate is only waste acid and is heated to destroy it',
        ],
        "correct_index": 2,
        "why": 'Copper chloride is soluble, so it passes through the paper and '
               'is recovered by driving off the water from the filtrate.',
    },
]
