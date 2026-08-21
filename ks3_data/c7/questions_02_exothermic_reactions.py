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
]
