"""Chemistry · Chemical changes — the MRB-338 expansion for `electrolysis-aqueous`.

Water is the whole difficulty, so the leaf opens with what it adds — a supply of
hydrogen and hydroxide ions that competes with the compound's own — and then
works the two discharge rules until they are portable. At the cathode the
reactivity series decides: a metal below hydrogen is deposited, a metal above it
is not and hydrogen comes off instead. At the anode a concentrated halide gives
the halogen and anything else gives oxygen.

Named solutions carry the applied rows — copper sulfate, silver nitrate, brine,
dilute sulfuric acid, potassium nitrate — and the chlor-alkali products close
it. Inert against reactive electrodes appears only where it changes the answer,
because copper purification belongs to the extraction leaf. Gas tests are asked
as observations, never as a list.
"""

TOPIC = "chemical-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ---------------------------------------------------------------- easier
    {
        "id": 'ks4-electrolysis-aqueous-e05',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is meant by an aqueous solution.',
        "options": [
            'A substance that has been melted by strong heating',
            'A solid that has been ground to a very fine powder',
            'A mixture of two liquids that will not mix',
            'A substance dissolved in water',
        ],
        "correct_index": 3,
        "why": 'Aqueous means the solute is dissolved in water, which is what '
               'brings extra ions into the cell.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e06',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the metal deposited at the cathode when copper sulfate '
                'solution is electrolysed.',
        "options": [
            'Sulfur',
            'Hydrogen',
            'Copper',
            'Sodium',
        ],
        "correct_index": 2,
        "why": 'Copper lies below hydrogen in the reactivity series, so copper '
               'ions are discharged in preference to hydrogen ions.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e07',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State the common name for a concentrated solution of sodium '
                'chloride.',
        "options": [
            'Caustic soda',
            'Bleach',
            'Lime water',
            'Brine',
        ],
        "correct_index": 3,
        "why": 'Brine is concentrated sodium chloride solution, and it is the '
               'feedstock of the chlor-alkali industry.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e08',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the gas given off at the anode when concentrated brine is '
                'electrolysed.',
        "options": [
            'Oxygen',
            'Chlorine',
            'Hydrogen',
            'Sodium vapour',
        ],
        "correct_index": 1,
        "why": 'The chloride ions are concentrated enough to be discharged in '
               'preference to the hydroxide ions from the water.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e09',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State which gas is produced at the cathode from a solution of a '
                'reactive metal salt.',
        "options": [
            'Oxygen',
            'Chlorine',
            'Hydrogen',
            'Nitrogen',
        ],
        "correct_index": 2,
        "why": 'A metal above hydrogen stays in solution, so it is the hydrogen '
               'ions from the water that are discharged instead.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e10',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the three useful products of the chlor-alkali process.',
        "options": [
            'Oxygen, hydrogen and sodium chloride',
            'Chlorine, oxygen and sodium hydroxide',
            'Chlorine, hydrogen and sodium metal',
            'Chlorine, hydrogen and sodium hydroxide',
        ],
        "correct_index": 3,
        "why": 'The anode gives chlorine, the cathode gives hydrogen, and the '
               'sodium and hydroxide ions left behind make the alkali.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e11',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State which ion from water is discharged at the anode when no '
                'halide is present.',
        "options": [
            'The hydrogen ion',
            'The hydroxide ion',
            'The sulfate ion',
            'The sodium ion',
        ],
        "correct_index": 1,
        "why": 'Hydroxide ions are negative, so they travel to the anode and are '
               'oxidised there to oxygen.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-e12',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'easier',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify a use of the chlorine made from brine.',
        "options": [
            'Filling weather balloons for the forecast service',
            'Welding steel plates in a shipyard',
            'Sterilising the water in a swimming pool',
            'Fertilising farmland in the spring',
        ],
        "correct_index": 2,
        "why": 'Chlorine kills microorganisms, which is why it is dosed into '
               'drinking water and swimming pools.',
    },
    # -------------------------------------------------------------- standard
    {
        "id": 'ks4-electrolysis-aqueous-s05',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why more than one ion could be discharged at the '
                'cathode of an aqueous cell.',
        "options": [
            'The solution holds two metals at once',
            'Water splits the metal ions in two',
            'The cathode attracts every kind of ion',
            'Water supplies hydrogen ions alongside the metal ions',
        ],
        "correct_index": 3,
        "why": 'The compound and the water both supply positive ions, so there '
               'are two candidates competing to be reduced.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s06',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Potassium nitrate solution is electrolysed. Name the '
                'substance formed at the negative electrode.',
        "options": [
            'Potassium metal',
            'Hydrogen gas',
            'Nitrogen gas',
            'Oxygen gas',
        ],
        "correct_index": 1,
        "why": 'Potassium is far above hydrogen in the reactivity series, so the '
               'hydrogen ions from the water are discharged instead.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s07',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what is seen at the cathode during the electrolysis '
                'of concentrated brine.',
        "options": [
            'A grey metal coating slowly forming',
            'A stream of colourless bubbles',
            'A pale green gas collecting above it',
            'A white solid settling beneath it',
        ],
        "correct_index": 1,
        "why": 'Hydrogen ions are discharged there in preference to sodium, so '
               'the product is a colourless gas rather than a deposit.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s08',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what would be observed at the cathode when silver nitrate '
                'solution is electrolysed.',
        "options": [
            'Colourless bubbles streaming off the surface',
            'A shiny grey coating building up on the electrode',
            'The electrode slowly dissolving into the solution',
            'A white precipitate settling under the electrode',
        ],
        "correct_index": 1,
        "why": 'Silver is below hydrogen, so silver ions are reduced there and a '
               'layer of the metal is deposited.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s09',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why sodium hydroxide is left in the tank after brine '
                'has been electrolysed.',
        "options": [
            'Hydrogen reacts with the sodium chloride still in the tank',
            'Sodium metal reacts with the water as soon as it forms',
            'Chlorine dissolves in the water and makes the alkali',
            'Sodium and hydroxide ions are the two left undischarged',
        ],
        "correct_index": 3,
        "why": 'Hydrogen leaves at the cathode and chlorine at the anode, so the '
               'remaining ions form sodium hydroxide solution.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s10',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why copper is deposited rather than hydrogen from copper '
                'sulfate solution.',
        "options": [
            'There are more copper ions than hydrogen ions',
            'Copper ions carry twice as much charge',
            'Copper ions are much larger and move faster',
            'Copper is less reactive than hydrogen',
        ],
        "correct_index": 3,
        "why": 'The less reactive of the two competing ions is the one '
               'discharged at the cathode.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s11',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Describe what happens to the blue colour of copper sulfate '
                'solution during electrolysis with inert electrodes.',
        "options": [
            'It deepens as more copper ions are made in the liquid',
            'It fades as copper ions are removed from the solution',
            'It turns green as the sulfate ions are discharged',
            'It stays exactly the same throughout the process',
        ],
        "correct_index": 1,
        "why": 'The blue comes from dissolved copper ions, and every one plated '
               'onto the cathode is one fewer left in solution.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s12',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict the two products of electrolysing concentrated '
                'potassium bromide solution.',
        "options": [
            'Potassium at the cathode and bromine at the anode',
            'Hydrogen at the cathode and bromine at the anode',
            'Hydrogen at the cathode and oxygen at the anode',
            'Potassium at the cathode and oxygen at the anode',
        ],
        "correct_index": 1,
        "why": 'Potassium is too reactive to be deposited, and the concentrated '
               'bromide is discharged in preference to hydroxide.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s13',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a little dilute sulfuric acid is added before water '
                'is electrolysed.',
        "options": [
            'The acid raises the temperature of the water',
            'The acid supplies the oxygen that is collected',
            'The acid adds ions so that the current can flow',
            'The acid stops the two gases from recombining',
        ],
        "correct_index": 2,
        "why": 'Pure water holds too few ions to conduct, so an electrolyte is '
               'added to carry the charge.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s14',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Name the gas collected at the anode when dilute sodium sulfate '
                'solution is electrolysed.',
        "options": [
            'Sulfur dioxide',
            'Hydrogen',
            'Oxygen',
            'Nitrogen',
        ],
        "correct_index": 2,
        "why": 'Sulfate ions are not discharged, so the hydroxide ions from the '
               'water are oxidised and oxygen comes off.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s15',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why the hydrogen made in the chlor-alkali process is '
                'worth collecting.',
        "options": [
            'It is used to dissolve the chlorine afterwards',
            'It is used to fill the pipes of the plant',
            'It is used to keep the brine warm in winter',
            'It is used to make ammonia and as a fuel',
        ],
        "correct_index": 3,
        "why": 'Hydrogen is a feedstock for the Haber process and a fuel in its '
               'own right, so it is a saleable product.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s16',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a gas collected over the cathode gives a squeaky '
                'pop with a lit splint.',
        "options": [
            'The gas is chlorine, which reacts with the burning wood',
            'The gas is oxygen, which makes the splint burn faster',
            'The gas is hydrogen, which burns explosively in air',
            'The gas is carbon dioxide, which puts the flame out',
        ],
        "correct_index": 2,
        "why": 'Hydrogen mixed with air burns with a sharp pop, and that is what '
               'identifies it.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s17',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what happens to the pH of the solution around the cathode '
                'during the electrolysis of brine.',
        "options": [
            'It falls, because hydrogen ions are being added',
            'It rises, because hydrogen ions are being removed',
            'It stays at 7, because the solution is a neutral salt',
            'It falls, because chlorine dissolves back into it',
        ],
        "correct_index": 1,
        "why": 'Taking hydrogen ions out leaves hydroxide ions in excess, so the '
               'solution around that electrode turns alkaline.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s18',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify the solution that would give a metal at the cathode '
                'and oxygen at the anode.',
        "options": [
            'Sodium chloride solution',
            'Potassium sulfate solution',
            'Copper nitrate solution',
            'Magnesium sulfate solution',
        ],
        "correct_index": 2,
        "why": 'Copper is below hydrogen so the metal is deposited, and nitrate '
               'ions leave the hydroxide ions to give oxygen.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s19',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why chlorine, not oxygen, comes off the anode in '
                'concentrated brine.',
        "options": [
            'The chloride ions are present in much the higher concentration',
            'The chloride ions are heavier and reach the anode sooner',
            'The hydroxide ions are attracted to the cathode instead',
            'The chloride ions are the only negative ions in the tank',
        ],
        "correct_index": 0,
        "why": 'Where a halide is concentrated it is discharged ahead of the '
               'hydroxide from the water.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s20',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State what is left in the beaker once dilute sulfuric acid has '
                'been electrolysed for a long time.',
        "options": [
            'Pure water, since the acid has been used up',
            'A solution that has become neutral',
            'A solution of sodium hydroxide',
            'A more concentrated sulfuric acid solution',
        ],
        "correct_index": 3,
        "why": 'Water is removed as hydrogen and oxygen while the sulfate stays '
               'behind, so the acid left is stronger than before.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s21',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why damp litmus paper is used to test the gas from the '
                'anode of a brine cell.',
        "options": [
            'It relights when chlorine reaches it',
            'It is turned blue by chlorine',
            'It is bleached white by chlorine',
            'It smells strongly once chlorine touches it',
        ],
        "correct_index": 2,
        "why": 'Chlorine bleaches moist indicator paper, and the test is made at '
               'arms length rather than by smelling the gas.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s22',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why sodium is never obtained from sodium chloride '
                'solution.',
        "options": [
            'Sodium chloride does not dissolve well enough in water',
            'Sodium ions are attracted to the anode in a solution',
            'Sodium ions cannot move through a watery solution',
            'Sodium is above hydrogen, so hydrogen forms instead',
        ],
        "correct_index": 3,
        "why": 'The less reactive of the competing positive ions is discharged, '
               'and hydrogen is far less reactive than sodium.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s23',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why it is the water, and not the salt, that is '
                'decomposed in a dilute sodium sulfate cell.',
        "options": [
            'Sodium sulfate is too dilute to take part in any reaction',
            'Neither the sodium ion nor the sulfate ion is discharged',
            'Water is the only substance present that contains any ions',
            'The salt is decomposed first and the water only afterwards',
        ],
        "correct_index": 1,
        "why": 'Sodium is above hydrogen and sulfate loses to hydroxide, so both '
               'of the discharged ions come from the water.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s24',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'State why a copper electrode is used when copper is to be '
                'plated onto an object.',
        "options": [
            'It attracts the copper ions more strongly than graphite',
            'It conducts electricity better than graphite does',
            'It dissolves and keeps the copper ions topped up',
            'It stops oxygen being released at the same electrode',
        ],
        "correct_index": 2,
        "why": 'A reactive anode replaces the ions being taken out at the '
               'cathode, so the solution does not run down.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s25',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the two gases from dilute sulfuric acid are '
                'collected in separate tubes.',
        "options": [
            'So that the current can pass through both of them',
            'So that they do not react and re-form the acid',
            'So that the volumes are kept exactly equal',
            'So that each can be identified by its own test',
        ],
        "correct_index": 3,
        "why": 'Hydrogen and oxygen are told apart by different splint tests, '
               'which only works if each is kept on its own.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-s26',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'standard',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Identify a use of the sodium hydroxide made from brine.',
        "options": [
            'Sweetening acidic fruit juice',
            'Filling fire extinguishers',
            'Making soap and paper',
            'Preserving fresh meat',
        ],
        "correct_index": 2,
        "why": 'Sodium hydroxide is the alkali used in soap making, paper '
               'manufacture and many cleaning products.',
    },
    # ---------------------------------------------------------------- harder
    {
        "id": 'ks4-electrolysis-aqueous-h05',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the electrolysis of dilute sulfuric acid is really '
                'the decomposition of water.',
        "options": [
            'The acid is neutralised by the hydroxide ions as it works',
            'Sulfuric acid is mostly water, so the two are the same thing',
            'The sulfate ions are turned into water at the anode',
            'Hydrogen and oxygen both come from the water, not the acid',
        ],
        "correct_index": 3,
        "why": 'Neither the hydrogen ion from the acid nor the sulfate survives '
               'as a product; the gases both trace back to water.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h06',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which solution would give the same two gases as dilute '
                'sulfuric acid does.',
        "options": [
            'Concentrated sodium chloride solution',
            'Dilute potassium nitrate solution',
            'Copper sulfate solution',
            'Silver nitrate solution',
        ],
        "correct_index": 1,
        "why": 'Potassium is above hydrogen and nitrate is not discharged, so '
               'hydrogen and oxygen come off just as with the acid.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h07',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A copper sulfate solution is electrolysed with copper '
                'electrodes. Predict what happens to the blue colour.',
        "options": [
            'It fades, because copper is taken out at the cathode',
            'It deepens, because the anode adds copper ions steadily',
            'It stays much the same, because the anode replaces what is lost',
            'It disappears, because the sulfate is discharged as well',
        ],
        "correct_index": 2,
        "why": 'A reactive anode dissolves at the rate the cathode plates, so '
               'the concentration of copper ions is held steady.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h08',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the volume of gas at one electrode is twice that at '
                'the other when water is decomposed.',
        "options": [
            'Oxygen dissolves in the water while hydrogen does not',
            'Hydrogen is lighter, so the same mass fills twice the space',
            'The cathode is twice the size of the anode in the cell',
            'Each water molecule gives two hydrogen atoms and one oxygen',
        ],
        "correct_index": 3,
        "why": 'The two-to-one ratio of atoms in water carries straight through '
               'to the two-to-one ratio of gas volumes.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h09',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare the cathode products of copper chloride solution and '
                'magnesium chloride solution.',
        "options": [
            'Copper from one and magnesium from the other',
            'Hydrogen from both, since water is present in each',
            'Copper from one and hydrogen from the other',
            'Chlorine from both, since both are chlorides',
        ],
        "correct_index": 2,
        "why": 'Copper is below hydrogen so the metal is deposited, while '
               'magnesium is above it so hydrogen comes off instead.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h10',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the chlorine and the sodium hydroxide are kept in '
                'separate compartments of an industrial brine cell.',
        "options": [
            'They would take up too much space in a single vessel',
            'They would freeze if they were allowed to mix in one tank',
            'They would react together and the products would be lost',
            'They would slow the current down if they were mixed',
        ],
        "correct_index": 2,
        "why": 'Chlorine reacts with sodium hydroxide solution, so mixing them '
               'destroys two saleable products at once.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h11',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what would happen to the anode product if the brine '
                'were diluted a great deal with water.',
        "options": [
            'Chlorine would still be the only gas released',
            'Oxygen would begin to replace the chlorine',
            'Hydrogen would be released there instead',
            'Nothing would be released at that electrode',
        ],
        "correct_index": 1,
        "why": 'Once the chloride is dilute it loses its advantage, and the '
               'hydroxide ions from water are discharged instead.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h12',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce what happens to the mass of the solution as hydrogen and '
                'oxygen are collected from it.',
        "options": [
            'It rises, because gases are drawn in from the air',
            'It falls, because water leaves the beaker as gas',
            'It stays the same, because mass cannot be lost',
            'It falls, because the electrodes take material away',
        ],
        "correct_index": 1,
        "why": 'The water decomposed leaves as two gases, so the liquid that '
               'remains weighs less than it did.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h13',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the cathode gains mass in copper sulfate solution '
                'but not in sodium sulfate solution.',
        "options": [
            'Sodium sulfate solution is not able to conduct a current',
            'Copper sulfate is a stronger electrolyte than sodium sulfate',
            'Sodium ions are far too large to reach the electrode surface',
            'Copper ions are discharged as metal; sodium ions are not',
        ],
        "correct_index": 3,
        "why": 'A metal below hydrogen plates out, while a metal above it leaves '
               'hydrogen gas and nothing solid behind.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h14',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that the anode always produces oxygen from a '
                'solution.',
        "options": [
            'Correct, because water is present in every solution',
            'Correct, because hydroxide ions are the fastest to arrive',
            'Wrong, because a concentrated halide gives the halogen',
            'Wrong, because the anode gives hydrogen from a solution',
        ],
        "correct_index": 2,
        "why": 'Concentration can overturn the default, which is why brine gives '
               'chlorine while sodium sulfate gives oxygen.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h15',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Determine the volume of oxygen collected when 30 cm3 of '
                'hydrogen is collected from acidified water.',
        "options": [
            '60 cm3',
            '30 cm3',
            '15 cm3',
            '10 cm3',
        ],
        "correct_index": 2,
        "why": 'The gases come off in a two-to-one ratio, so 30 cm3 of hydrogen '
               'is matched by half that volume of oxygen.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h16',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the oxygen collected from acidified water is often '
                'a little less than half the volume of the hydrogen.',
        "options": [
            'Oxygen is more soluble in water than hydrogen is',
            'Oxygen is heavier, so some of it sinks back down',
            'Oxygen reacts with the graphite anode as it forms',
            'Oxygen escapes past the seal at the top of the tube',
        ],
        "correct_index": 0,
        "why": 'Some of the oxygen dissolves in the solution before it can reach '
               'the collecting tube, so less is measured.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h17',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce which solution would deposit a metal at the cathode and '
                'give a halogen at the anode.',
        "options": [
            'Concentrated copper chloride solution',
            'Concentrated sodium chloride solution',
            'Dilute copper sulfate solution',
            'Dilute sodium sulfate solution',
        ],
        "correct_index": 0,
        "why": 'Copper is below hydrogen so the metal plates out, and the '
               'concentrated chloride is discharged as chlorine.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h18',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why the solution slowly becomes acidic when copper '
                'sulfate is electrolysed with inert electrodes.',
        "options": [
            'The oxygen dissolves in the water and turns it acidic',
            'Sulfuric acid is produced directly at the anode surface',
            'The copper deposited reacts with the water around it',
            'Hydrogen ions are left behind as copper and oxygen leave',
        ],
        "correct_index": 3,
        "why": 'Copper is removed at the cathode and hydroxide at the anode, so '
               'hydrogen ions and sulfate ions are what remain.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h19',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Compare what an inert anode and a copper anode do in copper '
                'sulfate solution.',
        "options": [
            'Both release oxygen, since the electrolyte is the same',
            'Both dissolve, since any anode loses material as it works',
            'The inert one releases oxygen; the copper one dissolves',
            'The inert one dissolves; the copper one releases oxygen',
        ],
        "correct_index": 2,
        "why": 'An inert anode only discharges ions from the solution, while a '
               'reactive one is itself oxidised into the solution.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h20',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why the chlorine from a brine cell is dried before it '
                'is stored in steel cylinders.',
        "options": [
            'Damp chlorine would turn back into brine in the cylinder',
            'Damp chlorine would freeze inside the cylinder in winter',
            'Damp chlorine takes up far more room than dry chlorine',
            'Damp chlorine attacks the steel, but dry chlorine does not',
        ],
        "correct_index": 3,
        "why": 'Water lets chlorine corrode the steel, so the gas is dried to '
               'keep the containers sound.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h21',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Predict what is collected at each electrode when very dilute '
                'copper chloride solution is electrolysed.',
        "options": [
            'Copper at the cathode and chlorine at the anode',
            'Hydrogen at the cathode and oxygen at the anode',
            'Copper at the cathode and oxygen at the anode',
            'Copper at the anode and chlorine at the cathode',
        ],
        "correct_index": 2,
        "why": 'Copper is still below hydrogen so the metal plates out, but a '
               'dilute chloride loses to the hydroxide ions from the water.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h22',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'A student collects no gas at the cathode of a silver nitrate '
                'cell. Explain the observation.',
        "options": [
            'The cell has been connected the wrong way round',
            'Silver is deposited there as a solid, so no gas forms',
            'Nitrogen is formed but dissolves back into the solution',
            'The solution is too dilute for anything to be discharged',
        ],
        "correct_index": 1,
        "why": 'Silver ions are reduced in preference to hydrogen ions, so the '
               'cathode product is a metal rather than a gas.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h23',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Deduce what would be produced at both electrodes if pure molten '
                'sodium chloride were used instead of brine.',
        "options": [
            'Sodium at the cathode and oxygen at the anode',
            'Hydrogen at the cathode and chlorine at the anode',
            'Sodium at the cathode and chlorine at the anode',
            'Hydrogen at the cathode and oxygen at the anode',
        ],
        "correct_index": 2,
        "why": 'With no water present there are no hydrogen or hydroxide ions to '
               'compete, so the compound gives its own two elements.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h24',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Suggest why a brine cell is run on concentrated rather than '
                'dilute solution.',
        "options": [
            'Concentration is what makes chlorine the anode product',
            'Concentration lowers the voltage that the cell requires',
            'Concentration stops the cell from heating up too much',
            'Concentration keeps the sodium hydroxide from dissolving',
        ],
        "correct_index": 0,
        "why": 'Chlorine is the product worth having, and it is only favoured '
               'over oxygen while the chloride stays concentrated.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h25',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Explain why a copper sulfate cell with inert electrodes '
                'eventually starts to give hydrogen at the cathode.',
        "options": [
            'The sulfate ions break down and release hydrogen into the liquid',
            'The cathode becomes coated and can no longer hold more copper',
            'The solution warms up, and hydrogen forms above 40 degrees C',
            'The copper ions run out, leaving hydrogen ions to be discharged',
        ],
        "correct_index": 3,
        "why": 'Preference only decides between ions that are present, so once '
               'the copper is exhausted the water takes over.',
    },
    {
        "id": 'ks4-electrolysis-aqueous-h26',
        "subtopic_slug": 'electrolysis-aqueous',
        "band": 'harder',
        "tier": 'foundation',
        "triple_only": False,
        "text": 'Evaluate the claim that adding water to a cell can change which '
                'products are formed.',
        "options": [
            'Wrong, because water takes no part in the electrolysis',
            'Wrong, because only the voltage decides what is produced',
            'Correct, because water supplies ions that can compete',
            'Correct, because water reacts with the electrodes as well',
        ],
        "correct_index": 2,
        "why": 'Hydrogen and hydroxide ions from the water can be discharged in '
               'place of the compound, which is why a melt and a solution differ.',
    },
]
