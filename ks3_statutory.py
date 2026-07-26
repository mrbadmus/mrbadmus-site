"""KS3 statutory register — source data and renderer.

SINGLE SOURCE OF TRUTH for KS3 statutory statement IDs.

Produces ``docs/ks3/statutory-register.md`` (Phase 0 of docs/ks3/architecture.md §10.1).

Why this is a module and not hand-written markdown
--------------------------------------------------
Originally, because architecture.md §11 decision 6 (the ``KS3.C.PNM.02`` ID
scheme) was unblessed and IDs had to be mechanically reissuable.

**Mide blessed the scheme on 2026-07-26** and decision 6 is closed, so the 155
IDs this module mints are now **permanent** (§4.4 rule 1: an ID never changes
meaning; a superseded ID is never reused). The single-mint-point design stays —
it is what makes the register regenerable and diffable against the source — but
**editing ``STRAND_CODES`` or the ordinal rule is now a breaking change, not a
routine re-run.** Do not renumber existing statements. If the statutory document
is revised, append new IDs and mark superseded ones; never reuse.

    python3 ks3_statutory.py

Fidelity
--------
``STRANDS`` was extracted programmatically from the HTML of the statutory
document — the bullet text was **copied, never retyped**. ``TRANSCRIPTION_SHA256``
fingerprints the concatenated bullet corpus so drift is detectable.

**Independently re-verified 2026-07-26** by a second extraction from the live
published HTML, diffed bullet-by-bullet against ``STRANDS``: 155/155 matched,
153 byte-identical, and the 2 remainders differ only where the published page
contains a double space (``KS3.C.EA.05``, ``KS3.P.ECT.01``). Per-discipline
counts (B 39 / C 36 / P 62 / WS 18) and the heading structure also matched.

Source: *National curriculum in England: science programmes of study*, DfE, 2014
(still in force), Key stage 3 section.
https://www.gov.uk/government/publications/national-curriculum-in-england-science-programmes-of-study/national-curriculum-in-england-science-programmes-of-study

ID scheme (architecture.md §4.4): ``KS3.<D>.<STRAND>.<nn>``

``<STRAND>`` is the code for **the heading that directly owns the bullets**, and
``<nn>`` is the bullet's ordinal within that heading as printed. That reading is
forced by §4.4's own wording ("the bullet's ordinal within that strand as
printed"), and it is the reading under which all three of §4.4's worked examples
(``PNM``, ``CELLS``, ``FORCES``) resolve. Where the document nests a heading
inside a broader area (Biology, Physics), the area is kept as ``area`` — it is
the unit's ``statutory_area`` per §4.1, not part of the ID.

Working Scientifically carries ``KS3.WS.<STRAND>.<nn>``. ⊕ This is an extension:
§4.4 defines ``<D>`` as ``B|C|P`` only, but §4.4 also says *every* statutory
bullet gets an ID and §5.7.4 requires WS coverage to be auditable the same way.
WS statements are **exempt from the exactly-once ownership rule** — §5.7 taps
them through ``ws: []`` strand tags on many lessons, by design.
"""
STRANDS = [{'discipline': 'WS',
  'area': 'Scientific attitudes',
  'strand': 'Scientific attitudes',
  'code': 'ATT',
  'bullets': ['pay attention to objectivity and concern for accuracy, precision, repeatability and '
              'reproducibility',
              'understand that scientific methods and theories develop as earlier explanations are '
              'modified to take account of new evidence and ideas, together with the importance of '
              'publishing results and peer review',
              'evaluate risks']},
 {'discipline': 'WS',
  'area': 'Experimental skills and investigations',
  'strand': 'Experimental skills and investigations',
  'code': 'EXP',
  'bullets': ['ask questions and develop a line of enquiry based on observations of the real '
              'world, alongside prior knowledge and experience',
              'make predictions using scientific knowledge and understanding',
              'select, plan and carry out the most appropriate types of scientific enquiries to '
              'test predictions, including identifying independent, dependent and control '
              'variables',
              'use appropriate techniques, apparatus, and materials during fieldwork and '
              'laboratory work, paying attention to health and safety',
              'make and record observations and measurements using a range of methods for '
              'different investigations; and evaluate the reliability of methods and suggest '
              'possible improvements',
              'apply sampling techniques']},
 {'discipline': 'WS',
  'area': 'Analysis and evaluation',
  'strand': 'Analysis and evaluation',
  'code': 'ANA',
  'bullets': ['apply mathematical concepts and calculate results',
              'present observations and data using appropriate methods, including tables and '
              'graphs',
              'interpret observations and data, including identifying patterns and using '
              'observations, measurements and data to draw conclusions',
              'present reasoned explanations, including explaining data in relation to predictions '
              'and hypotheses',
              'evaluate data, showing awareness of potential sources of random and systematic '
              'error',
              'identify further questions arising from their results']},
 {'discipline': 'WS',
  'area': 'Measurement',
  'strand': 'Measurement',
  'code': 'MEA',
  'bullets': ['understand and use SI units and IUPAC (International Union of Pure and Applied '
              'Chemistry) chemical nomenclature',
              'use and derive simple equations and carry out appropriate calculations',
              'undertake basic data analysis including simple statistical techniques']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'Cells and organisation',
  'code': 'CELLS',
  'bullets': ['cells as the fundamental unit of living organisms, including how to observe, '
              'interpret and record cell structure using a light microscope',
              'the functions of the cell wall, cell membrane, cytoplasm, nucleus, vacuole, '
              'mitochondria and chloroplasts',
              'the similarities and differences between plant and animal cells',
              'the role of diffusion in the movement of materials in and between cells',
              'the structural adaptations of some unicellular organisms',
              'the hierarchical organisation of multicellular organisms: from cells to tissues to '
              'organs to systems to organisms']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'The skeletal and muscular systems',
  'code': 'SKEL',
  'bullets': ['the structure and functions of the human skeleton, to include support, protection, '
              'movement and making blood cells',
              'biomechanics – the interaction between skeleton and muscles, including the '
              'measurement of force exerted by different muscles',
              'the function of muscles and examples of antagonistic muscles']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'Nutrition and digestion',
  'code': 'NUT',
  'bullets': ['the content of a healthy human diet: carbohydrates, lipids (fats and oils), '
              'proteins, vitamins, minerals, dietary fibre and water, and why each is needed',
              'calculations of energy requirements in a healthy daily diet',
              'the consequences of imbalances in the diet, including obesity, starvation and '
              'deficiency diseases',
              'the tissues and organs of the human digestive system, including adaptations to '
              'function and how the digestive system digests food (enzymes simply as biological '
              'catalysts)',
              'the importance of bacteria in the human digestive system',
              'plants making carbohydrates in their leaves by photosynthesis and gaining mineral '
              'nutrients and water from the soil via their roots']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'Gas exchange systems',
  'code': 'GAS',
  'bullets': ['the structure and functions of the gas exchange system in humans, including '
              'adaptations to function',
              'the mechanism of breathing to move air in and out of the lungs, using a pressure '
              'model to explain the movement of gases, including simple measurements of lung '
              'volume',
              'the impact of exercise, asthma and smoking on the human gas exchange system',
              'the role of leaf stomata in gas exchange in plants']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'Reproduction',
  'code': 'REP',
  'bullets': ['reproduction in humans (as an example of a mammal), including the structure and '
              'function of the male and female reproductive systems, menstrual cycle (without '
              'details of hormones), gametes, fertilisation, gestation and birth, to include the '
              'effect of maternal lifestyle on the foetus through the placenta',
              'reproduction in plants, including flower structure, wind and insect pollination, '
              'fertilisation, seed and fruit formation and dispersal, including quantitative '
              'investigation of some dispersal mechanisms']},
 {'discipline': 'B',
  'area': 'Structure and function of living organisms',
  'strand': 'Health',
  'code': 'HLTH',
  'bullets': ['the effects of recreational drugs (including substance misuse) on behaviour, health '
              'and life processes']},
 {'discipline': 'B',
  'area': 'Material cycles and energy',
  'strand': 'Photosynthesis',
  'code': 'PHOT',
  'bullets': ['the reactants in, and products of, photosynthesis, and a word summary for '
              'photosynthesis',
              'the dependence of almost all life on Earth on the ability of photosynthetic '
              'organisms, such as plants and algae, to use sunlight in photosynthesis to build '
              'organic molecules that are an essential energy store and to maintain levels of '
              'oxygen and carbon dioxide in the atmosphere',
              'the adaptations of leaves for photosynthesis']},
 {'discipline': 'B',
  'area': 'Material cycles and energy',
  'strand': 'Cellular respiration',
  'code': 'RESP',
  'bullets': ['aerobic and anaerobic respiration in living organisms, including the breakdown of '
              'organic molecules to enable all the other chemical processes necessary for life',
              'a word summary for aerobic respiration',
              'the process of anaerobic respiration in humans and micro-organisms, including '
              'fermentation, and a word summary for anaerobic respiration',
              'the differences between aerobic and anaerobic respiration in terms of the '
              'reactants, the products formed and the implications for the organism']},
 {'discipline': 'B',
  'area': 'Interactions and interdependencies',
  'strand': 'Relationships in an ecosystem',
  'code': 'ECO',
  'bullets': ['the interdependence of organisms in an ecosystem, including food webs and insect '
              'pollinated crops',
              'the importance of plant reproduction through insect pollination in human food '
              'security',
              'how organisms affect, and are affected by, their environment, including the '
              'accumulation of toxic materials']},
 {'discipline': 'B',
  'area': 'Genetics and evolution',
  'strand': 'Inheritance, chromosomes, DNA and genes',
  'code': 'INH',
  'bullets': ['heredity as the process by which genetic information is transmitted from one '
              'generation to the next',
              'a simple model of chromosomes, genes and DNA in heredity, including the part played '
              'by Watson, Crick, Wilkins and Franklin in the development of the DNA model',
              'differences between species',
              'the variation between individuals within a species being continuous or '
              'discontinuous, to include measurement and graphical representation of variation',
              'the variation between species and between individuals of the same species meaning '
              'some organisms compete more successfully, which can drive natural selection',
              'changes in the environment which may leave individuals within a species, and some '
              'entire species, less well adapted to compete successfully and reproduce, which in '
              'turn may lead to extinction',
              'the importance of maintaining biodiversity and the use of gene banks to preserve '
              'hereditary material']},
 {'discipline': 'C',
  'area': 'The particulate nature of matter',
  'strand': 'The particulate nature of matter',
  'code': 'PNM',
  'bullets': ['the properties of the different states of matter (solid, liquid and gas) in terms '
              'of the particle model, including gas pressure',
              'changes of state in terms of the particle model']},
 {'discipline': 'C',
  'area': 'Atoms, elements and compounds',
  'strand': 'Atoms, elements and compounds',
  'code': 'AEC',
  'bullets': ['a simple (Dalton) atomic model',
              'differences between atoms, elements and compounds',
              'chemical symbols and formulae for elements and compounds',
              'conservation of mass changes of state and chemical reactions']},
 {'discipline': 'C',
  'area': 'Pure and impure substances',
  'strand': 'Pure and impure substances',
  'code': 'PIS',
  'bullets': ['the concept of a pure substance',
              'mixtures, including dissolving',
              'diffusion in terms of the particle model',
              'simple techniques for separating mixtures: filtration, evaporation, distillation '
              'and chromatography',
              'the identification of pure substances']},
 {'discipline': 'C',
  'area': 'Chemical reactions',
  'strand': 'Chemical reactions',
  'code': 'CR',
  'bullets': ['chemical reactions as the rearrangement of atoms',
              'representing chemical reactions using formulae and using equations',
              'combustion, thermal decomposition, oxidation and displacement reactions',
              'defining acids and alkalis in terms of neutralisation reactions',
              'the pH scale for measuring acidity/alkalinity; and indicators',
              'reactions of acids with metals to produce a salt plus hydrogen',
              'reactions of acids with alkalis to produce a salt plus water',
              'what catalysts do']},
 {'discipline': 'C',
  'area': 'Energetics',
  'strand': 'Energetics',
  'code': 'ENER',
  'bullets': ['energy changes on changes of state (qualitative)',
              'exothermic and endothermic chemical reactions (qualitative)']},
 {'discipline': 'C',
  'area': 'The periodic table',
  'strand': 'The periodic table',
  'code': 'PT',
  'bullets': ['the varying physical and chemical properties of different elements',
              'the principles underpinning the Mendeleev periodic table',
              'the periodic table: periods and groups; metals and non-metals',
              'how patterns in reactions can be predicted with reference to the periodic table',
              'the properties of metals and non-metals',
              'the chemical properties of metal and non-metal oxides with respect to acidity']},
 {'discipline': 'C',
  'area': 'Materials',
  'strand': 'Materials',
  'code': 'MATS',
  'bullets': ['the order of metals and carbon in the reactivity series',
              'the use of carbon in obtaining metals from metal oxides',
              'properties of ceramics, polymers and composites (qualitative)']},
 {'discipline': 'C',
  'area': 'Earth and atmosphere',
  'strand': 'Earth and atmosphere',
  'code': 'EA',
  'bullets': ['the composition of the Earth',
              'the structure of the Earth',
              'the rock cycle and the formation of igneous, sedimentary and metamorphic rocks',
              'Earth as a source of limited resources and the efficacy of recycling',
              'the composition of the atmosphere',
              'the production of carbon dioxide by human activity and the impact on climate']},
 {'discipline': 'P',
  'area': 'Energy',
  'strand': 'Calculation of fuel uses and costs in the domestic context',
  'code': 'FUEL',
  'bullets': ['comparing energy values of different foods (from labels) (kJ)',
              'comparing power ratings of appliances in watts (W, kW)',
              'comparing amounts of energy transferred (J, kJ, kW hour)',
              'domestic fuel bills, fuel use and costs',
              'fuels and energy resources']},
 {'discipline': 'P',
  'area': 'Energy',
  'strand': 'Energy changes and transfers',
  'code': 'ECT',
  'bullets': ['simple machines give bigger force but at the expense of smaller movement (and vice '
              'versa): product of force and displacement unchanged',
              'heating and thermal equilibrium: temperature difference between 2 objects leading '
              'to energy transfer from the hotter to the cooler one, through contact (conduction) '
              'or radiation; such transfers tending to reduce the temperature difference; use of '
              'insulators',
              'other processes that involve energy transfer: changing motion, dropping an object, '
              'completing an electrical circuit, stretching a spring, metabolism of food, burning '
              'fuels']},
 {'discipline': 'P',
  'area': 'Energy',
  'strand': 'Changes in systems',
  'code': 'CIS',
  'bullets': ['energy as a quantity that can be quantified and calculated; the total energy has '
              'the same value before and after a change',
              'comparing the starting with the final conditions of a system and describing '
              'increases and decreases in the amounts of energy associated with movements, '
              'temperatures, changes in positions in a field, in elastic distortions and in '
              'chemical compositions',
              'using physical processes and mechanisms, rather than energy, to explain the '
              'intermediate steps that bring about such changes']},
 {'discipline': 'P',
  'area': 'Motion and forces',
  'strand': 'Describing motion',
  'code': 'MOT',
  'bullets': ['speed and the quantitative relationship between average speed, distance and time '
              '(speed = distance ÷ time)',
              'the representation of a journey on a distance-time graph',
              'relative motion: trains and cars passing one another']},
 {'discipline': 'P',
  'area': 'Motion and forces',
  'strand': 'Forces',
  'code': 'FORCES',
  'bullets': ['forces as pushes or pulls, arising from the interaction between 2 objects',
              'using force arrows in diagrams, adding forces in 1 dimension, balanced and '
              'unbalanced forces',
              'moment as the turning effect of a force',
              'forces: associated with deforming objects; stretching and squashing – springs; with '
              'rubbing and friction between surfaces, with pushing things out of the way; '
              'resistance to motion of air and water',
              'forces measured in newtons, measurements of stretch or compression as force is '
              'changed',
              'force-extension linear relation; Hooke’s Law as a special case',
              'work done and energy changes on deformation',
              'non-contact forces: gravity forces acting at a distance on Earth and in space, '
              'forces between magnets, and forces due to static electricity']},
 {'discipline': 'P',
  'area': 'Motion and forces',
  'strand': 'Pressure in fluids',
  'code': 'PRES',
  'bullets': ['atmospheric pressure, decreases with increase of height as weight of air above '
              'decreases with height',
              'pressure in liquids, increasing with depth; upthrust effects, floating and sinking',
              'pressure measured by ratio of force over area – acting normal to any surface']},
 {'discipline': 'P',
  'area': 'Motion and forces',
  'strand': 'Balanced forces',
  'code': 'BAL',
  'bullets': ['opposing forces and equilibrium: weight held by stretched spring or supported on a '
              'compressed surface']},
 {'discipline': 'P',
  'area': 'Motion and forces',
  'strand': 'Forces and motion',
  'code': 'FMOT',
  'bullets': ['forces being needed to cause objects to stop or start moving, or to change their '
              'speed or direction of motion (qualitative only)',
              'change depending on direction of force and its size']},
 {'discipline': 'P',
  'area': 'Waves',
  'strand': 'Observed waves',
  'code': 'OBW',
  'bullets': ['waves on water as undulations which travel through water with transverse motion; '
              'these waves can be reflected, and add or cancel – superposition']},
 {'discipline': 'P',
  'area': 'Waves',
  'strand': 'Sound waves',
  'code': 'SND',
  'bullets': ['frequencies of sound waves, measured in hertz (Hz); echoes, reflection and '
              'absorption of sound',
              'sound needs a medium to travel, the speed of sound in air, in water, in solids',
              'sound produced by vibrations of objects, in loudspeakers, detected by their effects '
              'on microphone diaphragm and the ear drum; sound waves are longitudinal',
              'the auditory range of humans and animals']},
 {'discipline': 'P',
  'area': 'Waves',
  'strand': 'Energy and waves',
  'code': 'EAW',
  'bullets': ['pressure waves transferring energy; use for cleaning and physiotherapy by '
              'ultrasound; waves transferring information for conversion to electrical signals by '
              'microphone']},
 {'discipline': 'P',
  'area': 'Waves',
  'strand': 'Light waves',
  'code': 'LGT',
  'bullets': ['the similarities and differences between light waves and waves in matter',
              'light waves travelling through a vacuum; speed of light',
              'the transmission of light through materials: absorption, diffuse scattering and '
              'specular reflection at a surface',
              'use of ray model to explain imaging in mirrors, the pinhole camera, the refraction '
              'of light and action of convex lens in focusing (qualitative); the human eye',
              'light transferring energy from source to absorber, leading to chemical and '
              'electrical effects; photosensitive material in the retina and in cameras',
              'colours and the different frequencies of light, white light and prisms (qualitative '
              'only); differential colour effects in absorption and diffuse reflection']},
 {'discipline': 'P',
  'area': 'Electricity and electromagnetism',
  'strand': 'Current electricity',
  'code': 'CUR',
  'bullets': ['electric current, measured in amperes, in circuits, series and parallel circuits, '
              'currents add where branches meet and current as flow of charge',
              'potential difference, measured in volts, battery and bulb ratings; resistance, '
              'measured in ohms, as the ratio of potential difference (p.d.) to current',
              'differences in resistance between conducting and insulating components '
              '(quantitative)']},
 {'discipline': 'P',
  'area': 'Electricity and electromagnetism',
  'strand': 'Static electricity',
  'code': 'STAT',
  'bullets': ['separation of positive or negative charges when objects are rubbed together: '
              'transfer of electrons, forces between charged objects',
              'the idea of electric field, forces acting across the space between objects not in '
              'contact']},
 {'discipline': 'P',
  'area': 'Electricity and electromagnetism',
  'strand': 'Magnetism',
  'code': 'MAG',
  'bullets': ['magnetic poles, attraction and repulsion',
              'magnetic fields by plotting with compass, representation by field lines',
              'Earth’s magnetism, compass and navigation',
              'the magnetic effect of a current, electromagnets, DC motors (principles only)']},
 {'discipline': 'P',
  'area': 'Matter',
  'strand': 'Physical changes',
  'code': 'PHYC',
  'bullets': ['conservation of material and of mass, and reversibility, in melting, freezing, '
              'evaporation, sublimation, condensation, dissolving',
              'similarities and differences, including density differences, between solids, '
              'liquids and gases',
              'Brownian motion in gases',
              'diffusion in liquids and gases driven by differences in concentration',
              'the difference between chemical and physical changes']},
 {'discipline': 'P',
  'area': 'Matter',
  'strand': 'Particle model',
  'code': 'PMOD',
  'bullets': ['the differences in arrangements, in motion and in closeness of particles explaining '
              'changes of state, shape and density; the anomaly of ice-water transition',
              'atoms and molecules as particles']},
 {'discipline': 'P',
  'area': 'Matter',
  'strand': 'Energy in matter',
  'code': 'EIM',
  'bullets': ['changes with temperature in motion and spacing of particles',
              'internal energy stored in materials']},
 {'discipline': 'P',
  'area': 'Space physics',
  'strand': 'Space physics',
  'code': 'SPACE',
  'bullets': ['gravity force, weight = mass x gravitational field strength (g), on Earth g=10 '
              'N/kg, different on other planets and stars; gravity forces between Earth and Moon, '
              'and between Earth and sun (qualitative only)',
              'our sun as a star, other stars in our galaxy, other galaxies',
              'the seasons and the Earth’s tilt, day length at different times of year, in '
              'different hemispheres',
              'the light year as a unit of astronomical distance']}]

PROPOSED_UNIT = {'B.CELLS': ['B1', 'B1', 'B1', 'B1', 'B1', 'B1'],
 'B.SKEL': ['B2', 'B2', 'B2'],
 'B.NUT': ['B3', 'B3', 'B3', 'B3', 'B3', 'B7'],
 'B.GAS': ['B4', 'B4', 'B4', 'B4'],
 'B.REP': ['B5', 'B5'],
 'B.HLTH': ['B6'],
 'B.PHOT': ['B7', 'B7', 'B7'],
 'B.RESP': ['B8', 'B8', 'B8', 'B8'],
 'B.ECO': ['B9', 'B9', 'B9'],
 'B.INH': ['B10', 'B10', 'B10', 'B10', 'B11', 'B11', 'B11'],
 'C.PNM': ['C1', 'C1'],
 'C.AEC': ['C2', 'C2', 'C2', 'C2'],
 'C.PIS': ['C3', 'C3', 'C1', 'C3', 'C3'],
 'C.CR': ['C4', 'C4', 'C5', 'C6', 'C6', 'C6', 'C6', 'C6'],
 'C.ENER': ['C7', 'C7'],
 'C.PT': ['C8', 'C8', 'C8', 'C8', 'C8', 'C8'],
 'C.MATS': ['C9', 'C9', 'C9'],
 'C.EA': ['C10', 'C10', 'C10', 'C10', 'C10', 'C10'],
 'P.FUEL': ['P2', 'P2', 'P2', 'P2', 'P2'],
 'P.ECT': ['P1', 'P1', 'P1'],
 'P.CIS': ['P1', 'P1', 'P1'],
 'P.MOT': ['P3', 'P3', 'P3'],
 'P.FORCES': ['P4', 'P4', 'P4', 'P4', 'P4', 'P4', 'P4', 'P4'],
 'P.PRES': ['P5', 'P5', 'P5'],
 'P.BAL': ['P4'],
 'P.FMOT': ['P4', 'P4'],
 'P.OBW': ['P6'],
 'P.SND': ['P6', 'P6', 'P6', 'P6'],
 'P.EAW': ['P6'],
 'P.LGT': ['P7', 'P7', 'P7', 'P7', 'P7', 'P7'],
 'P.CUR': ['P8', 'P8', 'P8'],
 'P.STAT': ['P9', 'P9'],
 'P.MAG': ['P10', 'P10', 'P10', 'P10'],
 'P.PHYC': ['C1', 'P11', 'P11', 'C1', 'C4'],
 'P.PMOD': ['P11', 'C2'],
 'P.EIM': ['P11', 'P11'],
 'P.SPACE': ['P12', 'P12', 'P12', 'P12']}

DISCIPLINE_NAMES = {"WS": "Working scientifically", "B": "Biology",
                    "C": "Chemistry", "P": "Physics"}

TRANSCRIPTION_SHA256 = (
    "3d6a2ee2a0c6785a9987c3b6d67fddd58b917377ace53bc7bc127e06627b8b9a")

# Lesson counts per unit as published in architecture.md §7. Used only by the
# coverage audit, which compares statutory supply against authoring demand.
SECTION7_LESSON_COUNTS = {
    "B1": 8, "B2": 4, "B3": 8, "B4": 5, "B5": 8, "B6": 3, "B7": 4, "B8": 5,
    "B9": 6, "B10": 5, "B11": 4,
    "C1": 6, "C2": 6, "C3": 7, "C4": 5, "C5": 5, "C6": 7, "C7": 4, "C8": 5,
    "C9": 4, "C10": 6,
    "P1": 8, "P2": 5, "P3": 3, "P4": 9, "P5": 4, "P6": 9, "P7": 7, "P8": 7,
    "P9": 3, "P10": 5, "P11": 4, "P12": 6,
}


def statement_id(discipline, code, ordinal):
    """The one place an ID is constructed. Change here to reissue (§11 dec. 6)."""
    return "KS3.%s.%s.%02d" % (discipline, code, ordinal)


def statements():
    """Yield every statutory statement in printed order."""
    for group in STRANDS:
        key = "%s.%s" % (group["discipline"], group["code"])
        owners = PROPOSED_UNIT.get(key, [])
        for i, text in enumerate(group["bullets"], 1):
            yield {
                "id": statement_id(group["discipline"], group["code"], i),
                "discipline": group["discipline"],
                "area": group["area"],
                "strand": group["strand"],
                "code": group["code"],
                "ordinal": i,
                "text": text,
                "proposed_unit": owners[i - 1] if i <= len(owners) else None,
            }


def verify():
    """Fail loudly if the transcription drifts or the ID space collides."""
    import hashlib
    corpus = "\n".join(b for g in STRANDS for b in g["bullets"])
    digest = hashlib.sha256(corpus.encode("utf-8")).hexdigest()
    if digest != TRANSCRIPTION_SHA256:
        raise SystemExit("transcription drift: %s != %s"
                         % (digest, TRANSCRIPTION_SHA256))
    ids = [s["id"] for s in statements()]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate statement IDs")
    for group in STRANDS:
        key = "%s.%s" % (group["discipline"], group["code"])
        if group["discipline"] == "WS":
            continue
        if len(PROPOSED_UNIT.get(key, [])) != len(group["bullets"]):
            raise SystemExit("PROPOSED_UNIT arity mismatch for %s" % key)
    return len(ids)


def _rows(entries, with_owner):
    head = ("| ID | Statutory statement (verbatim) | Proposed owning unit |\n"
            "|---|---|---|\n") if with_owner else (
            "| ID | Statutory statement (verbatim) |\n|---|---|\n")
    out = [head]
    for s in entries:
        text = s["text"].replace("|", "\\|")
        if with_owner:
            out.append("| `%s` | %s | %s |\n"
                       % (s["id"], text, s["proposed_unit"] or "—"))
        else:
            out.append("| `%s` | %s |\n" % (s["id"], text))
    return "".join(out)


def render():
    allst = list(statements())
    subject = [s for s in allst if s["discipline"] != "WS"]
    ws = [s for s in allst if s["discipline"] == "WS"]

    supply = {}
    for s in subject:
        supply.setdefault(s["proposed_unit"], []).append(s["id"])

    L = []
    w = L.append
    w("# KS3 statutory register\n\n")
    w("**Generated file — do not hand-edit.** Source of truth is `ks3_statutory.py` "
      "at the repo root; regenerate with `python3 ks3_statutory.py`.\n\n")
    w("Phase 0 of `docs/ks3/architecture.md` §10.1. Every statutory bullet of the "
      "Key stage 3 programme of study, given a permanent ID per §4.4.\n\n")
    w("**Source.** *National curriculum in England: science programmes of study*, "
      "DfE, 2014 (still in force), Key stage 3 section. Bullet text was extracted "
      "programmatically from the published HTML and **copied, never retyped**.\n\n")
    w("**Transcription fingerprint.** `sha256:%s` over the concatenated bullet "
      "corpus. Re-running the generator re-checks it.\n\n" % TRANSCRIPTION_SHA256)
    w("**Independently verified, 2026-07-26.** The register was re-extracted from "
      "the live published HTML by a second, independent pass and diffed against "
      "this corpus. **All 155 bullets matched**, and the per-discipline counts "
      "(B 39 / C 36 / P 62 / WS 18) and the full heading structure were confirmed "
      "against the source. **153 of 155 are byte-identical.** The 2 exceptions "
      "differ only where the published HTML contains a double space, which this "
      "register renders as a single space:\n\n")
    w("- `KS3.C.EA.05` — published page has two spaces between \"of\" and \"the\" "
      "in \"the composition of the atmosphere\"\n")
    w("- `KS3.P.ECT.01` — published page has two spaces between \"smaller\" and "
      "\"movement\"\n\n")
    w("No word, symbol or punctuation mark differs anywhere in the corpus. Those "
      "two are whitespace artefacts of the published page, not wording, and are "
      "recorded here so the gate check is complete rather than silent.\n\n")
    w("| | Count |\n|---|---|\n")
    for d in ("B", "C", "P"):
        w("| %s statements | %d |\n"
          % (DISCIPLINE_NAMES[d], len([s for s in subject if s["discipline"] == d])))
    w("| **Subject content total** | **%d** |\n" % len(subject))
    w("| Working Scientifically statements | %d |\n" % len(ws))
    w("| **All statutory statements** | **%d** |\n\n" % len(allst))

    w("## How to read this\n\n")
    w("- **ID** — permanent (§4.4 rule 1). Once a lesson references it, it never "
      "changes meaning. If the statutory document is revised, new IDs are added "
      "and old ones marked `superseded`; they are never reused.\n")
    w("- **Statutory statement** — verbatim. Not paraphrased, merged or tidied. "
      "This column is what Mide checks against the source document.\n")
    w("- **Proposed owning unit** — ⚠️ **advisory, and NOT part of the "
      "transcription gate.** It is this register's reading of architecture.md §7, "
      "recorded so coverage becomes computable. Ownership is finally fixed at "
      "lesson grain during authoring, not here.\n\n")
    w("**The single-source rule (§4.4 rule 3).** Every subject-content statement "
      "must be owned by exactly one lesson. Zero owners is a coverage hole; two "
      "owners is duplicated content. Both are build-blocking defects.\n\n")
    w("**Working Scientifically is exempt.** WS is taught *through* content "
      "(§5.7), tagged per lesson via `ws: []` at strand grain. WS statements are "
      "listed here for audit, and are expected to be exercised many times.\n\n")
    w("**ID scheme blessed by Mide, 2026-07-26** (§11 decision 6, now closed). "
      "The §4.4 `KS3.C.PNM.02` form was adopted exactly as specified, including "
      "both details Phase 0 flagged: strand = the heading that directly owns the "
      "bullets, and `KS3.WS.<STRAND>.<nn>` for Working Scientifically.\n\n")
    w("**These 155 IDs are therefore permanent.** §4.4 rule 1 now binds: an ID "
      "never changes meaning, and a superseded ID is never reused. IDs are still "
      "minted in one place (`statement_id()`) so the register regenerates "
      "wholesale — but a re-mint is now a **breaking change**, not a routine "
      "command. Do not renumber.\n\n")
    w("---\n\n")

    for d in ("B", "C", "P"):
        w("## %s\n\n" % DISCIPLINE_NAMES[d])
        area = None
        for group in STRANDS:
            if group["discipline"] != d:
                continue
            if group["area"] != area:
                area = group["area"]
                w("### %s\n\n" % area)
            if group["strand"] != group["area"]:
                w("#### %s\n\n" % group["strand"])
            w("Strand code `%s`.\n\n" % group["code"])
            w(_rows([s for s in subject if s["discipline"] == d
                     and s["code"] == group["code"]], True))
            w("\n")

    w("## Working scientifically\n\n")
    w("Taught through the content across all three disciplines (§5.7). "
      "Audit-only — exempt from the exactly-once rule.\n\n")
    for group in STRANDS:
        if group["discipline"] != "WS":
            continue
        w("### %s\n\nStrand code `%s`. Tag as `ws: [\"%s\"]`.\n\n"
          % (group["strand"], group["code"],
             group["strand"].lower().replace(" and ", "-and-").replace(" ", "-")))
        w(_rows([s for s in ws if s["code"] == group["code"]], False))
        w("\n")

    w("---\n\n## Appendix — coverage audit (advisory)\n\n")
    w("Statutory *supply* per unit (statements this register proposes it owns) "
      "against authoring *demand* (lessons architecture.md §7 gives it).\n\n")
    w("| Unit | Statements | §7 lessons | Statements per lesson |\n|---|---|---|---|\n")
    short = 0
    for u in sorted(SECTION7_LESSON_COUNTS, key=lambda x: (x[0], int(x[1:]))):
        n, l = len(supply.get(u, [])), SECTION7_LESSON_COUNTS[u]
        if n < l:
            short += 1
        w("| %s | %d | %d | %.2f%s |\n"
          % (u, n, l, n / l, " ⚠️" if n < l else ""))
    w("| **Total** | **%d** | **%d** | **%.2f** |\n\n"
      % (len(subject), sum(SECTION7_LESSON_COUNTS.values()),
         len(subject) / sum(SECTION7_LESSON_COUNTS.values())))
    w("**%d of %d units are marked ⚠️** — §7 gives them more lessons than there "
      "are statutory statements for those lessons to own.\n\n"
      % (short, len(SECTION7_LESSON_COUNTS)))
    w("This is the register's principal finding and it is recorded as open "
      "decision **§11.11**. There are %d subject-content statements and %d "
      "lessons in §7, so under §4.4 rule 3 (exactly one owner) at least %d "
      "lessons must own nothing — which §10.2 forbids (`covers` non-empty). "
      "The two rules cannot both hold as written.\n"
      % (len(subject), sum(SECTION7_LESSON_COUNTS.values()),
         sum(SECTION7_LESSON_COUNTS.values()) - len(subject)))
    return "".join(L)


def main():
    import os
    n = verify()
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "docs", "ks3", "statutory-register.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render())
    print("verified %d statements; wrote %s" % (n, out))


if __name__ == "__main__":
    main()
