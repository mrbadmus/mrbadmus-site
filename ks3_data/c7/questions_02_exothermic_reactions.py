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
            {"text": "The cupboard that the chemicals are kept in, out of the "
                     "way and locked up",
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
            {"text": "Because it is heavy enough to do real damage to anybody "
                     "underneath if a bag of it falls from scaffolding",
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
            {"text": "Nothing but the frost outside, which insulates the heap "
                     "and stops the middle of it cooling down",
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
                     "needs no source of energy from anywhere else at all",
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
            {"text": "The slow one shows the larger rise, because it has a "
                     "great deal longer in which to build up",
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

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "c7-02-e14",
        "band": "easier",
        "text": "What is combustion?",
        "options": [
            {"text": "A substance reacting with oxygen, which always "
                     "releases energy",
             "correct": True},
            {"text": "A substance getting hot enough to melt and then to "
                     "boil away", "correct": False,
             "why": "Melting and boiling are changes of state. No new "
                    "substance is made, and nothing needs oxygen."},
            {"text": "A substance being broken down into simpler substances by strongly heating it", "correct": False,
             "why": "That is thermal decomposition, and it takes energy in "
                    "rather than giving it out."},
            {"text": "A substance giving off light while staying the same "
                     "substance",
             "correct": False,
             "why": "The substance is changed — it has reacted with oxygen "
                    "to make new products."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e15",
        "band": "easier",
        "text": "A reusable hand warmer works by sodium ethanoate "
                "crystallising out of a solution. Is that a chemical "
                "reaction?",
        "options": [
            {"text": "Yes, because a solid appears in the pouch where there was none before it was snapped", "correct": False,
             "why": "A solid appearing from a solution is a change of state, "
                    "not a new substance being made."},
            {"text": "No — it is a change of state, but it still gives "
                     "energy out", "correct": True},
            {"text": "Yes, because only a reaction can release energy",
             "correct": False,
             "why": "Freezing and condensing release energy too, and neither "
                    "is a reaction."},
            {"text": "No, and that means it is not exothermic either",
             "correct": False,
             "why": "Exothermic describes any change that gives energy out. "
                    "The warmer plainly does."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e16",
        "band": "easier",
        "text": "A Bunsen flame is held against a coil of magnesium ribbon "
                "to get it burning. What is the flame supplying?",
        "options": [
            {"text": "The oxygen the magnesium reacts with, which the air "
                     "around it cannot provide", "correct": False,
             "why": "The oxygen comes from the air. A Bunsen supplies no "
                    "oxygen to the ribbon at all."},
            {"text": "The chemical store the magnesium later releases",
             "correct": False,
             "why": "That store was in the magnesium before anybody lit "
                    "anything. The flame cannot fill it."},
            {"text": "Most of the energy the reaction then gives out",
             "correct": False,
             "why": "The Bunsen is turned away once the ribbon catches, and "
                    "far more energy comes out afterwards."},
            {"text": "The energy needed to get the reaction started",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e17",
        "band": "easier",
        "text": "Why is burning magnesium never watched directly with "
                "unprotected eyes?",
        "options": [
            {"text": "Because the smoke it gives off is poisonous to breathe "
                     "in", "correct": False,
             "why": "The hazard the teacher guards against here is the "
                    "light, and the demonstration is watched rather than "
                    "inhaled."},
            {"text": "Because the metal can spit pieces as far as the front "
                     "bench", "correct": False,
             "why": "A coil of ribbon does not spit. It is the brightness "
                    "that makes it a demonstration rather than a class "
                    "practical."},
            {"text": "Because it always gives out so much energy that the "
                     "light is blinding", "correct": True},
            {"text": "Because the reaction takes energy in from anything nearby, including a person's eyes", "correct": False,
             "why": "It gives energy out, not in. Combustion is exothermic."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "c7-02-s14",
        "band": "standard",
        "text": "A sports hall with the heating switched off gets noticeably "
                "warmer once two hundred people are inside it. What is doing "
                "the heating?",
        "options": [
            {"text": "Respiration in their cells, which is exothermic",
             "correct": True},
            {"text": "The friction of that many people moving about", "correct": False,
             "why": "A hall full of people sitting still warms up too, so "
                    "movement is not what does it."},
            {"text": "Their breath, which is warmer than the air outside", "correct": False,
             "why": "Warm breath is the result rather than the cause — the "
                    "energy came from respiration in the first place."},
            {"text": "The lights, which have to be switched on brighter when there are more people in the hall", "correct": False,
             "why": "The lighting does not change with the number of people, "
                    "and an unlit hall still warms up."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s15",
        "band": "standard",
        "text": "A student holds a thin glass beaker while an acid and an "
                "alkali react inside it, and the outside of the glass gets "
                "warm. Trace the path the energy took.",
        "options": [
            {"text": "Out of the student's hand, into the glass and then "
                     "into the mixture", "correct": False,
             "why": "That is the direction energy travels when you warm "
                    "something up. Here the beaker is getting warmer, not "
                    "the hand."},
            {"text": "Out of the chemicals, into the mixture, through the "
                     "glass, into the hand", "correct": True},
            {"text": "Out of the warm air in the room, in through the glass and then into the reacting mixture", "correct": False,
             "why": "The room is not losing energy here. The rise is coming "
                    "from the reaction itself."},
            {"text": "Created in the mixture, then shared between the glass "
                     "and the hand", "correct": False,
             "why": "Nothing creates energy. It was stored in the chemicals "
                    "before they were mixed."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s16",
        "band": "standard",
        "text": "A reusable hand warmer stays hot for about an hour and then "
                "goes cold. Why does it stop giving energy out?",
        "options": [
            {"text": "Because the pouch has cooled the chemicals down too far for the change to carry on running", "correct": False,
             "why": "The pouch is the warmest thing in the pocket while it "
                    "is working. Nothing has cooled it."},
            {"text": "Because the energy it stored has been destroyed by the "
                     "time the hour is up", "correct": False,
             "why": "Energy is never destroyed. It has been transferred to "
                    "the pocket, the hand and the air."},
            {"text": "Because the change has finished, so there is nothing "
                     "left to release its energy", "correct": True},
            {"text": "Because the air around it has warmed up as much as it "
                     "possibly can", "correct": False,
             "why": "The air around a pocket is nowhere near as warm as the "
                    "pouch was, and the pouch stops anyway."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s17",
        "band": "standard",
        "text": "After an exothermic reaction the products hold less energy "
                "in their chemical store than the reactants did. Where is "
                "the difference?",
        "options": [
            {"text": "It was destroyed as the reactants were used up",
             "correct": False,
             "why": "Energy is never destroyed. The total before and after "
                    "is the same."},
            {"text": "It is hidden inside the products, in a place where no thermometer can read it", "correct": False,
             "why": "The products have LESS than the reactants had. What "
                    "they lost has gone outside them."},
            {"text": "It was not there to begin with — the store fills as "
                     "the reaction runs", "correct": False,
             "why": "The store was full before the reaction started. That is "
                    "why the reaction had something to release."},
            {"text": "In the surroundings — that is always where the "
                     "difference goes", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ────────────────────────────────────────
    {
        "id": "c7-02-h14",
        "band": "harder",
        "text": "A hand warmer and a battery both give out energy with "
                "nothing plugged in. What do they have in common, and what "
                "is different?",
        "options": [
            {"text": "Both hold a store put in when they were made; one "
                     "gives heat and one electricity", "correct": True},
            {"text": "Both make their own energy as they run; one makes heat "
                     "and one makes electricity", "correct": False,
             "why": "Neither makes energy. Both release a store that was "
                    "filled before you bought them."},
            {"text": "Both take energy in from the air around them; one then releases it as heat and the other as electricity", "correct": False,
             "why": "A change that took energy in from the air would leave "
                    "the room colder, and neither of these does."},
            {"text": "Both hold a store put in when they were made, and "
                     "both release it as heat", "correct": False,
             "why": "A battery's whole purpose is releasing it as "
                    "electricity. Heat from a battery is the waste."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h15",
        "band": "harder",
        "text": "Two designs for a self-heating can release the same total "
                "energy, one over ten seconds and one over three minutes. "
                "Why is the slower design the safer product?",
        "options": [
            {"text": "Because a slower reaction releases less energy "
                     "altogether, so less can go wrong", "correct": False,
             "why": "The totals are stated to be equal. Slower is not "
                    "smaller."},
            {"text": "Because the same energy released in ten seconds would "
                     "reach a far higher temperature", "correct": True},
            {"text": "Because a slow reaction can be stopped part-way through if the user decides they no longer want it",
             "correct": False,
             "why": "Neither design can be halted once it has started, and "
                    "that is not what makes one safer."},
            {"text": "Because a slow reaction cannot build up any pressure "
                     "inside a sealed can", "correct": False,
             "why": "Pressure depends on what the reaction makes and how hot "
                    "it gets, and a slow one left to run could reach the "
                    "same place."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h16",
        "band": "harder",
        "text": "A student puts a thermometer into the flame above burning "
                "magnesium, records 600 °C, and says that proves the "
                "reaction is exothermic. Why is that not a valid test?",
        "options": [
            {"text": "Because a thermometer cannot survive a flame, so the "
                     "reading means nothing", "correct": False,
             "why": "The problem is what was measured rather than whether "
                    "the instrument coped with measuring it."},
            {"text": "Because a single reading proves nothing without a "
                     "second one taken later on", "correct": False,
             "why": "Two readings in the flame would be no better. The site "
                    "is wrong, not the number of readings."},
            {"text": "Because the flame is part of the reaction, and the "
                     "test is the surroundings warming", "correct": True},
            {"text": "Because 600 °C is far too hot to have come from the magnesium rather than from the Bunsen that lit it", "correct": False,
             "why": "Burning magnesium is far hotter than the Bunsen that "
                    "lit it, so the reading is perfectly believable."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h17",
        "band": "harder",
        "text": "A neutralisation is exothermic in a 50 cm³ beaker on a "
                "school bench. Why is the same reaction still exothermic in "
                "an industrial tank a thousand times bigger?",
        "options": [
            {"text": "Because a bigger tank loses heat more slowly, which is "
                     "what keeps it warming", "correct": False,
             "why": "Losing heat slowly changes how long it stays warm. It "
                    "does not decide which way the energy went."},
            {"text": "Because industrial reactions are run hot, and a hot "
                     "start makes any reaction exothermic", "correct": False,
             "why": "Starting temperature does not change the direction of "
                    "the transfer. A cold start would be exothermic too."},
            {"text": "Because the temperature rise in the tank would be a thousand times bigger, which is far easier to detect", "correct": False,
             "why": "A thousand times the chemicals in a thousand times the "
                    "solution gives about the same rise, not a bigger one."},
            {"text": "Because the direction of the transfer always belongs "
                     "to the reaction, not to its size", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier, second pass ───────────────────────────
    {
        "id": "c7-02-e18",
        "band": "easier",
        "text": "Which gas is given off when magnesium reacts with dilute "
                "hydrochloric acid?",
        "options": [
            {"text": "Hydrogen", "correct": True},
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen relights a glowing splint. This gas pops, which "
                    "is the test for hydrogen."},
            {"text": "Carbon dioxide", "correct": False,
             "why": "Carbon dioxide comes off when an acid meets a "
                    "carbonate, and it puts a splint out."},
            {"text": "Chlorine", "correct": False,
             "why": "The chlorine stays in the solution as part of the salt "
                    "that forms."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e19",
        "band": "easier",
        "text": "What is made when an acid is neutralised by an alkali?",
        "options": [
            {"text": "An acid that is weaker than the one you started with",
             "correct": False,
             "why": "Neither substance is left. Two new ones are made in "
                    "their place."},
            {"text": "A salt and water", "correct": True},
            {"text": "A salt and hydrogen", "correct": False,
             "why": "Hydrogen comes off when an acid meets a metal, not when "
                    "it meets an alkali."},
            {"text": "Water only, with the acid used up completely",
             "correct": False,
             "why": "The other product is a salt, and it is still there "
                    "dissolved in the water."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e20",
        "band": "easier",
        "text": "Roughly what temperature does a reusable hand warmer reach?",
        "options": [
            {"text": "About 20 °C", "correct": False,
             "why": "That is room temperature, which is where it started."},
            {"text": "About 35 °C", "correct": False,
             "why": "A pouch at 35 °C would feel no warmer than your own "
                    "hand does."},
            {"text": "About 50 °C", "correct": True},
            {"text": "About 100 °C", "correct": False,
             "why": "Something at 100 °C would scald a pocket. That is the "
                    "temperature it is RESET at, not the one it reaches."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e21",
        "band": "easier",
        "text": "Roughly how long does a snapped hand warmer stay hot for?",
        "options": [
            {"text": "About ten seconds", "correct": False,
             "why": "Ten seconds would be no use to anybody on a cold walk."},
            {"text": "About five minutes", "correct": False,
             "why": "It runs far longer than that, which is what makes it "
                    "worth carrying."},
            {"text": "Until it is snapped a second time", "correct": False,
             "why": "Snapping it again does nothing. It is reset by boiling, "
                    "not by snapping."},
            {"text": "About an hour", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e22",
        "band": "easier",
        "text": "How is a reusable hand warmer safely reset?",
        "options": [
            {"text": "By boiling it in a pan of water on a hob",
             "correct": True},
            {"text": "By heating it in a microwave for a minute",
             "correct": False,
             "why": "A sealed pouch in a microwave can burst, and it is "
                    "named as the thing not to do."},
            {"text": "By leaving it on a radiator overnight",
             "correct": False,
             "why": "A radiator is nowhere near hot enough to run the change "
                    "backwards."},
            {"text": "By putting it in a freezer until it is solid",
             "correct": False,
             "why": "Cooling it is the opposite of supplying the energy the "
                    "reset needs."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e23",
        "band": "easier",
        "text": "Roughly what temperature does the middle of a working "
                "compost heap reach?",
        "options": [
            {"text": "About 20 °C", "correct": False,
             "why": "That is the temperature of the garden around it on a "
                    "mild day."},
            {"text": "About 60 °C", "correct": True},
            {"text": "About 5 °C", "correct": False,
             "why": "A heap at 5 °C would be colder than the summer air, and "
                    "nothing in it is taking energy in."},
            {"text": "About 200 °C", "correct": False,
             "why": "Nothing in a garden heap is anywhere near that, though "
                    "a very large hay pile can reach the point of igniting."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e24",
        "band": "easier",
        "text": "What happened to the temperature in every reaction of the "
                "displacement grid?",
        "options": [
            {"text": "It fell, because a metal has to be pulled out of its "
                     "compound", "correct": False,
             "why": "Displacement reactions warm their mixtures. Every one "
                    "of them gave energy out."},
            {"text": "It stayed the same, because no new substances were "
                     "made", "correct": False,
             "why": "New substances were made — that is what displacement "
                    "is."},
            {"text": "It rose", "correct": True},
            {"text": "It rose only where a very reactive metal was used",
             "correct": False,
             "why": "All of them gave energy out. The more reactive metals "
                    "simply gave out more."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e25",
        "band": "easier",
        "text": "Rusting is exothermic. What type of reaction is it?",
        "options": [
            {"text": "A neutralisation, because rain is slightly acidic",
             "correct": False,
             "why": "No alkali is involved, and iron rusts in pure water "
                    "with air just as well."},
            {"text": "A displacement, because the iron takes the place of "
                     "something else", "correct": False,
             "why": "Nothing is displaced. The iron combines with oxygen "
                    "rather than swapping with anything."},
            {"text": "A thermal decomposition, because the iron breaks down",
             "correct": False,
             "why": "The iron is not broken down. It joins with oxygen to "
                    "make a new compound."},
            {"text": "An oxidation", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e26",
        "band": "easier",
        "text": "What does the sodium ethanoate inside a reusable hand "
                "warmer do when the disc is snapped?",
        "options": [
            {"text": "It crystallises out of the solution", "correct": True},
            {"text": "It burns, using the air sealed inside the pouch",
             "correct": False,
             "why": "There is no flame and no air supply. A sealed pouch "
                    "cannot burn anything."},
            {"text": "It dissolves into the water around it", "correct": False,
             "why": "It is already dissolved. Snapping the disc starts it "
                    "coming out of solution."},
            {"text": "It reacts with the metal disc to make a new compound",
             "correct": False,
             "why": "The disc sets the change off; it is not one of the "
                    "substances that change."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e27",
        "band": "easier",
        "text": "Four of the five beakers on the bench warmed up. What did "
                "the fifth one do?",
        "options": [
            {"text": "It warmed up more slowly than the rest", "correct": False,
             "why": "It did not warm at all. Its thermometer went the other "
                    "way."},
            {"text": "Its temperature fell", "correct": True},
            {"text": "It stayed at exactly the temperature it started at",
             "correct": False,
             "why": "A reaction with no temperature change would be a fourth "
                    "possibility, and it is not what that beaker did."},
            {"text": "It warmed up and then cooled below where it started",
             "correct": False,
             "why": "There was no warming stage. The reading fell from the "
                    "moment the two were stirred together."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e28",
        "band": "easier",
        "text": "What does a self-heating can of coffee do in about three "
                "minutes?",
        "options": [
            {"text": "Cools the drink to just above freezing",
             "correct": False,
             "why": "It is a heater. Cooling a drink on demand is a "
                    "different device altogether."},
            {"text": "Boils the drink, which is why the can must be opened "
                     "first", "correct": False,
             "why": "Boiling a sealed can would be dangerous, and no drink "
                    "is served at 100 °C."},
            {"text": "Brings the drink up to serving temperature",
             "correct": True},
            {"text": "Keeps the drink at the temperature it was bought at",
             "correct": False,
             "why": "Holding a temperature is what a flask does. This can "
                    "raises it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e29",
        "band": "easier",
        "text": "What does snapping the metal disc inside a hand warmer do?",
        "options": [
            {"text": "It makes the pouch airtight so the reaction can begin",
             "correct": False,
             "why": "The pouch was already sealed, and no air is needed by "
                    "what happens inside it."},
            {"text": "It generates heat by friction as the metal bends",
             "correct": False,
             "why": "Bending a small disc could never warm a pouch to "
                    "50 °C for an hour."},
            {"text": "It lets the two chemicals inside mix together for the "
                     "first time", "correct": False,
             "why": "Everything in the pouch is already mixed. What the disc "
                    "does is get the change going."},
            {"text": "It starts the change that releases the stored energy",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-e30",
        "band": "easier",
        "text": "Grass cuttings piled up in a garden heat up on their own. "
                "What is releasing that energy?",
        "options": [
            {"text": "Warm air that was trapped between the cuttings when "
                     "the pile was made", "correct": False,
             "why": "A pocket of warm air would cool to the temperature of "
                    "the garden within minutes. It could not hold a pile "
                    "warm for weeks."},
            {"text": "The weight of the pile squashing the lower layers "
                     "together", "correct": False,
             "why": "Pressing material together does not release energy "
                    "from it. A stack of bricks does not warm up."},
            {"text": "Bacteria respiring as they break down the plant "
                     "material", "correct": True},
            {"text": "The grass drying out, which gives energy out as water "
                     "leaves it", "correct": False,
             "why": "Water leaving a liquid takes energy in, not out, so "
                    "drying would cool the pile rather than warm it."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard, second pass ─────────────────────────
    {
        "id": "c7-02-s18",
        "band": "standard",
        "text": "The temperatures on the five-beaker bench are described as "
                "typical classroom values rather than readings from one "
                "afternoon. Why does saying so matter?",
        "options": [
            {"text": "Because a number given without that warning claims to "
                     "be a measurement somebody took", "correct": True},
            {"text": "Because the values measured on a real afternoon would "
                     "be much larger than the ones printed", "correct": False,
             "why": "They are the right size. What is being flagged is where "
                    "they came from, not how big they are."},
            {"text": "Because a reaction gives a different result every time "
                     "it is run", "correct": False,
             "why": "Repeats agree closely. The warning is about how these "
                    "particular figures were chosen."},
            {"text": "Because temperatures cannot be measured accurately in "
                     "a school laboratory", "correct": False,
             "why": "They can, and the measuring lesson is about doing "
                    "exactly that well."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s19",
        "band": "standard",
        "text": "Four beakers on the bench are said to cover most of the "
                "chemistry done so far. What does that tell you about "
                "reactions in general?",
        "options": [
            {"text": "That a metal has to be involved for a reaction to "
                     "give energy out", "correct": False,
             "why": "Neutralisation involves no metal at all and still warms "
                    "the beaker."},
            {"text": "That every reaction met so far had to be started with "
                     "a flame", "correct": False,
             "why": "The hand warmer and the neutralisation needed no flame "
                    "of any kind."},
            {"text": "That most of the reactions a student meets give energy "
                     "out", "correct": True},
            {"text": "That the four types are the only exothermic reactions "
                     "there are", "correct": False,
             "why": "They are examples, not a complete list. Respiration and "
                    "rusting are exothermic too."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s20",
        "band": "standard",
        "text": "Magnesium dropped into acid fizzes, gives off a gas, and "
                "warms the tube. Which of those observations shows the "
                "reaction is exothermic?",
        "options": [
            {"text": "The fizzing, because bubbles form as the energy is "
                     "released", "correct": False,
             "why": "Bubbles show a gas is being made. A reaction that took "
                    "energy in could fizz just as hard."},
            {"text": "The gas, because a gas carries energy away from the "
                     "tube", "correct": False,
             "why": "Making a gas tells you a reaction happened. It says "
                    "nothing about which way the energy went."},
            {"text": "All three together, since any change at all means "
                     "energy was released", "correct": False,
             "why": "Plenty of changes take energy in. Two of these three "
                    "would happen either way."},
            {"text": "The warming, because that is always the surroundings "
                     "gaining energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s21",
        "band": "standard",
        "text": "A student holds a warm hand warmer and says their own hand "
                "is what is heating it. How would you settle that in one "
                "step?",
        "options": [
            {"text": "Snap a fresh one on a cold bench and watch it warm up "
                     "anyway", "correct": True},
            {"text": "Hold it for longer and see whether it gets hotter "
                     "still", "correct": False,
             "why": "It would warm on its own either way, so a longer hold "
                    "settles nothing."},
            {"text": "Ask a second student to hold it and compare how warm "
                     "it feels", "correct": False,
             "why": "Two hands test the same idea twice. Neither run has the "
                    "hand taken away."},
            {"text": "Put it in a pocket and check that it still reaches "
                     "50 °C", "correct": False,
             "why": "A pocket is warm too, so that leaves the same "
                    "explanation open."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s22",
        "band": "standard",
        "text": "Magnesium can be burned in a tongs in open air, or lowered "
                "into a beaker of water with a thermometer in it. Which "
                "set-up shows that burning is exothermic?",
        "options": [
            {"text": "The open air one, because the flame proves energy is "
                     "coming out", "correct": False,
             "why": "The flame is part of the reaction. Exothermic is "
                    "measured in the surroundings."},
            {"text": "The beaker one only, because the water is the "
                     "surroundings and it warms", "correct": True},
            {"text": "Neither, because burning is a reaction with air and "
                     "not with the water", "correct": False,
             "why": "What it reacts with does not matter. The water is there "
                    "to receive the energy and report it."},
            {"text": "Both equally, because the same reaction is happening "
                     "in each of them", "correct": False,
             "why": "The same reaction, but only one of the two has anything "
                    "measuring the surroundings."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s23",
        "band": "standard",
        "text": "Iron wool is dipped in salty water and sealed in an "
                "insulated flask with a thermometer. Predict what the "
                "thermometer does over the next hour.",
        "options": [
            {"text": "It falls, because rusting takes oxygen out of the air "
                     "in the flask", "correct": False,
             "why": "Using up oxygen is not a cooling process. The rusting "
                    "itself gives energy out."},
            {"text": "It stays level, because rusting is far too slow to "
                     "measure", "correct": False,
             "why": "Insulating it and using wool rather than a solid bar is "
                    "exactly what makes it measurable."},
            {"text": "It rises slowly", "correct": True},
            {"text": "It rises sharply and then drops back below where it "
                     "started", "correct": False,
             "why": "Nothing here releases energy in a burst, and nothing "
                    "takes any in afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s24",
        "band": "standard",
        "text": "Acid and alkali are both clear liquids, and the mixture "
                "looks unchanged afterwards. So why does the thermometer "
                "rise?",
        "options": [
            {"text": "Because stirring two liquids together warms them a "
                     "little on its own", "correct": False,
             "why": "Stirring water into water warms nothing. It is the "
                    "reaction that does it."},
            {"text": "Because the acid was slightly warmer than the alkali "
                     "to begin with", "correct": False,
             "why": "Both start at the same temperature, and the rise is far "
                    "bigger than any small difference."},
            {"text": "Because a thermometer reads higher in a mixture than "
                     "in a pure liquid", "correct": False,
             "why": "A thermometer reads the temperature of whatever it sits "
                    "in. Mixtures are no different."},
            {"text": "Because a reaction happened and made new substances, "
                     "releasing stored energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s25",
        "band": "standard",
        "text": "A student says any reaction that gets hot must be "
                "dangerous. Use two examples from this lesson to judge that.",
        "options": [
            {"text": "It depends on how hot and how fast — 50 °C in a pocket "
                     "is safe, burning magnesium is not", "correct": True},
            {"text": "They are right: every exothermic reaction there is "
                     "has to be treated as a serious hazard", "correct": False,
             "why": "A hand warmer is sold for children to carry. Being "
                    "exothermic does not make something dangerous."},
            {"text": "They are wrong: no reaction that warms its "
                     "surroundings can do any harm", "correct": False,
             "why": "Burning magnesium and quicklime in an eye are both "
                    "exothermic and both genuinely dangerous."},
            {"text": "They are right for reactions with flames and wrong for "
                     "every other kind", "correct": False,
             "why": "Quicklime and water has no flame at all and is still "
                    "hazardous."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s26",
        "band": "standard",
        "text": "Burning magnesium took its beaker of water to 60 °C; "
                "magnesium with acid reached 34 °C. What can you conclude?",
        "options": [
            {"text": "That magnesium with acid is not really an exothermic "
                     "reaction", "correct": False,
             "why": "It warmed its surroundings by fourteen degrees. That is "
                    "exothermic by the only test there is."},
            {"text": "Both warmed their surroundings, but the amounts used "
                     "were not matched, so this is not a fair comparison",
             "correct": True},
            {"text": "That burning always releases more energy than any "
                     "other kind of reaction", "correct": False,
             "why": "Not from two unmatched runs. Some non-burning reactions "
                    "release a great deal."},
            {"text": "That the acid absorbed a large part of the released "
                     "energy before the thermometer in the beaker could "
                     "read it", "correct": False,
             "why": "The acid is part of the surroundings being warmed, "
                    "which is what the 34 °C shows."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s27",
        "band": "standard",
        "text": "A bonfire and a candle are both combustion, yet the bonfire "
                "feels far hotter from a distance. What is the difference?",
        "options": [
            {"text": "The bonfire reaches a higher flame temperature than a "
                     "candle can", "correct": False,
             "why": "Flame temperatures are not far apart. It is how much "
                    "fuel is burning that differs."},
            {"text": "The candle's reaction is exothermic and the bonfire's "
                     "is something stronger than that", "correct": False,
             "why": "There is no stronger category. Both are combustion, and "
                    "both give energy out."},
            {"text": "The bonfire releases far more energy every second, "
                     "because far more fuel is reacting", "correct": True},
            {"text": "The bonfire has more oxygen available, and oxygen is "
                     "what carries the heat", "correct": False,
             "why": "Oxygen is a reactant, not a carrier of energy from one "
                    "place to another."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s28",
        "band": "standard",
        "text": "When magnesium is burned as a demonstration, everybody in "
                "the room wears eye protection, not only the person holding "
                "the tongs. Why?",
        "options": [
            {"text": "Because the light that makes it a hazard reaches "
                     "everybody in the room", "correct": True},
            {"text": "Because the smoke travels across the room within "
                     "seconds", "correct": False,
             "why": "Eye protection is worn for the brightness, and it would "
                    "not help with anything breathed in."},
            {"text": "Because the magnesium can spit as far as the back "
                     "bench", "correct": False,
             "why": "A coil of ribbon burning in tongs does not throw "
                    "material across a room."},
            {"text": "Because the same eye-protection rule is applied to "
                     "every school practical", "correct": False,
             "why": "Eye protection is worn widely, but this demonstration "
                    "has its own specific reason."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s29",
        "band": "standard",
        "text": "Which observation from the acids unit already showed that "
                "neutralisation is exothermic, before it had a name?",
        "options": [
            {"text": "The indicator changed colour as soon as the alkali "
                     "started going in", "correct": False,
             "why": "A colour change shows the acid being used up. It says "
                    "nothing about energy."},
            {"text": "The beaker warmed while the two solutions were being "
                     "mixed", "correct": True},
            {"text": "Bubbles appeared as soon as the two liquids met",
             "correct": False,
             "why": "Neutralisation makes a salt and water, with no gas to "
                    "bubble off."},
            {"text": "A solid formed at the bottom of the flask as they "
                     "mixed", "correct": False,
             "why": "The salt stays dissolved, and a solid appearing would "
                    "not tell you the direction anyway."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-s30",
        "band": "standard",
        "text": "A candle burns steadily for an hour with nobody adding "
                "anything to it. Is anything being fed into the reaction?",
        "options": [
            {"text": "No — that is exactly what makes combustion "
                     "exothermic", "correct": False,
             "why": "What makes it exothermic is energy coming out. "
                    "Something IS being fed in."},
            {"text": "Yes — oxygen, which the flame is always drawing from "
                     "the air around it",
             "correct": True},
            {"text": "Yes — energy, radiated back into the flame by the warm "
                     "air above it", "correct": False,
             "why": "The warm air is carrying energy away from the flame, "
                    "not returning it."},
            {"text": "No — the wax holds everything the reaction needs "
                     "inside it", "correct": False,
             "why": "Put a jar over the candle and it goes out, which shows "
                    "something outside was needed."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder, second pass ───────────────────────────
    {
        "id": "c7-02-h18",
        "band": "harder",
        "text": "A camping stove needs a spark to light. Describe the single "
                "observation that settles whether the reaction is "
                "exothermic.",
        "options": [
            {"text": "Measure how much energy the spark delivers and compare "
                     "it with the gas used", "correct": False,
             "why": "A great deal of work for something one observation "
                    "settles: take the spark away and watch."},
            {"text": "Light it in a colder room and check that it still "
                     "catches", "correct": False,
             "why": "That tests how easy it is to start, which is a "
                    "different question from the direction."},
            {"text": "Stop the spark and see the flame keep burning on its "
                     "own", "correct": True},
            {"text": "Turn the gas up and see whether the flame gets hotter",
             "correct": False,
             "why": "A bigger flame releases more energy per second, which "
                    "was never in doubt."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h19",
        "band": "harder",
        "text": "Two identical self-heating cans are tested, one in a warm "
                "kitchen and one in a fridge. Compare the temperature RISE "
                "each one produces.",
        "options": [
            {"text": "The fridge one produces a bigger rise, because it has "
                     "further to climb", "correct": False,
             "why": "How far it has to climb is not something the reaction "
                    "knows about."},
            {"text": "The kitchen one produces a bigger rise, because warmth "
                     "speeds the reaction up", "correct": False,
             "why": "A warmer start can make it run faster, but the energy "
                    "released is the same either way."},
            {"text": "The kitchen one produces a rise and the fridge one "
                     "does not, because the cold cancels it", "correct": False,
             "why": "A fridge removes energy slowly. It cannot cancel a "
                    "reaction releasing its store in three minutes."},
            {"text": "Both rise by about the same amount, though the fridge "
                     "one ends up colder", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h20",
        "band": "harder",
        "text": "The hand warmer is not a chemical reaction at all. Why is "
                "it still put on a bench of exothermic reactions?",
        "options": [
            {"text": "Because the energy accounting is the same whether the "
                     "change is chemical or physical", "correct": True},
            {"text": "Because it is the only one of the five on the bench "
                     "that a student could buy in a shop", "correct": False,
             "why": "Being buyable is what makes it a good example, not what "
                    "makes it belong on the list."},
            {"text": "Because a change of state counts as a reaction once it "
                     "releases energy", "correct": False,
             "why": "It never counts as a reaction. No new substance is "
                    "made, however much energy comes out."},
            {"text": "Because the sodium ethanoate reacts with the metal "
                     "disc as it crystallises", "correct": False,
             "why": "The disc only sets the change off. It is not one of the "
                    "substances that change."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h21",
        "band": "harder",
        "text": "Rusting, combustion and respiration all involve a substance "
                "combining with oxygen, and all three give energy out. What "
                "does that suggest?",
        "options": [
            {"text": "That a reaction gives energy out only when oxygen is "
                     "one of the reactants", "correct": False,
             "why": "Neutralisation and displacement are exothermic with no "
                    "oxygen involved anywhere."},
            {"text": "That oxidations are exothermic", "correct": True},
            {"text": "That oxygen carries energy into a reaction and lets it "
                     "out again", "correct": False,
             "why": "Oxygen is a reactant. The energy was stored in the "
                    "arrangement of the substances, not carried in."},
            {"text": "That the three reactions are really the same reaction "
                     "under different names", "correct": False,
             "why": "They have quite different reactants and products. What "
                    "they share is the type of change."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h22",
        "band": "harder",
        "text": "A reaction warms 100 cm³ of water by 8 °C. The same amounts "
                "of the same chemicals are reacted in 200 cm³ of water "
                "instead. Predict the rise.",
        "options": [
            {"text": "About 16 °C, because there is more water to hold the "
                     "energy", "correct": False,
             "why": "More water to share the same energy means a smaller "
                    "rise, not a bigger one."},
            {"text": "About 8 °C, because the reaction has not changed",
             "correct": False,
             "why": "The reaction is the same, but the energy is now "
                    "spreading through twice as much water."},
            {"text": "About 4 °C", "correct": True},
            {"text": "No rise at all, because the extra water cools the "
                     "mixture down", "correct": False,
             "why": "Water at the same temperature cools nothing. It simply "
                    "shares the energy released."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h23",
        "band": "harder",
        "text": "What is the strongest evidence that the energy a hand "
                "warmer releases was in it before anybody snapped the disc?",
        "options": [
            {"text": "That it reaches 50 °C with nothing plugged into it",
             "correct": False,
             "why": "Good evidence that nothing was supplied at the time, "
                    "but it does not show when the store was filled."},
            {"text": "That it stays hot for an hour rather than a few "
                     "seconds", "correct": False,
             "why": "How long it lasts tells you the store is large, not "
                    "when it was filled."},
            {"text": "That snapping the disc does nothing until the pouch "
                     "has been sealed", "correct": False,
             "why": "The pouch is sealed at the factory and stays sealed "
                    "throughout. Nothing here is a test."},
            {"text": "That boiling it refills the store, so it can be "
                     "snapped and used again", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h24",
        "band": "harder",
        "text": "A student suggests ranking reactions by how exothermic they "
                "are, using how bright each flame is. Evaluate that.",
        "options": [
            {"text": "It fails, because brightness is not a measure of the "
                     "energy transferred to the surroundings", "correct": True},
            {"text": "It works, because the brighter flame in any pair is "
                     "the hotter one", "correct": False,
             "why": "Even where that held, flame temperature is not the same "
                    "thing as energy released."},
            {"text": "It works, as long as every reaction is given the same "
                     "amount of oxygen", "correct": False,
             "why": "Matching the oxygen does not turn brightness into a "
                    "measurement of energy."},
            {"text": "It fails, because some exothermic reactions release "
                     "their energy as light rather than heat",
             "correct": False,
             "why": "Releasing energy as light is still exothermic. The "
                    "problem is that brightness measures nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h25",
        "band": "harder",
        "text": "Two hand warmers are snapped at the same moment. One is "
                "left on a bench and one is wrapped in a thick towel. "
                "Compare what their thermometers show.",
        "options": [
            {"text": "The bench one gets hotter, because air can reach it "
                     "and air is a reactant", "correct": False,
             "why": "Nothing in a sealed pouch needs air. The change is a "
                    "crystallisation."},
            {"text": "The wrapped one gets hotter and stays hot longer, "
                     "because less energy escapes", "correct": True},
            {"text": "Both behave identically, because the same change "
                     "releases the same energy", "correct": False,
             "why": "The same energy released, but not the same amount "
                    "retained — that is what the towel changes."},
            {"text": "The wrapped one gets hotter but runs out sooner, "
                     "because heat speeds the change up", "correct": False,
             "why": "Insulating it does not use the store up faster. It "
                    "holds the energy in for longer."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h26",
        "band": "harder",
        "text": "A reaction gives out its energy almost entirely as light "
                "and hardly warms anything. Is it exothermic?",
        "options": [
            {"text": "No, because exothermic means the surroundings must "
                     "get warmer, and nothing here does", "correct": False,
             "why": "Warming is the usual sign, not the definition. Energy "
                    "leaving the chemicals is what counts."},
            {"text": "No, because light is not a form of energy a reaction "
                     "can release", "correct": False,
             "why": "A firework releases a great deal of its energy as "
                    "light, and so does burning magnesium."},
            {"text": "Yes, because energy is still leaving the chemicals and "
                     "going out into the surroundings", "correct": True},
            {"text": "Not unless the light is later absorbed by something "
                     "and turned into heat", "correct": False,
             "why": "It is exothermic the moment the energy leaves. What "
                    "happens to the light afterwards changes nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h27",
        "band": "harder",
        "text": "A student argues that neutralisation must be exothermic "
                "because acids are dangerous substances. What is wrong with "
                "the argument?",
        "options": [
            {"text": "Nothing — the more hazardous the reactants, the more "
                     "energy a reaction gives out", "correct": False,
             "why": "There is no such rule. Plenty of hazardous substances "
                    "react with very little energy change."},
            {"text": "It has the direction backwards: a dangerous substance "
                     "makes a reaction endothermic", "correct": False,
             "why": "Hazard does not set the direction either way. That is "
                    "the whole point."},
            {"text": "It is wrong about acids, which are not hazardous at "
                     "the concentrations used in school", "correct": False,
             "why": "School acids are still handled with care. The fault is "
                    "in the reasoning, not in that claim."},
            {"text": "How hazardous a substance is never tells you which "
                     "way its energy goes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h28",
        "band": "harder",
        "text": "A compost heap holds 60 °C in a frost and about 65 °C in "
                "summer. What does that narrow difference show?",
        "options": [
            {"text": "That the energy is coming from inside the heap rather "
                     "than from the weather", "correct": True},
            {"text": "That the heap is storing summer warmth and releasing "
                     "it through the winter", "correct": False,
             "why": "No pile of grass could hold months of warmth. It is "
                    "making the energy afresh the whole time."},
            {"text": "That the bacteria work equally well at any temperature "
                     "they are given", "correct": False,
             "why": "Their rate does change with temperature. What the "
                    "figures show is where the energy comes from."},
            {"text": "That most of the heat in a heap comes from sunlight "
                     "falling on it", "correct": False,
             "why": "Sunlight would give a far bigger summer-to-winter gap, "
                    "and a heap works in the dark."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h29",
        "band": "harder",
        "text": "A hand warmer only reaches 50 °C, so why does resetting it "
                "need a pan of boiling water rather than a 50 °C bath?",
        "options": [
            {"text": "Because a bath at 50 °C would take far longer to do "
                     "the same job", "correct": False,
             "why": "It would not do the job at all, however long it was "
                    "left."},
            {"text": "Because resetting has to put back all the energy the "
                     "change gave out", "correct": True},
            {"text": "Because the pouch has to be sterilised between uses",
             "correct": False,
             "why": "Nothing inside a sealed pouch needs sterilising, and "
                    "that would not refill the store."},
            {"text": "Because boiling water is the only way to soften the "
                     "metal disc again", "correct": False,
             "why": "The disc is unchanged by being snapped. It is the "
                    "sodium ethanoate that has to be redissolved."},
        ],
        "figure": None,
    },
    {
        "id": "c7-02-h30",
        "band": "harder",
        "text": "A camping stove needs a spark and a hand warmer needs a "
                "snap. What do those two very different starts have in "
                "common?",
        "options": [
            {"text": "Both supply the whole of the energy that comes out of "
                     "the reaction afterwards", "correct": False,
             "why": "Both supply a tiny fraction of it. The rest was already "
                    "stored in the chemicals."},
            {"text": "Both add a substance that the reaction cannot run "
                     "without", "correct": False,
             "why": "A spark adds no substance at all, and snapping a disc "
                    "adds nothing to the pouch."},
            {"text": "Both give a small push that lets a store of energy "
                     "start releasing itself", "correct": True},
            {"text": "Both work by warming the chemicals up to the "
                     "temperature they need", "correct": False,
             "why": "A snapped disc warms nothing. The pouch is at room "
                    "temperature when the change begins."},
        ],
        "figure": None,
    },
]
