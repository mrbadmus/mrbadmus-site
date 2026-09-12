"""Chemistry · Chemical analysis — the MRB-338 expansion for `testing-for-gases`.

Four gases, four tests, and almost all of the demand lies in NOT confusing
them: lit splint against glowing splint, limewater against water, damp litmus
against dry. Rows are written so the observation a pupil has to reason from is
always stated in the stem itself.

The harder band carries the equations behind the tests (hydrogen burning, a
metal with acid, a carbonate with acid, chlorine dissolving) and the
interpretation questions — what a negative result does and does not rule out,
and why one positive test is not yet an identification. Formulae are FLAT, as
KS4 requires.
"""

TOPIC = "analysis"
SUBJECT = "chemistry"

QUESTIONS = [
    {
        "id": 'ks4-testing-for-gases-e06',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is heard in the positive test for hydrogen.',
        "options": [
            'A squeaky pop',
            'A long, low hiss from the burning gas',
            'A sharp crack',
            'A quiet fizzing',
        ],
        "correct_index": 0,
        "why": 'The hydrogen burns rapidly with the oxygen in the air, and that '
               'very fast combustion is heard as a squeaky pop.',
    },
    {
        "id": 'ks4-testing-for-gases-e07',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the solution that is used as limewater.',
        "options": [
            'Sodium hydroxide solution',
            'Calcium hydroxide solution',
            'Calcium carbonate solution',
            'Sodium carbonate solution',
        ],
        "correct_index": 1,
        "why": 'Limewater is a solution of calcium hydroxide, and it is the calcium '
               'in it that forms the insoluble white solid with carbon dioxide.',
    },
    {
        "id": 'ks4-testing-for-gases-e08',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why damp rather than dry litmus paper is used when testing for chlorine.',
        "options": [
            'The water makes the paper stick inside the test tube',
            'Damp paper is easier to see a colour change on',
            'Chlorine needs water to form the bleaching agent',
            'The water stops the litmus paper catching fire',
        ],
        "correct_index": 2,
        "why": 'Chlorine reacts with water to make hypochlorous acid, and that is '
               'what bleaches the dye; on dry paper no such reaction can happen.',
    },
    {
        "id": 'ks4-testing-for-gases-e09',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the formula of the gas that is tested for using limewater.',
        "options": [
            'H2',
            'Cl2',
            'O2',
            'CO2',
        ],
        "correct_index": 3,
        "why": 'Carbon dioxide, CO2, forms insoluble calcium carbonate with '
               'limewater and turns it milky.',
    },
    {
        "id": 'ks4-testing-for-gases-e10',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why carbon dioxide is used in some fire extinguishers.',
        "options": [
            'It does not support combustion, so a flame goes out',
            'It reacts chemically with the fuel and neutralises it completely',
            'It is lighter than air and lifts the flame away',
            'It dissolves the smoke that the fire produces',
        ],
        "correct_index": 0,
        "why": 'Carbon dioxide will not burn and will not let anything else burn in '
               'it, so it smothers a flame.',
    },
    {
        "id": 'ks4-testing-for-gases-e11',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the process in the body that produces the carbon dioxide a person breathes out.',
        "options": [
            'Photosynthesis',
            'Respiration',
            'Digestion',
            'Combustion',
        ],
        "correct_index": 1,
        "why": 'Respiration in cells releases energy from glucose and produces '
               'carbon dioxide as a waste product.',
    },
    {
        "id": 'ks4-testing-for-gases-e12',
        "subtopic_slug": 'testing-for-gases',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why chlorine gas is handled inside a fume cupboard.',
        "options": [
            'Chlorine is so cold that it would burn the skin',
            'Chlorine explodes if it is exposed to daylight',
            'Chlorine is toxic and must not be breathed in',
            'Chlorine dissolves the glass of an open gas jar',
        ],
        "correct_index": 2,
        "why": 'Chlorine is a toxic gas that damages the lungs, so it is kept '
               'behind the sash and extracted away.',
    },
    {
        "id": 'ks4-testing-for-gases-s08',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain what causes the sound heard when a lit splint is put into a tube of hydrogen.',
        "options": [
            'The hydrogen expands quickly and pushes the air out of the tube',
            'The hydrogen cools the flame and the splint cracks as it does',
            'The hydrogen dissolves in the wood and makes the splint vibrate',
            'The hydrogen burns very rapidly with the oxygen in the air',
        ],
        "correct_index": 3,
        "why": 'Hydrogen and oxygen react explosively to form water, and the sudden '
               'combustion of a small volume is heard as the pop.',
    },
    {
        "id": 'ks4-testing-for-gases-s09',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the word equation for the reaction that makes limewater turn milky.',
        "options": [
            'carbon dioxide + calcium hydroxide to calcium carbonate + water',
            'carbon dioxide + calcium carbonate to calcium hydroxide + water',
            'carbon dioxide + sodium hydroxide to sodium carbonate + water',
            'carbon monoxide + calcium hydroxide solution to calcium carbonate + water',
        ],
        "correct_index": 0,
        "why": 'The calcium carbonate formed is insoluble, so it appears as the '
               'fine white solid that makes the limewater look milky.',
    },
    {
        "id": 'ks4-testing-for-gases-s10',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student breathes out through a tube into limewater. Predict what happens and explain why.',
        "options": [
            'It stays clear, because breath contains mostly nitrogen gas',
            'It turns milky, because exhaled breath contains carbon dioxide',
            'It turns blue, because breath is slightly alkaline when exhaled',
            'It bubbles and boils, because exhaled breath is warmer than air',
        ],
        "correct_index": 1,
        "why": 'Respiration produces carbon dioxide, and enough of it is exhaled to '
               'form the white calcium carbonate precipitate.',
    },
    {
        "id": 'ks4-testing-for-gases-s11',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Chlorine gas is passed over damp universal indicator paper. Describe the two changes that are seen.',
        "options": [
            'It turns blue and then fades slowly back to its first colour',
            'It turns white and is then stained red by the gas',
            'It turns red and is then bleached white',
            'It turns green and then stays green for the rest of the test',
        ],
        "correct_index": 2,
        "why": 'Chlorine dissolves to form acids, which turn the indicator red, and '
               'the hypochlorous acid then destroys the dye and leaves the paper '
               'white.',
    },
    {
        "id": 'ks4-testing-for-gases-s12',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A colourless gas relights a glowing splint. Identify the gas and name one place it is used.',
        "options": [
            'Hydrogen, used to fill weather balloons in the atmosphere',
            'Chlorine, used to kill bacteria in swimming pool water',
            'Carbon dioxide, used in extinguishers to smother a fire',
            'Oxygen, used in hospitals to help patients to breathe',
        ],
        "correct_index": 3,
        "why": 'Only oxygen relights a glowing splint, because it supports '
               'combustion.',
    },
    {
        "id": 'ks4-testing-for-gases-s13',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a gas test is carried out on gas collected in a tube rather than in the open laboratory.',
        "options": [
            'In the open the gas mixes with air and the result is lost',
            'Collected gas is much colder, so the reaction is far easier to see happen',
            'Collected gas has been purified by the tube it travelled along',
            'In the open the gas would react with the glass of the apparatus',
        ],
        "correct_index": 0,
        "why": 'A test needs a reasonable concentration of the gas, and in the open '
               'the gas is diluted by air until no change can be seen.',
    },
    {
        "id": 'ks4-testing-for-gases-s14',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe a single test that would distinguish a tube of hydrogen from a tube of oxygen.',
        "options": [
            'Bubble each through limewater and see which one turns milky',
            'Hold a glowing splint in each and see which one relights it',
            'Hold damp litmus in each and see which one bleaches it white',
            'Weigh each tube and see which of the two is the heavier one',
        ],
        "correct_index": 1,
        "why": 'Oxygen relights a glowing splint while hydrogen does not, so one '
               'glowing splint separates the two gases.',
    },
    {
        "id": 'ks4-testing-for-gases-s15',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how a student could show that the gas in a cylinder labelled nitrogen is not oxygen.',
        "options": [
            'Bubble it through limewater and see if it clears',
            'Hold damp litmus in it and see if it is bleached',
            'Hold a glowing splint in it and check that it does not relight',
            'Hold a lit splint in it and listen for a pop',
        ],
        "correct_index": 2,
        "why": 'The glowing splint is the test for oxygen, so a splint that stays '
               'glowing and does not relight shows the gas is not oxygen.',
    },
    {
        "id": 'ks4-testing-for-gases-s16',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the balanced symbol equation for hydrogen burning in oxygen.',
        "options": [
            'H2 + O2 to H2O',
            'H2 + 2O2 to 2H2O',
            '2H2 + 2O2 to 2H2O2',
            '2H2 + O2 to 2H2O',
        ],
        "correct_index": 3,
        "why": 'Four hydrogen atoms and two oxygen atoms appear on each side, so '
               '2H2 + O2 to 2H2O is the balanced equation.',
    },
    {
        "id": 'ks4-testing-for-gases-s17',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the gas must be bubbled through limewater rather than held in a tube above it.',
        "options": [
            'The gas must mix with the solution for the reaction to happen',
            'The gas is denser than the limewater and would sink straight out of it',
            'Bubbling warms the limewater and makes the solid form faster',
            'Bubbling stops air reaching the limewater and spoiling the test',
        ],
        "correct_index": 0,
        "why": 'Carbon dioxide has to dissolve and react with the calcium '
               'hydroxide, and bubbling is what brings the gas into contact with '
               'the solution.',
    },
    {
        "id": 'ks4-testing-for-gases-s18',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Carbon dioxide is bubbled through limewater for a long time and the milkiness disappears. Name the substance now in the solution.',
        "options": [
            'Calcium oxide',
            'Calcium hydrogencarbonate',
            'Calcium hydroxide',
            'Calcium chloride',
        ],
        "correct_index": 1,
        "why": 'Excess carbon dioxide converts the insoluble calcium carbonate into '
               'soluble calcium hydrogencarbonate, so the solution clears again.',
    },
    {
        "id": 'ks4-testing-for-gases-s19',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A gas relights a glowing splint. Explain why this does not prove the sample is pure oxygen.',
        "options": [
            'Other gases such as nitrogen will also relight a glowing splint quickly',
            'A glowing splint relights in any gas if it is hot enough',
            'A mixture rich in oxygen would give the same result',
            'The splint relights on its own once it has been taken out',
        ],
        "correct_index": 2,
        "why": 'The test shows that oxygen is present in enough quantity to support '
               'combustion, not that nothing else is in the tube.',
    },
    {
        "id": 'ks4-testing-for-gases-s20',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why chlorine acts as a bleaching agent only once it has dissolved in water.',
        "options": [
            'Water makes the chlorine molecules very much more concentrated',
            'Water carries the chlorine deeper into the fibres of the paper',
            'Dissolving turns chlorine into chloride ions, which are bleaches',
            'Dissolving forms hypochlorous acid, which destroys the dye',
        ],
        "correct_index": 3,
        "why": 'Chlorine reacts with water to give hydrochloric acid and '
               'hypochlorous acid, and it is the hypochlorous acid that breaks down '
               'the coloured dye.',
    },
    {
        "id": 'ks4-testing-for-gases-s21',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the word equation for the reaction between zinc and dilute hydrochloric acid.',
        "options": [
            'zinc + hydrochloric acid to zinc chloride + hydrogen',
            'zinc + hydrochloric acid to zinc oxide + hydrogen',
            'zinc + hydrochloric acid to zinc chloride + chlorine',
            'zinc + dilute hydrochloric acid to zinc hydroxide + chlorine',
        ],
        "correct_index": 0,
        "why": 'A metal with an acid always gives a salt and hydrogen, and the salt '
               'of hydrochloric acid is a chloride.',
    },
    {
        "id": 'ks4-testing-for-gases-s22',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe how a delivery tube is used to carry a gas from a reaction flask into limewater.',
        "options": [
            'It is held just above the limewater so the gas can settle on it',
            'It is sealed into the flask and its end sits under the limewater',
            'It is filled with limewater first so the gas can react inside it',
            'It is left open at the flask end so that air can push the gas along',
        ],
        "correct_index": 1,
        "why": 'A gas-tight seal at the flask and an outlet below the surface make '
               'every bubble of gas pass through the solution.',
    },
    {
        "id": 'ks4-testing-for-gases-s23',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student collects gases over water. Suggest why this method is unsuitable for collecting chlorine.',
        "options": [
            'Chlorine is lighter than air and escapes from the top of the trough',
            'Chlorine freezes on contact with cold water in the trough',
            'Chlorine dissolves in the water, so little of it is collected',
            'Chlorine reacts with the glass of the gas jar being used',
        ],
        "correct_index": 2,
        "why": 'Chlorine is appreciably soluble in water, so most of it dissolves '
               'before it can reach the collecting jar.',
    },
    {
        "id": 'ks4-testing-for-gases-s24',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the pop test for hydrogen is done on a small test tube of gas rather than on a large flask.',
        "options": [
            'A small tube lets the hydrogen escape before it can ignite',
            'A large volume of hydrogen cannot be lit by a splint at all',
            'A small tube makes the pop quieter and so easier to hear',
            'A large volume would burn violently and could be dangerous',
        ],
        "correct_index": 3,
        "why": 'Hydrogen and air burn explosively, so the volume tested is kept to '
               'a few cubic centimetres to keep the energy released small.',
    },
    {
        "id": 'ks4-testing-for-gases-s25',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what a student would see if a glowing splint were lowered into a tube of carbon dioxide.',
        "options": [
            'The splint goes out, because the gas does not support burning',
            'The splint relights and burns brightly in the gas',
            'The splint pops loudly and then goes out immediately',
            'The splint turns white, because the gas bleaches the wood',
        ],
        "correct_index": 0,
        "why": 'Carbon dioxide does not support combustion, so the glowing ember is '
               'extinguished rather than relit.',
    },
    {
        "id": 'ks4-testing-for-gases-s26',
        "subtopic_slug": 'testing-for-gases',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why limewater left standing in an open beaker slowly goes cloudy.',
        "options": [
            'Water evaporates and leaves solid calcium hydroxide behind',
            'Carbon dioxide in the air reacts with it to form a white solid',
            'Dust settles into the beaker and makes the solution look cloudy',
            'Oxygen in the air oxidises the calcium and turns it into a solid',
        ],
        "correct_index": 1,
        "why": 'Air contains carbon dioxide, and given enough time it forms the '
               'same insoluble calcium carbonate that the test relies on.',
    },
    {
        "id": 'ks4-testing-for-gases-h08',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the balanced symbol equation for zinc reacting with dilute hydrochloric acid.',
        "options": [
            'Zn + HCl to ZnCl + H',
            'Zn + 2HCl to ZnCl2 + 2H2',
            'Zn + 2HCl to ZnCl2 + H2',
            '2Zn + 2HCl to 2ZnCl + H2',
        ],
        "correct_index": 2,
        "why": 'One zinc, two hydrogen and two chlorine atoms appear on each side, '
               'and hydrogen is released as the molecule H2.',
    },
    {
        "id": 'ks4-testing-for-gases-h09',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Marble chips fizz vigorously in dilute hydrochloric acid. Determine the balanced symbol equation for that reaction.',
        "options": [
            'CaCO3 + HCl to CaCl + H2O + CO2',
            'CaCO3 + 2HCl to CaCl2 + H2 + CO2',
            'CaCO3 + 2HCl to CaCl2 + H2O + CO',
            'CaCO3 + 2HCl to CaCl2 + H2O + CO2',
        ],
        "correct_index": 3,
        "why": 'Two chlorides are needed for the calcium ion, and the carbonate '
               'becomes water and carbon dioxide.',
    },
    {
        "id": 'ks4-testing-for-gases-h10',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A colourless gas gives no pop with a lit splint, does not relight a glowing splint, does not bleach damp litmus and leaves limewater clear. Deduce a possible identity.',
        "options": [
            'Nitrogen, since it fails all four of the tests carried out',
            'Hydrogen, since the splint was not close enough to ignite it',
            'Oxygen, since a glowing splint does not always relight in it',
            'Chlorine, since damp litmus only bleaches when it is left for longer',
        ],
        "correct_index": 0,
        "why": 'Four negative results rule out the four gases those tests detect, '
               'and nitrogen is the common unreactive gas that gives none of them.',
    },
    {
        "id": 'ks4-testing-for-gases-h11',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why limewater staying clear shows that a gas is not carbon dioxide but does not show that the gas is not acidic.',
        "options": [
            'Limewater only works on gases that are denser than the air is',
            'Limewater detects one particular gas and not acidity in general',
            'Limewater reacts with every acidic gas, so acidity is ruled out',
            'Limewater must be warmed before any acidic gas will react in it',
        ],
        "correct_index": 1,
        "why": 'The white solid formed is calcium carbonate, so the test responds '
               'to carbon dioxide specifically rather than to acidity as a '
               'property.',
    },
    {
        "id": 'ks4-testing-for-gases-h12',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Damp blue litmus paper held in a gas turns red and is then bleached white. Deduce the gas and explain both changes.',
        "options": [
            'Carbon dioxide, which is acidic and then removes the colour',
            'Hydrogen, which is acidic and burns the paper white as it goes',
            'Chlorine, which forms acids in water and then bleaches the dye',
            'Oxygen, which oxidises the litmus first to red and then to white',
        ],
        "correct_index": 2,
        "why": 'Chlorine dissolves in the water on the paper to give hydrochloric '
               'and hypochlorous acids; the acid turns litmus red and the second '
               'bleaches it.',
    },
    {
        "id": 'ks4-testing-for-gases-h13',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the lit splint test for hydrogen is carried out well away from any large supply of the gas.',
        "options": [
            'A large supply would draw all of the oxygen out of the small test tube',
            'A large supply would make the pop too quiet to be heard at all',
            'Hydrogen from a cylinder is too cold to pop when it is lit',
            'A flame could ignite the larger volume and cause an explosion',
        ],
        "correct_index": 3,
        "why": 'Hydrogen forms an explosive mixture with air over a wide range of '
               'proportions, so a source of ignition is kept away from any bulk '
               'supply.',
    },
    {
        "id": 'ks4-testing-for-gases-h14',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Two unlabelled cylinders contain oxygen and carbon dioxide. Determine one test that identifies both cylinders.',
        "options": [
            'A glowing splint, which relights in one and goes out in the other',
            'Damp litmus paper, which bleaches in one and stays blue in the other',
            'A lit splint, which pops in one and burns brighter in the other',
            'Weighing, since the denser gas must be the oxygen one',
        ],
        "correct_index": 0,
        "why": 'Oxygen relights the splint and carbon dioxide extinguishes it, so a '
               'single glowing splint gives a different, definite result for each '
               'cylinder.',
    },
    {
        "id": 'ks4-testing-for-gases-h15',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A lit splint burns more brightly in oxygen. Explain why a glowing splint is used as the test instead.',
        "options": [
            'A lit splint would use up all of the oxygen before it was seen',
            'Relighting is a clear yes or no, while brighter burning is a judgement',
            'A lit splint reacts with oxygen and forms carbon dioxide instead',
            'A glowing splint is hotter, so it gives a much faster reaction',
        ],
        "correct_index": 1,
        "why": 'A test needs an unambiguous positive result, and a glowing ember '
               'bursting back into flame is far less open to interpretation than '
               "'brighter'.",
    },
    {
        "id": 'ks4-testing-for-gases-h16',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A reaction produces 0.10 mol of carbon dioxide. One mole of any gas occupies 24 dm3 at room temperature and pressure. Calculate the volume produced.',
        "options": [
            '240 dm3',
            '0.24 dm3',
            '2.4 dm3',
            '24 dm3',
        ],
        "correct_index": 2,
        "why": '0.10 × 24 = 2.4 dm3 of carbon dioxide.',
    },
    {
        "id": 'ks4-testing-for-gases-h17',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why chlorine turns damp universal indicator red before the paper is bleached.',
        "options": [
            'The gas is itself an acid before any water is involved at all',
            'The indicator is red until the gas warms it enough to bleach',
            'Chlorine is red, and its colour transfers before it fades away',
            'Acids form first in the water, and bleaching then follows',
        ],
        "correct_index": 3,
        "why": 'Chlorine reacting with water gives two acids immediately, which the '
               'indicator shows as red; the slower bleaching then destroys the dye.',
    },
    {
        "id": 'ks4-testing-for-gases-h18',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A gas turns limewater milky. Explain why a careful chemist might still run a second test before reporting carbon dioxide.',
        "options": [
            'Other acidic gases can also form a white solid with limewater',
            'Limewater goes milky with time whether or not a gas is present',
            'Limewater only goes milky if the gas is at the right pressure',
            'A milky result always fades, so the first reading is unreliable',
        ],
        "correct_index": 0,
        "why": 'Sulfur dioxide also gives a white precipitate with limewater, so '
               'the milkiness alone is strong but not conclusive evidence.',
    },
    {
        "id": 'ks4-testing-for-gases-h19',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Equal volumes of two gases are mixed in a tube and a lit splint is applied. A loud pop is heard and droplets of liquid form. Deduce which gases were mixed.',
        "options": [
            'Carbon dioxide and nitrogen, which condense into a liquid',
            'Hydrogen and oxygen, which react together to form water',
            'Chlorine and nitrogen, which pop and leave a liquid behind',
            'Oxygen and nitrogen, which are the two main gases of the air',
        ],
        "correct_index": 1,
        "why": 'The pop is the combustion of hydrogen, and the liquid formed is '
               'water, which is the product of hydrogen burning in oxygen.',
    },
    {
        "id": 'ks4-testing-for-gases-h20',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student writes that limewater turns milky because bubbles of gas are trapped in it. Identify the error and give the correct explanation.',
        "options": [
            'Wrong: the gas dissolves and then evaporates out again slowly',
            'Right: trapped bubbles are exactly what makes the solution look milky',
            'Wrong: an insoluble white solid is formed by a reaction',
            'Wrong: the limewater boils and the steam makes it look cloudy',
        ],
        "correct_index": 2,
        "why": 'The cloudiness is solid calcium carbonate suspended in the '
               'solution, not bubbles; bubbles rise and clear, while the '
               'precipitate does not.',
    },
    {
        "id": 'ks4-testing-for-gases-h21',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the tests for hydrogen and for oxygen, stating what is the same and what differs.',
        "options": [
            'Both use limewater, but the colour change is a different one',
            'Both use a glowing splint, but one relights and one goes out',
            'Both use damp litmus, but one bleaches and the other turns red',
            'Both use a splint, but one must be lit and the other glowing',
        ],
        "correct_index": 3,
        "why": 'A splint is the apparatus in both, but hydrogen needs a flame to '
               'ignite it and oxygen is shown by an ember bursting back into flame.',
    },
    {
        "id": 'ks4-testing-for-gases-h22',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'The equation Cl2 + H2O to HCl + HClO describes chlorine dissolving. Use it to explain why only damp paper is bleached.',
        "options": [
            'Without water no HClO is made, and HClO is the bleaching agent',
            'Without water the chlorine cannot reach the dye inside the paper',
            'Without water the HCl formed would burn the paper instead',
            'Without water the chlorine stays as ions and cannot react at all',
        ],
        "correct_index": 0,
        "why": 'The equation shows water is a reactant, so on dry paper the '
               'reaction that produces the bleaching hypochlorous acid cannot '
               'happen.',
    },
    {
        "id": 'ks4-testing-for-gases-h23',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Calcium carbonate decomposes on heating to calcium oxide and carbon dioxide. Calculate the mass of carbon dioxide lost when 10.0 g decomposes completely. Mr of CaCO3 = 100, Mr of CO2 = 44.',
        "options": [
            '10.0 g',
            '4.4 g',
            '5.6 g',
            '44 g',
        ],
        "correct_index": 1,
        "why": '10.0 ÷ 100 = 0.100 mol of calcium carbonate gives 0.100 mol of '
               'carbon dioxide, and 0.100 × 44 = 4.4 g.',
    },
    {
        "id": 'ks4-testing-for-gases-h24',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A sample is thought to be a mixture of oxygen and carbon dioxide. Suggest how two tests together could support that.',
        "options": [
            'Limewater stays clear and a glowing splint fails to relight',
            'Damp litmus bleaches and a lit splint gives a squeaky pop',
            'Limewater turns milky and a glowing splint still relights',
            'Limewater turns milky and a lit splint gives a squeaky pop',
        ],
        "correct_index": 2,
        "why": 'Each test is positive for one component, so both positives together '
               'point to both gases being present in the same sample.',
    },
    {
        "id": 'ks4-testing-for-gases-h25',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Damp blue litmus held in carbon dioxide turns red but is not bleached. Explain why this does not mean the gas is chlorine.',
        "options": [
            'Red is the wrong shade, so the change should not be recorded',
            'Litmus turns red in every gas, so the result means nothing here',
            'Chlorine turns litmus blue first, so red rules chlorine out',
            'Carbon dioxide is acidic in water, and only chlorine bleaches',
        ],
        "correct_index": 3,
        "why": 'Carbon dioxide dissolves to form a weak acid, which reddens litmus; '
               'the bleaching to white is what identifies chlorine.',
    },
    {
        "id": 'ks4-testing-for-gases-h26',
        "subtopic_slug": 'testing-for-gases',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the statement: a gas that turns limewater milky must have come from a carbonate.',
        "options": [
            'False, because respiration and combustion also give that gas',
            'True, because only a carbonate can ever release carbon dioxide',
            'True, because limewater responds to carbonate ions directly',
            'False, because limewater goes milky with any gas at all',
        ],
        "correct_index": 0,
        "why": 'The test identifies carbon dioxide, and carbon dioxide is produced '
               'by burning fuels and by respiration as well as by carbonates and '
               'acid.',
    },
]
