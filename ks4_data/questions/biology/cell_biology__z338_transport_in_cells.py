"""Biology · Cell biology — the MRB-338 expansion of `transport-in-cells`.

One leaf only: AQA 8461 §4.1.3. The original twelve rows in `cell_biology.py`
take equilibrium, the carrier protein, the animal cell in pure water, the word
turgid, the pair of changes that speed diffusion up, urea leaving the liver,
the one-cell-thick alveolus wall, cyanide stopping active transport alone,
nitrate into a root hair cell, the cut-up potato and its extra surface, the
mouse against the single-celled organism, and the last of the glucose in the
small intestine.

This file takes what they leave. The three processes are defined from their own
side — the direction of diffusion, water alone in osmosis, the partially
permeable membrane, low-to-high for active transport and ATP as its cost — and
then applied: plasmolysis and wilting, lysis and crenation, the plant cell that
firms up rather than bursting, the gradient a respiring muscle keeps steep, the
blood supply and the ventilation that keep a gradient steep from outside, and
the four named exchange surfaces with the three features they share. The whole
misconception set is examined from the wrong side: glucose moving by osmosis,
diffusion paying for itself out of respiration, water travelling towards the
dilute side, and a cell wall imagined as waterproof.

The weight follows the CONTENT. `easier` takes only eight because the recall
here is a short list of definitions and directions, and a ninth way of asking
which process needs energy is the same question in new words. The demand lives
in applying one of three processes to a context the pupil has not met — a
tapeworm, a pond amoeba, a waterlogged root, a U-tube — and in comparing two
processes or two surfaces, so `standard` and `harder` carry twenty-two each.

Two things the lesson offers are deliberately NOT here. The percentage change
in mass of a potato cylinder is the lesson's own worked FIFA example and is
also flagged Higher-only, so the RP2 rows examine the method instead — the
independent variable, blotting, controlling time, and why a change rather than
a final mass. Surface-area-to-volume ARITHMETIC belongs to the
`eukaryotes-prokaryotes` leaf, which already owns the cube calculations, so
SA:V appears here only as the reason an organism needs exchange surfaces at
all.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The direction of diffusion, what moves in osmosis, plasmolysis, ATP as
    # the cost of active transport, the partially permeable membrane, the
    # direction active transport works in, the gas leaving the blood at the
    # alveoli, and the animal cell that shrinks.
    {
        "id": "ks4-transport-in-cells-e05",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the direction in which particles move during "
                "diffusion.",
        "options": [
            "From where they are more concentrated to where they are less concentrated",
            "In one fixed direction, set by the carrier proteins in the membrane",
            "Towards whichever side of the membrane happens to be the warmer one",
            "From where they are less concentrated to where they are more concentrated",
        ],
        "correct_index": 0,
        "why": "Diffusion is the net movement of particles down a "
               "concentration gradient, from a higher to a lower "
               "concentration.",
    },
    {
        "id": "ks4-transport-in-cells-e06",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which substance moves during osmosis.",
        "options": [
            "Dissolved sugars, but not water itself",
            "Water molecules only",
            "Any dissolved solute, such as glucose or a salt",
            "Water molecules and any dissolved ions, together",
        ],
        "correct_index": 1,
        "why": "Osmosis is the net movement of water molecules only, across a "
               "partially permeable membrane.",
    },
    {
        "id": "ks4-transport-in-cells-e07",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the change in which a plant cell's membrane pulls away "
                "from its cell wall.",
        "options": [
            "Diffusion",
            "Turgor",
            "Plasmolysis",
            "Lysis",
        ],
        "correct_index": 2,
        "why": "A plant cell that loses water by osmosis shrinks until its "
               "membrane pulls away from the wall, which is plasmolysis.",
    },
    {
        "id": "ks4-transport-in-cells-e08",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the substance that supplies the energy for active "
                "transport.",
        "options": [
            "Glucose, used directly by each carrier protein in the membrane",
            "Oxygen, which pushes the ions across the cell membrane itself",
            "Heat taken in from the surroundings by the cell membrane",
            "ATP, released by respiration",
        ],
        "correct_index": 3,
        "why": "Carrier proteins are powered by ATP, and a cell's ATP comes "
               "from respiration.",
    },
    {
        "id": "ks4-transport-in-cells-e09",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the term for a membrane that lets water molecules "
                "through but holds larger solute molecules back.",
        "options": [
            "Partially permeable",
            "Fully permeable",
            "Impermeable",
            "Waterproof",
        ],
        "correct_index": 0,
        "why": "A partially permeable membrane has pores small enough to let "
               "water through but not larger dissolved molecules.",
    },
    {
        "id": "ks4-transport-in-cells-e10",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the direction in which active transport moves a "
                "substance across a membrane.",
        "options": [
            "Down the concentration gradient, from a higher to a lower concentration",
            "Against the concentration gradient, from a lower to a higher concentration",
            "Outwards, since a carrier protein can pump a substance out of a cell but not into one",
            "In whichever direction the water inside the cell happens to be moving",
        ],
        "correct_index": 1,
        "why": "Active transport moves a substance from a lower to a higher "
               "concentration, against the gradient, using carrier proteins "
               "and ATP.",
    },
    {
        "id": "ks4-transport-in-cells-e11",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the waste gas made by respiring cells that diffuses out "
                "of the blood and into the air in the alveoli.",
        "options": [
            "Nitrogen",
            "Water vapour",
            "Carbon dioxide",
            "Oxygen",
        ],
        "correct_index": 2,
        "why": "Respiring cells make carbon dioxide, so it is more "
               "concentrated in the blood than in alveolar air and diffuses "
               "out of the blood.",
    },
    {
        "id": "ks4-transport-in-cells-e12",
        "subtopic_slug": "transport-in-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "An animal cell is put into a very concentrated salt "
                "solution. State the change in its size.",
        "options": [
            "It stays exactly the same size, because a cell membrane blocks water",
            "It bursts, because the salt raises the pressure inside it",
            "It swells and then bursts, because dissolved salt pulls extra water in through the membrane",
            "It shrinks, because water leaves it by osmosis",
        ],
        "correct_index": 3,
        "why": "The salt solution is more concentrated than the cell "
               "contents, so water leaves the cell by osmosis and it shrinks.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Applying one of the three processes to a familiar context: gas exchange
    # at the alveolus, the cell wall, wilting, microvilli and villi, the
    # gradient kept steep by respiration, blood flow and ventilation, the
    # three misconceptions from the wrong side, RP2's method, and why the
    # body holds the plasma steady.
    {
        "id": "ks4-transport-in-cells-s05",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why oxygen diffuses from the air in an alveolus into "
                "the blood.",
        "options": [
            "Because oxygen is more concentrated in the alveolus than in the blood arriving",
            "Because carrier proteins in the wall of the alveolus pump the oxygen inwards",
            "Because the alveolus is warmer than the blood, so oxygen moves towards the cold",
            "Because the alveolus squeezes as you breathe out, and that forces the oxygen across",
        ],
        "correct_index": 0,
        "why": "Blood arriving at the lungs is low in oxygen, so oxygen "
               "diffuses down the concentration gradient into it.",
    },
    {
        "id": "ks4-transport-in-cells-s06",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A red blood cell bursts in distilled water but a plant cell "
                "does not. Explain the difference.",
        "options": [
            "The plant cell's vacuole breaks the water down before any pressure builds",
            "The plant cell has a strong cell wall that resists the pressure as water enters",
            "The plant cell takes in no water, because its wall is waterproof",
            "The plant cell pumps the extra water straight back out by active transport",
        ],
        "correct_index": 1,
        "why": "Water enters both cells by osmosis, but a plant cell's rigid "
               "cellulose wall stops it swelling far enough to burst.",
    },
    {
        "id": "ks4-transport-in-cells-s07",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a houseplant wilts when its soil dries out.",
        "options": [
            "Its cells take in air instead of water, and air cannot hold a stem upright",
            "Active transport reverses and pumps water out of every cell into the dry soil",
            "Water leaves its cells by osmosis, so they become flaccid and give less support",
            "Its cell walls dissolve away once there is no water left in the surrounding soil to hold them up",
        ],
        "correct_index": 2,
        "why": "Dry soil is more concentrated than the cell contents, so "
               "water leaves by osmosis and turgid cells become flaccid.",
    },
    {
        "id": "ks4-transport-in-cells-s08",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the microvilli on the cells lining the small "
                "intestine speed up absorption.",
        "options": [
            "They push the food along the intestine so that it meets a fresh set of absorbing cells",
            "They shorten the intestine, so food stays in contact with it for longer",
            "They add extra enzymes to the food, so that far more of it becomes small enough to be absorbed",
            "They greatly increase the surface area across which molecules are absorbed",
        ],
        "correct_index": 3,
        "why": "Microvilli are tiny folds on each cell's surface, and a "
               "larger surface area means more molecules absorbed each "
               "second.",
    },
    {
        "id": "ks4-transport-in-cells-s09",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why oxygen diffuses into a muscle cell faster during "
                "exercise.",
        "options": [
            "The muscle uses oxygen quickly, so the gradient into the cell is steeper",
            "The muscle cell grows a thicker membrane, which holds more oxygen inside",
            "Warm muscle makes oxygen molecules larger, so they cross a membrane sooner",
            "The muscle switches over to active transport, which is faster than diffusion",
        ],
        "correct_index": 0,
        "why": "A respiring muscle uses oxygen up, keeping its internal "
               "concentration low and the concentration gradient steep.",
    },
    {
        "id": "ks4-transport-in-cells-s10",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a rich blood supply makes the small intestine a "
                "better absorbing surface.",
        "options": [
            "It presses on the intestine wall, forcing molecules through into the blood",
            "It carries absorbed molecules away, which keeps the concentration gradient steep",
            "It warms the gut contents, and warm food is digested into smaller molecules",
            "It supplies the water that dissolves the food before it can be absorbed",
        ],
        "correct_index": 1,
        "why": "Blood flowing past removes absorbed molecules, so the "
               "concentration inside the gut stays higher than the "
               "concentration in the blood.",
    },
    {
        "id": "ks4-transport-in-cells-s11",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that glucose enters a cell by osmosis. "
                "Identify the error.",
        "options": [
            "Osmosis needs ATP, and a cell has no ATP left once it absorbs glucose",
            "Osmosis happens in plant cells, so an animal cell cannot use it",
            "Osmosis moves water molecules only, so glucose cannot move by osmosis",
            "Osmosis moves glucose outwards, and not inwards, across a membrane",
        ],
        "correct_index": 2,
        "why": "Osmosis is the movement of water alone across a partially "
               "permeable membrane; glucose moves by diffusion or by active "
               "transport.",
    },
    {
        "id": "ks4-transport-in-cells-s12",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that diffusion uses energy from "
                "respiration. Explain why this is wrong.",
        "options": [
            "Diffusion uses energy taken from the Sun instead, which is what warms the particles up",
            "Diffusion uses energy inside plant cells, where respiration runs much more slowly",
            "Diffusion releases energy rather than using any of it up, which is why it warms a cell through",
            "Diffusion is passive, and the particles' own random movement is what drives it",
        ],
        "correct_index": 3,
        "why": "Particles diffuse because of their own kinetic energy, so no "
               "ATP from respiration is needed.",
    },
    {
        "id": "ks4-transport-in-cells-s13",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why warming a solution increases the rate at which "
                "a dye diffuses through it.",
        "options": [
            "The dye particles gain kinetic energy, so they spread out more quickly",
            "The solution becomes more dilute, and a dilute solution lets a dye through faster",
            "Warming makes the dye particles smaller, so they slip past one another sooner",
            "Warming supplies the ATP that the dye particles need in order to keep moving",
        ],
        "correct_index": 0,
        "why": "Raising the temperature gives particles more kinetic energy, "
               "so they move faster and spread out sooner.",
    },
    {
        "id": "ks4-transport-in-cells-s14",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Potato cylinders are left in sucrose solutions to "
                "investigate osmosis. Identify the variable that is "
                "deliberately changed.",
        "options": [
            "The starting mass of each of the potato cylinders that is used",
            "The concentration of the sucrose solution each cylinder is placed in",
            "The length of time for which each of the potato cylinders is left standing in its tube",
            "The temperature of the solution in each of the separate test tubes",
        ],
        "correct_index": 1,
        "why": "Concentration is the independent variable; time, temperature "
               "and cylinder size are all controlled so that only "
               "concentration differs.",
    },
    {
        "id": "ks4-transport-in-cells-s15",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why potato cylinders are blotted with paper before "
                "they are weighed at the end of an osmosis investigation.",
        "options": [
            "So that any sucrose still inside a cylinder is drawn out of it onto the paper towel",
            "So that osmosis is stopped before a cylinder can lose any further water",
            "So that solution left on the surface is not weighed as part of the potato",
            "So that each cylinder is dry enough for the electronic balance to switch itself on",
        ],
        "correct_index": 2,
        "why": "Liquid clinging to the surface adds mass that has nothing to "
               "do with water entering or leaving the cells, so it would "
               "distort the change.",
    },
    {
        "id": "ks4-transport-in-cells-s16",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant cell placed in pure water becomes firm "
                "rather than bursting.",
        "options": [
            "It pushes the same amount of water back out again as fast as it comes in",
            "Its cell membrane becomes waterproof once enough water has entered the cell",
            "It turns all of the extra water into starch and then stores that inside its vacuole",
            "Its cellulose cell wall stops it swelling any further once it is turgid",
        ],
        "correct_index": 3,
        "why": "Water enters by osmosis until the pressure on the rigid cell "
               "wall stops any more coming in, so the cell becomes turgid "
               "rather than bursting.",
    },
    {
        "id": "ks4-transport-in-cells-s17",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's contents are a more concentrated solution than the "
                "liquid around it. Predict the net movement of water.",
        "options": [
            "Into the cell, because water moves to the more concentrated solution",
            "Out of the cell, because water moves to the more dilute solution",
            "There is none, because a partially permeable membrane stops water crossing",
            "Out of the cell, for as long as the cell goes on respiring",
        ],
        "correct_index": 0,
        "why": "Water moves by osmosis from the more dilute solution outside "
               "to the more concentrated solution inside the cell.",
    },
    {
        "id": "ks4-transport-in-cells-s18",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the lungs contain millions of tiny alveoli "
                "rather than two large air sacs.",
        "options": [
            "Small sacs let the lungs warm the incoming air before it meets the blood",
            "Millions of small sacs give a far greater total surface area for exchange",
            "Millions of small sacs hold a far greater total volume of air than two large ones could",
            "Small sacs have thinner walls, so each one can be squeezed completely empty on breathing out",
        ],
        "correct_index": 1,
        "why": "Splitting the same volume into millions of sacs gives a huge "
               "surface area, so far more oxygen diffuses across each second.",
    },
    {
        "id": "ks4-transport-in-cells-s19",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how breathing in and out helps oxygen to keep "
                "diffusing into the blood.",
        "options": [
            "It presses the alveoli against the capillaries, pushing oxygen into the blood",
            "It removes the water from the alveoli, so the oxygen has no liquid to cross",
            "It brings in fresh air, which keeps the oxygen concentration in the alveoli high",
            "It warms the air inside the alveoli, and warm oxygen dissolves far more easily in the blood",
        ],
        "correct_index": 2,
        "why": "Ventilation replaces used air with fresh air, so the "
               "concentration gradient between the alveolus and the blood "
               "stays steep.",
    },
    {
        "id": "ks4-transport-in-cells-s20",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what is meant by describing a cell membrane as "
                "partially permeable.",
        "options": [
            "It lets every substance cross it, but in one direction and not back",
            "It lets nothing cross it unless the cell happens to be respiring",
            "It lets substances cross during the time when the cell is dividing in two",
            "It lets some substances cross it but holds other substances back",
        ],
        "correct_index": 3,
        "why": "Small molecules such as water pass freely through the "
               "membrane, while larger or charged particles do not.",
    },
    {
        "id": "ks4-transport-in-cells-s21",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an amoeba, a single-celled organism, needs no "
                "lungs and no blood system.",
        "options": [
            "Its surface area is large compared with its volume, and nothing lies far inside",
            "It does not respire, so it has no need to take in oxygen",
            "It absorbs oxygen by active transport, which needs no transport system",
            "Its volume is large compared with its surface area, so diffusion is enough",
        ],
        "correct_index": 0,
        "why": "A tiny organism has a high surface area to volume ratio and a "
               "short diffusion path, so diffusion alone supplies every part "
               "of it.",
    },
    {
        "id": "ks4-transport-in-cells-s22",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why sprinkling sugar over sliced strawberries draws "
                "juice out of them.",
        "options": [
            "The sugar cools the fruit down, and a cold cell cannot hold on to its water",
            "The sugar makes a concentrated solution outside, so water leaves by osmosis",
            "The sugar dissolves the cell walls, which lets the juice run out of a slice",
            "The sugar is absorbed by active transport, and the juice follows it outwards",
        ],
        "correct_index": 1,
        "why": "Sugar dissolving on the surface makes the outside more "
               "concentrated than the cell contents, so water leaves the "
               "cells by osmosis.",
    },
    {
        "id": "ks4-transport-in-cells-s23",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the long, narrow projection of a root hair cell "
                "helps a plant to take up water.",
        "options": [
            "It works in the way a drinking straw does, sucking soil water up towards the root",
            "It gives the cell more room inside to store the water it takes in",
            "It increases the surface area in contact with the water in the soil",
            "It reaches down as far as the water table, so the cell stands in free water",
        ],
        "correct_index": 2,
        "why": "A long projection greatly increases the surface area across "
               "which water can enter the cell by osmosis.",
    },
    {
        "id": "ks4-transport-in-cells-s24",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a substance diffuses more slowly across a "
                "thicker membrane.",
        "options": [
            "A thicker membrane has fewer pores in total for particles to pass through",
            "A thicker membrane holds the particles still until the cell respires again",
            "A thicker membrane is colder, so the particles inside it move more slowly",
            "The particles have a longer distance to travel in order to get across it",
        ],
        "correct_index": 3,
        "why": "The rate of diffusion falls as the diffusion path lengthens, "
               "which is why exchange surfaces are only one cell thick.",
    },
    {
        "id": "ks4-transport-in-cells-s25",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a cell has to respire in order to absorb ions by "
                "active transport.",
        "options": [
            "Respiration releases the ATP that the carrier proteins use to pump the ions",
            "Respiration breaks the mineral ions into smaller pieces, so a carrier protein can hold them",
            "Respiration removes the water from around the ions, so a carrier protein can grip them",
            "Respiration makes the membrane thinner, so the ions have less far to go",
        ],
        "correct_index": 0,
        "why": "Carrier proteins are powered by ATP, and ATP comes from "
               "respiration, so no respiration means no active transport.",
    },
    {
        "id": "ks4-transport-in-cells-s26",
        "subtopic_slug": "transport-in-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the body keeps the concentration of the blood "
                "plasma steady.",
        "options": [
            "So that the active transport that goes on in the kidney can be switched off to save energy",
            "So that water does not enter or leave body cells fast enough to damage them",
            "So that the plasma stays thin enough for the heart to be able to keep pumping it",
            "So that oxygen can dissolve in the plasma, which it cannot do once that alters",
        ],
        "correct_index": 1,
        "why": "If the plasma became too dilute or too concentrated, cells "
               "would swell or shrink by osmosis and stop working properly.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Comparison of two processes or two surfaces, unfamiliar contexts (a
    # tapeworm, a fish's gills, a pond amoeba, a waterlogged root, a U-tube,
    # a wilted lettuce), the two-step diffusion path, RP2 evaluation, and
    # three claims to weigh.
    {
        "id": "ks4-transport-in-cells-h05",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare osmosis with diffusion.",
        "options": [
            "Both are passive, but osmosis moves water only, through a partially permeable membrane",
            "Both move water, but diffusion needs a membrane whereas osmosis does not",
            "Both need ATP, but osmosis uses much less of it than diffusion ever does",
            "Both move particles up a gradient, but diffusion alone needs a membrane",
        ],
        "correct_index": 0,
        "why": "Osmosis is a special case of diffusion: both are passive and "
               "go down a gradient, but osmosis is water alone crossing a "
               "partially permeable membrane.",
    },
    {
        "id": "ks4-transport-in-cells-h06",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare active transport with diffusion.",
        "options": [
            "Active transport moves water, whereas diffusion moves other substances",
            "Active transport goes against the gradient and needs ATP; diffusion needs neither",
            "Both go against the gradient, but active transport carries the larger particles",
            "Both need ATP, but active transport needs carrier proteins as well as the ATP",
        ],
        "correct_index": 1,
        "why": "Diffusion is passive and runs down the gradient; active "
               "transport runs the other way and costs ATP, spent by carrier "
               "proteins.",
    },
    {
        "id": "ks4-transport-in-cells-h07",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diffusion experiment is repeated at 20 °C instead of "
                "40 °C, with the concentration gradient unchanged. Predict "
                "and explain the effect on the rate.",
        "options": [
            "Unchanged, because only the concentration gradient can alter a rate of diffusion",
            "Unchanged, because diffusion is passive and a passive process has one fixed rate",
            "Slower, because the particles have less kinetic energy and so move less quickly",
            "Faster, because cool particles are denser and therefore travel further each second",
        ],
        "correct_index": 2,
        "why": "Temperature sets how fast particles move, so cooling reduces "
               "the rate of diffusion even when the gradient is the same.",
    },
    {
        "id": "ks4-transport-in-cells-h08",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fish's gills are made of many thin filaments, and water "
                "flows over them constantly. Explain how these two features "
                "speed up gas exchange.",
        "options": [
            "Many thin filaments make the gills lighter, and the flowing water pushes oxygen into the blood",
            "Many thin filaments store oxygen between them, and the flowing water washes it inwards",
            "Many thin filaments warm the water, and warm water holds far more oxygen than cold",
            "Many thin filaments give a large surface area and a short path, and flowing water keeps the gradient steep",
        ],
        "correct_index": 3,
        "why": "A large, thin surface with a steep gradient maintained across "
               "it is what every efficient exchange surface has.",
    },
    {
        "id": "ks4-transport-in-cells-h09",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tapeworm lives in the intestine, has no gut and no blood "
                "system, and its body is very flat and thin. Suggest how it "
                "obtains its nutrients.",
        "options": [
            "It absorbs dissolved nutrients across the whole of its surface by diffusion",
            "It pumps nutrients in through a single opening in its head end, using active transport",
            "It makes its own nutrients by photosynthesis inside its flat body",
            "It stores all the nutrients it will ever need before entering the host",
        ],
        "correct_index": 0,
        "why": "A flat, thin body has a high surface area to volume ratio, so "
               "diffusion across the body surface reaches every cell.",
    },
    {
        "id": "ks4-transport-in-cells-h10",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is left in waterlogged soil, so its roots cannot "
                "respire aerobically. Predict the effect on its uptake of "
                "water and of mineral ions.",
        "options": [
            "Both speed up, because waterlogged soil is far more dilute than the cells",
            "Mineral ion uptake falls away, but water uptake by osmosis can carry on",
            "Water uptake stops, but mineral ion uptake by diffusion can carry on",
            "Both stop, because a root cell needs ATP for every substance it takes in",
        ],
        "correct_index": 1,
        "why": "Mineral ions enter by active transport, which needs ATP from "
               "respiration; water enters by osmosis, which needs none.",
    },
    {
        "id": "ks4-transport-in-cells-h11",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potato cylinder gains mass after two hours in a sucrose "
                "solution. Deduce what this shows about the solution.",
        "options": [
            "It held no sucrose, since sucrose is what makes a potato lose mass",
            "It was at the same concentration as the cell contents, so nothing moved",
            "It was more dilute than the cell contents, so water entered by osmosis",
            "It was more concentrated than the cell contents, so sucrose entered the cells",
        ],
        "correct_index": 2,
        "why": "A gain in mass means water moved into the cells, so the "
               "solution outside must have been the more dilute of the two.",
    },
    {
        "id": "ks4-transport-in-cells-h12",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An alveolus wall and the capillary wall beside it are each "
                "one cell thick, and each of those cells is 0.20 µm thick. "
                "Calculate the distance oxygen diffuses to reach the blood.",
        "options": [
            "2.00 µm",
            "0.10 µm",
            "0.20 µm",
            "0.40 µm",
        ],
        "correct_index": 3,
        "why": "Oxygen crosses one cell in each wall, so the diffusion path "
               "is 0.20 µm + 0.20 µm = 0.40 µm.",
    },
    {
        "id": "ks4-transport-in-cells-h13",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a turgid plant cell with a flaccid one, and give the "
                "effect of each on the plant.",
        "options": [
            "Turgid cells are full of water and support the plant; flaccid cells have lost water and it wilts",
            "Turgid cells have lost water and the plant wilts; flaccid cells are full and hold it up",
            "Turgid cells are dividing and flaccid cells are not, so only turgid cells give support",
            "Turgid and flaccid cells hold the same water, and just their wall thickness differs",
        ],
        "correct_index": 0,
        "why": "Turgid cells press against their walls and hold the plant up; "
               "once water is lost they become flaccid and the plant wilts.",
    },
    {
        "id": "ks4-transport-in-cells-h14",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In an osmosis investigation one potato cylinder is left in "
                "its solution for 20 minutes and another for 60 minutes. "
                "Explain how this affects the conclusion.",
        "options": [
            "Time matters only for active transport, so the conclusion is unaffected by it",
            "Time was not controlled, so the two changes in mass cannot fairly be compared",
            "Time makes no difference here, because osmosis finishes within the first minute",
            "The longer time is the better one, so the 20-minute result should be doubled",
        ],
        "correct_index": 1,
        "why": "Time is a control variable: unless every cylinder is left for "
               "the same time, a difference in mass may be caused by time "
               "rather than by concentration.",
    },
    {
        "id": "ks4-transport-in-cells-h15",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an osmosis investigation records the change in "
                "each potato cylinder's mass rather than only its final mass.",
        "options": [
            "A balance reads a change in mass directly, so no final mass has to be recorded at all",
            "Only a change in mass can be read from a balance that shows two decimal places",
            "The cylinders do not all start at the same mass, so only the change compares them",
            "A final mass cannot be measured accurately once a cylinder has been blotted dry",
        ],
        "correct_index": 2,
        "why": "Cylinders differ slightly at the start, so the difference "
               "between the starting and final mass is the only fair measure "
               "of the water gained or lost.",
    },
    {
        "id": "ks4-transport-in-cells-h16",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cells that absorb large quantities of mineral ions contain "
                "unusually many mitochondria. Explain why.",
        "options": [
            "Mitochondria hold the mineral ions until the cell is ready to use them",
            "Mitochondria make the carrier proteins the membrane needs for those ions",
            "Mitochondria make the membrane more permeable, so more ions can diffuse in",
            "Mitochondria release the ATP that the active transport of the ions needs",
        ],
        "correct_index": 3,
        "why": "Active transport is powered by ATP from aerobic respiration, "
               "and aerobic respiration takes place in the mitochondria.",
    },
    {
        "id": "ks4-transport-in-cells-h17",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single-celled organism living in a pond takes in water "
                "continuously and has to pump it back out again. Explain why "
                "water keeps entering it.",
        "options": [
            "The pond water is more dilute than its cytoplasm, so water enters by osmosis",
            "The pond water is more concentrated than its cytoplasm, so water is drawn in",
            "Its membrane pumps water in by active transport, and then has to pump it out",
            "Water is the only substance small enough to cross a membrane either way",
        ],
        "correct_index": 0,
        "why": "Pond water is a very dilute solution, so there is a permanent "
               "osmotic gradient into the more concentrated cytoplasm.",
    },
    {
        "id": "ks4-transport-in-cells-h18",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that because diffusion is passive, an "
                "organism can do nothing to make oxygen diffuse into its "
                "cells faster. Evaluate this statement.",
        "options": [
            "Wrong — an organism speeds diffusion up by switching its cells to active transport",
            "Wrong — it cannot push the particles, but it can keep the gradient steep and the path short",
            "Right — a passive process has one fixed rate, and nothing outside it can alter that",
            "Right — only active transport can be speeded up, because a pump can be driven harder",
        ],
        "correct_index": 1,
        "why": "Diffusion needs no ATP, but surface area, thickness and the "
               "concentration gradient all set its rate, and an organism "
               "controls all three.",
    },
    {
        "id": "ks4-transport-in-cells-h19",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The alveoli and the villi are both exchange surfaces. State "
                "the feature they share and what each of them exchanges.",
        "options": [
            "Both use active transport only; alveoli take in oxygen and the villi take in water",
            "Both are five cells thick; alveoli absorb digested food and the villi take in oxygen",
            "Both are thin with a large surface area; alveoli exchange gases and villi absorb nutrients",
            "Both are thick with a small surface area; alveoli absorb nutrients and villi exchange gases",
        ],
        "correct_index": 2,
        "why": "Every efficient exchange surface is thin with a large surface "
               "area; alveoli exchange oxygen and carbon dioxide, while villi "
               "absorb digested food.",
    },
    {
        "id": "ks4-transport-in-cells-h20",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sucrose solution and pure water are separated by a "
                "partially permeable membrane in a U-tube. Predict what "
                "happens to the two liquid levels.",
        "options": [
            "The level rises on the water side and falls on the sucrose side",
            "Both levels rise, because the sucrose and the water swell as they mix",
            "Neither level changes, because such a membrane stops water crossing it",
            "The level rises on the sucrose side and falls on the water side",
        ],
        "correct_index": 3,
        "why": "Water moves by osmosis from the pure water into the more "
               "concentrated sucrose solution, so that side gains volume.",
    },
    {
        "id": "ks4-transport-in-cells-h21",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why drinking a very large volume of pure water in a "
                "short time could damage a person's red blood cells.",
        "options": [
            "The plasma becomes too dilute, so water enters the cells by osmosis and they may burst",
            "The plasma becomes too concentrated, so water leaves the cells and they shrivel up",
            "The extra water dissolves the cell membranes, so haemoglobin leaks into the plasma",
            "The extra water dilutes the haemoglobin, so each cell must swell to hold more of it",
        ],
        "correct_index": 0,
        "why": "Diluting the plasma makes it less concentrated than the cell "
               "contents, so water enters by osmosis, and a red blood cell "
               "has no wall to stop it bursting.",
    },
    {
        "id": "ks4-transport-in-cells-h22",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two exchange surfaces have the same surface area, but one is "
                "one cell thick and the other is five cells thick. Determine "
                "which exchanges oxygen faster, and why.",
        "options": [
            "The five-cell-thick surface, because it has more membranes to carry the oxygen",
            "The one-cell-thick surface, because the diffusion path across it is shorter",
            "The five-cell-thick surface, because it holds more oxygen at any one moment",
            "Neither, because surface area is the only feature that sets a rate of diffusion",
        ],
        "correct_index": 1,
        "why": "The rate of diffusion rises as the path shortens, so at the "
               "same area and gradient the thinner surface exchanges oxygen "
               "faster.",
    },
    {
        "id": "ks4-transport-in-cells-h23",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The cells lining the small intestine have many microvilli "
                "and many mitochondria. Explain what each of these features "
                "contributes to absorption.",
        "options": [
            "Microvilli digest the food into smaller molecules; the mitochondria then store them",
            "Microvilli hold the food still against the wall; the mitochondria destroy pathogens",
            "Microvilli enlarge the surface area; the mitochondria supply the ATP for active transport",
            "Microvilli supply the ATP for absorption; the mitochondria enlarge the absorbing surface",
        ],
        "correct_index": 2,
        "why": "A large surface area speeds diffusion up, and ATP from the "
               "mitochondria lets the cell go on absorbing once the gradient "
               "has run out.",
    },
    {
        "id": "ks4-transport-in-cells-h24",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that active transport is better than "
                "diffusion because it is faster. Evaluate this statement.",
        "options": [
            "Right — a carrier protein moves a substance far more quickly than diffusion can",
            "Right — any process that uses ATP is faster than any process that uses none",
            "Wrong — its advantage is that it needs no ATP, unlike diffusion, which does",
            "Wrong — its advantage is direction, not speed: it can move a substance up a gradient",
        ],
        "correct_index": 3,
        "why": "Active transport is useful because it works against a "
               "concentration gradient, which diffusion can never do; speed "
               "is not the point.",
    },
    {
        "id": "ks4-transport-in-cells-h25",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wilted lettuce leaf becomes crisp again after an hour in "
                "cold water. Explain why.",
        "options": [
            "Water enters its cells by osmosis until they are turgid and support the leaf",
            "The cold water makes the cell walls contract, and that pulls the leaf straight",
            "Water is absorbed by active transport, which is faster in cold conditions",
            "The cold water fills the air spaces inside the leaf, and that stiffens it",
        ],
        "correct_index": 0,
        "why": "The water is more dilute than the cell contents, so water "
               "enters by osmosis and the cells become turgid again.",
    },
    {
        "id": "ks4-transport-in-cells-h26",
        "subtopic_slug": "transport-in-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the way water enters a root hair cell from the soil "
                "with the way mineral ions enter it.",
        "options": [
            "Both enter by active transport, because soil water is too dilute for either alone",
            "Water enters by osmosis with no ATP; mineral ions enter by active transport, using ATP",
            "Water enters by active transport, using ATP, while mineral ions enter by osmosis with none",
            "Both enter by osmosis, though the mineral ions also need a carrier protein to help them cross",
        ],
        "correct_index": 1,
        "why": "Soil water is more dilute than the cell, so water enters by "
               "osmosis; mineral ions are already more concentrated inside, "
               "so they need active transport.",
    },
]
