"""Chemistry · Chemical changes — the MRB-338 expansion for `strong-weak-acids`.

One distinction and one confusion. The distinction is the degree of ionisation:
a strong acid hands over every hydrogen ion, a weak acid only a small fraction
of them, and the one-way arrow against the reversible arrow is where that is
written down. The confusion is strength against concentration, and the leaf
returns to it from several sides because it is the error AQA examiners report
most often on this spec point.

The consequences carry the applied and harder rows: conductivity, the vigour of
a reaction with a metal or a carbonate, the same total gas from the same number
of moles, the pH of two solutions at matched concentration, and the tenfold rule
that links a change in hydrogen ion concentration to a change of one pH unit.
Named weak acids — ethanoic, citric, carbonic, lactic — give the real contexts.
Indicator colours and the pH scale itself belong to `ph-scale`.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-strong-weak-acids-e05',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what is meant by a weak acid.',
        "options": [
            'An acid that has been diluted with plenty of water',
            'An acid with very few moles in each cubic decimetre',
            'An acid that cannot neutralise an alkali',
            'An acid that is only partly ionised in water',
        ],
        "correct_index": 3,
        "why": 'Weakness is about the fraction of molecules that release their '
               'hydrogen ion, not about how much acid is present.',
    },
    {
        "id": 'ks4-strong-weak-acids-e06',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify which of these is a strong acid.',
        "options": [
            'Citric acid',
            'Carbonic acid',
            'Nitric acid',
            'Lactic acid',
        ],
        "correct_index": 2,
        "why": 'Nitric acid ionises completely in water, while citric, carbonic '
               'and lactic acids all ionise only partly.',
    },
    {
        "id": 'ks4-strong-weak-acids-e07',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Name the acid found in vinegar.',
        "options": [
            'Hydrochloric acid',
            'Sulfuric acid',
            'Citric acid',
            'Ethanoic acid',
        ],
        "correct_index": 3,
        "why": 'Vinegar is a dilute solution of ethanoic acid, the standard '
               'laboratory example of a weak acid.',
    },
    {
        "id": 'ks4-strong-weak-acids-e08',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what the term concentrated tells you about an acid.',
        "options": [
            'How completely its molecules have ionised in water',
            'How many moles of it there are in each cubic decimetre',
            'How quickly it reacts with a piece of magnesium ribbon',
            'How corrosive it is to the skin when it is spilled',
        ],
        "correct_index": 1,
        "why": 'Concentration counts the acid present in a given volume and says '
               'nothing about how far it has ionised.',
    },
    {
        "id": 'ks4-strong-weak-acids-e09',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State the type of arrow used to write the ionisation of a '
                'strong acid.',
        "options": [
            'A dotted arrow with no arrowhead',
            'A pair of arrows pointing both ways at once',
            'A single arrow pointing one way',
            'A double-headed straight line',
        ],
        "correct_index": 2,
        "why": 'The change goes essentially to completion, so it is written with '
               'one arrow rather than a reversible pair.',
    },
    {
        "id": 'ks4-strong-weak-acids-e10',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Name the acid that gives a fizzy drink its sharp taste and its '
                'dissolved gas.',
        "options": [
            'Nitric acid',
            'Carbonic acid',
            'Hydrochloric acid',
            'Sulfuric acid',
        ],
        "correct_index": 1,
        "why": 'Carbon dioxide dissolved under pressure forms carbonic acid, a '
               'weak acid that releases the gas again when opened.',
    },
    {
        "id": 'ks4-strong-weak-acids-e11',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State which particle a strong acid releases into solution.',
        "options": [
            'The hydroxide ion',
            'The oxide ion',
            'The chloride ion from the acid',
            'The hydrogen ion',
        ],
        "correct_index": 3,
        "why": 'Every acid is an acid because of the hydrogen ions it puts into '
               'water; strength is how completely it does so.',
    },
    {
        "id": 'ks4-strong-weak-acids-e12',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State roughly what fraction of ethanoic acid molecules are '
                'ionised in a typical solution.',
        "options": [
            'Very nearly all of them',
            'About three quarters',
            'About one hundredth',
            'None of them',
        ],
        "correct_index": 2,
        "why": 'Only about one per cent of the molecules split up, which is what '
               'makes ethanoic acid a weak acid.',
    },
    {
        "id": 'ks4-strong-weak-acids-e13',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the acid produced by muscles during hard exercise.',
        "options": [
            'Lactic acid',
            'Ethanoic acid',
            'Carbonic acid',
            'Sulfuric acid',
        ],
        "correct_index": 0,
        "why": 'Lactic acid is a weak acid, so it ionises only partly in the '
               'watery surroundings of a muscle.',
    },
    {
        "id": 'ks4-strong-weak-acids-e14',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State which solution contains the greater number of hydrogen '
                'ions at the same concentration.',
        "options": [
            'The weak acid, because it holds ions in reserve',
            'The weak acid, because its molecules are larger',
            'Neither, because concentration fixes the number of ions',
            'The strong acid, because it ionises completely',
        ],
        "correct_index": 3,
        "why": 'At matched concentration the strong acid has released every '
               'hydrogen ion while the weak acid has released few.',
    },
    {
        "id": 'ks4-strong-weak-acids-e15',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A bottle is labelled dilute sulfuric acid. State what that '
                'label describes.',
        "options": [
            'That few of its molecules have ionised',
            'That it has a small amount of acid per unit volume',
            'That it will not burn the skin',
            'That it reacts just with the most reactive metals',
        ],
        "correct_index": 1,
        "why": 'Dilute is the opposite of concentrated and describes how much '
               'acid is present, not how far it has ionised.',
    },
    {
        "id": 'ks4-strong-weak-acids-e16',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Name the two ions formed when hydrochloric acid ionises in '
                'water.',
        "options": [
            'Hydrogen ions and hydroxide ions',
            'Hydrogen ions and chloride ions',
            'Chloride ions and oxide ions',
            'Hydroxide ions and chloride ions',
        ],
        "correct_index": 1,
        "why": 'The molecule splits into the hydrogen ion that makes it an acid '
               'and the chloride ion that names its salts.',
    },
    {
        "id": 'ks4-strong-weak-acids-e17',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State whether a weak acid can be concentrated.',
        "options": [
            'No, because weak and dilute mean the same thing',
            'No, because a weak acid can never be made concentrated enough',
            'Yes, because strength and concentration are separate ideas',
            'Yes, but after it has been heated for some time',
        ],
        "correct_index": 2,
        "why": 'Strength counts the fraction ionised and concentration counts '
               'the moles per cubic decimetre, so any combination is possible.',
    },
    {
        "id": 'ks4-strong-weak-acids-e18',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'easier',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what happens to most of the molecules of a weak acid in '
                'solution.',
        "options": [
            'They react with the water and are destroyed by it',
            'They split up and release their hydrogen ion instead',
            'They join together into much larger molecules',
            'They stay whole and keep their hydrogen atom',
        ],
        "correct_index": 3,
        "why": 'Only a small fraction ionise at any moment; the rest remain as '
               'undissociated molecules.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-strong-weak-acids-s05',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State how the pH changes when a strong acid is diluted ten '
                'times over.',
        "options": [
            'It remains unchanged',
            'It falls by one unit',
            'It rises by ten units',
            'It rises by one unit',
        ],
        "correct_index": 3,
        "why": 'Dividing the hydrogen ion concentration by ten moves the pH one '
               'place up the scale.',
    },
    {
        "id": 'ks4-strong-weak-acids-s06',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why the marble chips fizz more slowly in ethanoic acid '
                'than in hydrochloric acid of the same concentration.',
        "options": [
            'Ethanoic acid molecules are far too large to reach the marble',
            'Ethanoic acid has a much lower hydrogen ion concentration',
            'Ethanoic acid coats the marble and blocks its whole surface',
            'Ethanoic acid reacts with carbonates just when it is warm',
        ],
        "correct_index": 1,
        "why": 'It is the hydrogen ions that attack the carbonate, and a weak '
               'acid provides far fewer of them per cubic decimetre.',
    },
    {
        "id": 'ks4-strong-weak-acids-s07',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Deduce the pH of a 0.01 mol/dm3 solution of hydrochloric acid.',
        "options": [
            'pH 1',
            'pH 2',
            'pH 3',
            'pH 7',
        ],
        "correct_index": 1,
        "why": 'A strong acid is fully ionised, so 0.01 mol/dm3 of acid gives '
               '0.01 mol/dm3 of hydrogen ions, which is pH 2.',
    },
    {
        "id": 'ks4-strong-weak-acids-s08',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Describe an experiment that would show which of two acids at '
                'the same concentration is the stronger.',
        "options": [
            'Warm both and compare how quickly each one evaporates',
            'Weigh out equal masses of each and compare the volumes',
            'Add an indicator to each and compare the final colours',
            'Measure the pH of each with a meter and compare them',
        ],
        "correct_index": 3,
        "why": 'At matched concentration the lower pH belongs to whichever acid '
               'has released more hydrogen ions.',
    },
    {
        "id": 'ks4-strong-weak-acids-s09',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State how a bulb in a conductivity circuit behaves in a weak '
                'acid compared with a strong one of the same concentration.',
        "options": [
            'It glows more brightly, because the molecules are much bigger',
            'It does not glow, because a weak acid contains no ions to move',
            'It glows more dimly, because there are fewer ions present',
            'It glows just as brightly, because the concentrations match',
        ],
        "correct_index": 2,
        "why": 'Current through a solution is carried by ions, and a partly '
               'ionised acid supplies far fewer of them.',
    },
    {
        "id": 'ks4-strong-weak-acids-s10',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the correct way to write the ionisation of carbonic '
                'acid in water.',
        "options": [
            'H2CO3 -> 2H+ + CO3 2-',
            'H2CO3 is in equilibrium with H+ + HCO3-',
            'H2CO3 -> H+ + HCO3-',
            'H2CO3 is in equilibrium with OH- + HCO3-',
        ],
        "correct_index": 1,
        "why": 'Carbonic acid is weak, so the release of a hydrogen ion is '
               'written as a reversible change rather than a complete one.',
    },
    {
        "id": 'ks4-strong-weak-acids-s11',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why 1 mol/dm3 citric acid is less hazardous than '
                '1 mol/dm3 sulfuric acid.',
        "options": [
            'Citric acid is found in food, so it must be harmless',
            'Citric acid is much more dilute than the sulfuric acid',
            'Citric acid releases far fewer hydrogen ions into solution',
            'Citric acid molecules are too large to touch the skin',
        ],
        "correct_index": 2,
        "why": 'It is the hydrogen ion concentration that does the damage, and a '
               'weak acid at the same concentration supplies far less of it.',
    },
    {
        "id": 'ks4-strong-weak-acids-s12',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State what happens to the pH if the hydrogen ion concentration '
                'is multiplied by one hundred.',
        "options": [
            'It stays exactly where it was',
            'It falls by one hundred units',
            'It rises by two units',
            'It falls by two units',
        ],
        "correct_index": 3,
        "why": 'Each tenfold rise in hydrogen ion concentration lowers the pH by '
               'one, so a hundredfold rise lowers it by two.',
    },
    {
        "id": 'ks4-strong-weak-acids-s13',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Identify the correct equation for the ionisation of nitric acid '
                'in water.',
        "options": [
            'HNO3 is in equilibrium with H+ + NO3-',
            'HNO3 -> H+ + NO3-',
            'HNO3 -> OH- + NO3-',
            'HNO3 is in equilibrium with OH- + NO2-',
        ],
        "correct_index": 1,
        "why": 'Nitric acid is strong, so the ionisation goes to completion and '
               'takes a single arrow.',
    },
    {
        "id": 'ks4-strong-weak-acids-s14',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Compare the volume of alkali needed to neutralise 25 cm3 of '
                '0.1 mol/dm3 hydrochloric acid and 25 cm3 of 0.1 mol/dm3 '
                'ethanoic acid.',
        "options": [
            'More alkali is needed for the hydrochloric acid',
            'More alkali is needed for the ethanoic acid, which is weaker',
            'The same volume is needed for each of them',
            'No alkali is needed for the ethanoic acid',
        ],
        "correct_index": 2,
        "why": 'Neutralisation uses up the total acid present, and both '
               'solutions hold the same number of moles.',
    },
    {
        "id": 'ks4-strong-weak-acids-s15',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why hydrofluoric acid is described as weak even though '
                'it attacks glass.',
        "options": [
            'Attacking glass is not a chemical reaction',
            'It is weak just while it is kept inside a plastic bottle and sealed',
            'It becomes strong as soon as it touches any glass',
            'Weakness describes only its ionisation, not what it can attack',
        ],
        "correct_index": 3,
        "why": 'Strength is a statement about the fraction of molecules that '
               'ionise and says nothing about what a substance can corrode.',
    },
    {
        "id": 'ks4-strong-weak-acids-s16',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Predict the pH of 0.1 mol/dm3 hydrochloric acid.',
        "options": [
            'pH 0',
            'pH 1',
            'pH 2',
            'pH 4',
        ],
        "correct_index": 1,
        "why": 'Full ionisation gives 0.1 mol/dm3 of hydrogen ions, which sits '
               'at pH 1 on the scale.',
    },
    {
        "id": 'ks4-strong-weak-acids-s17',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'State why rainwater is slightly acidic even in clean air.',
        "options": [
            'Nitric acid is formed by lightning in every storm',
            'Sulfuric acid from volcanoes reaches all of the sky',
            'Carbon dioxide dissolves in it and forms carbonic acid',
            'Water itself is a weak acid once it leaves a cloud',
        ],
        "correct_index": 2,
        "why": 'Atmospheric carbon dioxide dissolves to give carbonic acid, a '
               'weak acid that brings clean rain to about pH 5.6.',
    },
    {
        "id": 'ks4-strong-weak-acids-s18',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'standard',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why a strong acid and a weak acid at the same '
                'concentration give the same mass of salt on neutralisation.',
        "options": [
            'Both acids form salts with the same formula mass',
            'Both acids have the same hydrogen ion concentration',
            'Both solutions hold the same total number of acid moles',
            'Both acids are fully ionised by the time they react',
        ],
        "correct_index": 2,
        "why": 'As the free hydrogen ions are used up a weak acid ionises '
               'further, so all of it reacts in the end.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-strong-weak-acids-h05',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine the hydrogen ion concentration of a solution of pH 4 '
                'compared with one of pH 2.',
        "options": [
            'Two times smaller',
            'Ten times smaller',
            'One hundred times smaller',
            'One hundred times larger',
        ],
        "correct_index": 2,
        "why": 'Two pH units is two factors of ten, so the more acidic solution '
               'holds a hundred times the hydrogen ions.',
    },
    {
        "id": 'ks4-strong-weak-acids-h06',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A 0.1 mol/dm3 acid is found to have a pH of 1. Deduce whether '
                'it is strong or weak, and justify the answer.',
        "options": [
            'Weak, because a pH that low needs a reversible ionisation step',
            'Weak, because 0.1 mol/dm3 is a very dilute solution',
            'Strong, because full ionisation of 0.1 mol/dm3 gives pH 1',
            'Strong, because any acid at 0.1 mol/dm3 must have a pH of 1',
        ],
        "correct_index": 2,
        "why": 'The hydrogen ion concentration matches the acid concentration '
               'exactly, which can only happen if every molecule has ionised.',
    },
    {
        "id": 'ks4-strong-weak-acids-h07',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why a weak acid keeps reacting with excess magnesium '
                'long after a strong acid of the same concentration has stopped.',
        "options": [
            'The weak acid is attacked by the magnesium more easily',
            'The weak acid contains more moles of acid to begin with',
            'The weak acid becomes stronger as the reaction warms it up',
            'The weak acid is slowly ionising further as its ions are used',
        ],
        "correct_index": 3,
        "why": 'Removing hydrogen ions shifts the ionisation equilibrium to the '
               'right, so the reaction continues at a lower rate for longer.',
    },
    {
        "id": 'ks4-strong-weak-acids-h08',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Two acids have the same pH but one is strong. Deduce which '
                'needs the larger volume of alkali to neutralise it.',
        "options": [
            'The strong acid, because it holds far more hydrogen ions',
            'The weak acid, because it holds more acid altogether',
            'Neither, because the same pH means the same amount of acid',
            'The strong acid, because it reacts more vigorously',
        ],
        "correct_index": 1,
        "why": 'Matching the pH means matching the free hydrogen ions, and the '
               'weak acid needs far more molecules to supply that many.',
    },
    {
        "id": 'ks4-strong-weak-acids-h09',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": '0.001 mol/dm3 nitric acid is tested with a pH meter. '
                'Determine the reading.',
        "options": [
            'pH 1',
            'pH 2',
            'pH 3',
            'pH 4',
        ],
        "correct_index": 2,
        "why": 'Nitric acid is strong, so the hydrogen ion concentration is also '
               '0.001 mol/dm3, which is pH 3.',
    },
    {
        "id": 'ks4-strong-weak-acids-h10',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Evaluate the claim that a dilute acid cannot be dangerous.',
        "options": [
            'Correct, because dilution always makes an acid harmless',
            'Correct, because a concentrated acid alone can burn the skin',
            'Wrong, because a dilute strong acid can still be corrosive',
            'Wrong, because dilution makes an acid more strongly ionised',
        ],
        "correct_index": 2,
        "why": 'Dilute hydrochloric acid still supplies enough hydrogen ions to '
               'damage the eye, so dilution is not the same as safety.',
    },
    {
        "id": 'ks4-strong-weak-acids-h11',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Compare the initial rate and the final volume of gas when equal '
                'volumes of 1 mol/dm3 ethanoic acid and 1 mol/dm3 nitric acid '
                'are added to excess calcium carbonate.',
        "options": [
            'Nitric acid is faster and gives more gas in the end',
            'Ethanoic acid is faster but gives less gas in the end',
            'Nitric acid is faster but both give the same gas in the end',
            'Both start at the same rate and both give the same gas',
        ],
        "correct_index": 2,
        "why": 'Rate follows the hydrogen ion concentration, while the total gas '
               'follows the total moles of acid, which are equal here.',
    },
    {
        "id": 'ks4-strong-weak-acids-h12',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Deduce which solution has the higher hydrogen ion '
                'concentration: 0.01 mol/dm3 hydrochloric acid or 0.10 mol/dm3 '
                'ethanoic acid.',
        "options": [
            'The hydrochloric acid, because it is the stronger acid',
            'The ethanoic acid, because it is ten times as concentrated',
            'They are about equal, because one per cent of 0.10 is 0.001',
            'The ethanoic acid, because a weak acid ionises fully in time',
        ],
        "correct_index": 0,
        "why": 'The strong acid gives 0.01 mol/dm3 of hydrogen ions, while one '
               'per cent of 0.10 mol/dm3 gives only 0.001 mol/dm3.',
    },
    {
        "id": 'ks4-strong-weak-acids-h13',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Explain why measuring the pH alone does not tell you whether an '
                'acid is strong or weak.',
        "options": [
            'A pH meter cannot be read accurately enough to tell',
            'The pH changes as soon as the electrode is put in',
            'The pH of every acid is the same at room temperature',
            'The pH also depends on how concentrated the solution is',
        ],
        "correct_index": 3,
        "why": 'A concentrated weak acid and a dilute strong acid can read the '
               'same pH, so the concentration has to be known as well.',
    },
    {
        "id": 'ks4-strong-weak-acids-h14',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Suggest why a weak acid is chosen for descaling a domestic '
                'kettle rather than a strong one.',
        "options": [
            'It leaves no residue, because nothing reacts',
            'It is the one kind of acid that will ever dissolve limescale',
            'It removes the limescale without attacking the metal quickly',
            'It is more concentrated, so less of it has to be used',
        ],
        "correct_index": 2,
        "why": 'A low hydrogen ion concentration still attacks the carbonate but '
               'is gentle enough to be safe on the element and the hands.',
    },
    {
        "id": 'ks4-strong-weak-acids-h15',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Determine how many times more concentrated a 1 per cent '
                'ionised weak acid must be to match the pH of a strong acid.',
        "options": [
            'Ten times',
            'Fifty times',
            'One hundred times',
            'One thousand times',
        ],
        "correct_index": 2,
        "why": 'Only one hundredth of the weak acid supplies hydrogen ions, so a '
               'hundredfold concentration is needed to match.',
    },
    {
        "id": 'ks4-strong-weak-acids-h16',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'A student writes that ethanoic acid becomes a strong acid when '
                'it is heated. Identify the error.',
        "options": [
            'Heating makes a weak acid weaker rather than stronger',
            'Heating cannot change the temperature of a weak acid',
            'Heating only changes the rate, not the class the acid belongs to',
            'Heating turns ethanoic acid into a different compound',
        ],
        "correct_index": 2,
        "why": 'Strong and weak label the acid itself, and warming a solution '
               'does not move it from one class to the other.',
    },
    {
        "id": 'ks4-strong-weak-acids-h17',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Predict what happens to the electrical conductivity of a weak '
                'acid as it is diluted step by step.',
        "options": [
            'It rises steadily, because dilution makes more ions',
            'It falls to zero once the acid has become dilute enough',
            'It stays the same, because the acid itself is unchanged',
            'It falls, because the ions are spread more thinly',
        ],
        "correct_index": 3,
        "why": 'The fraction ionised does rise on dilution, but there are fewer '
               'ions in each cubic centimetre overall, so conduction falls.',
    },
    {
        "id": 'ks4-strong-weak-acids-h18',
        "subtopic_slug": 'strong-weak-acids',
        "band": 'harder',
        "tier": 'higher',
        "triple_only": False,
        "text": 'Compare what a titration and a pH measurement each reveal about '
                'an unknown acid.',
        "options": [
            'Both reveal the concentration and neither reveals the strength',
            'The titration gives the total acid; the pH gives the free ions',
            'The titration gives the free ions; the pH gives the total acid',
            'Both reveal the strength of the acid and neither its concentration',
        ],
        "correct_index": 1,
        "why": 'Neutralisation consumes every mole of acid present, while pH '
               'reports only the hydrogen ions released at that moment.',
    },
]
