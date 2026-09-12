"""Chemistry · Chemical analysis — the MRB-338 expansion for `chromatography`.

KS4 depth throughout: the two phases and why a substance distributes between
them, Rf as a ratio with no unit, the calculation and both of its
rearrangements, and the practical decisions that decide whether an Rf is worth
quoting — spot size, where the distance is measured from, solvent depth, the
solvent named alongside the value.

Every distance a row needs is written into the stem, so nothing here asks a
pupil to look at a chromatogram. Harder rows lean on rearrangement, on the
limits of a single Rf match, and on evaluating a result rather than producing one.
"""

TOPIC = "analysis"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-chromatography-e07',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the process by which the solvent rises up the chromatography paper.',
        "options": [
            'Capillary action',
            'Evaporation of the solvent',
            'Diffusion',
            'Condensation',
        ],
        "correct_index": 0,
        "why": 'The solvent is drawn up through the fine spaces between the paper '
               'fibres by capillary action, carrying dissolved substances with it.',
    },
    {
        "id": 'ks4-chromatography-e08',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what an Rf value of 1 would tell you about a substance.',
        "options": [
            'It stayed exactly where it was placed on the baseline',
            'It travelled as far up the paper as the solvent front',
            'It travelled exactly one centimetre up the paper',
            'It dissolved completely and left no spot behind at all',
        ],
        "correct_index": 1,
        "why": 'Rf is the spot distance divided by the solvent front distance, so a '
               'value of 1 means the two distances are equal.',
    },
    {
        "id": 'ks4-chromatography-e09',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the unit of an Rf value.',
        "options": [
            'Centimetres',
            'Centimetres per minute',
            'It has no unit',
            'Grams per centimetre',
        ],
        "correct_index": 2,
        "why": 'Rf is one distance divided by another distance, so the units cancel '
               'and the value is a plain number.',
    },
    {
        "id": 'ks4-chromatography-e10',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A substance does not move from the baseline during a run. State its Rf value.',
        "options": [
            '1, because it stayed on the paper the whole time',
            '0.5, because it lies halfway between 0 and 1',
            'It has no Rf value that can be worked out',
            '0, because it travelled no distance at all',
        ],
        "correct_index": 3,
        "why": 'A distance of zero divided by the solvent front distance gives '
               'zero, so the substance stayed on the baseline.',
    },
    {
        "id": 'ks4-chromatography-e11',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Calculate the Rf value of a spot 2.0 cm from the baseline when the solvent front is at 8.0 cm.',
        "options": [
            '0.25',
            '4.0',
            '0.40',
            '6.0',
        ],
        "correct_index": 0,
        "why": 'Rf = 2.0 ÷ 8.0 = 0.25.',
    },
    {
        "id": 'ks4-chromatography-e12',
        "subtopic_slug": 'chromatography',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why a substance that is insoluble in the solvent stays on the baseline.',
        "options": [
            'It is too heavy to be lifted up the paper by the solvent',
            'It is not carried, because it does not dissolve in the solvent',
            'It reacts with the paper fibres and so becomes permanently fixed there',
            'It evaporates before the solvent can reach it on the paper',
        ],
        "correct_index": 1,
        "why": 'Only substances that dissolve in the mobile phase can be carried up '
               'the paper, so an insoluble substance cannot move.',
    },
    {
        "id": 'ks4-chromatography-s11',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why one substance in a mixture travels further up the paper than another.',
        "options": [
            'It has smaller particles, and small particles always move faster',
            'It is denser, so gravity pulls on it less as it rises up the paper',
            'It is more soluble in the solvent and less attracted to the paper',
            'It was spotted onto the baseline first, so it had a head start',
        ],
        "correct_index": 2,
        "why": 'A substance held more strongly by the mobile phase than by the '
               'stationary phase spends more time moving, so it travels further.',
    },
    {
        "id": 'ks4-chromatography-s12',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In one run the solvent front reaches 8.0 cm and a green dye reaches 5.6 cm. Calculate the Rf value of the green dye.',
        "options": [
            '1.43',
            '0.56',
            '2.40',
            '0.70',
        ],
        "correct_index": 3,
        "why": 'Rf = 5.6 ÷ 8.0 = 0.70.',
    },
    {
        "id": 'ks4-chromatography-s13',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the distance travelled by a spot is measured to the centre of the spot.',
        "options": [
            'The centre is where the substance is most concentrated on average',
            'The centre is the only part of the spot that moved',
            'The centre is always exactly halfway to the solvent front',
            'The edge is where the solvent collects and dries first',
        ],
        "correct_index": 0,
        "why": 'A spot spreads as it rises, so its centre is the best single '
               'measure of how far the substance has travelled and keeps results '
               'comparable.',
    },
    {
        "id": 'ks4-chromatography-s14',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why only a shallow depth of solvent is placed in the chromatography tank.',
        "options": [
            'A deep solvent would simply evaporate away before it ever reached the paper',
            'A deep solvent would reach the baseline and dissolve the spots away',
            'A deep solvent would make the paper too heavy to stay upright',
            'A deep solvent would react with the dyes and change their colours',
        ],
        "correct_index": 1,
        "why": 'The solvent must start below the baseline so the sample is carried '
               'up the paper rather than washed off into the solvent.',
    },
    {
        "id": 'ks4-chromatography-s15',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how a reference spot of a known substance is used to identify an unknown sample.',
        "options": [
            'Run them on separate papers and compare how long each run took',
            'Run the unknown first and then add the reference to the same spot',
            'Run them side by side and compare how far each one travels',
            'Run them together and measure the total distance of both spots',
        ],
        "correct_index": 2,
        "why": 'Run in the same solvent at the same time, two substances with the '
               'same Rf are very likely to be the same substance.',
    },
    {
        "id": 'ks4-chromatography-s16',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why an Rf value must always be quoted together with the solvent that was used.',
        "options": [
            'Different solvents evaporate at different rates as the run goes on',
            'Some solvents are too dangerous for a school laboratory to use',
            'The solvent has to be named so the paper can be reused afterwards',
            'The same substance gives a different Rf value in a different solvent',
        ],
        "correct_index": 3,
        "why": 'Rf depends on how the substance divides between that solvent and '
               'the paper, so the value only identifies a substance within a named '
               'solvent.',
    },
    {
        "id": 'ks4-chromatography-s17',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how chromatography is used to check whether a food contains a colouring that is not declared on its label.',
        "options": [
            "Compare the food's spots with reference spots of permitted colourings",
            'Measure the melting point of the food and check it in a data book',
            'Add silver nitrate solution to the food and record the colour of any solid formed',
            'Weigh the food before and after running it to find the mass lost',
        ],
        "correct_index": 0,
        "why": "A spot in the food's chromatogram that matches no declared "
               'colouring, or that matches a banned dye run alongside, reveals the '
               'undeclared additive.',
    },
    {
        "id": 'ks4-chromatography-s18',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A dye has an Rf value of 0.40 in a solvent. In one run the solvent front travels 7.5 cm. Calculate the distance the dye travels.',
        "options": [
            '18.8 cm',
            '3.0 cm',
            '4.5 cm',
            '0.05 cm',
        ],
        "correct_index": 1,
        "why": 'Rearranging Rf = spot ÷ front gives spot = 0.40 × 7.5 = 3.0 cm.',
    },
    {
        "id": 'ks4-chromatography-s19',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why two substances with very similar solubilities are hard to separate by paper chromatography.',
        "options": [
            'They react together on the paper and form a single new compound',
            'They dissolve so well that neither of them leaves the baseline',
            'They travel almost the same distance, so their spots overlap',
            'They both travel to the solvent front and cannot be measured',
        ],
        "correct_index": 2,
        "why": 'Separation depends on a difference in how far each substance is '
               'carried, so similar solubilities give Rf values too close to tell '
               'apart.',
    },
    {
        "id": 'ks4-chromatography-s20',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student marks the baseline with a ballpoint pen instead of a pencil. Predict what appears on the finished chromatogram.',
        "options": [
            'Nothing at all, because ballpoint ink is fixed permanently onto the paper fibres',
            'A single black line that rises with the solvent front unchanged',
            'The sample spots disappear, because ink dissolves them away',
            'Extra spots, because the ink itself separates as the solvent rises',
        ],
        "correct_index": 3,
        "why": 'Ballpoint ink is itself a mixture of dyes, so it runs with the '
               'solvent and adds spots that did not come from the sample.',
    },
    {
        "id": 'ks4-chromatography-s21',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": "Describe how chromatography is used to test an athlete's urine sample for a banned substance.",
        "options": [
            'Separate the sample and compare it with a reference of the substance',
            'Measure the boiling point of the sample and check it against published data',
            'Warm the sample with sodium hydroxide and test the gas released',
            "Weigh the sample and compare the mass with a healthy athlete's",
        ],
        "correct_index": 0,
        "why": 'The sample is separated into its components and a spot matching the '
               'reference substance, at the same Rf in the same solvent, identifies '
               'it.',
    },
    {
        "id": 'ks4-chromatography-s22',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two dyes give Rf values of 0.45 and 0.48 in the same solvent. Explain why this makes identification unreliable.',
        "options": [
            'Rf values this close cannot both be correct, so one must be wrong',
            'The values are so close that measurement error could swap them',
            'An Rf value below 0.50 is never accepted as an identification',
            'Two dyes can never have Rf values that differ by less than 0.10',
        ],
        "correct_index": 1,
        "why": 'Ordinary uncertainty in measuring the spot and the front is '
               'comparable with the difference between the two values, so they '
               'cannot be told apart.',
    },
    {
        "id": 'ks4-chromatography-s23',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the chromatography paper must not touch the sides of the tank during a run.',
        "options": [
            'Contact would make the paper heat up and dry out the solvent',
            'Contact would stop capillary action starting anywhere on the paper',
            'Contact would let solvent travel unevenly and distort the front',
            'Contact would make the dyes react with the glass of the tank',
        ],
        "correct_index": 2,
        "why": 'Solvent wicking along the glass makes the front rise unevenly, so '
               'the distances measured no longer correspond to a single front.',
    },
    {
        "id": 'ks4-chromatography-s24',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student finds the solvent front on their finished chromatogram is curved rather than straight. Suggest a cause.',
        "options": [
            'The baseline was drawn with a pencil rather than with a pen',
            'The spot placed on the baseline was too small to be seen',
            'The solvent used was water rather than an organic solvent',
            'The paper was not hanging vertically in the solvent',
        ],
        "correct_index": 3,
        "why": 'If the paper is tilted or uneven in the solvent, one side starts '
               'rising before the other and the front is no longer a straight line.',
    },
    {
        "id": 'ks4-chromatography-s25',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a spot that is too large gives a less reliable Rf value.',
        "options": [
            'A large spot spreads further, so its centre is harder to locate',
            'A large spot dissolves so much solvent that the front slows down',
            'A large spot always travels further than a small one would',
            'A large spot changes the solvent into a mixture as it dissolves',
        ],
        "correct_index": 0,
        "why": 'The measurement is taken to the centre of the spot, and a broad '
               'smear makes that centre uncertain, so the calculated Rf is '
               'uncertain too.',
    },
    {
        "id": 'ks4-chromatography-s26',
        "subtopic_slug": 'chromatography',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how a chemist uses chromatography to check that a medicine contains only its intended active ingredient.',
        "options": [
            'Run the medicine and measure the total distance that all of the spots travel',
            'Run the medicine and look for any spot other than the expected one',
            'Run the medicine twice and check the second run takes less time',
            'Run the medicine and weigh the paper before and after the run',
        ],
        "correct_index": 1,
        "why": 'Any additional spot is a component that should not be there, so a '
               'single spot at the expected Rf is the evidence the chemist is '
               'looking for.',
    },
    {
        "id": 'ks4-chromatography-h10',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A spot has an Rf value of 0.75 and the solvent front travelled 12.0 cm. Determine the distance travelled by the spot.',
        "options": [
            '16.0 cm',
            '3.0 cm',
            '9.0 cm',
            '0.06 cm',
        ],
        "correct_index": 2,
        "why": 'spot = Rf × front = 0.75 × 12.0 = 9.0 cm.',
    },
    {
        "id": 'ks4-chromatography-h11',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A blue dye of known Rf value 0.35 leaves a spot 4.2 cm above the baseline. Determine how far the solvent front rose.',
        "options": [
            '1.47 cm',
            '8.4 cm',
            '0.08 cm',
            '12 cm',
        ],
        "correct_index": 3,
        "why": 'front = spot ÷ Rf = 4.2 ÷ 0.35 = 12 cm.',
    },
    {
        "id": 'ks4-chromatography-h12',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why an Rf value has no unit even though both measurements are made in centimetres.',
        "options": [
            'One distance is divided by another, so the centimetres cancel',
            'Distances measured on paper are always treated as plain numbers',
            'The value is a percentage, and percentages never carry any unit',
            'The unit is dropped because the answer is always less than one',
        ],
        "correct_index": 0,
        "why": 'Dividing a length by a length leaves a pure ratio, which is why the '
               'same Rf comes out whether the distances are in centimetres or '
               'millimetres.',
    },
    {
        "id": 'ks4-chromatography-h13',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why paper is used as the stationary phase rather than a strip of smooth plastic.',
        "options": [
            'Paper is cheaper, and cost is the only reason',
            'Solvent rises through paper fibres but not through plastic',
            'Paper is made of fibres that push the dyes upwards themselves',
            'Paper reacts with the dyes and holds them still',
        ],
        "correct_index": 1,
        "why": 'Capillary action needs the fine spaces between the fibres; a smooth '
               'non-absorbent strip gives the solvent nothing to rise through.',
    },
    {
        "id": 'ks4-chromatography-h14',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two spots in one run have Rf values of 0.25 and 0.80. Determine which substance is more soluble in the solvent used, and justify the choice.',
        "options": [
            'The 0.25 one, because a low Rf shows it dissolved most quickly',
            'Neither, because Rf depends only on the paper and not the solvent',
            'The 0.80 one, because it was carried further by the solvent',
            'The 0.25 one, because it stayed nearer the solvent it dissolved in',
        ],
        "correct_index": 2,
        "why": 'The substance held more strongly by the mobile phase spends more of '
               'the run moving, so the higher Rf belongs to the more soluble '
               'substance.',
    },
    {
        "id": 'ks4-chromatography-h15',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why gas chromatography linked to a mass spectrometer identifies a drug more reliably than paper chromatography does.',
        "options": [
            'It uses no solvent, so there is nothing left to cause any error',
            'It gives an Rf value that is correct in every possible solvent',
            'It works on coloured substances, which paper chromatography cannot',
            'It separates the mixture and then measures each component directly',
        ],
        "correct_index": 3,
        "why": 'Paper chromatography can only say that something travelled the same '
               'distance as a reference, while the mass spectrometer measures the '
               'component itself.',
    },
    {
        "id": 'ks4-chromatography-h16',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A dye has an Rf value of 0.60 in one solvent. Predict its Rf value in a different solvent and explain your prediction.',
        "options": [
            'Probably different, because solubility in the new solvent differs',
            'Exactly 0.60, because Rf is a fixed property of the dye itself',
            'Exactly 0.40, because the two values must always add up to one',
            'Always higher, because a second solvent adds its own effect to the first one',
        ],
        "correct_index": 0,
        "why": 'Rf describes how the dye divides between one particular solvent and '
               'the paper, so changing the solvent generally changes the value.',
    },
    {
        "id": 'ks4-chromatography-h17',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Ink taken from a signed document separates into four spots. Ink from the pen said to have written it separates into three. Deduce what this shows.',
        "options": [
            'The two inks are the same, since three of the spots do match',
            'The two inks are different, since their components are not the same',
            'The document ink is purer, since it produced more separate spots',
            'Nothing can be deduced, since spot counts vary between any two runs',
        ],
        "correct_index": 1,
        "why": 'A chromatogram shows how many components a mixture has, so an extra '
               'component means the document ink is not the ink from that pen.',
    },
    {
        "id": 'ks4-chromatography-h18',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A spot travels 33 mm while the solvent front travels 88 mm. Calculate the Rf value to 2 significant figures.',
        "options": [
            '2.7',
            '0.27',
            '0.38',
            '3.8',
        ],
        "correct_index": 2,
        "why": '33 ÷ 88 = 0.375, which is 0.38 to 2 significant figures.',
    },
    {
        "id": 'ks4-chromatography-h19',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student reports that one run of a mixture gave three spots with Rf values of 0.15, 0.15 and 0.62. Explain why a chemist would question this result.',
        "options": [
            'Three spots is too many for any mixture run in one solvent',
            'Rf values below 0.20 are always rejected as unreliable readings',
            'The three values should have added up to 1.00 for one run',
            'Two spots with the same Rf would have travelled together as one',
        ],
        "correct_index": 3,
        "why": 'Rf is the distance travelled, so two components with the same Rf '
               'finish in the same place and cannot appear as two separate spots.',
    },
    {
        "id": 'ks4-chromatography-h20',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why chromatography is described as separating substances between two phases rather than simply dissolving them.',
        "options": [
            'Each substance is shared between the moving solvent and the paper',
            'Only one of the substances dissolves and the rest stay behind',
            'The solvent dissolves the paper, which is the second phase',
            'Dissolving all happens first and then the separating happens afterwards',
        ],
        "correct_index": 0,
        "why": 'A substance is constantly held by the paper and released into the '
               'solvent, and the balance between the two decides how far it '
               'travels.',
    },
    {
        "id": 'ks4-chromatography-h21',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'On a finished chromatogram all four dyes have run to the very top of the paper and bunched together. Determine the change that would separate them better.',
        "options": [
            'Use a shorter piece of paper, so the dyes have less room to bunch',
            'Use a solvent the dyes are less soluble in, so they travel less far',
            'Use a larger spot, so each dye leaves a wider mark on the paper',
            'Leave the paper in the tank for longer, so the dyes spread apart',
        ],
        "correct_index": 1,
        "why": 'Dyes that all reach the front have Rf values near 1 and cannot be '
               'told apart, so a solvent that carries them less far spreads the '
               'values out.',
    },
    {
        "id": 'ks4-chromatography-h22',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two samples each give a single spot with the same Rf value in one solvent. Determine what further test would give better evidence that they are the same substance.',
        "options": [
            'Repeat the identical run and check the same value comes out',
            'Run one sample on a longer piece of chromatography paper',
            'Run both samples again in a second, different solvent',
            'Leave both papers in the tank for twice as long as before',
        ],
        "correct_index": 2,
        "why": 'Two different substances rarely share an Rf in two different '
               'solvents, so agreement in both runs is much stronger evidence than '
               'agreement in one.',
    },
    {
        "id": 'ks4-chromatography-h23',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A medicine is 99% pure by mass. Explain why its chromatogram may still show a second, faint spot.',
        "options": [
            'The active ingredient always splits into two spots',
            'A faint spot appears whenever a sample is 90% pure',
            'The solvent leaves a spot of its own at the top',
            'The 1% impurity is still present and separates as its own spot',
        ],
        "correct_index": 3,
        "why": 'Chromatography detects a component regardless of how little of it '
               'there is, so a small impurity still produces a spot, only a fainter '
               'one.',
    },
    {
        "id": 'ks4-chromatography-h24',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'In one run the solvent front travels 10.0 cm and three spots travel 2.5 cm, 5.0 cm and 7.5 cm. Calculate the Rf value of the middle spot.',
        "options": [
            '0.50',
            '0.25',
            '2.00',
            '0.75',
        ],
        "correct_index": 0,
        "why": 'Rf = 5.0 ÷ 10.0 = 0.50 for the middle spot.',
    },
    {
        "id": 'ks4-chromatography-h25',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a chemist testing for a banned substance runs a reference sample of it on the same paper at the same time.',
        "options": [
            'The reference makes the unknown sample dissolve much more readily',
            'Both then experience the same solvent and the same conditions',
            'The reference is needed to make the solvent rise up the paper',
            'Two samples always separate better than one sample does alone',
        ],
        "correct_index": 1,
        "why": 'Rf depends on the solvent, the paper and the conditions, so a '
               'reference run alongside removes those variables from the '
               'comparison.',
    },
    {
        "id": 'ks4-chromatography-h26',
        "subtopic_slug": 'chromatography',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student measures distances to the nearest millimetre on a run where the solvent front reaches 10.0 cm, then reports Rf values to three decimal places. Evaluate this.',
        "options": [
            'Reasonable, because dividing two numbers always adds precision',
            'Reasonable, because Rf values are always quoted to three places',
            'Unjustified, because the measurements only support two places',
            'Unjustified, because Rf values should be given as whole numbers',
        ],
        "correct_index": 2,
        "why": 'A reading to the nearest millimetre out of 100 mm is uncertain in '
               'the second decimal place, so a third decimal place claims precision '
               'not measured.',
    },
]
