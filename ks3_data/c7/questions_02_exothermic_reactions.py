"""C7 lesson 02 — Exothermic reactions: twelve questions (MRB-272).

The lesson's argument is one shape: an exothermic change transfers energy OUT
to its surroundings, so the mixture warms — and the energy was stored in the
chemicals before anything happened. The page teaches it by running five beakers
with a prediction in front of each, so these twelve probe the angles the
mastery ladder leaves alone: what the thermometer is actually in, where the
energy was before the reaction, and what "needs a spark" does and does not
imply.

The distractors are built from the lesson's two declared misconceptions.

`ENER-03` (a reaction that needs heating to start cannot be exothermic) drives
the wrong options in e02, s01, s03 and h01. Each treats the start of a reaction
as its whole energy account. s03 is the one that matters: it removes the
starter altogether — a hand warmer needs no flame — so the belief has nowhere
left to stand.

`ENER-04` (chemical reactions create energy) drives e04, s02, h02 and h04,
where energy appears from nothing. h04 is the register's own case put as an
engineering question, which is where a student actually meets it.

A third strand, on the page and in neither register entry, is that a
temperature rise must mean something got hot enough to see. e03 and h03 are
built on it: rusting is exothermic like every oxidation and normally too slow
for anybody to notice.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes.
"""

UNIT = "C7"
LESSON = "exothermic-reactions"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-02-e01",
        "band": "easier",
        "text": "An acid and an alkali are mixed and the thermometer in the "
                "beaker rises from 20 °C to 27 °C. What does that tell you?",
        "options": [
            {"text": "The reaction is exothermic, because energy has been "
                     "transferred out to the surroundings", "correct": True},
            {"text": "The reaction is endothermic, because the mixture "
                     "absorbed energy and got hotter", "correct": False,
             "why": "Endothermic means energy goes IN to the reaction, and "
                    "the surroundings then get colder. This mixture got "
                    "warmer."},
            {"text": "Nothing yet, because a temperature change on its own "
                     "does not show a reaction happened", "correct": False,
             "why": "A temperature change with no heater and no cooler is "
                    "exactly the evidence that a reaction has released "
                    "energy."},
            {"text": "The acid was warmer than the alkali before they were "
                     "mixed", "correct": False,
             "why": "Both were at 20 °C. The rise happened after mixing, and "
                    "the reaction is the only thing that changed."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e02",
        "band": "easier",
        "text": "Magnesium ribbon has to be lit with a Bunsen before it will "
                "burn. Is burning magnesium exothermic?",
        "options": [
            {"text": "No, because energy had to be supplied to get it going",
             "correct": False,
             "why": "Supplying a start is not the same as taking energy in "
                    "overall. What decides it is the balance."},
            {"text": "Yes, because far more energy comes out than the flame "
                     "put in", "correct": True},
            {"text": "No, because the Bunsen is the real source of the heat "
                     "and light", "correct": False,
             "why": "Take the Bunsen away and the magnesium keeps burning. "
                    "The energy is coming out of the reaction."},
            {"text": "Only after the flame is removed, when it stops taking "
                     "energy in", "correct": False,
             "why": "It is exothermic throughout. The flame only gets the "
                    "first few particles going."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e03",
        "band": "easier",
        "text": "Where does the thermometer have to be to test whether a "
                "reaction is exothermic?",
        "options": [
            {"text": "In the flame that started the reaction", "correct": False,
             "why": "The flame is the starter, not the reaction. Its "
                    "temperature says nothing about what the reaction did."},
            {"text": "In the air just above the beaker", "correct": False,
             "why": "Some energy does reach the air, but most of it goes into "
                    "the mixture, which is what you are trying to measure."},
            {"text": "In the mixture, because exothermic is defined by the "
                     "surroundings getting warmer", "correct": True},
            {"text": "Inside the reacting particles themselves", "correct": False,
             "why": "Nothing can put a thermometer inside a particle, and "
                    "nothing needs to. The definition is about the "
                    "surroundings."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e04",
        "band": "easier",
        "text": "A firework gives out light, heat and sound. Where did that "
                "energy come from?",
        "options": [
            {"text": "It was created by the reaction, which is what makes "
                     "fireworks impressive", "correct": False,
             "why": "Energy is never created. The reaction released "
                    "something that was already there."},
            {"text": "It came from the match or the fuse that lit it",
             "correct": False,
             "why": "The fuse supplies a tiny amount to get things started. "
                    "It is nowhere near what comes out."},
            {"text": "It came from the air, which supplies oxygen and energy "
                     "together", "correct": False,
             "why": "The air supplies oxygen, which is a reactant. Oxygen is "
                    "matter, not a delivery of energy."},
            {"text": "It was stored in the chemicals when the firework was "
                     "made", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-02-s01",
        "band": "standard",
        "text": "A camping stove needs a spark to light and then burns "
                "steadily for an hour. What does that show about the energy?",
        "options": [
            {"text": "The spark supplies the energy and the gas simply "
                     "carries it around the flame", "correct": False,
             "why": "The spark stops the instant it fires. The flame goes on "
                    "for an hour, which the spark cannot pay for."},
            {"text": "The reaction gives out far more than the spark put in, "
                     "which is why it keeps going", "correct": True},
            {"text": "The reaction is endothermic while lighting and "
                     "exothermic once it settles down", "correct": False,
             "why": "It is exothermic throughout. Needing a start is a "
                    "property of getting going, not of the energy account."},
            {"text": "The energy is being created continuously as long as the "
                     "gas keeps flowing", "correct": False,
             "why": "Nothing is created. It was stored in the gas, and when "
                    "the cylinder is empty the flame stops."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s02",
        "band": "standard",
        "text": "A reusable hand warmer reaches 50 °C, goes cold after an "
                "hour, and can be reset by boiling it in a pan. What does the "
                "boiling actually do?",
        "options": [
            {"text": "It sterilises the pouch so the reaction can be run "
                     "again cleanly", "correct": False,
             "why": "The pouch is sealed and nothing gets into it. Boiling is "
                    "doing something to the contents, not to the outside."},
            {"text": "It heats the pouch up so that the warmth can be stored "
                     "and released later", "correct": False,
             "why": "The stored heat would leak away in minutes. What is "
                    "stored is the arrangement of the particles, not the "
                    "warmth."},
            {"text": "It supplies the energy the change gave out, running the "
                     "change backwards so it can be used again",
             "correct": True},
            {"text": "It dissolves the metal disc so it can be snapped a "
                     "second time", "correct": False,
             "why": "The disc is only a trigger. What has to be undone is the "
                    "crystallisation of the sodium ethanoate."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s03",
        "band": "standard",
        "text": "A disposable hand warmer is a packet of iron powder, salt "
                "and sawdust that warms up when the packet is opened. Why "
                "does opening it start the reaction?",
        "options": [
            {"text": "Because the sawdust starts smouldering in the air, and "
                     "that is what warms the packet", "correct": False,
             "why": "The sawdust never burns — the packet would be ruined if "
                    "it did. It is there to hold everything loosely in "
                    "contact with the air."},
            {"text": "Because the salt only starts working once it is exposed "
                     "to the air", "correct": False,
             "why": "The salt speeds the rusting up but it is not what the "
                    "iron reacts with. The reactant that was missing is "
                    "oxygen."},
            {"text": "Because opening the packet lets warm room air in and "
                     "the reaction needs that heat", "correct": False,
             "why": "The room air is at room temperature and supplies no "
                    "heat. What it supplies is oxygen."},
            {"text": "Because oxygen from the air is a reactant, and rusting "
                     "the iron releases energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s04",
        "band": "standard",
        "text": "Why is an exothermic reaction useful in a power station but "
                "an endothermic one would not be?",
        "options": [
            {"text": "Because energy given out can be used to do something, "
                     "and energy taken in gives you nothing back",
             "correct": True},
            {"text": "Because endothermic reactions are too slow to be worth "
                     "running at that scale", "correct": False,
             "why": "Speed is not the problem. The direction of the transfer "
                    "is: you would have to keep supplying energy."},
            {"text": "Because exothermic reactions are the only kind that "
                     "make a gas to turn a turbine", "correct": False,
             "why": "Plenty of endothermic changes make gases. What matters "
                    "is which way the energy goes."},
            {"text": "Because endothermic reactions break the law of "
                     "conservation of energy at large scales",
             "correct": False,
             "why": "They break nothing. The energy is stored in the "
                    "products, which is exactly why you get nothing back."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-02-h01",
        "band": "harder",
        "text": "A forest fire needs a lightning strike to begin but then "
                "burns for days. Which statement describes the energy "
                "correctly?",
        "options": [
            {"text": "The lightning supplies the energy and the trees release "
                     "it slowly over the following days", "correct": False,
             "why": "A single strike lasts a fraction of a second. It cannot "
                    "pay for days of burning."},
            {"text": "The fire is endothermic while it spreads and exothermic "
                     "only where it is already alight", "correct": False,
             "why": "Combustion is exothermic everywhere it happens. Spread "
                    "is a fire starting new fires, not a different reaction."},
            {"text": "The lightning starts it, and the energy released then "
                     "starts the next tree, and the next", "correct": True},
            {"text": "The heat of the day is what keeps it going, which is "
                     "why fires spread fastest in summer", "correct": False,
             "why": "Dry conditions do help a fire spread, but the energy "
                    "keeping it going comes out of the wood."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h02",
        "band": "harder",
        "text": "A compost heap holds its middle at 60 °C right through a "
                "frost, with nothing plugged in. Which explanation is "
                "correct?",
        "options": [
            {"text": "Rotting plants create heat, which is why a heap has to "
                     "be turned to let it escape", "correct": False,
             "why": "Nothing is created. The energy was stored in the plant "
                    "material by photosynthesis before it was cut."},
            {"text": "The heap traps sunlight during the day and releases it "
                     "through the night", "correct": False,
             "why": "A heap holds 60 °C in the dark and under snow. Sunlight "
                    "cannot account for that."},
            {"text": "The rotting is endothermic, and taking energy in from "
                     "the frost is what warms the middle", "correct": False,
             "why": "Taking energy in would make the heap colder, not "
                    "warmer. Respiration gives energy out."},
            {"text": "Bacteria are respiring the plant material, which is "
                     "exothermic, and the heap insulates itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h03",
        "band": "harder",
        "text": "Rusting is exothermic, yet an iron gate rusting in a garden "
                "never feels warm. Why not?",
        "options": [
            {"text": "Because the energy released is spread over years, so at "
                     "any moment there is almost none of it", "correct": True},
            {"text": "Because rusting outdoors is endothermic, and only "
                     "rusting in a sealed packet gives energy out",
             "correct": False,
             "why": "The reaction is the same reaction. Salt and a packet "
                    "make it faster, not different."},
            {"text": "Because the rain washes the heat away as fast as the "
                     "reaction produces it", "correct": False,
             "why": "A dry gate in a dry garden still does not feel warm. "
                    "Rate is what explains it."},
            {"text": "Because iron is a good conductor, so any heat is "
                     "carried into the ground instantly", "correct": False,
             "why": "Conduction would spread it, but the real reason is that "
                    "there is very little of it per second to spread."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h04",
        "band": "harder",
        "text": "A company designs a self-heating food can and claims it "
                "needs no energy source of any kind. What is wrong with the "
                "claim?",
        "options": [
            {"text": "Nothing — an exothermic reaction genuinely needs no "
                     "energy source to run", "correct": False,
             "why": "It needs no source while it runs, but the energy it "
                    "gives out was put into its chemicals when they were "
                    "made."},
            {"text": "The chemicals inside ARE the energy source; the energy "
                     "was stored in them when they were manufactured",
             "correct": True},
            {"text": "It is wrong because every reaction needs a spark, and a "
                     "spark needs a battery", "correct": False,
             "why": "Plenty of reactions start without a spark — a hand "
                    "warmer needs only a snap. The flaw is about storage, "
                    "not starting."},
            {"text": "It is wrong because heating food always needs "
                     "electricity somewhere in the chain", "correct": False,
             "why": "It genuinely does not. A chemical reaction can heat food "
                    "with nothing plugged in; the energy still had to be put "
                    "in somewhere first."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-02-e05",
        "band": "easier",
        "text": "What does exothermic mean?",
        "options": [
            {"text": "A change that gets hot enough to burn whatever it is "
                     "touching, which is why the word is used of fires and "
                     "not of a beaker that warms by a few degrees",
             "correct": False,
             "why": "A rise of seven degrees in a beaker is exothermic. How "
                    "hot it gets is not part of the definition"},
            {"text": "A change that transfers energy out to its surroundings",
             "correct": True},
            {"text": "A change that takes energy in from its surroundings",
             "correct": False,
             "why": "That is endothermic — the next lesson"},
            {"text": "A change that needs a flame to start it",
             "correct": False,
             "why": "A hand warmer needs no flame and is exothermic"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e06",
        "band": "easier",
        "text": "What are the SURROUNDINGS of a reaction?",
        "options": [
            {"text": "The room the experiment is being carried out in",
             "correct": False,
             "why": "The beaker and the water count as surroundings too. "
                    "Everything but the reacting substances does"},
            {"text": "The reactants and products together",
             "correct": False,
             "why": "Those ARE the reaction. The surroundings are what is "
                    "left"},
            {"text": "Everything that is not the reaction itself — the water, "
                     "the beaker, the bench and the air",
             "correct": True},
            {"text": "The flame under the beaker",
             "correct": False,
             "why": "A flame is one thing that can be part of the "
                    "surroundings. It is not what the word means"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e07",
        "band": "easier",
        "text": "Which of these is exothermic?",
        "options": [
            {"text": "Copper carbonate decomposing in a hot tube",
             "correct": False,
             "why": "That takes energy in, which is why it stops when the "
                    "flame comes off"},
            {"text": "Photosynthesis",
             "correct": False,
             "why": "It takes energy in from sunlight. It is the largest "
                    "endothermic process on Earth"},
            {"text": "Ammonium nitrate dissolving in water, which is why a "
                     "cold pack drops close to freezing within a few seconds "
                     "of being squeezed",
             "correct": False,
             "why": "It drops because the change takes energy IN. That is "
                    "endothermic"},
            {"text": "A metal reacting with an acid",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e08",
        "band": "easier",
        "text": "A hand warmer gets hot with nothing plugged in. Where did "
                "the energy come from?",
        "options": [
            {"text": "From the chemical store in the substances inside it",
             "correct": True},
            {"text": "It was created by the reaction, which is what a "
                     "chemical change does when the substances in it come "
                     "into contact for the first time",
             "correct": False,
             "why": "No reaction creates energy. It was stored in the "
                    "chemicals beforehand"},
            {"text": "From the air, which is warmer than the packet",
             "correct": False,
             "why": "The packet ends up far warmer than the air, so the air "
                    "cannot be the source"},
            {"text": "From the friction of shaking it",
             "correct": False,
             "why": "Shaking helps the air reach the powder. It supplies "
                    "almost none of the energy"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e09",
        "band": "easier",
        "text": "What is neutralisation, and is it exothermic?",
        "options": [
            {"text": "An acid being watered down until its pH reaches 7, and "
                     "no — diluting takes energy in rather than giving it "
                     "out",
             "correct": False,
             "why": "Diluting is not neutralisation, and neutralisation warms "
                    "the beaker"},
            {"text": "An acid reacting with an alkali, and yes",
             "correct": True},
            {"text": "An acid reacting with an alkali, and no",
             "correct": False,
             "why": "Right about what it is. The thermometer rises, so it "
                    "gives energy out"},
            {"text": "An acid reacting with a metal, and yes",
             "correct": False,
             "why": "Right about the energy and wrong about the reaction. A "
                    "metal and an acid give hydrogen"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e10",
        "band": "easier",
        "text": "What does the chemical store of a substance mean?",
        "options": [
            {"text": "The heat a substance is holding at the moment, which is "
                     "why a hot substance has a larger store than a cold one "
                     "of the same kind",
             "correct": False,
             "why": "That is thermal energy and depends on temperature. The "
                    "chemical store is in the arrangement"},
            {"text": "The cupboard the chemicals are kept in",
             "correct": False,
             "why": "The word is being used in the scientific sense of an "
                    "energy store"},
            {"text": "Energy held in the way the substance's particles are "
                     "arranged",
             "correct": True},
            {"text": "How much of the substance there is",
             "correct": False,
             "why": "The amount decides how much energy in total. The store "
                    "is what kind of energy it is"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e11",
        "band": "easier",
        "text": "What happens to the TOTAL energy in the universe during an "
                "exothermic reaction?",
        "options": [
            {"text": "It increases, because the reaction has released energy "
                     "into the room that was not there in that form before "
                     "the two substances were mixed",
             "correct": False,
             "why": "It was there, in the chemical store. Changing store is "
                    "not creating"},
            {"text": "It decreases, because the chemicals have used some of "
                     "it up",
             "correct": False,
             "why": "Nothing is used up in the sense of ceasing to exist. The "
                    "total never moves"},
            {"text": "It increases while the reaction runs and then falls "
                     "back",
             "correct": False,
             "why": "The total is constant throughout. Only where the energy "
                    "sits changes"},
            {"text": "Nothing — it is moved from one store to another",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e12",
        "band": "easier",
        "text": "Is every combustion exothermic?",
        "options": [
            {"text": "Yes",
             "correct": True},
            {"text": "No — a fuel that has to be lit takes energy in from the "
                     "match, so burning is endothermic until the flame is "
                     "established",
             "correct": False,
             "why": "Needing a start is not taking energy in overall. Far "
                    "more comes out than the match put in"},
            {"text": "Only if it burns with a visible flame",
             "correct": False,
             "why": "Slow oxidation gives energy out too. Combustion always "
                    "does"},
            {"text": "Only for fuels containing carbon",
             "correct": False,
             "why": "Hydrogen contains none and burning it releases a great "
                    "deal of energy"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e13",
        "band": "easier",
        "text": "What happens to the temperature of the surroundings when "
                "respiration takes place in a living thing?",
        "options": [
            {"text": "It falls, because the reaction needs energy to build "
                     "the substances the body uses",
             "correct": False,
             "why": "Respiration RELEASES energy, which is why you are warm. "
                    "Building is a different process"},
            {"text": "It rises",
             "correct": True},
            {"text": "It stays exactly the same",
             "correct": False,
             "why": "Then a body would be at room temperature. Yours is "
                    "not"},
            {"text": "It depends on what has been eaten",
             "correct": False,
             "why": "What is eaten changes how much energy, never the "
                    "direction"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c7-02-s05",
        "band": "standard",
        "text": "A self-heating can uses calcium oxide and water. Why does "
                "that make it a hazard on a building site?",
        "options": [
            {"text": "Because the reaction gives off a gas that is dangerous "
                     "to breathe in a confined space such as the inside of a "
                     "partly built structure",
             "correct": False,
             "why": "No gas is produced. The hazard is the energy released "
                    "where there is water"},
            {"text": "Because quicklime dust in a wet eye releases its energy "
                     "exactly where you would least want it",
             "correct": True},
            {"text": "Because calcium oxide is radioactive",
             "correct": False,
             "why": "It is not radioactive at all. It is the heat of the "
                    "reaction that harms"},
            {"text": "Because it is heavy enough to fall from scaffolding",
             "correct": False,
             "why": "That would be true of any bag of powder. The chemical "
                    "hazard is what makes quicklime particular"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s06",
        "band": "standard",
        "text": "A student mixes acid and alkali, the thermometer rises by "
                "7 °C, and half an hour later the beaker is back at room "
                "temperature. Has the energy been destroyed?",
        "options": [
            {"text": "Yes — the reaction has finished, so the energy it made "
                     "has gone with it",
             "correct": False,
             "why": "Energy is never destroyed. The warm beaker has passed it "
                    "to the room"},
            {"text": "No — it has gone back into the chemicals",
             "correct": False,
             "why": "The reaction does not run backwards on its own. The "
                    "energy has spread into the surroundings"},
            {"text": "No — the beaker has passed it on to the room",
             "correct": True},
            {"text": "Yes — the thermometer is back where it started, so "
                     "nothing is left",
             "correct": False,
             "why": "The reading returning does not mean the energy vanished. "
                    "It is now spread through a whole room"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s07",
        "band": "standard",
        "text": "A disposable hand warmer works only once, and a reusable one "
                "can be boiled and used again. What does the boiling supply?",
        "options": [
            {"text": "Fresh chemicals, carried in by the boiling water",
             "correct": False,
             "why": "Nothing crosses the seal. The same chemicals are used "
                    "over and over"},
            {"text": "Oxygen, which the reaction needs",
             "correct": False,
             "why": "That is the DISPOSABLE kind, which rusts iron and cannot "
                    "be reset. The reusable one is sealed"},
            {"text": "Water, which had evaporated out of the pack",
             "correct": False,
             "why": "The pack is sealed and loses nothing. What it needs back "
                    "is energy"},
            {"text": "The energy the change gave out, so the change can be "
                     "run backwards",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s08",
        "band": "standard",
        "text": "A neutralisation warms a beaker by 7 °C. It is run again "
                "with twice the volume of BOTH solutions. What happens to the "
                "temperature rise?",
        "options": [
            {"text": "It stays at about 7 °C",
             "correct": True},
            {"text": "It doubles to about 14 °C, because twice as much of "
                     "each solution means twice as much reaction and so twice "
                     "as much energy released into the beaker",
             "correct": False,
             "why": "Twice the energy is released into twice as much liquid "
                    "to warm. The two double together"},
            {"text": "It halves to about 3.5 °C",
             "correct": False,
             "why": "Nothing has been diluted. Both the energy and the amount "
                    "being warmed have gone up"},
            {"text": "It cannot be predicted",
             "correct": False,
             "why": "It can: doubling both sides of the comparison leaves the "
                    "rise where it was"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s09",
        "band": "standard",
        "text": "A student wants to compare how much energy two different "
                "reactions release. What must be kept the same?",
        "options": [
            {"text": "The temperature the mixture reaches, so that both "
                     "reactions are being judged at the same point on the "
                     "thermometer as each other",
             "correct": False,
             "why": "The temperature reached is the RESULT. Fixing it would "
                    "remove the thing being measured"},
            {"text": "The volumes, the concentrations and the container",
             "correct": True},
            {"text": "The time each reaction is left to run",
             "correct": False,
             "why": "Each is read at its own peak. A fixed clock would catch "
                    "one of them early"},
            {"text": "Nothing — the reactions are different, so nothing can "
                     "be held constant",
             "correct": False,
             "why": "Everything except the reaction itself can and should be "
                    "held constant. That is what makes it a comparison"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s10",
        "band": "standard",
        "text": "Two beakers hold the same acid at 20 °C. Alkali is added to "
                "one and water to the other. What do the thermometers do?",
        "options": [
            {"text": "Both rise, because adding anything to an acid releases "
                     "energy as the two liquids mix together in the beaker",
             "correct": False,
             "why": "Mixing releases very little. What warms the first beaker "
                    "is a REACTION"},
            {"text": "Both stay the same",
             "correct": False,
             "why": "The neutralisation is exothermic and shows clearly on a "
                    "thermometer"},
            {"text": "The alkali one rises and the water one barely moves",
             "correct": True},
            {"text": "The water one rises and the alkali one falls",
             "correct": False,
             "why": "Exactly the wrong way round. Neutralisation is the "
                    "exothermic one here"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s11",
        "band": "standard",
        "text": "A compost heap holds its middle at 60 °C through a frost. "
                "Which two things are needed for that?",
        "options": [
            {"text": "Sunlight falling on the top of the heap, and a dark "
                     "surface layer that absorbs it well enough to carry the "
                     "middle through a night below freezing",
             "correct": False,
             "why": "It holds 60 °C at night and under snow. The energy is "
                    "coming from inside"},
            {"text": "A large surface area and a dry interior",
             "correct": False,
             "why": "A large surface would lose heat faster, and a heap needs "
                    "to be damp to work"},
            {"text": "Nothing but the frost, which insulates the heap",
             "correct": False,
             "why": "Frost does not supply energy. Something inside is "
                    "releasing it"},
            {"text": "An exothermic process inside it, and enough material "
                     "around it to hold the energy in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s12",
        "band": "standard",
        "text": "A firework is described as a container for energy. When was "
                "that energy put into it?",
        "options": [
            {"text": "When it was manufactured",
             "correct": True},
            {"text": "When the fuse was lit, since that is the moment at "
                     "which the chemicals inside it first begin to hold any "
                     "energy at all",
             "correct": False,
             "why": "Lighting it RELEASES what was already there. The fuse "
                    "supplies almost nothing"},
            {"text": "As it flies upwards",
             "correct": False,
             "why": "Flying upwards is the firework SPENDING energy rather "
                    "than gaining it"},
            {"text": "It was never put in — the reaction creates it",
             "correct": False,
             "why": "Nothing creates energy. A reaction moves it between "
                    "stores"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s13",
        "band": "standard",
        "text": "Which of these tells you a change is exothermic, without any "
                "assumptions?",
        "options": [
            {"text": "It produces a gas",
             "correct": False,
             "why": "Plenty of endothermic changes do — a decomposing "
                    "carbonate for one"},
            {"text": "A thermometer in the mixture reads higher than it did "
                     "at the start",
             "correct": True},
            {"text": "It happens quickly",
             "correct": False,
             "why": "Speed and energy direction are separate. A cold pack "
                    "works in seconds"},
            {"text": "It needed heating to start, so energy has passed into "
                     "it",
             "correct": False,
             "why": "Needing a start says nothing about the direction "
                    "overall. Burning methane needs a spark"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-02-h05",
        "band": "harder",
        "text": "A badly managed hay pile can catch fire on its own. Which "
                "chain of reasoning explains it?",
        "options": [
            {"text": "Hay dries out in a large pile, and dry hay is easily "
                     "set alight",
             "correct": False,
             "why": "It happens in the dark and in the middle of a pile. What "
                    "raises the temperature is respiration"},
            {"text": "Bacteria respire exothermically, the pile insulates "
                     "itself, and the temperature climbs until something "
                     "ignites",
             "correct": True},
            {"text": "The weight of the pile compresses the hay until "
                     "friction sets it alight",
             "correct": False,
             "why": "Compression heats a gas, not a haystack. The heat here "
                    "is chemical"},
            {"text": "Damp hay decomposes endothermically, and the cold "
                     "brittle stalks then snap and spark",
             "correct": False,
             "why": "Endothermic would COOL the pile. And nothing sparks"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h06",
        "band": "harder",
        "text": "A company advertises a self-heating can as needing no energy "
                "source at all. What is the honest correction?",
        "options": [
            {"text": "The can does need an energy source, and it is the air, "
                     "which supplies the oxygen that the reaction inside the "
                     "compartment burns to warm the drink",
             "correct": False,
             "why": "The calcium oxide reaction needs no air. And air would "
                    "be a reactant rather than an energy source"},
            {"text": "There is no correction — a chemical reaction genuinely "
                     "needs no source",
             "correct": False,
             "why": "Every joule out of it was in the chemicals first. Energy "
                    "is never made"},
            {"text": "The chemicals inside are the energy source, and the "
                     "energy was put into them when they were made",
             "correct": True},
            {"text": "The user supplies it by squeezing the can",
             "correct": False,
             "why": "Squeezing breaks a seal. It supplies an amount too small "
                    "to matter"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h07",
        "band": "harder",
        "text": "Rusting is exothermic, and an iron gate rusting over ten "
                "years never feels warm. What does that tell you about the "
                "word exothermic?",
        "options": [
            {"text": "That rusting is exothermic only in a laboratory, where "
                     "it can be made to run fast enough for the energy to be "
                     "detected on a thermometer",
             "correct": False,
             "why": "It is exothermic on the gate as well. The energy is "
                    "simply spread over years"},
            {"text": "That the word only applies to reactions that give out "
                     "enough energy to be felt",
             "correct": False,
             "why": "A hand warmer and a rusting gate are both exothermic. "
                    "One is felt and one is not"},
            {"text": "That rusting must really be endothermic",
             "correct": False,
             "why": "It releases energy — which is exactly what a disposable "
                    "hand warmer uses"},
            {"text": "That it describes the DIRECTION of the transfer and not "
                     "how fast it happens",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h08",
        "band": "harder",
        "text": "A forest fire needs a lightning strike and then burns for "
                "days. Where does each tree's energy come from?",
        "options": [
            {"text": "From the previous tree burning, which released enough "
                     "to start it — the lightning only started the first",
             "correct": True},
            {"text": "From the lightning strike, carried along the branches",
             "correct": False,
             "why": "Nothing of the strike travels. Each tree is lit by the "
                    "energy the one before it released"},
            {"text": "From the sun, which is heating the forest at the same "
                     "time",
             "correct": False,
             "why": "Fires burn through the night. The energy is chemical, "
                    "and it was stored by the sun long ago"},
            {"text": "From the wind, which supplies the energy as well as the "
                     "oxygen",
             "correct": False,
             "why": "Wind supplies oxygen and carries embers. It brings "
                    "almost no energy of its own"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h09",
        "band": "harder",
        "text": "A designer wants a self-heating can that reaches 200 °C so "
                "the food is really hot. Why is that a bad specification?",
        "options": [
            {"text": "Because no reaction releases enough energy to reach 200 "
                     "°C",
             "correct": False,
             "why": "Plenty do — thermite reaches 2500 °C. The problem is "
                    "safety rather than possibility"},
            {"text": "Because a can that hot would burn the user, and the "
                     "pressure inside it could burst it",
             "correct": True},
            {"text": "Because food cannot be heated above 100 °C",
             "correct": False,
             "why": "An oven does it every day. The objection is about the "
                    "can and the person holding it"},
            {"text": "Because an exothermic reaction cannot be controlled",
             "correct": False,
             "why": "They are controlled constantly — that is what a boiler "
                    "is. The specification is simply too hot"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h10",
        "band": "harder",
        "text": "A student says an exothermic reaction creates energy, "
                "because the beaker is warmer at the end than at the start. "
                "What is the precise correction?",
        "options": [
            {"text": "The beaker is not really warmer, because the "
                     "thermometer reads the reaction",
             "correct": False,
             "why": "The beaker genuinely is warmer, and a thermometer in the "
                    "mixture is exactly the right test"},
            {"text": "The energy came from the air, so nothing was created",
             "correct": False,
             "why": "The air is being warmed rather than drained. The source "
                    "is the chemicals"},
            {"text": "The energy moved out of a chemical store and into the "
                     "surroundings — the total is unchanged",
             "correct": True},
            {"text": "The energy was created and then destroyed again as the "
                     "beaker cooled",
             "correct": False,
             "why": "Neither happened. It was moved twice — into the "
                    "surroundings, then into the room"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h11",
        "band": "harder",
        "text": "A disposable hand warmer contains iron powder, salt and "
                "sawdust, and starts when the packet is opened. Explain the "
                "part each plays.",
        "options": [
            {"text": "The iron rusts, the salt reacts with it, and the "
                     "sawdust cools the packet",
             "correct": False,
             "why": "The salt does not react — it only speeds the rusting. "
                    "The sawdust holds moisture and spreads the powder"},
            {"text": "The salt rusts, the iron holds the heat, and the "
                     "sawdust supplies the oxygen",
             "correct": False,
             "why": "Salt does not rust and sawdust supplies no oxygen. The "
                    "air does"},
            {"text": "All three react together, which is why all three have "
                     "to be present",
             "correct": False,
             "why": "Only the iron reacts. The other two are there to make "
                    "that reaction go at a useful rate"},
            {"text": "The iron rusts and releases the energy, the salt speeds "
                     "the rusting up, and opening the packet lets the oxygen "
                     "in",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h12",
        "band": "harder",
        "text": "Why does a reaction needing a spark not count as taking "
                "energy in?",
        "options": [
            {"text": "Because the spark only starts it, and the reaction then "
                     "releases far more than the spark supplied",
             "correct": True},
            {"text": "Because a spark carries no energy at all, being "
                     "electrical",
             "correct": False,
             "why": "A spark does carry energy, and a small amount of it. The "
                    "point is the balance"},
            {"text": "Because the spark is not part of the reaction",
             "correct": False,
             "why": "It is what gets the reaction going, so it is very much "
                    "part of the story. What matters is the total"},
            {"text": "Because a spark is a condition rather than a reactant",
             "correct": False,
             "why": "True about equations, and it is not what decides the "
                    "energy direction. The size of the transfer is"},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h13",
        "band": "harder",
        "text": "Two exothermic reactions release the same total energy, one "
                "over a second and one over a year. How would you tell that "
                "from thermometers?",
        "options": [
            {"text": "Both would show the same rise, because the same total "
                     "energy has been transferred and a thermometer reads the "
                     "total",
             "correct": False,
             "why": "A thermometer reads temperature at a moment. Energy "
                    "spread over a year leaks away as fast as it arrives"},
            {"text": "The fast one shows a large rise and the slow one barely "
                     "moves the reading at all",
             "correct": True},
            {"text": "The slow one shows the larger rise, because it has "
                     "longer to build up",
             "correct": False,
             "why": "Nothing builds up. Heat escapes to the room as it is "
                    "released"},
            {"text": "Neither shows anything, because the totals are equal",
             "correct": False,
             "why": "The fast one shows a great deal. Equal totals do not "
                    "mean equal readings"},
        ],
        "figure": None,
    },
]
