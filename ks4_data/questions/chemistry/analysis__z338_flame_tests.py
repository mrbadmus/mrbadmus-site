"""Chemistry · Chemical analysis — the MRB-338 expansion for `flame-tests`.

Five colours, one method, and a great deal of interpretation. The colours are
written exactly as AQA gives them — lithium crimson, sodium yellow, potassium
lilac, calcium orange-red, copper green — and every row that needs an
observation states it in the stem.

Most of the weight sits on what the test can and cannot say: it identifies the
METAL ION and never the negative ion, one strong colour masks a weaker one,
two of the five colours are genuinely hard to tell apart by eye, and a judgement
made by eye is subjective. Named compounds (lithium carbonate, copper(II)
sulfate, potassium nitrate, calcium chloride) supply the applied rows.
"""

TOPIC = "analysis"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-flame-tests-e05',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the flame colour produced by sodium ions.',
        "options": [
            'Yellow',
            'Lilac',
            'Crimson',
            'Green',
        ],
        "correct_index": 0,
        "why": 'Sodium gives a strong yellow flame, and even a trace of it produces '
               'a clear colour.',
    },
    {
        "id": 'ks4-flame-tests-e06',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State the flame colour produced by calcium ions.',
        "options": [
            'Lilac',
            'Orange-red',
            'Green',
            'Bright yellow-green',
        ],
        "correct_index": 1,
        "why": 'Calcium gives an orange-red flame, which is close enough to '
               "lithium's crimson that the two are easily confused.",
    },
    {
        "id": 'ks4-flame-tests-e07',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the metal that the wire loop used in a flame test is made from.',
        "options": [
            'Copper coated with tin',
            'Iron',
            'Nichrome',
            'Lead',
        ],
        "correct_index": 2,
        "why": 'Nichrome is used because it has a high melting point, does not '
               'react and gives no flame colour of its own.',
    },
    {
        "id": 'ks4-flame-tests-e08',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Name the acid used to clean the wire loop before a flame test.',
        "options": [
            'Sulfuric acid',
            'Nitric acid',
            'Concentrated ethanoic acid solution',
            'Hydrochloric acid',
        ],
        "correct_index": 3,
        "why": 'Dilute hydrochloric acid converts any ions left on the wire into '
               'volatile chlorides that burn off in the flame.',
    },
    {
        "id": 'ks4-flame-tests-e09',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State where in the Bunsen flame the loaded loop should be held.',
        "options": [
            'In the edge of a blue flame',
            'Inside the barrel of the burner',
            'Above the top of the flame',
            'Below the air hole of the burner',
        ],
        "correct_index": 0,
        "why": 'The edge of a hot blue flame gives enough energy to excite the ions '
               'while keeping the flame itself almost colourless.',
    },
    {
        "id": 'ks4-flame-tests-e10',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State what part of a compound a flame test identifies.',
        "options": [
            'The negative ion present',
            'The metal ion present',
            'The total mass of the sample',
            'The water content of the sample',
        ],
        "correct_index": 1,
        "why": 'The colour comes from electrons in the metal ion, so the test says '
               'nothing at all about the negative ion.',
    },
    {
        "id": 'ks4-flame-tests-e11',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the wire loop is cleaned between one flame test and the next.',
        "options": [
            'So the loop does not get so hot that it cannot be held safely at all',
            'So the loop does not melt in the blue Bunsen flame',
            'So the colour of the previous sample is not seen again',
            'So the acid has time to dry before the next sample',
        ],
        "correct_index": 2,
        "why": 'Traces left on the wire would colour the next flame and give a '
               'false result for the new sample.',
    },
    {
        "id": 'ks4-flame-tests-e12',
        "subtopic_slug": 'flame-tests',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'State why the wire is dipped in acid rather than rinsed in water before a test.',
        "options": [
            'Water would cool the wire far too much to be useful',
            'Water would react with the metal of the loop and corrode it very badly',
            'Acid makes the sample stick to the loop much more firmly',
            'Acid removes ions that a rinse in water would leave behind',
        ],
        "correct_index": 3,
        "why": 'Many metal salts are not washed off by water, but acid converts '
               'them into chlorides that evaporate away in the flame.',
    },
    {
        "id": 'ks4-flame-tests-s05',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the wire loop used in a flame test is not made of copper.',
        "options": [
            'Copper ions would colour the flame green and hide the result',
            'Copper is too expensive to use for a simple laboratory wire',
            'Copper does not conduct heat well enough to reach the sample',
            'Copper dissolves completely in the acid used to clean the wire',
        ],
        "correct_index": 0,
        "why": 'A loop that coloured the flame itself would make every result '
               'unreadable, so a metal giving no colour of its own is used.',
    },
    {
        "id": 'ks4-flame-tests-s06',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Predict the flame colour given by lithium carbonate.',
        "options": [
            'Green, because carbonates always burn with a green flame',
            'Crimson, because the metal ion present is lithium',
            'Yellow, because carbon in the carbonate glows yellow hot',
            'Lilac, because carbonates of group 1 all give a lilac flame',
        ],
        "correct_index": 1,
        "why": 'The colour depends only on the metal ion, so any lithium compound '
               'gives the crimson flame of lithium.',
    },
    {
        "id": 'ks4-flame-tests-s07',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Predict the flame colour given by copper(II) sulfate.',
        "options": [
            'Blue, because copper(II) sulfate crystals are blue',
            'Yellow, because sulfates always give a yellow flame',
            'Green, because the metal ion present is copper',
            'Crimson, because sulfur burns with a crimson flame',
        ],
        "correct_index": 2,
        "why": 'Copper ions give a green flame whatever the compound, and the blue '
               'of the crystals has nothing to do with the flame colour.',
    },
    {
        "id": 'ks4-flame-tests-s08',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why sodium chloride and sodium carbonate give the same flame colour.',
        "options": [
            'Both compounds contain chlorine, which colours the flame',
            'Both compounds are white solids, and white solids burn alike',
            'Sodium carbonate turns into sodium chloride in the flame first',
            'The colour comes from the sodium ion, which both contain',
        ],
        "correct_index": 3,
        "why": 'Only the metal ion emits the characteristic light, so every sodium '
               'compound gives the same yellow flame.',
    },
    {
        "id": 'ks4-flame-tests-s09',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a flame test cannot distinguish sodium chloride from sodium sulfate.',
        "options": [
            'The test responds to the metal ion, which is sodium in both',
            'Both are soluble, and soluble salts all behave in the same way',
            'Both salts decompose in the flame before any colour appears',
            'Chloride and sulfate ions happen to give the same colour',
        ],
        "correct_index": 0,
        "why": 'A flame test is blind to the negative ion, so an anion test such as '
               'acidified silver nitrate or barium chloride is needed as well.',
    },
    {
        "id": 'ks4-flame-tests-s10',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe how a flame test is carried out on a solution rather than on a solid.',
        "options": [
            'Pour the solution straight into the flame from a beaker',
            'Dip the cleaned loop into the solution and hold it in the flame',
            'Evaporate the solution completely to dryness before any test is possible',
            'Boil the solution and hold the loop in the steam given off',
        ],
        "correct_index": 1,
        "why": 'A drop held in the loop carries enough of the metal ion into the '
               'flame for the colour to be seen.',
    },
    {
        "id": 'ks4-flame-tests-s11',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the loop is cleaned repeatedly until it gives no colour at all.',
        "options": [
            'A clean loop is needed so the acid can wet it properly',
            'Repeated heating makes the nichrome wire much stronger',
            'Any colour remaining means ions are still on the wire',
            'The loop must be cold before a new sample is picked up',
        ],
        "correct_index": 2,
        "why": 'A colourless flame is the only proof that nothing is left on the '
               'wire to contaminate the next result.',
    },
    {
        "id": 'ks4-flame-tests-s12',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why a faint yellow tinge appears in very many flame tests.',
        "options": [
            'Yellow is the natural colour of a hot nichrome wire',
            'Yellow appears whenever the air hole is fully open',
            'Every metal ion gives a little yellow as well as its own colour',
            'Traces of sodium are present almost everywhere',
        ],
        "correct_index": 3,
        "why": 'Sodium compounds are so common, in glass, dust, tap water and on '
               'skin, that small amounts contaminate samples easily and sodium '
               'colours strongly.',
    },
    {
        "id": 'ks4-flame-tests-s13',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Predict the flame colour given by potassium nitrate.',
        "options": [
            'Lilac, because the metal ion present is potassium',
            'Orange-red, because nitrates give an orange-red flame',
            'Green, because nitrogen burns with a green flame',
            'Yellow, because all nitrates contain traces of sodium',
        ],
        "correct_index": 0,
        "why": 'Potassium gives a lilac flame in any of its compounds, since the '
               'nitrate ion contributes no colour.',
    },
    {
        "id": 'ks4-flame-tests-s14',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a flame test is described as a qualitative test.',
        "options": [
            'It uses too small a sample for any number to be given',
            'It tells you which ion is there but not how much',
            'It names the amount present but never says which ion it is',
            'It gives a quality score out of ten for each sample',
        ],
        "correct_index": 1,
        "why": "Qualitative means it answers 'which substance', while a "
               'quantitative method such as flame emission spectroscopy answers '
               "'how much'.",
    },
    {
        "id": 'ks4-flame-tests-s15',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A solid gives a lilac flame. Identify the metal ion and name one compound the solid could be.',
        "options": [
            'Lithium, and the solid could be lithium chloride',
            'Calcium, and the solid could be calcium carbonate or chloride',
            'Potassium, and the solid could be potassium chloride',
            'Copper, and the solid could be copper(II) sulfate',
        ],
        "correct_index": 2,
        "why": 'Lilac is the flame colour of potassium, and any potassium compound '
               'would give it.',
    },
    {
        "id": 'ks4-flame-tests-s16',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a street lamp containing sodium gives out an orange-yellow light.',
        "options": [
            'The glass of the lamp is tinted orange-yellow by the maker',
            'Orange-yellow is the colour of the sodium metal inside the lamp',
            'The filament inside the lamp glows orange-yellow when hot',
            'Excited sodium atoms emit light of that particular colour',
        ],
        "correct_index": 3,
        "why": 'It is the same emission that colours a flame test: electrons fall '
               'back to lower levels and release light of a characteristic colour.',
    },
    {
        "id": 'ks4-flame-tests-s17',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe how a student would use flame tests to tell lithium chloride from potassium chloride.',
        "options": [
            'Test both and look for crimson from one and lilac from the other',
            'Test both and look for yellow from one and green from the other',
            'Test both and compare how long each flame colour lasts for',
            'Test both and measure how hot each of the two flames becomes',
        ],
        "correct_index": 0,
        "why": 'The chloride is common to both, so only the metal ion differs, and '
               'crimson against lilac separates them clearly.',
    },
    {
        "id": 'ks4-flame-tests-s18',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student cannot decide whether a flame is crimson or orange-red. Suggest what they should do next.',
        "options": [
            'Record both colours and leave the identification open',
            'Test known lithium and calcium samples alongside for comparison',
            'Repeat the test with a much larger amount of the same solid',
            'Choose whichever colour the rest of the class has already recorded',
        ],
        "correct_index": 1,
        "why": 'Running known samples under identical conditions gives a direct '
               'comparison and removes most of the guesswork from the judgement.',
    },
    {
        "id": 'ks4-flame-tests-s19',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a flame test gives no information about whether a compound is a carbonate.',
        "options": [
            'Carbonates decompose completely before the flame is ever hot enough to test',
            'Carbonate ions give the same green colour as copper ions do',
            'Only the metal ion emits light, and carbonate is a negative ion',
            'The carbon in a carbonate burns away before any colour shows',
        ],
        "correct_index": 2,
        "why": 'Identifying a carbonate needs a separate test, adding dilute acid '
               'and showing the gas turns limewater milky.',
    },
    {
        "id": 'ks4-flame-tests-s20',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Predict what is seen when calcium chloride is held in a blue Bunsen flame on a clean loop.',
        "options": [
            'A green flame, because chloride ions colour a flame green',
            'A lilac flame, because calcium is in the same group as potassium',
            'No colour at all, because calcium chloride is a white solid',
            'An orange-red flame, because the metal ion is calcium',
        ],
        "correct_index": 3,
        "why": 'Calcium gives an orange-red flame, and the chloride ion contributes '
               'no colour of its own.',
    },
    {
        "id": 'ks4-flame-tests-s21',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why flame tests are easier to judge in a shaded part of the laboratory.',
        "options": [
            'Bright light washes out the colour and makes it hard to see',
            'Shade keeps the sample cool so it lasts a great deal longer',
            'Shade makes the Bunsen flame burn at a much higher temperature',
            'Bright light reacts with the sample and changes its colour',
        ],
        "correct_index": 0,
        "why": 'The emitted light is faint, so a bright background makes '
               'distinguishing crimson from orange-red harder still.',
    },
    {
        "id": 'ks4-flame-tests-s22',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe a fair way to compare two unknown solids using flame tests.',
        "options": [
            'Use two loops at once so both flames can be seen together',
            'Use the same loop, same flame and clean it between the tests',
            'Use a larger amount of the second solid to make it clearer',
            'Use a yellow flame for one solid and a blue flame for the other',
        ],
        "correct_index": 1,
        "why": 'Keeping everything except the sample the same is what makes the '
               'comparison fair, and cleaning prevents one result carrying into the '
               'next.',
    },
    {
        "id": 'ks4-flame-tests-s23',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why copper compounds are added to a firework that is meant to burn green.',
        "options": [
            'Copper metal itself is green, so the flame takes that colour',
            'Copper reacts with the gunpowder and produces a green gas',
            'Copper ions emit green light when they are heated strongly',
            'Copper reflects the green part of the light from the flame',
        ],
        "correct_index": 2,
        "why": 'It is the same emission as the flame test: energy excites electrons '
               'in the copper ions and green light is given out as they fall back.',
    },
    {
        "id": 'ks4-flame-tests-s24',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why a wooden splint soaked in the sample can be used in place of a wire loop.',
        "options": [
            'A splint is a metal, so it behaves in the same way as a loop',
            'A splint burns with a flame that has no colour of its own',
            'A splint can be cleaned in acid and used again many times',
            'A splint carries the sample into the flame and is thrown away after',
        ],
        "correct_index": 3,
        "why": 'A fresh splint each time removes the risk of carry-over entirely, '
               'which is the main thing the acid cleaning is there to prevent.',
    },
    {
        "id": 'ks4-flame-tests-s25',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a flame test on its own cannot identify an unknown compound.',
        "options": [
            'It shows the metal ion but not the negative ion present',
            'It shows the negative ion but never the metal ion present',
            'It shows the mass of the sample but not what it contains',
            'It only works on compounds that have already been named',
        ],
        "correct_index": 0,
        "why": 'A compound is a metal ion and a negative ion together, so a second '
               'test is always needed before the compound itself can be named.',
    },
    {
        "id": 'ks4-flame-tests-s26',
        "subtopic_slug": 'flame-tests',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the colour in a flame test is described as light being given out rather than absorbed.',
        "options": [
            'The sample takes light from the flame and keeps hold of it',
            'Electrons fall back to lower levels and release the light',
            'The flame becomes darker where the sample is being heated',
            'The colour is the sample reflecting the light of the Bunsen',
        ],
        "correct_index": 1,
        "why": 'Energy from the flame lifts electrons to higher levels, and the '
               'light is emitted when they drop back down again.',
    },
    {
        "id": 'ks4-flame-tests-h05',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the light emitted in a flame test has particular colours rather than a continuous spread of colours.',
        "options": [
            'The flame filters out every colour except one at a time',
            'Only one electron in the sample can move at a time',
            'Electrons drop between fixed levels, so fixed energies are emitted',
            'The colours seen depend on how hot the Bunsen flame is made',
        ],
        "correct_index": 2,
        "why": 'Energy levels in an atom are fixed, so only certain energy '
               'differences, and therefore only certain colours of light, are '
               'possible.',
    },
    {
        "id": 'ks4-flame-tests-h06',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A compound gives a green flame, and its solution gives a blue precipitate with sodium hydroxide. Deduce which metal ion it contains.',
        "options": [
            'Iron(II), Fe2+',
            'Calcium, Ca2+',
            'Iron(III), Fe3+',
            'Copper(II), Cu2+',
        ],
        "correct_index": 3,
        "why": 'Copper(II) is the ion that gives both a green flame and a blue '
               'hydroxide precipitate, so the two results agree.',
    },
    {
        "id": 'ks4-flame-tests-h07',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Two students test the same solid. One records crimson and the other records orange-red. Determine how the disagreement should be settled.',
        "options": [
            'Analyse the sample by flame emission spectroscopy instead',
            'Take the average of the two colours that were recorded',
            'Accept whichever student carried out the test more recently',
            'Repeat the test with more sample until one colour dominates',
        ],
        "correct_index": 0,
        "why": 'The instrument measures wavelength rather than relying on a '
               'judgement by eye, so it separates lithium from calcium without '
               'argument.',
    },
    {
        "id": 'ks4-flame-tests-h08',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why a flame test gives a colour with an ionic compound but no colour with a sample of pure water.',
        "options": [
            'Water is a liquid, and only solids can be tested in a flame',
            'Pure water contains no metal ions to emit coloured light',
            'Water puts out the flame before any colour has time to form',
            'Water absorbs all the light emitted before it can be seen',
        ],
        "correct_index": 1,
        "why": 'The colour comes from electrons in metal ions, and pure water has '
               'none, which is also why tap water can give a faint sodium colour.',
    },
    {
        "id": 'ks4-flame-tests-h09',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Describe how to show that a yellow flame comes from the sample itself rather than from a dirty wire.',
        "options": [
            'Use a bigger sample so contamination matters less',
            'Test the sample twice and see whether the colour is the same',
            'Hold the cleaned wire in the flame alone and check it stays colourless',
            'Clean the wire in water instead and repeat the test with it',
        ],
        "correct_index": 2,
        "why": 'A blank run on the clean wire is the control: if the empty loop '
               'gives no colour, the yellow must have come from the sample.',
    },
    {
        "id": 'ks4-flame-tests-h10',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A mixture contains a lithium compound and a copper compound. Predict what a single flame test would show and explain.',
        "options": [
            'A clear crimson and a clear green side by side in the flame',
            'No colour at all, because the two colours cancel each other out',
            'Only crimson, because lithium always masks every other colour',
            'One blended colour, so neither ion can be named with confidence',
        ],
        "correct_index": 3,
        "why": 'The emitted colours overlap in the same flame, which is exactly the '
               'limitation that flame emission spectroscopy removes.',
    },
    {
        "id": 'ks4-flame-tests-h11',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why flame tests are still taught and used in schools although instruments are more reliable.',
        "options": [
            'The apparatus is cheap and the result appears within seconds',
            'Instruments give the wrong answer more often than the eye does',
            'Flame tests can identify negative ions that instruments cannot',
            'Instruments are not allowed to be used in a school laboratory',
        ],
        "correct_index": 0,
        "why": 'A Bunsen burner and a wire cost almost nothing and give an '
               'immediate answer, which is enough when only a rough identification '
               'is needed.',
    },
    {
        "id": 'ks4-flame-tests-h12',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Four solids give crimson, yellow, lilac and green flames in that order. Determine the four metal ions present.',
        "options": [
            'Sodium, lithium, copper, potassium',
            'Lithium, sodium, potassium, copper',
            'Calcium, sodium, lithium, copper',
            'Lithium, calcium, sodium, potassium',
        ],
        "correct_index": 1,
        "why": 'Crimson is lithium, yellow is sodium, lilac is potassium and green '
               'is copper, taken in the order given.',
    },
    {
        "id": 'ks4-flame-tests-h13',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the flame colour fades if the loaded loop is held in the flame for a long time.',
        "options": [
            'The metal ion is changed into a different element by the heat',
            'The eye adjusts to the colour and stops being able to see it',
            'The sample on the loop is used up and burns away from the wire',
            'The flame gradually cools and stops exciting the electrons',
        ],
        "correct_index": 2,
        "why": 'Only a small amount of sample sits on the loop, and once it has '
               'volatilised away there is nothing left to emit light.',
    },
    {
        "id": 'ks4-flame-tests-h14',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Evaluate the claim that a flame test proves which compound is present in a sample.',
        "options": [
            'True, because each compound gives its own individual colour',
            'True, provided the wire has been cleaned properly beforehand',
            'False, because the colours are far too faint ever to be used',
            'False, because the test names the metal ion and nothing more',
        ],
        "correct_index": 3,
        "why": 'Every compound of one metal gives the same colour, so the negative '
               'ion remains unidentified and the compound is not yet known.',
    },
    {
        "id": 'ks4-flame-tests-h15',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Every flame test carried out in a laboratory over one week shows a yellow tinge. Suggest a cause and a remedy.',
        "options": [
            'Sodium is contaminating the apparatus, so clean it thoroughly',
            'The Bunsen burners are faulty and must all be replaced',
            'The samples have all expired, so an entirely fresh set must be ordered',
            'The room is too warm, so the laboratory should be cooled',
        ],
        "correct_index": 0,
        "why": 'Sodium colours very strongly at tiny concentrations, so a shared '
               'spatula, unwashed loop or contaminated bench readily gives a yellow '
               'tinge.',
    },
    {
        "id": 'ks4-flame-tests-h16',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A solution contains either calcium ions or copper(II) ions. Determine whether a flame test alone can decide which, and justify.',
        "options": [
            'No, because both of these ions give an orange-red flame colour',
            'Yes, because orange-red and green are easy to tell apart',
            'No, because a flame test cannot be carried out on a solution',
            'Yes, because only copper compounds will dissolve in water',
        ],
        "correct_index": 1,
        "why": 'Calcium gives orange-red and copper gives green, two colours nobody '
               'confuses, so here a flame test on its own is enough.',
    },
    {
        "id": 'ks4-flame-tests-h17',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Predict the flame colour of copper(II) carbonate and justify the prediction.',
        "options": [
            'Crimson, because carbonates all give a crimson flame colour',
            'Yellow, because the carbon in it glows yellow when it is hot',
            'Green, because the copper ion is the source of the colour',
            'No colour, because copper(II) carbonate is already green',
        ],
        "correct_index": 2,
        "why": 'Copper gives green whatever it is combined with, and the green '
               'colour of the solid is unrelated to the colour of the flame.',
    },
    {
        "id": 'ks4-flame-tests-h18',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why energy must be supplied before a metal ion will emit light in a flame.',
        "options": [
            'Energy is needed to melt the sample into a liquid form first',
            'Energy is needed to break all of the ionic bonds inside the compound first',
            'Light can only be emitted by a substance that is already hot',
            'Electrons must be raised to a higher level before they can fall',
        ],
        "correct_index": 3,
        "why": 'Light is emitted as an electron drops back down, so it must first '
               'be excited upwards by energy taken from the flame.',
    },
    {
        "id": 'ks4-flame-tests-h19',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Compare the flame test with the sodium hydroxide test for identifying copper(II) in a solution.',
        "options": [
            'Flame gives green and hydroxide gives a blue solid, so both agree',
            'Both give a green result, so either test can be used alone',
            'Only the flame test works, since hydroxide gives no result',
            'Only the hydroxide test works, since a solution never gives any flame colour',
        ],
        "correct_index": 0,
        "why": 'Two independent tests pointing at the same ion is much stronger '
               'evidence than either result taken on its own.',
    },
    {
        "id": 'ks4-flame-tests-h20',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A student concludes that a compound contains calcium because the flame looked red. Evaluate this conclusion.',
        "options": [
            'Sound, because red is the flame colour of calcium ions',
            'Unsafe, because lithium gives crimson and could look red too',
            'Sound, because no other metal ion gives any shade of red',
            'Unsafe, because a red flame always means no metal is present',
        ],
        "correct_index": 1,
        "why": 'Lithium crimson and calcium orange-red are the pair most often '
               "confused, so 'red' is not precise enough to settle which is "
               'present.',
    },
    {
        "id": 'ks4-flame-tests-h21',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the flame test is described as a subjective method.',
        "options": [
            'It depends on the subject the sample was taken from',
            'It depends on how much of the sample is used each time',
            "It depends on a colour judged by a person's own eye",
            'It depends on the person choosing which ion to test for',
        ],
        "correct_index": 2,
        "why": 'Two observers can name the same flame differently, whereas an '
               'instrument records a wavelength that is the same for everybody.',
    },
    {
        "id": 'ks4-flame-tests-h22',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Suggest why a platinum wire may be preferred to the usual wire in a research laboratory.',
        "options": [
            'Platinum is cheaper than the usual wire for the same length',
            'Platinum melts at a lower temperature and so heats up faster',
            'Platinum gives a colour of its own that marks the starting point clearly',
            'Platinum is even less reactive, so contamination is lower still',
        ],
        "correct_index": 3,
        "why": 'Platinum is extremely unreactive and holds very little residue, so '
               'the blank run is cleaner, which matters when trace amounts are '
               'involved.',
    },
    {
        "id": 'ks4-flame-tests-h23',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A compound gives no flame colour at all. Suggest what this result shows.',
        "options": [
            'Its metal ion may be one that gives no visible colour',
            'The compound contains no atoms of any kind at all',
            'The compound must be an acid rather than a salt',
            'The Bunsen flame must have been on the yellow setting',
        ],
        "correct_index": 0,
        "why": 'Only a few metal ions colour a flame, so a colourless result rules those few out and says nothing about the many that never colour one.',
    },
    {
        "id": 'ks4-flame-tests-h24',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Explain why the flame test is described as a test for the metal ion rather than for the metal element.',
        "options": [
            'Metal elements are far too unreactive to give any colour',
            'The metal in a salt is present as an ion, not as an atom',
            'The ion is heavier, so it emits light more easily than an atom',
            'A metal element would melt the wire before it gave a colour',
        ],
        "correct_index": 1,
        "why": 'In an ionic compound the metal exists as a positive ion, and it is '
               "that ion's electrons that are excited in the flame.",
    },
    {
        "id": 'ks4-flame-tests-h25',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'A firework is designed to burn crimson. Determine which metal compound should be added and justify the choice.',
        "options": [
            'A copper compound, because copper ions emit crimson light',
            'A sodium compound, because sodium ions emit crimson light',
            'A lithium compound, because lithium ions emit crimson light',
            'A potassium compound, because potassium emits crimson light',
        ],
        "correct_index": 2,
        "why": 'Crimson is the characteristic emission of lithium; copper gives '
               'green, sodium yellow and potassium lilac.',
    },
    {
        "id": 'ks4-flame-tests-h26',
        "subtopic_slug": 'flame-tests',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": True,
        "text": 'Two white solids both give an orange-red flame. Determine one further test that would distinguish them.',
        "options": [
            'Repeat the flame test and compare which colour lasts longer',
            'Weigh equal volumes and compare the two densities found',
            'Heat both solids and compare how quickly each one melts',
            'Add dilute acid and see whether either of them fizzes',
        ],
        "correct_index": 3,
        "why": 'Both contain calcium, so the metal ion cannot separate them; '
               'testing the negative ion, such as for a carbonate, can.',
    },
]
