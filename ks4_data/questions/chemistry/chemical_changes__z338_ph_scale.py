"""Chemistry · Chemical changes — the MRB-338 expansion for `ph-scale`.

The 0 to 14 scale, the two ions that decide where a solution sits on it, and the
four indicators AQA names — universal indicator, litmus, methyl orange and
phenolphthalein — with their colours stated as observations rather than recalled
in a list. The weight then falls on the two places pupils lose marks: reading a
pH value the wrong way round (pH 12 is not richer in hydrogen ions than pH 2),
and treating an indicator's colour as a measurement.

The rest is neutralisation seen through pH — an alkali added to an acid raising
the pH towards 7, excess taking it past 7, and the pH finally levelling off at
the pH of whatever is being added. Named real contexts carry the applied rows:
liming acidic soil, an indigestion remedy, rainwater at pH 5.6, river water
tested in the field. No titration technique and no strong-versus-weak acid
arithmetic — both belong to neighbouring leaves.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-ph-scale-e05',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the range of values used on the pH scale.',
        "options": [
            'From 1 to 10',
            'From 0 to 14',
            'From 0 to 100',
            'From 7 to 14',
        ],
        "correct_index": 1,
        "why": 'The scale runs from 0 to 14, with 0 the strongly acidic end and '
               '14 the strongly alkaline end.',
    },
    {
        "id": 'ks4-ph-scale-e06',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Universal indicator is added to a solution of pH 1. State the '
                'colour that develops.',
        "options": [
            'Green',
            'Red',
            'Purple',
            'Blue',
        ],
        "correct_index": 1,
        "why": 'pH 1 is strongly acidic, and universal indicator is red at the '
               'acidic end of the scale.',
    },
    {
        "id": 'ks4-ph-scale-e07',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify what a green colour with universal indicator shows '
                'about a solution.',
        "options": [
            'That it is strongly acidic',
            'That it is slightly alkaline',
            'That it is neutral',
            'That it holds no dissolved ions',
        ],
        "correct_index": 2,
        "why": 'Green is the colour universal indicator gives at pH 7, which is '
               'neutral.',
    },
    {
        "id": 'ks4-ph-scale-e08',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the ion produced by an acid when it dissolves in water.',
        "options": [
            'Hydroxide ions, OH-',
            'Oxide ions, O2-',
            'Hydride ions, H-',
            'Hydrogen ions, H+',
        ],
        "correct_index": 3,
        "why": 'An acid releases hydrogen ions, H+, into solution, and the '
               'concentration of those ions is what the pH reports.',
    },
    {
        "id": 'ks4-ph-scale-e09',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the ion present in excess in an alkaline solution.',
        "options": [
            'Hydroxide ions, OH-',
            'Chloride ions, Cl-',
            'Hydrogen ions, H+',
            'Sodium ions, Na+',
        ],
        "correct_index": 0,
        "why": 'An alkaline solution holds more hydroxide ions, OH-, than '
               'hydrogen ions.',
    },
    {
        "id": 'ks4-ph-scale-e10',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the colour of phenolphthalein in sodium hydroxide '
                'solution.',
        "options": [
            'Colourless',
            'Pink',
            'Teal',
            'A deep blue-green',
        ],
        "correct_index": 1,
        "why": 'Sodium hydroxide solution is alkaline, and phenolphthalein is '
               'pink in alkali.',
    },
    {
        "id": 'ks4-ph-scale-e11',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Blue litmus paper is dipped into dilute hydrochloric acid. '
                'State the colour it turns.',
        "options": [
            'A pale greenish tint',
            'Bright pink',
            'Red',
            'A deep orange-brown',
        ],
        "correct_index": 2,
        "why": 'Litmus is red in acid, so blue litmus paper turns red.',
    },
    {
        "id": 'ks4-ph-scale-e12',
        "subtopic_slug": 'ph-scale',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the colour methyl orange shows in a solution of pH 2.',
        "options": [
            'Colourless',
            'Yellow',
            'Green',
            'Red',
        ],
        "correct_index": 3,
        "why": 'pH 2 is acidic, and methyl orange is red in acid.',
    },
    {
        "id": 'ks4-ph-scale-s05',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Solution A has a pH of 3 and solution B has a pH of 11. '
                'Compare the two solutions.',
        "options": [
            'A is acidic and B is alkaline',
            'A is alkaline and B is acidic',
            'Both are acidic, because neither of them sits at 7',
            'Both are alkaline, because both values are above 0',
        ],
        "correct_index": 0,
        "why": 'Values below 7 are acidic and values above 7 are alkaline, so '
               'pH 3 is acidic and pH 11 alkaline.',
    },
    {
        "id": 'ks4-ph-scale-s06',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Four solutions are measured at pH 1, pH 5, pH 9 and pH 13. '
                'Identify the one with the greatest concentration of hydrogen '
                'ions.',
        "options": [
            'The solution at pH 13',
            'The solution at pH 9',
            'The solution at pH 5',
            'The solution at pH 1',
        ],
        "correct_index": 3,
        "why": 'The lower the pH, the greater the hydrogen ion concentration, '
               'so pH 1 holds the most.',
    },
    {
        "id": 'ks4-ph-scale-s07',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain what is true about the ions in a solution measured at '
                'pH 7.',
        "options": [
            'It holds hydrogen ions but no hydroxide ions',
            'It holds no ions, which is what makes it neutral',
            'It holds hydrogen ions and hydroxide ions in equal numbers',
            'It holds far more hydroxide ions than hydrogen ions',
        ],
        "correct_index": 2,
        "why": 'A neutral solution has equal concentrations of hydrogen ions '
               'and hydroxide ions.',
    },
    {
        "id": 'ks4-ph-scale-s08',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Dry citric acid crystals are touched onto dry universal '
                'indicator paper and no colour change is seen. Suggest why.',
        "options": [
            'Universal indicator paper responds to alkalis and not to acids',
            'The crystals are neutral, and turn acidic only on being heated',
            'The paper has to be moistened with oil before it will work',
            'The acid must dissolve in water before it can release its '
            'hydrogen ions',
        ],
        "correct_index": 3,
        "why": 'pH describes hydrogen ions in solution, and a dry solid has not '
               'released any.',
    },
    {
        "id": 'ks4-ph-scale-s09',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Place these four universal indicator colours in order, '
                'starting with the most acidic: blue, red, green, yellow.',
        "options": [
            'Red, yellow, green, blue',
            'Blue, green, yellow, red',
            'Red, green, yellow, blue',
            'Yellow, red, blue, green',
        ],
        "correct_index": 0,
        "why": 'Universal indicator runs red, orange, yellow, green, blue then '
               'purple as pH rises from 0 to 14.',
    },
    {
        "id": 'ks4-ph-scale-s10',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A solution turns universal indicator yellow. Deduce its '
                'approximate pH.',
        "options": [
            'About pH 13',
            'About pH 6',
            'About pH 9',
            'About pH 2',
        ],
        "correct_index": 1,
        "why": 'Yellow sits between the orange of a moderate acid and the green '
               'of neutral, so the solution is weakly acidic at about pH 6.',
    },
    {
        "id": 'ks4-ph-scale-s11',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Litmus solution is added to a beaker of distilled water. '
                'State the colour observed.',
        "options": [
            'Colourless',
            'Red',
            'Purple',
            'Blue',
        ],
        "correct_index": 2,
        "why": 'Distilled water is neutral, and litmus is purple in a neutral '
               'solution.',
    },
    {
        "id": 'ks4-ph-scale-s12',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why universal indicator cannot be used to report a pH '
                'as 4.7.',
        "options": [
            'It changes colour once, at pH 7, so no other value can be read',
            'It reacts with the solution, altering the pH before it is read',
            'It works on alkalis, so readings below pH 7 are unreliable',
            'Each colour covers a range of pH values, so it gives only an '
            'approximate figure',
        ],
        "correct_index": 3,
        "why": 'Universal indicator shows a band of colour for a band of pH '
               'values, so it identifies a range rather than a precise number.',
    },
    {
        "id": 'ks4-ph-scale-s13',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student needs the pH of a deep purple solution of potassium '
                'manganate(VII). Suggest why a pH probe is chosen rather than '
                'universal indicator.',
        "options": [
            "The solution's own colour would mask the indicator, while a probe "
            'reports a number',
            'A probe works faster, and speed is what decides how accurate a pH '
            'reading is',
            'Universal indicator fails on any solution that contains a metal '
            'compound',
            'A probe raises the pH of the solution slightly, which makes the '
            'reading easier',
        ],
        "correct_index": 0,
        "why": 'A colour change cannot be judged against a strongly coloured '
               'background, but a probe gives a numerical reading regardless of '
               'colour.',
    },
    {
        "id": 'ks4-ph-scale-s14',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what a pH probe is placed in first, before a set of '
                'readings is taken.',
        "options": [
            'Distilled water, so that its reading begins at zero',
            'A buffer solution of known pH, to calibrate it',
            'Concentrated acid, to clean the glass bulb thoroughly',
            'Universal indicator, to check that the two agree',
        ],
        "correct_index": 1,
        "why": 'A probe is calibrated against solutions of known pH, otherwise '
               'its precise-looking readings may be wrong.',
    },
    {
        "id": 'ks4-ph-scale-s15',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Dilute hydrochloric acid is exactly neutralised by sodium '
                'hydroxide solution, and a further 10 cm3 of that alkali is '
                'then added. Predict the pH of the final mixture.',
        "options": [
            'Exactly 7, since a neutralised mixture cannot change its pH again',
            'Below 7, because the extra alkali makes the mixture more acidic',
            'Above 7, because there is now excess alkali in the mixture',
            'Exactly 14, since sodium hydroxide solution is a strong alkali',
        ],
        "correct_index": 2,
        "why": 'Once all the acid has reacted, further alkali is left over and '
               'the mixture becomes alkaline.',
    },
    {
        "id": 'ks4-ph-scale-s16',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A field of soil is tested at pH 5.2. Explain how spreading '
                'powdered calcium hydroxide over it changes the pH.',
        "options": [
            'The pH falls towards 0, as the powder adds hydrogen ions to the '
            'soil water',
            'The pH rises towards 7 as the alkali neutralises acid in the soil',
            'The pH stays at 5.2, because a solid cannot alter the pH of soil '
            'water',
            'The pH rises straight to 14, because calcium hydroxide is an '
            'alkali',
        ],
        "correct_index": 1,
        "why": 'Calcium hydroxide is a base, so it removes hydrogen ions from '
               'the soil water and the pH climbs towards neutral.',
    },
    {
        "id": 'ks4-ph-scale-s17',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Stomach contents at pH 2 are treated with an indigestion '
                'remedy containing magnesium hydroxide. Describe the change in '
                'pH.',
        "options": [
            'It rises towards 7 as acid is neutralised',
            'It falls below 2, because the remedy is itself an acid',
            'It rises to 14, because magnesium hydroxide is an alkali',
            'It is unchanged, since magnesium hydroxide is insoluble and so '
            'cannot react with acid',
        ],
        "correct_index": 0,
        "why": 'The base neutralises some of the stomach acid, lowering the '
               'hydrogen ion concentration and raising the pH towards neutral.',
    },
    {
        "id": 'ks4-ph-scale-s18',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student must tell a solution of pH 3 apart from one of pH 5. '
                'Identify the better test, with a reason.',
        "options": [
            'Red litmus paper, because it turns a deeper red the more acidic a '
            'solution is',
            'Universal indicator, because it gives a different colour for each '
            'of those values',
            'Phenolphthalein, because it shows a paler pink in the more acidic '
            'of the two',
            'Blue litmus paper, because the stronger acid alone is able to turn '
            'it red',
        ],
        "correct_index": 1,
        "why": 'Universal indicator changes through several colours across the '
               'scale, so pH 3 and pH 5 look different; litmus only separates '
               'acid from alkali.',
    },
    {
        "id": 'ks4-ph-scale-s19',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Phenolphthalein is added to a sample of vinegar and to a '
                'sample of dilute nitric acid. Explain why it cannot tell them '
                'apart.',
        "options": [
            'It turns pink in both, since it responds to anything that is not '
            'water',
            'It turns pink in the vinegar alone, because vinegar holds a '
            'different acid',
            'It is colourless in both, because it only turns pink in alkali',
            'It gives no colour in either, because it has to be warmed first',
        ],
        "correct_index": 2,
        "why": 'Phenolphthalein has one colour change, from colourless to pink '
               'on the alkaline side, so every acid looks the same to it.',
    },
    {
        "id": 'ks4-ph-scale-s20',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State one disadvantage of judging a pH from the colour of '
                'universal indicator paper.',
        "options": [
            'The paper adds hydroxide ions, which raises the pH it then reads',
            'The paper can be used only on solutions already known to be '
            'alkaline',
            'The paper reports a value to two decimal places, which is more '
            'than is needed',
            'Matching a colour by eye is a judgement, so two people may report '
            'different values',
        ],
        "correct_index": 3,
        "why": 'Reading a colour against a chart is subjective, which is why a '
               'probe is used where the value matters.',
    },
    {
        "id": 'ks4-ph-scale-s21',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A liquid is measured at pH 6.4. Deduce whether it is acidic, '
                'neutral or alkaline.',
        "options": [
            'Acidic, because every value below 7 lies on the acidic side',
            'Neutral, because 6.4 is near enough to 7 to count as neutral',
            'Alkaline, because 6.4 sits well above the bottom of the scale',
            'Neutral, because only a whole number can describe an acid',
        ],
        "correct_index": 0,
        "why": 'The neutral point is pH 7 exactly, so 6.4 is on the acidic '
               'side, though only slightly.',
    },
    {
        "id": 'ks4-ph-scale-s22',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a few drops of a solution are placed onto '
                'indicator paper, rather than the paper being dipped into the '
                'stock bottle.',
        "options": [
            'The paper changes colour only when a drop falls onto it from above',
            'Dipping the paper in would contaminate the whole stock bottle',
            'Dipping the paper in would dilute the solution and raise its pH '
            'towards 7',
            'The paper would take far too long to change colour inside a bottle',
        ],
        "correct_index": 1,
        "why": 'Indicator carried in on the paper would spoil the rest of the '
               'bottle for everyone else using it.',
    },
    {
        "id": 'ks4-ph-scale-s23',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify which of these solutions has a pH closest to 9.',
        "options": [
            'Concentrated hydrochloric acid',
            'Sodium hydroxide solution',
            'Baking soda solution',
            'Pure distilled water',
        ],
        "correct_index": 2,
        "why": 'Baking soda solution is weakly alkaline at about pH 9; sodium '
               'hydroxide solution is far higher, at about pH 13.',
    },
    {
        "id": 'ks4-ph-scale-s24',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A technician must record the pH of a reaction mixture every 10 '
                'seconds for 5 minutes. Explain why a pH probe is chosen.',
        "options": [
            'Universal indicator would be used up by the reaction within the '
            'first minute',
            'A probe is the one piece of apparatus that works on a mixture '
            'still reacting',
            'It reports a number at once, so readings can be taken again and '
            'again quickly',
            'Universal indicator can be added to a mixture once, and never a '
            'second time',
        ],
        "correct_index": 2,
        "why": 'A probe reads continuously and numerically, so a series of '
               'values can be logged without disturbing the mixture.',
    },
    {
        "id": 'ks4-ph-scale-s25',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what a pH probe and litmus paper each tell you about a '
                'solution.',
        "options": [
            'The probe reports a numerical pH; litmus only separates acid from '
            'alkali',
            'Both report a numerical pH, but the probe is quicker to set up',
            'Litmus reports a numerical pH, while the probe shows a colour '
            'change',
            'Both show a colour, but the probe is read against a printed chart',
        ],
        "correct_index": 0,
        "why": 'Litmus answers one question — acid or alkali — while a probe '
               'gives the value itself.',
    },
    {
        "id": 'ks4-ph-scale-s26',
        "subtopic_slug": 'ph-scale',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Universal indicator is mixed into dilute hydrochloric acid, '
                'and sodium hydroxide is then run in until it is in excess. '
                'State the order of the colours seen.',
        "options": [
            'Purple, then green, then red',
            'Red, then green, then purple',
            'Green, then red, then purple',
            'Red, then purple, then green',
        ],
        "correct_index": 1,
        "why": 'The mixture starts acidic (red), passes through neutral (green) '
               'and finishes alkaline (purple) once alkali is in excess.',
    },
    {
        "id": 'ks4-ph-scale-h05',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A calibrated probe reads pH 14.6 for a concentrated sodium '
                'hydroxide solution. Evaluate whether that reading can be '
                'correct.',
        "options": [
            'It cannot, because a value above 14 would mean no hydroxide ions '
            'were present',
            'It cannot, because 14 is the highest value a solution can reach',
            'It can, because 0 to 14 is the usual span of the scale rather than '
            'a hard limit',
            'It can, but only because the probe was set to the wrong units',
        ],
        "correct_index": 2,
        "why": 'Values a little outside 0 to 14 are possible; the familiar '
               'range covers the solutions met at GCSE, not every solution.',
    },
    {
        "id": 'ks4-ph-scale-h06',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two samples of hydrochloric acid read pH 4 and pH 6 on a '
                'probe. Deduce which sample is the more concentrated.',
        "options": [
            'The pH 6 sample, since a higher number means more acid dissolved',
            'Neither, since both samples contain the same acid',
            'The pH 6 sample, since the scale counts upwards from the weakest',
            'The pH 4 sample, because a lower pH means more hydrogen ions',
        ],
        "correct_index": 3,
        "why": 'pH falls as hydrogen ion concentration rises, so the sample at '
               'pH 4 is the more concentrated of the two.',
    },
    {
        "id": 'ks4-ph-scale-h07',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Rainwater is often measured at about pH 5.6, while pure water '
                'is pH 7. Explain what this shows about rainwater.',
        "options": [
            'It is slightly acidic, because gases dissolved from the air '
            'release hydrogen ions',
            'It is neutral, because 5.6 is close enough to 7 for water to count '
            'as neutral',
            'It is alkaline, because gases dissolved from the air add hydroxide '
            'ions to it',
            'It is slightly acidic, because rain loses hydroxide ions as it '
            'falls through the air',
        ],
        "correct_index": 0,
        "why": 'Carbon dioxide and other gases dissolve in falling rain and '
               'release hydrogen ions, pulling the pH below 7.',
    },
    {
        "id": 'ks4-ph-scale-h08',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student adds alkali to acid containing universal indicator '
                'and stops the moment the colour shifts from orange to yellow. '
                'Evaluate whether the acid has been neutralised.',
        "options": [
            'Yes, because any colour change shows the neutral point has been '
            'passed',
            'No, because yellow is still on the acidic side, so acid remains',
            'No, because the colour has to reach blue before all the acid has '
            'reacted',
            'Yes, because yellow is the colour universal indicator gives at '
            'pH 7',
        ],
        "correct_index": 1,
        "why": 'Yellow corresponds to a pH of roughly 5 to 6, so the mixture is '
               'still acidic and more alkali is needed.',
    },
    {
        "id": 'ks4-ph-scale-h09',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Four samples read pH 1.0, 6.9, 7.0 and 12.8 on a calibrated '
                'probe. Determine how many of them are acidic.',
        "options": [
            'One of them',
            'Three of them',
            'Two of them',
            'None',
        ],
        "correct_index": 2,
        "why": 'Only values below 7 are acidic, so pH 1.0 and pH 6.9 qualify — '
               'pH 7.0 is neutral and pH 12.8 alkaline.',
    },
    {
        "id": 'ks4-ph-scale-h10',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student claims that mixing an acid with an alkali must '
                'always give a solution of pH 7. Evaluate this claim.',
        "options": [
            'Correct, because an acid and an alkali cancel out whenever they '
            'meet',
            'Wrong, because mixing an acid with an alkali leaves the mixture '
            'acidic',
            'Correct, because the pH of a mixture is the average of the two pH '
            'values',
            'Wrong, because the final pH depends on how much of each is added',
        ],
        "correct_index": 3,
        "why": 'pH 7 is reached only at the point where the two exactly '
               'neutralise; before or beyond it, one reactant is in excess.',
    },
    {
        "id": 'ks4-ph-scale-h11',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A pupil reads pH 5.5 from universal indicator paper and a '
                'probe then reads 4.8 for the same liquid. Evaluate the '
                "pupil's value.",
        "options": [
            'It is a rough estimate — the paper cannot be read to a tenth of a '
            'unit',
            'It is right, and the probe must have been faulty when it was used',
            'It is wrong, because indicator paper reads 0.7 high every single '
            'time',
            'Both are wrong, because no solution has a pH between two whole '
            'numbers',
        ],
        "correct_index": 0,
        "why": 'Indicator paper resolves the pH only to about one whole unit, so '
               '5.5 is a band rather than a measurement; the probe gives the '
               'value.',
    },
    {
        "id": 'ks4-ph-scale-h12',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'So much powdered calcium hydroxide is dug into acidic soil '
                'that it reaches pH 8.5. Explain the problem for a crop that '
                'grows best at pH 6.5.',
        "options": [
            'Nothing is wrong, because soil above pH 7 suits every crop that '
            'is grown',
            'Too much alkali has gone in, so the soil is now alkaline instead '
            'of neutral',
            'The soil remains acidic at pH 8.5, so a further dressing of lime '
            'is needed',
            'The lime has left the soil neutral, which is what this crop '
            'actually needs',
        ],
        "correct_index": 1,
        "why": 'The treatment has overshot pH 7, so the soil is now too '
               'alkaline for a crop suited to slightly acidic ground.',
    },
    {
        "id": 'ks4-ph-scale-h13',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student writes that a neutral liquid contains no hydrogen '
                'ions. Explain why that is wrong.',
        "options": [
            'It has no hydrogen ions, but the claim about hydroxide ions is '
            'wrong',
            'A neutral liquid holds hydroxide ions alone, which is why the pH '
            'reads 7',
            'It holds hydrogen ions, and exactly as many hydroxide ions as well',
            'A neutral liquid holds twice as many hydrogen ions as hydroxide '
            'ions',
        ],
        "correct_index": 2,
        "why": 'Neutral means the two ion concentrations are equal, not that '
               'either one is absent.',
    },
    {
        "id": 'ks4-ph-scale-h14',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Copper oxide neutralises dilute sulfuric acid, yet stirring it '
                'into water has no effect on red litmus paper. Explain why '
                'copper oxide is called a base and not an alkali.',
        "options": [
            'It is a metal oxide, and a metal oxide cannot be given the name '
            'alkali',
            'It neutralises an acid only when warmed, so it is not a true '
            'alkali',
            'It contains a metal, and an alkali has to be a non-metal compound',
            'It is insoluble, so it releases no hydroxide ions into solution',
        ],
        "correct_index": 3,
        "why": 'An alkali is a base that dissolves to give hydroxide ions in '
               'solution; copper oxide is a base that does not dissolve.',
    },
    {
        "id": 'ks4-ph-scale-h15',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student says a liquid at pH 12 must hold more hydrogen ions '
                'than one at pH 2, since 12 is the larger number. Identify the '
                'error.',
        "options": [
            'A higher pH means fewer hydrogen ions, not more',
            'A higher pH does mean more hydrogen ions, but 12 is not a possible '
            'pH value',
            'There is no error, because the pH counts hydrogen ions directly '
            'upwards',
            'The scale measures hydroxide ions, so hydrogen ions play no part '
            'in it',
        ],
        "correct_index": 0,
        "why": 'pH runs the opposite way to hydrogen ion concentration, so pH '
               '12 holds far fewer hydrogen ions than pH 2.',
    },
    {
        "id": 'ks4-ph-scale-h16',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student finds that 10 cm3 of a dilute nitric acid needs '
                '10 cm3 of a sodium hydroxide solution to reach neutral. If '
                'they instead mix 10 cm3 of that same acid with only 5 cm3 of '
                'the alkali, predict the resulting pH.',
        "options": [
            'Exactly 7, because the same two solutions are being mixed together',
            'Below 7, because half of the acid is left unreacted',
            'Above 7, because using less alkali leaves the mixture alkaline',
            'Exactly 3.5, because halving the alkali halves the pH as well',
        ],
        "correct_index": 1,
        "why": 'Only half the acid can be neutralised by half the alkali, so '
               'acid is in excess and the mixture stays below pH 7.',
    },
    {
        "id": 'ks4-ph-scale-h17',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Sodium hydroxide solution is run into dilute hydrochloric acid '
                'until the pH stops climbing and settles at about 13. Explain '
                'why it stops climbing.',
        "options": [
            'The water in the mixture has all been used up by the reaction',
            'The acid begins to re-form, which holds the pH steady',
            'The mixture is now almost pure alkali, so its pH cannot pass the '
            'pH of the alkali being added',
            'Sodium hydroxide stops releasing ions once the acid has all '
            'reacted',
        ],
        "correct_index": 2,
        "why": 'Beyond neutralisation the mixture is just diluted sodium '
               'hydroxide solution, so its pH approaches that of the alkali and '
               'goes no higher.',
    },
    {
        "id": 'ks4-ph-scale-h18',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare indicator paper and a pH probe as ways of measuring '
                'the pH of a river water sample out in the field.',
        "options": [
            'The probe is the quicker in the field, because it needs no '
            'calibration',
            'The paper gives the more precise value, because a colour can be '
            'matched exactly',
            'Both are equally precise, so the cost of the two is the only real '
            'difference',
            'The paper is quick and needs no power; the probe gives a more '
            'precise value',
        ],
        "correct_index": 3,
        "why": 'Paper is portable and immediate but resolves roughly one pH '
               'unit, while a probe is precise but needs power and calibration.',
    },
    {
        "id": 'ks4-ph-scale-h19',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine which ion is in excess in a liquid whose probe '
                'reading is 3.1.',
        "options": [
            'Hydrogen ions, because the liquid is acidic',
            'Hydroxide ions, because the reading lies below 7',
            'Hydroxide ions, because 3.1 sits in the alkaline part of the scale',
            'Neither, because the two are always present in equal numbers',
        ],
        "correct_index": 0,
        "why": 'A pH of 3.1 is below 7, so hydrogen ions outnumber hydroxide '
               'ions.',
    },
    {
        "id": 'ks4-ph-scale-h20',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'An unknown liquid turns blue litmus paper red and leaves '
                'phenolphthalein colourless. Deduce what the two results show.',
        "options": [
            'It is alkaline, because phenolphthalein is colourless in alkali',
            'It is acidic, because both results are the ones an acid gives',
            'It is neutral, because the two results disagree with each other',
            'It is alkaline, because an alkali alone can change the colour of '
            'litmus',
        ],
        "correct_index": 1,
        "why": 'Litmus turning red and phenolphthalein staying colourless both '
               'indicate an acid, so the two tests agree.',
    },
    {
        "id": 'ks4-ph-scale-h21',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Dilute acid holding universal indicator turns green after '
                'sodium carbonate solution is added. A further spatula of '
                'sodium carbonate is stirred in. Predict the new colour.',
        "options": [
            'Green still, because a neutral mixture cannot be changed again',
            'Red, because adding more solid to a mixture makes it more acidic',
            'Blue or purple, because the mixture is now alkaline',
            'Colourless, because the indicator is used up at the neutral point',
        ],
        "correct_index": 2,
        "why": 'Sodium carbonate solution is alkaline, so once the acid has all '
               'reacted the excess pushes the pH above 7.',
    },
    {
        "id": 'ks4-ph-scale-h22',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Universal indicator in a beaker of alkali is blue. Deduce what '
                'happens to the colour when a little dilute acid is stirred in.',
        "options": [
            'It moves towards purple, because acid raises the pH of an alkali',
            'It stays blue, because an indicator changes colour once only',
            'It jumps straight to red, because any acid takes the pH below 7',
            'It moves towards green, because the pH falls towards 7',
        ],
        "correct_index": 3,
        "why": 'Acid removes hydroxide ions, so the pH falls from the blue band '
               'towards the green of neutral.',
    },
    {
        "id": 'ks4-ph-scale-h23',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why an acid is defined by the ions it produces in '
                'aqueous solution, rather than by the ions in the pure '
                'substance.',
        "options": [
            'An acid releases its hydrogen ions only once it has dissolved in '
            'water',
            'A pure acid holds hydroxide ions, which the water then takes away '
            'from it',
            'The water supplies the hydrogen ions and the acid supplies the '
            'rest of the molecule',
            'A pure acid sits at pH 7 until water is added to bring the value '
            'down',
        ],
        "correct_index": 0,
        "why": 'pH is a property of a solution, and the hydrogen ions it '
               'reports appear only when the acid dissolves in water.',
    },
    {
        "id": 'ks4-ph-scale-h24',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A technician says a probe reading to 0.01 of a pH unit needs no '
                'calibration. Evaluate that statement.',
        "options": [
            'Right, because a meter reading to two decimal places cannot drift',
            'Wrong, because a probe reads precisely but must be calibrated to '
            'read correctly',
            'Wrong, because a probe is less precise than universal indicator '
            'paper',
            'Right, because calibration is needed for an indicator and not for '
            'a probe',
        ],
        "correct_index": 1,
        "why": 'Extra decimal places make a reading precise, not accurate; only '
               'calibration against known pH values makes it accurate.',
    },
    {
        "id": 'ks4-ph-scale-h25',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Equal volumes of dilute hydrochloric acid and sodium hydroxide '
                'solution that exactly neutralise each other are mixed. '
                'Determine the pH and name what is present afterwards.',
        "options": [
            'pH 0, with the acid and the alkali both present unchanged',
            'pH 14, with sodium hydroxide and water left in the beaker',
            'pH 7, with sodium chloride and water present',
            'pH 7, with water alone, since the salt is destroyed as it forms',
        ],
        "correct_index": 2,
        "why": 'Exact neutralisation of a strong acid by a strong alkali gives '
               'a neutral salt solution — sodium chloride dissolved in water.',
    },
    {
        "id": 'ks4-ph-scale-h26',
        "subtopic_slug": 'ph-scale',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A pupil has red litmus paper and nothing else. Determine '
                'whether it can be used to show that a liquid is acidic.',
        "options": [
            'Yes, because red litmus paper turns a deeper red in an acid',
            'Yes, because red litmus paper turns colourless in an acid',
            'No, because red litmus paper works on gases and never on liquids',
            'No, because red litmus stays red in acid, so no change is seen',
        ],
        "correct_index": 3,
        "why": 'Red litmus only changes in alkali, so an unchanged paper cannot '
               'distinguish an acid from a neutral liquid.',
    },
]
