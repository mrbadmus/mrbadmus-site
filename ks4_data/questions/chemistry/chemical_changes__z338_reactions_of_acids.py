"""Chemistry · Chemical changes — the MRB-338 expansion for `reactions-of-acids`.

Four reaction patterns and the salt each one leaves behind: acid with a metal,
with a metal oxide, with a metal hydroxide and with a carbonate. The weight sits
on the two places pupils lose marks — forgetting that a carbonate gives three
products rather than two, and building the salt's name from the wrong half of
the pair — so the rows keep asking for the products, the salt and the observed
change in named contexts rather than in the abstract.

The reactivity limit carries much of the rest: only a metal above hydrogen
releases hydrogen from a dilute acid, which is why copper oxide dissolves in
warm acid while copper metal sits unchanged in it. The two gas tests appear as
observations to be read rather than as a list to be recalled. No pH values, no
titration technique and no ionic equations — all three belong to neighbouring
leaves.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-reactions-of-acids-e05',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the two products formed when dilute acid is neutralised '
                'by an alkali.',
        "options": [
            'A salt and water',
            'A salt and hydrogen',
            'A salt and carbon dioxide',
            'An oxide and water',
        ],
        "correct_index": 0,
        "why": 'Neutralisation joins the hydrogen ions from the acid to the '
               'hydroxide ions from the alkali, leaving a salt and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-e06',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the family of salts that sulfuric acid produces.',
        "options": [
            'Sulfates',
            'Sulfides',
            'Sulfites',
            'Sulfur',
        ],
        "correct_index": 0,
        "why": 'Sulfuric acid, H2SO4, hands over the sulfate ion, so every salt '
               'it makes is a sulfate.',
    },
    {
        "id": 'ks4-reactions-of-acids-e07',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is meant by an alkali.',
        "options": [
            'A base that will not dissolve however much water is added to it',
            'Any solution that turns damp blue litmus paper red',
            'A base that dissolves in water and gives hydroxide ions',
            'A substance that releases hydrogen ions into water',
        ],
        "correct_index": 2,
        "why": 'An alkali is a soluble base, so dissolving it puts hydroxide '
               'ions, OH-, into the solution.',
    },
    {
        "id": 'ks4-reactions-of-acids-e08',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the gas given off when zinc is dropped into dilute '
                'hydrochloric acid.',
        "options": [
            'Chlorine',
            'Hydrogen',
            'Hydrogen chloride',
            'Oxygen',
        ],
        "correct_index": 1,
        "why": 'A metal above hydrogen in the reactivity series displaces '
               'hydrogen from a dilute acid, leaving a salt behind.',
    },
    {
        "id": 'ks4-reactions-of-acids-e09',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the metal that does not react with dilute sulfuric acid.',
        "options": [
            'Calcium',
            'Zinc',
            'Iron',
            'Copper',
        ],
        "correct_index": 3,
        "why": 'Copper sits below hydrogen in the reactivity series, so it '
               'cannot push hydrogen out of an acid.',
    },
    {
        "id": 'ks4-reactions-of-acids-e10',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper carbonate is stirred into dilute nitric acid. Name the '
                'three products formed.',
        "options": [
            'Copper nitrate, water and carbon dioxide',
            'Copper nitrate, water and hydrogen gas',
            'Copper nitrate, together with hydrogen and oxygen',
            'Copper oxide, water and carbon dioxide',
        ],
        "correct_index": 0,
        "why": 'An acid and a metal carbonate give a salt, water and carbon '
               'dioxide, and nitric acid makes nitrate salts.',
    },
    {
        "id": 'ks4-reactions-of-acids-e11',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the formula of nitric acid.',
        "options": [
            'HNO2',
            'H2SO4',
            'HNO3',
            'HCl',
        ],
        "correct_index": 2,
        "why": 'Nitric acid is HNO3 — one hydrogen joined to one nitrate group.',
    },
    {
        "id": 'ks4-reactions-of-acids-e12',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Dilute hydrochloric acid is poured onto marble chips. State '
                'what is seen.',
        "options": [
            'The chips glow red hot and give out a bright white light',
            'The liquid turns deep blue and no bubbles escape',
            'The chips float to the surface and stay unchanged',
            'The chips fizz steadily and slowly get smaller',
        ],
        "correct_index": 3,
        "why": 'Marble is calcium carbonate, so the acid releases carbon '
               'dioxide and the solid dissolves away as calcium chloride forms.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-reactions-of-acids-s05',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium ribbon is added to dilute sulfuric acid. Name the '
                'salt that forms.',
        "options": [
            'Magnesium sulfide',
            'Magnesium hydroxide',
            'Magnesium chloride',
            'Magnesium sulfate',
        ],
        "correct_index": 3,
        "why": 'The metal supplies the first half of the name and the acid the '
               'second, so sulfuric acid and magnesium give magnesium sulfate.',
    },
    {
        "id": 'ks4-reactions-of-acids-s06',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Choose the pair of substances that would be used to prepare '
                'potassium sulfate.',
        "options": [
            'Potassium hydroxide and dilute sulfuric acid',
            'Potassium hydroxide and dilute nitric acid',
            'Potassium chloride and dilute sulfuric acid',
            'Potassium sulfide and warm dilute hydrochloric acid',
        ],
        "correct_index": 0,
        "why": 'The metal comes from the hydroxide and the sulfate from the '
               'acid, so potassium hydroxide with sulfuric acid is the pair.',
    },
    {
        "id": 'ks4-reactions-of-acids-s07',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Calcium hydroxide is neutralised by dilute nitric acid. Name '
                'the two products.',
        "options": [
            'Calcium nitrate and hydrogen gas only',
            'Calcium nitrate and water',
            'Calcium nitrite and water',
            'Calcium oxide and water',
        ],
        "correct_index": 1,
        "why": 'An acid neutralised by a metal hydroxide gives only a salt and '
               'water, with no gas released at all.',
    },
    {
        "id": 'ks4-reactions-of-acids-s08',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a metal oxide such as zinc oxide is classed as a base.',
        "options": [
            'It dissolves readily in water to give a clear alkaline solution',
            'It neutralises an acid, giving a salt and water',
            'It releases hydrogen ions when it is warmed with water',
            'It reacts with other oxides to make a larger oxide',
        ],
        "correct_index": 1,
        "why": 'A base is anything that neutralises an acid, and a metal oxide '
               'does exactly that, producing a salt and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-s09',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium is dropped into dilute hydrochloric acid. Choose '
                'the symbol equation that balances.',
        "options": [
            'Mg + HCl -> MgCl2 + H2',
            'Mg + 2HCl -> MgCl + H2',
            'Mg + 2HCl -> MgCl2 + H2',
            'Mg + 2HCl -> MgCl2 + 2H2',
        ],
        "correct_index": 2,
        "why": 'Two chlorines are needed to balance MgCl2, and the two hydrogen '
               'atoms released pair up as one H2 molecule.',
    },
    {
        "id": 'ks4-reactions-of-acids-s10',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Green copper carbonate powder is added to warm dilute sulfuric '
                'acid. Describe the colour change seen in the liquid.',
        "options": [
            'It stays completely colourless throughout',
            'It turns from colourless to blue',
            'It turns from colourless to green',
            'It turns from colourless to orange',
        ],
        "correct_index": 1,
        "why": 'The copper sulfate formed dissolves to give the familiar blue '
               'solution, while the green solid disappears.',
    },
    {
        "id": 'ks4-reactions-of-acids-s11',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A white solid fizzes when dilute acid is dripped onto it, and '
                'the gas given off will not burn. Identify what the solid '
                'must contain.',
        "options": [
            'A metal, because only a metal can release a gas',
            'An oxide, because every oxide releases oxygen with acids',
            'A hydroxide, because hydroxides fizz with acids',
            'A carbonate, because it releases carbon dioxide',
        ],
        "correct_index": 3,
        "why": 'Of the common bases only a carbonate releases a gas with dilute '
               'acid, and that gas is carbon dioxide.',
    },
    {
        "id": 'ks4-reactions-of-acids-s12',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Complete the word equation: sodium carbonate + sulfuric acid -> ?',
        "options": [
            'Sodium sulfate + water + carbon dioxide',
            'Sodium sulfate + hydrogen + carbon dioxide',
            'Sodium sulfide + water + carbon dioxide',
            'Sodium sulfate + water only',
        ],
        "correct_index": 0,
        "why": 'Sulfuric acid gives a sulfate, and a carbonate always releases '
               'water and carbon dioxide alongside the salt.',
    },
    {
        "id": 'ks4-reactions-of-acids-s13',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Marble chips and dilute hydrochloric acid are reacted in an '
                'open conical flask on a balance. Explain why the reading falls.',
        "options": [
            'The acid evaporates away as the flask warms up',
            'The marble chips shrink, so the flask holds far less matter',
            'Carbon dioxide gas escapes from the open flask',
            'Water is used up as the reaction proceeds',
        ],
        "correct_index": 2,
        "why": 'Mass is conserved overall, but the carbon dioxide leaves the '
               'open flask and so is no longer weighed.',
    },
    {
        "id": 'ks4-reactions-of-acids-s14',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify which of these substances is a base but not an alkali.',
        "options": [
            'Sodium hydroxide',
            'Potassium hydroxide',
            'Copper(II) oxide',
            'Calcium hydroxide',
        ],
        "correct_index": 2,
        "why": 'Copper(II) oxide neutralises acids but is insoluble, and only a '
               'soluble base counts as an alkali.',
    },
    {
        "id": 'ks4-reactions-of-acids-s15',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the acid a technician would choose to make zinc nitrate '
                'from zinc oxide.',
        "options": [
            'Dilute hydrochloric acid',
            'Dilute sulfuric acid',
            'Dilute nitric acid',
            'Dilute carbonic acid',
        ],
        "correct_index": 2,
        "why": 'The nitrate half of the salt can only come from nitric acid, '
               'with the zinc supplied by the oxide.',
    },
    {
        "id": 'ks4-reactions-of-acids-s16',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why bubbling carbon dioxide through limewater makes it '
                'turn milky.',
        "options": [
            'A fine solid of calcium carbonate forms in the liquid',
            'The gas dissolves and colours the liquid pale white',
            'The limewater boils, and the bubbles cloud the liquid',
            'Calcium metal is released and floats as specks through the liquid',
        ],
        "correct_index": 0,
        "why": 'The gas reacts with the dissolved calcium hydroxide to make '
               'insoluble calcium carbonate, which clouds the liquid.',
    },
    {
        "id": 'ks4-reactions-of-acids-s17',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron(III) oxide is warmed with dilute sulfuric acid. Name the '
                'salt formed.',
        "options": [
            'Iron(III) sulfide',
            'Iron(II) sulfate',
            'Iron(III) sulfite',
            'Iron(III) sulfate',
        ],
        "correct_index": 3,
        "why": 'The iron keeps its 3+ charge from the oxide and sulfuric acid '
               'supplies the sulfate, giving iron(III) sulfate.',
    },
    {
        "id": 'ks4-reactions-of-acids-s18',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the fizzing stops when zinc granules are left in a '
                'fixed volume of dilute hydrochloric acid.',
        "options": [
            'The zinc has become coated and cannot react any further',
            'The mixture has cooled too far for a reaction to continue',
            'The hydrogen produced has pushed all of the acid out of the tube',
            'All the acid has been used up, so no more can react',
        ],
        "correct_index": 3,
        "why": 'With the metal in excess, the acid is the limiting reactant, so '
               'the reaction ends when the last of it has reacted.',
    },
    {
        "id": 'ks4-reactions-of-acids-s19',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe the test that tells hydrogen apart from carbon dioxide.',
        "options": [
            'Hydrogen relights a glowing splint; carbon dioxide puts it out',
            'Hydrogen turns limewater milky; carbon dioxide leaves it clear',
            'Hydrogen pops with a lit splint; carbon dioxide puts it out',
            'Hydrogen bleaches damp litmus; carbon dioxide turns it blue',
        ],
        "correct_index": 2,
        "why": 'Hydrogen burns with a squeaky pop, while carbon dioxide does '
               'not burn and smothers the flame instead.',
    },
    {
        "id": 'ks4-reactions-of-acids-s20',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A magnesium ion carries a 2+ charge and a chloride ion a 1- '
                'charge. State the formula of magnesium chloride.',
        "options": [
            'MgCl',
            'MgCl2',
            'Mg2Cl',
            'MgCl3',
        ],
        "correct_index": 1,
        "why": 'A magnesium ion carries a 2+ charge and a chloride ion a single '
               'negative charge, so two chlorides are needed.',
    },
    {
        "id": 'ks4-reactions-of-acids-s21',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Potassium carbonate solution is added to dilute sulfuric acid. '
                'Name the salt left in the solution.',
        "options": [
            'Potassium sulfate',
            'Potassium sulfite',
            'Potassium carbonate',
            'Potassium hydroxide',
        ],
        "correct_index": 0,
        "why": 'The potassium pairs with the sulfate from the acid, while the '
               'carbonate leaves as carbon dioxide and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-s22',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a metal oxide and a metal hydroxide give the same '
                'two products when each is added to the same acid.',
        "options": [
            'Both are bases, so each gives a salt and water',
            'Both contain the same metal in exactly the same proportion',
            'Both dissolve first, so both behave as an alkali',
            'Both release a gas, which then condenses to water',
        ],
        "correct_index": 0,
        "why": 'Oxides and hydroxides are both bases, and every base neutralised '
               'by an acid gives a salt together with water.',
    },
    {
        "id": 'ks4-reactions-of-acids-s23',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Sodium hydroxide solution is neutralised by dilute sulfuric '
                'acid. Determine how many sodium hydroxide formula units react '
                'with each sulfuric acid molecule.',
        "options": [
            'One',
            'Two',
            'Three',
            'Four',
        ],
        "correct_index": 1,
        "why": 'Sulfuric acid supplies two hydrogen ions, so two hydroxide ions '
               'are needed, one from each sodium hydroxide.',
    },
    {
        "id": 'ks4-reactions-of-acids-s24',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why limestone buildings slowly wear away in areas of '
                'acidic rainfall.',
        "options": [
            'The rain dissolves the limestone without reacting with it',
            'The acid reacts with the carbonate, so the stone dissolves',
            'The rain freezes inside the stone and splits it apart',
            'The acid coats the stone in a layer that flakes off dry',
        ],
        "correct_index": 1,
        "why": 'Limestone is calcium carbonate, and an acid converts it to a '
               'soluble salt, water and carbon dioxide, so stone is lost.',
    },
    {
        "id": 'ks4-reactions-of-acids-s25',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the acid needed to turn calcium carbonate into calcium '
                'chloride.',
        "options": [
            'Dilute nitric acid',
            'Dilute sulfuric acid',
            'Dilute hydrochloric acid',
            'Dilute phosphoric acid',
        ],
        "correct_index": 2,
        "why": 'Only hydrochloric acid supplies chloride ions, so it is the '
               'acid that turns a carbonate into a chloride.',
    },
    {
        "id": 'ks4-reactions-of-acids-s26',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what happens to the temperature of the mixture when '
                'dilute acid is neutralised by an alkali.',
        "options": [
            'It falls, because heat is taken in',
            'It rises, because the reaction releases energy',
            'It stays the same while mixing',
            'It rises then falls below the start',
        ],
        "correct_index": 1,
        "why": 'Neutralisation is exothermic, so the mixture warms as the '
               'hydrogen and hydroxide ions combine to form water.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-reactions-of-acids-h05',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the formula of the salt formed when calcium '
                'hydroxide is neutralised by dilute nitric acid.',
        "options": [
            'CaNO3',
            'Ca(NO3)2',
            'Ca2NO3',
            'Ca(NO2)2',
        ],
        "correct_index": 1,
        "why": 'A calcium ion carries a 2+ charge and each nitrate ion a single '
               'negative charge, so two nitrates balance one calcium.',
    },
    {
        "id": 'ks4-reactions-of-acids-h06',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Magnesium fizzes in dilute sulfuric acid, but magnesium oxide '
                'does not. Explain the difference.',
        "options": [
            'The oxide is insoluble, so no reaction can take place at all',
            'The oxide has already reacted, so its metal is used up',
            'The oxide is below hydrogen in the reactivity series',
            'The oxide is a base, and an acid with a base gives no gas',
        ],
        "correct_index": 3,
        "why": 'Acid with a metal gives hydrogen, but acid with a metal oxide '
               'gives only the salt and water, so nothing bubbles off.',
    },
    {
        "id": 'ks4-reactions-of-acids-h07',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Sodium carbonate is tipped into dilute sulfuric acid. Select '
                'the symbol equation that is balanced.',
        "options": [
            'Na2CO3 + H2SO4 -> Na2SO4 + H2O + CO2',
            'Na2CO3 + 2H2SO4 -> Na2SO4 + H2O + CO2',
            'Na2CO3 + H2SO4 -> NaSO4 + H2O + CO2',
            'Na2CO3 + H2SO4 -> Na2SO4 + H2 + CO2',
        ],
        "correct_index": 0,
        "why": 'One sulfuric acid supplies the two hydrogen ions that the two '
               'sodium ions release, and those hydrogens end up in water.',
    },
    {
        "id": 'ks4-reactions-of-acids-h08',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Excess magnesium is added to 50 cm3 of dilute hydrochloric '
                'acid. Determine what fixes the total volume of hydrogen made.',
        "options": [
            'The mass of magnesium added to the flask',
            'The surface area of the magnesium ribbon used',
            'The amount of acid present at the start',
            'The temperature the mixture reaches during the reaction',
        ],
        "correct_index": 2,
        "why": 'With the metal in excess the acid runs out first, so the acid '
               'alone decides how much hydrogen can be made.',
    },
    {
        "id": 'ks4-reactions-of-acids-h09',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Equal pieces of magnesium and of zinc are placed in separate '
                'tubes of the same dilute acid. Compare what is seen.',
        "options": [
            'Neither fizzes, because both lie below hydrogen',
            'The zinc fizzes faster, because zinc is the denser metal',
            'Both fizz at exactly the same rate as each other',
            'The magnesium fizzes faster, because it is more reactive',
        ],
        "correct_index": 3,
        "why": 'Both metals sit above hydrogen so both react, but magnesium is '
               'higher in the series and so reacts more vigorously.',
    },
    {
        "id": 'ks4-reactions-of-acids-h10',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper metal leaves dilute nitric acid unchanged, yet copper '
                'oxide dissolves in it readily. Explain why.',
        "options": [
            'The oxide is a powder, and powders react while lumps do not',
            'The metal is protected by a coat of oxide that the acid cannot cross',
            'The metal would have to displace hydrogen, which it cannot do',
            'The oxide is already oxidised, so the acid can reduce it easily',
        ],
        "correct_index": 2,
        "why": 'Reacting with the metal would mean pushing hydrogen out of the '
               'acid, and copper is below hydrogen, but neutralising an oxide '
               'needs no such displacement.',
    },
    {
        "id": 'ks4-reactions-of-acids-h11',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Marble chips and dilute acid react inside a sealed flask on a '
                'balance. Predict the reading and justify the prediction.',
        "options": [
            'It falls, because the gas made is lighter than the solid',
            'It rises, because a gas takes up far more space than any solid does',
            'It falls at first and then returns to its starting value',
            'It stays the same, because no gas can leave the flask',
        ],
        "correct_index": 3,
        "why": 'The carbon dioxide is still inside the sealed flask, so every '
               'atom present at the start is still being weighed.',
    },
    {
        "id": 'ks4-reactions-of-acids-h12',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A salt is found to be potassium nitrate. Deduce the acid and '
                'the base that were used to make it.',
        "options": [
            'Nitric acid and potassium hydroxide',
            'Nitric acid and sodium hydroxide',
            'Hydrochloric acid and potassium nitrate',
            'Sulfuric acid and potassium hydroxide',
        ],
        "correct_index": 0,
        "why": 'The metal half of the name points to a potassium base and the '
               'nitrate half to nitric acid.',
    },
    {
        "id": 'ks4-reactions-of-acids-h13',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student claims that any metal will fizz in any dilute acid. '
                'Evaluate the claim.',
        "options": [
            'Correct, because every metal reacts with every acid',
            'Correct, but only if the acid is warmed beforehand',
            'Wrong, because a metal below hydrogen releases no gas',
            'Wrong, because a dilute acid is too weak to attack a metal',
        ],
        "correct_index": 2,
        "why": 'Only metals above hydrogen in the reactivity series can displace '
               'hydrogen, so copper, silver and gold give nothing.',
    },
    {
        "id": 'ks4-reactions-of-acids-h14',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Iron(III) sulfate is prepared from iron(III) oxide and warm '
                'sulfuric acid. Determine its formula.',
        "options": [
            'FeSO4',
            'Fe3SO4',
            'Fe2(SO4)3',
            'Fe(SO4)3',
        ],
        "correct_index": 2,
        "why": 'Two iron ions at 3+ carry six positive charges, which three '
               'sulfate ions at 2- exactly balance.',
    },
    {
        "id": 'ks4-reactions-of-acids-h15',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Dilute sulfuric acid is added to barium carbonate. Explain why '
                'the fizzing soon stops even with acid left over.',
        "options": [
            'The barium sulfate made is insoluble and coats the solid',
            'The carbon dioxide dissolves back into the acid and blocks it off',
            'Barium carbonate is too unreactive for acid to attack it',
            'Sulfuric acid is used up far faster than any other acid',
        ],
        "correct_index": 0,
        "why": 'Barium sulfate will not dissolve, so it builds up as a layer '
               'that keeps the acid away from the carbonate beneath.',
    },
    {
        "id": 'ks4-reactions-of-acids-h16',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which two solids would both give zinc chloride when '
                'added to dilute hydrochloric acid.',
        "options": [
            'Zinc oxide and zinc carbonate',
            'Zinc oxide and zinc sulfate',
            'Zinc sulfate and zinc carbonate',
            'Zinc chloride and zinc sulfide',
        ],
        "correct_index": 0,
        "why": 'Both an oxide and a carbonate are bases neutralised by the acid, '
               'and each leaves the zinc paired with chloride.',
    },
    {
        "id": 'ks4-reactions-of-acids-h17',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An unknown carbonate fizzes with dilute nitric acid and leaves '
                'a blue solution. Identify the metal in the carbonate.',
        "options": [
            'Sodium',
            'Copper',
            'Calcium',
            'Magnesium',
        ],
        "correct_index": 1,
        "why": 'Copper salts in solution are blue, while the sodium, calcium '
               'and magnesium salts of nitric acid are all colourless.',
    },
    {
        "id": 'ks4-reactions-of-acids-h18',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the number of products formed when dilute acid reacts '
                'with a metal hydroxide and with a metal carbonate.',
        "options": [
            'Two from each, because both are bases of the same kind',
            'Three from each, since water forms in both reactions',
            'Two from the hydroxide and three from the carbonate',
            'Three from the hydroxide and two from the carbonate',
        ],
        "correct_index": 2,
        "why": 'A hydroxide gives a salt and water alone, while a carbonate '
               'adds carbon dioxide as a third product.',
    },
    {
        "id": 'ks4-reactions-of-acids-h19',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A technician needs a steady supply of hydrogen gas. Choose the '
                'pair that would deliver it.',
        "options": [
            'Copper turnings and dilute sulfuric acid',
            'Zinc granules and dilute sulfuric acid',
            'Zinc carbonate and dilute sulfuric acid',
            'Copper oxide and dilute hydrochloric acid',
        ],
        "correct_index": 1,
        "why": 'Only a metal above hydrogen reacting with a dilute acid gives '
               'hydrogen, and of these pairs only zinc metal qualifies.',
    },
    {
        "id": 'ks4-reactions-of-acids-h20',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why adding more dilute acid to a flask of excess marble '
                'chips increases the total volume of gas collected.',
        "options": [
            'More acid warms the flask, so the chips break faster',
            'More acid raises the pressure, forcing out extra gas',
            'More acid means more particles able to attack the carbonate',
            'More acid makes the chips dissolve without reacting',
        ],
        "correct_index": 2,
        "why": 'The chips are in excess, so the acid is limiting, and extra acid '
               'converts more of the carbonate into carbon dioxide.',
    },
    {
        "id": 'ks4-reactions-of-acids-h21',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why an indigestion remedy containing magnesium '
                'carbonate makes a patient belch.',
        "options": [
            'The carbonate traps air, which is released in the stomach',
            'The magnesium metal in it displaces hydrogen from the stomach acid',
            'The remedy boils at body temperature and gives off steam',
            'Stomach acid reacts with it and releases carbon dioxide',
        ],
        "correct_index": 3,
        "why": 'The hydrochloric acid in the stomach neutralises the carbonate, '
               'and the carbon dioxide that forms has to escape.',
    },
    {
        "id": 'ks4-reactions-of-acids-h22',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would be observed if a lit splint were held over '
                'a flask in which a carbonate was reacting with dilute acid.',
        "options": [
            'A squeaky pop, because the gas given off burns',
            'A bright white flame across the flask neck',
            'The splint would go out, because the gas does not burn at all',
            'The splint would relight, because oxygen forms',
        ],
        "correct_index": 2,
        "why": 'The gas is carbon dioxide, which neither burns nor supports '
               'burning, so the flame is smothered.',
    },
    {
        "id": 'ks4-reactions-of-acids-h23',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce the acid used if a sulfate salt and no gas at all were '
                'produced from a metal oxide.',
        "options": [
            'Hydrochloric acid, because chlorides give no gas',
            'Sulfuric acid, because the salt made is a sulfate',
            'Nitric acid, because nitrates are made without any gas',
            'Carbonic acid, because it is too weak to release a gas',
        ],
        "correct_index": 1,
        "why": 'The anion in the salt names the acid, and an oxide with any acid '
               'gives only a salt and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-h24',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Calcium hydroxide is spread on acidic farmland. Explain how it '
                'improves the soil.',
        "options": [
            'It coats the soil and stops more acid rain soaking in',
            'It releases carbon dioxide, which drives the acid out of the soil',
            'It dissolves the acid without reacting with any of it',
            'It neutralises the acid, forming a salt and water',
        ],
        "correct_index": 3,
        "why": 'Calcium hydroxide is a base, so it reacts with the acid in the '
               'soil to leave a neutral salt and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-h25',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two tubes hold the same dilute acid. One is given magnesium '
                'carbonate and the other magnesium hydroxide. Compare the gases.',
        "options": [
            'Both give hydrogen, since both contain a metal',
            'Both give carbon dioxide, since both hold carbon',
            'The carbonate gives carbon dioxide; the hydroxide gives none',
            'The hydroxide gives hydrogen; the carbonate none',
        ],
        "correct_index": 2,
        "why": 'Only the carbonate has a carbonate group to release as carbon '
               'dioxide, and a hydroxide with acid gives just salt and water.',
    },
    {
        "id": 'ks4-reactions-of-acids-h26',
        "subtopic_slug": 'reactions-of-acids',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a chemist warms the dilute acid gently before '
                'stirring in a powdered metal oxide.',
        "options": [
            'Warming makes the reaction faster without changing the products',
            'Warming turns the oxide into a hydroxide first',
            'Warming increases the amount of salt that can be formed',
            'Warming is needed before an acid will act as an acid',
        ],
        "correct_index": 0,
        "why": 'Heat raises the rate of a slow reaction between an acid and an '
               'insoluble base, but the salt and water formed are the same.',
    },
]
