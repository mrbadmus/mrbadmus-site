"""Chemistry · Chemical changes — the MRB-338 expansion for `titrations`.

The chemistry-only required practical, asked as a technique rather than as a
recipe. Apparatus first — which vessel measures and which delivers, why the
burette is read to two decimal places and the pipette is not read at all — then
the method in order, then the end point as the moment one further drop holds its
colour.

The heaviest weight falls on the places a titre goes wrong and by how much: an
air bubble under the tap, a burette rinsed with water, a flask rinsed with
alkali, a run overshot past the colour change. Concordance and the mean carry
the analysis rows, and the harder band takes the titre through to a
concentration in mol/dm3, with every step of the arithmetic kept in the
explanation and never in an option.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-titrations-e05',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the piece of apparatus that holds the acid during a '
                'titration.',
        "options": [
            'The pipette',
            'The burette',
            'The conical flask',
            'The evaporating basin',
        ],
        "correct_index": 1,
        "why": 'The burette is the graduated tube with a tap, so acid can be run '
               'in a little at a time and the volume read off.',
    },
    {
        "id": 'ks4-titrations-e06',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the acid is added from a burette rather than from a '
                'measuring cylinder.',
        "options": [
            'A burette holds a much larger volume of acid',
            'A burette measures the volume added far more precisely',
            'A burette keeps the acid at a steady temperature throughout',
            'A burette stops the acid reacting with the air',
        ],
        "correct_index": 1,
        "why": 'A burette is graduated every 0.10 cm3 and read to 0.05 cm3, so '
               'the volume delivered is known far more exactly.',
    },
    {
        "id": 'ks4-titrations-e07',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State how many decimal places a burette reading is recorded to.',
        "options": [
            'None',
            'One',
            'Two',
            'Three',
        ],
        "correct_index": 2,
        "why": 'A burette is graduated every 0.10 cm3 and estimated to the '
               'nearest 0.05 cm3, so readings are written to two decimal places.',
    },
    {
        "id": 'ks4-titrations-e08',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the conical flask is swirled while acid is being '
                'added.',
        "options": [
            'To stop the indicator from settling on the base of the flask',
            'To keep the flask from getting too warm',
            'To mix the acid and alkali as they meet',
            'To speed up the flow of acid from the tap',
        ],
        "correct_index": 2,
        "why": 'Swirling brings the whole of the alkali into contact with each '
               'drop of acid, so the colour change reports the whole flask.',
    },
    {
        "id": 'ks4-titrations-e09',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the part of the burette that is read when taking a volume.',
        "options": [
            'The top of the tap',
            'The bottom of the meniscus',
            'The very top of the liquid column',
            'The mark that is nearest the eye',
        ],
        "correct_index": 1,
        "why": 'The liquid curves at its surface, and the convention is to read '
               'the lowest point of that curve at eye level.',
    },
    {
        "id": 'ks4-titrations-e10',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State how many drops of indicator are added to the alkali in '
                'the flask.',
        "options": [
            'Two or three drops',
            'About ten drops',
            'Half a test tube',
            'No indicator is used',
        ],
        "correct_index": 0,
        "why": 'A few drops are enough to show the change, and more indicator '
               'would itself react with some of the acid.',
    },
    {
        "id": 'ks4-titrations-e11',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the safety equipment used when drawing alkali into a '
                'pipette.',
        "options": [
            'A pipette filler',
            'A pair of metal tongs',
            'A heatproof mat',
            'A pipe-clay triangle',
        ],
        "correct_index": 0,
        "why": 'A filler draws the solution up without anyone putting the '
               'pipette to the mouth.',
    },
    {
        "id": 'ks4-titrations-e12',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the name given to two titres that agree closely enough '
                'to be averaged.',
        "options": [
            'Anomalous results',
            'Concordant',
            'Rough',
            'Systematic',
        ],
        "correct_index": 1,
        "why": 'Concordant titres are the ones close enough to be averaged, and '
               'the agreed limit is 0.10 cm3.',
    },
    {
        "id": 'ks4-titrations-e13',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the type of acid and the type of alkali used in the '
                'required practical.',
        "options": [
            'A weak acid and a weak alkali',
            'A strong acid and a strong alkali',
            'A weak acid and a strong alkali',
            'A strong acid and a weak alkali',
        ],
        "correct_index": 1,
        "why": 'A strong acid with a strong alkali gives a single sharp colour '
               'change that is easy to judge.',
    },
    {
        "id": 'ks4-titrations-e14',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State what is recorded before any acid is run out of the '
                'burette.',
        "options": [
            'The mass of the alkali in the flask',
            'The colour of the white tile',
            'The volume of the conical flask',
            'The initial burette reading',
        ],
        "correct_index": 3,
        "why": 'The titre is a difference of two readings, so the level at the '
               'start has to be written down before a drop is delivered.',
    },
    {
        "id": 'ks4-titrations-e15',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the colour of methyl orange once excess acid has been '
                'added.',
        "options": [
            'Yellow',
            'Green',
            'Red',
            'Purple',
        ],
        "correct_index": 2,
        "why": 'Methyl orange is yellow in alkali and turns red once the flask '
               'has become acidic.',
    },
    {
        "id": 'ks4-titrations-e16',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the equipment used to pour acid into the burette without '
                'spilling it.',
        "options": [
            'A small funnel',
            'A dropping pipette',
            'A glass stirring rod',
            'A wash bottle',
        ],
        "correct_index": 0,
        "why": 'A funnel guides the acid into the narrow neck, and it is taken '
               'out again before the first reading is recorded.',
    },
    {
        "id": 'ks4-titrations-e17',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the uncertainty of a single burette reading.',
        "options": [
            'Plus or minus 0.05 cm3',
            'Plus or minus 0.50 cm3',
            'Plus or minus 1.00 cm3',
            'Plus or minus 5.00 cm3',
        ],
        "correct_index": 0,
        "why": 'The scale is marked every 0.10 cm3, so each reading is good to '
               'half a division.',
    },
    {
        "id": 'ks4-titrations-e18',
        "subtopic_slug": 'titrations',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State what is done with the rough titration result.',
        "options": [
            'It is averaged with the accurate runs',
            'It is left out of the mean titre',
            'It is used as the final answer instead',
            'It is doubled before use',
        ],
        "correct_index": 1,
        "why": 'The rough run only locates the end point roughly, so it is too '
               'imprecise to belong in the average.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-titrations-s05',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A burette reads 0.00 cm3 at the start and 22.40 cm3 at the end. '
                'Calculate the titre.',
        "options": [
            '22.40 cm3',
            '0.00 cm3',
            '22.00 cm3',
            '44.80 cm3',
        ],
        "correct_index": 0,
        "why": 'The titre is the final reading minus the initial one, and '
               '22.40 minus 0.00 is 22.40 cm3.',
    },
    {
        "id": 'ks4-titrations-s06',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the funnel is removed from the burette before the '
                'first reading is taken.',
        "options": [
            'A drip from the funnel would add acid after the reading',
            'The funnel makes the scale harder to see from the side',
            'The funnel would absorb some of the acid it has held',
            'The funnel changes the shape of the meniscus below it',
        ],
        "correct_index": 0,
        "why": 'Acid left in the funnel can run down afterwards, so the volume '
               'delivered would be larger than the readings show.',
    },
    {
        "id": 'ks4-titrations-s07',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student records titres of 24.80, 24.85 and 25.60 cm3. '
                'Calculate the mean titre that should be reported.',
        "options": [
            '25.08 cm3',
            '25.60 cm3',
            '24.80 cm3',
            '24.83 cm3',
        ],
        "correct_index": 3,
        "why": 'Only 24.80 and 24.85 are concordant, and their mean is '
               '49.65 divided by 2, which is 24.83 cm3.',
    },
    {
        "id": 'ks4-titrations-s08',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why universal indicator is a poor choice for a '
                'titration.',
        "options": [
            'It changes through a range of colours instead of sharply',
            'It reacts with the alkali and uses some of it up',
            'It is far too pale to be seen against a white tile',
            'It only works in solutions that are already neutral',
        ],
        "correct_index": 0,
        "why": 'A gradual sequence of colours gives no single moment to stop at, '
               'so the end point cannot be judged to one drop.',
    },
    {
        "id": 'ks4-titrations-s09',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe what the student does as the colour of the flask '
                'starts to flicker.',
        "options": [
            'Adds the remaining acid in one quick burst',
            'Adds the acid one drop at a time, swirling between drops',
            'Stops at once and records the reading as the titre',
            'Refills the burette before going any further',
        ],
        "correct_index": 1,
        "why": 'A flicker of colour that fades on swirling means the end point '
               'is close, so the last of the acid goes in dropwise.',
    },
    {
        "id": 'ks4-titrations-s10',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'An air bubble sits below the burette tap at the start and is '
                'gone by the end. Predict the effect on the titre.',
        "options": [
            'The titre is too small, because the bubble held back acid',
            'The titre is unchanged, because the bubble holds no acid',
            'The titre is too large, because the bubble volume is counted in',
            'The titre is unchanged, because the bubble rises and escapes',
        ],
        "correct_index": 2,
        "why": 'The level falls by the volume of the bubble as well as by the '
               'acid delivered, so the recorded titre overstates the acid used.',
    },
    {
        "id": 'ks4-titrations-s11',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the conical flask is not rinsed with alkali before '
                'the pipetted volume goes in.',
        "options": [
            'The rinse would add extra alkali and raise the titre',
            'The rinse would dilute the alkali that is added next',
            'The rinse would leave the glass much too wet to swirl it safely',
            'The rinse would use up the indicator before it is added',
        ],
        "correct_index": 0,
        "why": 'Only the pipetted volume should be in the flask, so any extra '
               'alkali clinging to the glass would need extra acid.',
    },
    {
        "id": 'ks4-titrations-s12',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why rinsing the conical flask with distilled water does '
                'not spoil the result.',
        "options": [
            'Water reacts with the acid and cancels the extra volume out again',
            'Water dilutes the alkali but not the number of moles present',
            'Water evaporates from the flask before the acid is added',
            'Water is neutral, so it cancels the acid and the alkali equally',
        ],
        "correct_index": 1,
        "why": 'The amount of alkali is fixed by the pipette, and extra water '
               'changes only the volume, not the moles to be neutralised.',
    },
    {
        "id": 'ks4-titrations-s13',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student overshoots the end point on the second run. Describe '
                'what should be done with that result.',
        "options": [
            'Report it, because every result that is collected must be used',
            'Subtract 0.50 cm3 from it and use the corrected value',
            'Discard it and carry out a further accurate run',
            'Average it with the rough run to cancel the error',
        ],
        "correct_index": 2,
        "why": 'An overshot titre is larger than the true value, so it is '
               'rejected rather than corrected by guesswork.',
    },
    {
        "id": 'ks4-titrations-s14',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the eye must be level with the liquid surface when '
                'a burette is read.',
        "options": [
            'Looking from above or below gives a parallax error',
            'The scale is printed on only one side of the glass tube',
            'The meniscus changes shape as the eye moves',
            'The liquid appears a different colour from other angles',
        ],
        "correct_index": 0,
        "why": 'A line of sight that is not square to the scale makes the mark '
               'appear beside the wrong graduation.',
    },
    {
        "id": 'ks4-titrations-s15',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Determine the amount in moles of sodium hydroxide in 25.0 cm3 '
                'of a 0.100 mol/dm3 solution.',
        "options": [
            '0.250 mol',
            '0.0250 mol',
            '2.50 mol',
            '0.00250 mol',
        ],
        "correct_index": 3,
        "why": 'Moles are concentration times volume in dm3, so 0.100 times '
               '0.0250 gives 0.00250 mol.',
    },
    {
        "id": 'ks4-titrations-s16',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the titration is repeated several times.',
        "options": [
            'To use up the rest of the acid in the burette',
            'To reduce the effect of random error on the mean',
            'To let the indicator work its way through the flask',
            'To make sure the alkali has had time to dissolve',
        ],
        "correct_index": 1,
        "why": 'Averaging concordant repeats makes a single misjudged drop '
               'matter less to the final value.',
    },
    {
        "id": 'ks4-titrations-s17',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe what would be seen in the flask at the end point with '
                'phenolphthalein.',
        "options": [
            'The solution turns from yellow through to red',
            'The solution turns from colourless to a deep pink',
            'The pink colour disappears and does not come back',
            'A pink precipitate settles out onto the white tile',
        ],
        "correct_index": 2,
        "why": 'Acid is being added to alkali, so the pink of the alkaline '
               'flask is lost as the last of the alkali reacts.',
    },
    {
        "id": 'ks4-titrations-s18',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Calculate the uncertainty in a titre found from two burette '
                'readings each good to 0.05 cm3.',
        "options": [
            '0.05 cm3',
            '0.10 cm3',
            '0.20 cm3',
            '0.025 cm3',
        ],
        "correct_index": 1,
        "why": 'A titre is a difference of two readings, so the two '
               'uncertainties add to give 0.10 cm3.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-titrations-h05',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": '25.0 cm3 of sodium hydroxide is neutralised by 20.0 cm3 of '
                '0.100 mol/dm3 hydrochloric acid. Determine the concentration '
                'of the alkali.',
        "options": [
            '0.125 mol/dm3',
            '0.200 mol/dm3',
            '0.100 mol/dm3',
            '0.080 mol/dm3',
        ],
        "correct_index": 3,
        "why": 'The acid supplies 0.100 times 0.0200, which is 0.00200 mol; the '
               'ratio is one to one, so 0.00200 divided by 0.0250 is '
               '0.080 mol/dm3.',
    },
    {
        "id": 'ks4-titrations-h06',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": '25.0 cm3 of 0.150 mol/dm3 potassium hydroxide needs 25.0 cm3 '
                'of nitric acid. Determine the concentration of the acid.',
        "options": [
            '0.075 mol/dm3',
            '0.300 mol/dm3',
            '0.150 mol/dm3',
            '0.050 mol/dm3',
        ],
        "correct_index": 2,
        "why": 'Equal volumes reacting in a one-to-one ratio must be at equal '
               'concentration, so the acid matches the alkali exactly.',
    },
    {
        "id": 'ks4-titrations-h07',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student rinses the burette with distilled water and fills it '
                'with acid without drying it. Predict the effect on the titre.',
        "options": [
            'It is too large, because the acid inside has been diluted',
            'It is too small, because water reacts with some of the acid',
            'It is unchanged, because water is neutral and cannot interfere',
            'It is too small, because the wet glass lets acid run out faster',
        ],
        "correct_index": 0,
        "why": 'Diluted acid carries fewer moles in each cm3, so a larger volume '
               'is needed to neutralise the same alkali.',
    },
    {
        "id": 'ks4-titrations-h08',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Compare the precision of a 25.00 cm3 pipette with that of a '
                '25 cm3 measuring cylinder.',
        "options": [
            'They are the same, since both hold the same volume',
            'The measuring cylinder is the more precise of the two',
            'The pipette is more precise, since it delivers one fixed volume',
            'Neither is precise, because both are read by eye',
        ],
        "correct_index": 2,
        "why": 'A pipette is made and calibrated for a single volume, so its '
               'uncertainty is far smaller than a graduated cylinder read by eye.',
    },
    {
        "id": 'ks4-titrations-h09',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student adds 20 drops of indicator instead of 3. Suggest '
                'the effect on the titration.',
        "options": [
            'The alkali is neutralised before any acid has been added',
            'The colour is too deep, so the end point is harder to judge',
            'No colour change happens, because the indicator is too strong',
            'The colour change happens sooner, so the reading is unusable',
        ],
        "correct_index": 1,
        "why": 'A few drops give a sharp change that can be caught to one drop, '
               'while a deeply coloured flask hides the moment it happens.',
    },
    {
        "id": 'ks4-titrations-h10',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Four titres are recorded: 18.65, 19.40, 18.60 and 18.70 cm3. '
                'Determine the mean titre.',
        "options": [
            '18.84 cm3',
            '18.65 cm3',
            '18.70 cm3',
            '19.40 cm3',
        ],
        "correct_index": 1,
        "why": 'The concordant set is 18.65, 18.60 and 18.70, whose total of '
               '55.95 divided by 3 gives 18.65 cm3.',
    },
    {
        "id": 'ks4-titrations-h11',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a mean titre carries a smaller uncertainty than any '
                'one of the runs that made it.',
        "options": [
            'Averaging lets random errors above and below partly cancel',
            'Averaging removes the systematic error in the burette scale',
            'Averaging always gives a smaller number than any single run',
            'Averaging counts each reading only once, halving the error',
        ],
        "correct_index": 0,
        "why": 'Random errors scatter either side of the true value, so the mean '
               'of several runs sits closer to it than a single run does.',
    },
    {
        "id": 'ks4-titrations-h12',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Determine the volume of 0.500 mol/dm3 hydrochloric acid needed '
                'to neutralise 25.0 cm3 of 0.250 mol/dm3 sodium hydroxide.',
        "options": [
            '50.0 cm3',
            '25.0 cm3',
            '6.25 cm3',
            '12.5 cm3',
        ],
        "correct_index": 3,
        "why": 'The alkali holds 0.250 times 0.0250, or 0.00625 mol, and '
               '0.00625 divided by 0.500 gives 0.0125 dm3, which is 12.5 cm3.',
    },
    {
        "id": 'ks4-titrations-h13',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Evaluate whether a set of titres reading 21.10, 21.15 and '
                '21.90 cm3 gives a reliable mean.',
        "options": [
            'Yes, because the mean of all three lies inside the range',
            'No, because three results are never enough for a mean',
            'Yes, but only after the two closest values are discarded',
            'No, because one result is outside 0.10 cm3 of the other two',
        ],
        "correct_index": 3,
        "why": 'The 21.90 value is not concordant with the others, so it is left '
               'out and a further run is needed before averaging.',
    },
    {
        "id": 'ks4-titrations-h14',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why a technician checks that the burette tap turns '
                'freely before a class uses it.',
        "options": [
            'A stiff tap makes dropwise addition near the end point impossible',
            'A stiff tap lets air into the acid and changes it',
            'A stiff tap alters the graduations printed on the glass',
            'A stiff tap makes the acid run out at the wrong temperature',
        ],
        "correct_index": 0,
        "why": 'The end point is judged one drop at a time, which needs fine '
               'control of the flow.',
    },
    {
        "id": 'ks4-titrations-h15',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the same titre is expected whether methyl orange '
                'or phenolphthalein is used with a strong acid and strong alkali.',
        "options": [
            'Both indicators are the same substance under different names',
            'Both change colour where the pH alters steeply at neutrality',
            'Both indicators react with the acid at the same rate as each other',
            'Both are added in the same number of drops, so both use equal acid',
        ],
        "correct_index": 1,
        "why": 'A strong acid with a strong alkali gives a near-vertical pH jump, '
               'so both indicators change within a fraction of a drop.',
    },
    {
        "id": 'ks4-titrations-h16',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A titration is repeated with 50.0 cm3 of the same alkali '
                'instead of 25.0 cm3. Predict the titre.',
        "options": [
            'It stays the same, because the concentrations are unchanged',
            'It doubles, because twice as many moles must be neutralised',
            'It halves, because the alkali is now more dilute in the flask',
            'It rises by a quarter, because the flask is fuller than before',
        ],
        "correct_index": 1,
        "why": 'Twice the volume at the same concentration is twice the moles, '
               'so twice the volume of acid is required.',
    },
    {
        "id": 'ks4-titrations-h17',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Determine the concentration in mol/dm3 of a nitric acid if '
                '18.0 cm3 of it neutralises 25.0 cm3 of 0.144 mol/dm3 potassium '
                'hydroxide.',
        "options": [
            '0.104 mol/dm3',
            '0.144 mol/dm3',
            '0.250 mol/dm3',
            '0.200 mol/dm3',
        ],
        "correct_index": 3,
        "why": 'The alkali holds 0.144 times 0.0250, or 0.00360 mol, and '
               '0.00360 divided by 0.0180 gives 0.200 mol/dm3.',
    },
    {
        "id": 'ks4-titrations-h18',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a titration gives a more accurate concentration '
                'than mixing until universal indicator reads green.',
        "options": [
            'A titration uses stronger chemicals than the indicator method',
            'A titre is measured to 0.05 cm3 and repeated until concordant',
            'A titration needs no indicator, so nothing can contaminate it',
            'A titration is carried out at a carefully controlled temperature',
        ],
        "correct_index": 1,
        "why": 'Precision comes from the graduated burette and from repeating '
               'until the runs agree, neither of which a colour match offers.',
    },

    # -------------------------------------------------------- standard (top-up)
    {
        "id": 'ks4-titrations-s19',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the purpose of carrying out a rough titration before the '
                'accurate repeats.',
        "options": [
            'To find roughly where the end point falls, so acid can be added '
            'dropwise near it on the next run',
            'To use up the first batch of acid in the burette before a fresh, more carefully measured batch is made up',
            'To check that the indicator has not gone off since it was bought some time earlier from the supplier',
            'To warm the alkali gently until it reaches the same temperature as the acid in the burette',
        ],
        "correct_index": 0,
        "why": 'A rough run locates the end point approximately, so the '
               'accurate runs can slow to dropwise addition just before it '
               'is reached.',
    },
    {
        "id": 'ks4-titrations-s20',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the acid run from the burette must be a '
                'solution of accurately known concentration.',
        "options": [
            'Without it, the calculation of the alkali\'s concentration '
            'from the titre has no known starting value to work from',
            'An acid of unknown concentration reacts too slowly with the '
            'alkali for the end point to be seen clearly by the student',
            'An acid of unknown concentration will not change the colour '
            'of the indicator at the correct moment during the titration',
            'Without it, the burette itself cannot be filled to the zero '
            'mark before the titration is allowed to begin',
        ],
        "correct_index": 0,
        "why": 'The whole calculation rests on knowing exactly how many '
               'moles of acid were added, so an unknown concentration would '
               'leave the alkali\'s concentration impossible to work out.',
    },
    {
        "id": 'ks4-titrations-s21',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'During a titration, distilled water from a wash bottle is used '
                'to rinse acid droplets down the inside of the conical flask. '
                'Explain why this does not add extra acid to the reaction.',
        "options": [
            'The water reacts chemically with the droplets and cancels the '
            'acid out before it can affect the reaction',
            'The water carries the droplets into the mixture rather than '
            'adding any acid of its own',
            'The water evaporates away before it can reach the bottom of '
            'the conical flask below it',
            'The water dilutes the alkali already in the flask, which '
            'balances out the extra acid added',
        ],
        "correct_index": 1,
        "why": 'The wash water contains no acid itself; it only washes acid '
               'that has already been measured out down into the reacting '
               'mixture.',
    },
    {
        "id": 'ks4-titrations-s22',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why the alkali is held in a conical flask during a '
                'titration rather than in an open beaker.',
        "options": [
            'A conical flask can be swirled vigorously without the '
            'contents splashing out over the sides',
            'A conical flask holds a larger volume of liquid than a beaker '
            'of the same height',
            'A conical flask is graduated more finely than a beaker, so '
            'the volume inside can be read precisely',
            'A conical flask reacts less with an alkali than a beaker '
            'would over the course of the titration',
        ],
        "correct_index": 0,
        "why": 'The sloped sides and narrow neck let the mixture be swirled '
               'briskly to mix in each drop of acid, without the liquid '
               'slopping over the rim as it would from an open beaker.',
    },
    {
        "id": 'ks4-titrations-s23',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Sulfuric acid reacts with sodium hydroxide: '
                'H2SO4 + 2NaOH -> Na2SO4 + 2H2O. State the number of moles of '
                'sodium hydroxide that react with one mole of sulfuric acid.',
        "options": [
            '1 mole',
            '2 moles',
            '3 moles',
            '0.5 moles',
        ],
        "correct_index": 1,
        "why": 'The balanced equation shows one H2SO4 reacting with two NaOH, '
               'so each mole of the acid needs two moles of the alkali.',
    },
    {
        "id": 'ks4-titrations-s24',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State what is meant by the titre in a titration.',
        "options": [
            'The total volume of alkali pipetted into the conical flask',
            'The volume of acid run from the burette to reach the end point',
            'The number of drops of indicator added to the alkali in the flask',
            'The concentration of the acid solution held in the burette',
        ],
        "correct_index": 1,
        "why": 'The titre is the volume delivered from the burette by the '
               'time the end point is reached, found from the final reading '
               'minus the initial one.',
    },
    {
        "id": 'ks4-titrations-s25',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State how a burette is numbered, from the top of the scale to '
                'the bottom.',
        "options": [
            '0 cm3 at the top, rising to 50 cm3 at the bottom',
            '50 cm3 at the top, falling to 0 cm3 at the bottom',
            '0 cm3 marked at the bottom, with no reading at the top of the scale',
            'The scale is the same reading at both the top and the bottom',
        ],
        "correct_index": 0,
        "why": 'A burette reads 0 cm3 at the top and increases going down, '
               'which is why the titre is the final reading minus the '
               'initial one rather than the other way round.',
    },
    {
        "id": 'ks4-titrations-s26',
        "subtopic_slug": 'titrations',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Place these three steps of the required practical in the '
                'order they are carried out.',
        "options": [
            'Add the indicator, pipette the alkali into the flask, rinse the '
            'burette with acid',
            'Pipette the alkali into the flask, rinse the burette with acid, '
            'add the indicator',
            'Rinse the burette with acid, add the indicator, pipette the '
            'alkali into the flask',
            'Rinse the burette with acid, pipette the alkali into the flask, '
            'add the indicator',
        ],
        "correct_index": 3,
        "why": 'The burette is prepared first, the exact volume of alkali is '
               'measured into the flask next, and the indicator is added to '
               'that measured alkali last.',
    },

    # --------------------------------------------------------- harder (top-up)
    {
        "id": 'ks4-titrations-h19',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": '25.0 cm3 of 0.100 mol/dm3 sodium hydroxide is exactly '
                'neutralised by 12.5 cm3 of sulfuric acid: '
                'H2SO4 + 2NaOH -> Na2SO4 + 2H2O. Determine the concentration '
                'of the sulfuric acid.',
        "options": [
            '0.0500 mol/dm3',
            '0.100 mol/dm3',
            '0.200 mol/dm3',
            '0.400 mol/dm3',
        ],
        "correct_index": 1,
        "why": 'The alkali holds 0.100 times 0.0250, which is 0.00250 mol; '
               'the ratio is two NaOH to one H2SO4, so the acid holds '
               '0.00125 mol, and 0.00125 divided by 0.0125 is 0.100 mol/dm3.',
    },
    {
        "id": 'ks4-titrations-h20',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A titration finds a hydrochloric acid concentration of '
                '0.200 mol/dm3. Calculate its concentration in g/dm3, given '
                'that the relative formula mass of HCl is 36.5.',
        "options": [
            '3.65 g/dm3',
            '7.30 g/dm3',
            '18.25 g/dm3',
            '73.0 g/dm3',
        ],
        "correct_index": 1,
        "why": 'Concentration in g/dm3 is the concentration in mol/dm3 '
               'multiplied by the relative formula mass, so 0.200 times '
               '36.5 gives 7.30 g/dm3.',
    },
    {
        "id": 'ks4-titrations-h21',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why a chemist dilutes an acid to a lower '
                'concentration before a titration, even though this makes the '
                'titre larger.',
        "options": [
            'A larger titre makes the fixed reading error a smaller '
            'percentage of the volume measured, which improves precision',
            'A dilute acid reacts with the alkali more completely than a '
            'concentrated acid of the same volume does',
            'A dilute acid changes the colour of the indicator more sharply '
            'and more suddenly than a concentrated one does',
            'A dilute acid is safer to store in the laboratory, and that is '
            'the real reason chemists dilute it',
        ],
        "correct_index": 0,
        "why": 'The burette\'s uncertainty stays the same however large the '
               'titre is, so a larger titre spreads that fixed error over a '
               'bigger volume and lowers the percentage uncertainty.',
    },
    {
        "id": 'ks4-titrations-h22',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Evaluate the claim that a titration can only be carried out '
                'if the acid or the alkali is itself coloured.',
        "options": [
            'Sound, because a colour change can be seen just when the '
            'solution already carries some colour of its own',
            'Sound, provided the acid rather than the alkali is the coloured '
            'one of the two',
            'Unsound: both solutions are usually colourless, and the '
            'indicator supplies the colour change instead',
            'Unsound, because a titration can be carried out with no '
            'colour of its own present in either solution',
        ],
        "correct_index": 2,
        "why": 'A strong acid and a strong alkali are both colourless in this '
               'required practical; the indicator, not the reactants, is what '
               'shows the end point.',
    },
    {
        "id": 'ks4-titrations-h23',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": '25.0 cm3 of a sodium hydroxide solution is titrated against '
                '15.0 cm3 of 0.200 mol/dm3 hydrochloric acid. Calculate the '
                'mass of sodium hydroxide dissolved in 250 cm3 of the '
                'original solution. (Mr of NaOH = 40)',
        "options": [
            '0.12 g',
            '0.30 g',
            '1.2 g',
            '3.0 g',
        ],
        "correct_index": 2,
        "why": 'The acid holds 0.00300 mol, so 25.0 cm3 of alkali holds '
               '0.00300 mol too, giving 0.120 mol/dm3; in 250 cm3 that is '
               '0.0300 mol, and 0.0300 times 40 is 1.2 g.',
    },
    {
        "id": 'ks4-titrations-h24',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A titre of 4.00 cm3 is measured with a standard burette '
                '(plus or minus 0.05 cm3 per reading) and, separately, with a '
                'micro-burette (plus or minus 0.01 cm3 per reading). Compare '
                'the percentage uncertainty each gives for this small titre.',
        "options": [
            'Standard burette 2.5%, micro-burette 0.5%',
            'Standard burette 0.5%, micro-burette 2.5%',
            'Both give exactly the same percentage uncertainty',
            'Standard burette 5.0%, micro-burette 1.0%',
        ],
        "correct_index": 0,
        "why": 'The standard burette carries a combined uncertainty of '
               '0.10 cm3, which is 2.5% of 4.00 cm3; the micro-burette\'s '
               '0.02 cm3 is only 0.5%, which is why a small titre is best '
               'measured on the finer scale.',
    },
    {
        "id": 'ks4-titrations-h25',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": '25.00 cm3 of 0.100 mol/dm3 hydrochloric acid exactly '
                'neutralises 25.00 cm3 of a sodium hydroxide solution that is '
                'also 0.100 mol/dm3. Deduce the mole ratio in which the acid '
                'and the alkali have reacted.',
        "options": [
            'One mole of acid to one mole of alkali',
            'One mole of acid to two moles of alkali',
            'Two moles of acid to one mole of alkali',
            'The ratio cannot be found from this information alone',
        ],
        "correct_index": 0,
        "why": 'Equal volumes at equal concentrations supply equal moles of '
               'each, 0.00250 mol, so the two must react in a one-to-one '
               'ratio.',
    },
    {
        "id": 'ks4-titrations-h26',
        "subtopic_slug": 'titrations',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A titration is repeated using acid of twice the original '
                'concentration, with the same volume and concentration of '
                'alkali as before. Predict the effect on the titre.',
        "options": [
            'The titre doubles, because a stronger acid needs a larger volume '
            'to react completely',
            'The titre halves, because each cm3 of the stronger acid '
            'neutralises twice as much alkali',
            'The titre is unchanged, because concentration has no effect on '
            'the volume needed',
            'The titre falls to a quarter of what it was, because both the '
            'rate and the concentration have changed',
        ],
        "correct_index": 1,
        "why": 'The alkali still needs the same number of moles of acid to '
               'neutralise it, and at double the concentration that many '
               'moles is delivered in half the volume.',
    },
]
