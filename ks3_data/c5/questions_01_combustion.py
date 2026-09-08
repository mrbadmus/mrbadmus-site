"""C5 lesson 01 — Combustion: twelve questions (MRB-246).

The lesson's argument is one sentence long — a fuel reacting with oxygen gives
out energy, and how much oxygen reaches it decides what comes out and how much
energy you get — and everything else on the page is either a consequence of
that or a case where the consequence surprises you. These twelve probe the
angles the mastery ladder leaves alone: what the colour of a flame is actually
telling you, what happens when the FUEL rather than the air is the thing that
changes, and where the same chemistry turns up outside a lab.

The distractors are built from the lesson's two declared misconceptions.
`REACT-10` (a bigger, brighter flame is a hotter flame) drives the wrong
options in e02, s04 and h02 — each of them reads brightness or size as heat,
which is the mistake that ends with a student heating a beaker on the safety
flame and wondering why nothing happens. `REACT-11` (shutting the air off makes
a flame burn hotter or more fiercely) drives e02 and h02 from the other side,
where the air hole is read as a power control rather than as the thing that
decides whether the reaction finishes.

A third strand runs through e01, s01, s02 and h04, and it is not in the
register because it is an over-generalisation rather than a belief: having
learned that combustion gives carbon dioxide and water, a student applies it to
every fuel, including one with no hydrogen in it and one with no carbon at all.
Those four are the same rule read honestly — every carbon atom in the fuel ends
up in carbon dioxide, every hydrogen atom ends up in water, and a fuel that
lacks one of them cannot make its product.

A fourth, in e03 and h03, is that combustion needs only fuel: oxygen is treated
as the room rather than as a reactant, so a candle going out under a jar gets
explained by heat, smoke or carbon dioxide pushing the air away, and a rocket
gets more fuel rather than an oxidiser.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §13's: every distractor is a WRONG
RULE in the correct answer's own shape, and every one is a mistake a real
student in a real lab actually makes. Every option set was measured for a
length tell and every fix was made AT THE DISTRACTOR.
"""

UNIT = "C5"
LESSON = "combustion"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c5-01-e01",
        "band": "easier",
        "text": "A fuel made only of carbon and hydrogen is burned with plenty "
                "of air. What are the products?",
        "options": [
            {"text": "Carbon dioxide and water", "correct": True},
            {"text": "Carbon monoxide and water", "correct": False,
             "why": "Carbon monoxide only appears when the oxygen supply runs "
                    "short. With plenty of air every carbon atom gets all the "
                    "way to carbon dioxide."},
            {"text": "Carbon dioxide and soot", "correct": False,
             "why": "Soot is carbon that never finished reacting. With plenty "
                    "of air there is none of it left over — that is what "
                    "'complete' means."},
            {"text": "Carbon dioxide and hydrogen", "correct": False,
             "why": "The hydrogen does not come back out as hydrogen. It "
                    "reacts with oxygen as well, and what it makes is water."},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e02",
        "band": "easier",
        "text": "A Bunsen burner is burning with a tall yellow flame. What "
                "does the colour tell you?",
        "options": [
            {"text": "More gas than usual is reaching the flame",
             "correct": False,
             "why": "The gas tap changes the size of the flame, not its "
                    "colour. Turn the gas up with the air hole open and you "
                    "get a bigger blue flame."},
            {"text": "Not enough air is reaching the gas", "correct": True},
            {"text": "The flame is hotter than a blue one", "correct": False,
             "why": "It is the other way round. The blue flame is the hot one, "
                    "at around 1500 °C against roughly 1000 °C for the "
                    "yellow, and the brightness is glowing soot."},
            {"text": "The gas supply has something else mixed in",
             "correct": False,
             "why": "Same gas, both flames. Open the air hole and the yellow "
                    "flame turns blue straight away, which no impurity in the "
                    "supply would do."},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e03",
        "band": "easier",
        "text": "A candle is burning. A jar is put over it and a few seconds "
                "later it goes out. Why?",
        "options": [
            {"text": "The candle has run out of wax to burn", "correct": False,
             "why": "There is plenty of wax left — you can light it again the "
                    "moment the jar comes off. What ran out was the other "
                    "reactant."},
            {"text": "The jar has made the candle too cold to burn",
             "correct": False,
             "why": "The jar traps heat rather than removing it, so the air "
                    "inside gets hotter, not colder. What it also traps is a "
                    "fixed amount of oxygen."},
            {"text": "The oxygen inside the jar has been used up",
             "correct": True},
            {"text": "The carbon dioxide made has pushed the oxygen out",
             "correct": False,
             "why": "It does not push anything anywhere. The oxygen is being "
                    "turned into carbon dioxide and water by the reaction "
                    "itself, so there is less and less of it until the flame "
                    "cannot keep going."},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e04",
        "band": "easier",
        "text": "A beaker is held over a yellow Bunsen flame and comes away "
                "black. What is the black substance?",
        "options": [
            {"text": "Ash — the solid left behind after the gas has burned",
             "correct": False,
             "why": "Natural gas leaves no ash: there is nothing solid in it "
                    "to leave. The black mark is carbon out of the gas "
                    "itself, stopped part way through reacting."},
            {"text": "Dirt — the burner had it in it before it was lit",
             "correct": False,
             "why": "It is not there before, and it appears on a clean beaker "
                    "within seconds. The flame is making it."},
            {"text": "Carbon dioxide — it turns black when it touches cold "
                     "glass", "correct": False,
             "why": "Carbon dioxide is a colourless gas and stays one however "
                    "cold the glass is. What lands on the beaker is solid "
                    "carbon."},
            {"text": "Soot — carbon from the gas that never finished reacting",
             "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c5-01-s01",
        "band": "standard",
        "text": "Hydrogen is burned as a fuel with plenty of air. What comes "
                "out?",
        "options": [
            {"text": "Water only", "correct": True},
            {"text": "Water and carbon dioxide", "correct": False,
             "why": "There is no carbon anywhere in hydrogen, so there is "
                    "nothing for carbon dioxide to be made from."},
            {"text": "Carbon dioxide only", "correct": False,
             "why": "Carbon dioxide needs carbon, and hydrogen has none. What "
                    "the hydrogen reacts with is oxygen, and that makes "
                    "water."},
            {"text": "Water and carbon monoxide", "correct": False,
             "why": "Carbon monoxide needs carbon too. Whatever the air "
                    "supply, a fuel with no carbon in it cannot make either "
                    "of the carbon gases."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-01-s02",
        "band": "standard",
        "text": "Charcoal is almost pure carbon. It is burned on a barbecue in "
                "the open air. What are the products?",
        "options": [
            {"text": "Carbon dioxide and water", "correct": False,
             "why": "Water comes from hydrogen in the fuel, and charcoal has "
                    "essentially none. No hydrogen means no water."},
            {"text": "Carbon dioxide only", "correct": True},
            {"text": "Carbon monoxide only", "correct": False,
             "why": "Carbon monoxide is what you get when the oxygen runs "
                    "short. In the open air there is plenty of it, so the "
                    "carbon goes all the way to carbon dioxide."},
            {"text": "Carbon dioxide and hydrogen", "correct": False,
             "why": "Hydrogen would have to be in the charcoal to come out of "
                    "it, and it is not. Charcoal is almost all carbon."},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s03",
        "band": "standard",
        "text": "Why is carbon monoxide more dangerous in a house than most "
                "other poisonous substances?",
        "options": [
            {"text": "It burns easily, so it can set the room on fire",
             "correct": False,
             "why": "It is flammable, and that is not what makes it dangerous "
                    "here. What harms you is breathing it, and you would be "
                    "breathing it long before it caught."},
            {"text": "It is heavier than air, so it collects at floor level",
             "correct": False,
             "why": "It is very slightly lighter than air and mixes right "
                    "through a room, so there is no safe height to be at. "
                    "There is nothing to move away from."},
            {"text": "It has no colour and no smell, so nothing warns you",
             "correct": True},
            {"text": "It stings your eyes and throat, which makes you panic",
             "correct": False,
             "why": "It does none of those things, and that is exactly the "
                    "problem. The first symptoms are a headache and "
                    "tiredness, which is what anyone would ignore."},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s04",
        "band": "standard",
        "text": "Two identical beakers of water are heated on identical "
                "burners, one on a blue flame and one on a yellow flame. "
                "Which boils first, and why?",
        "options": [
            {"text": "The yellow one, because a bigger flame gives out more "
                     "heat", "correct": False,
             "why": "Bigger and brighter is not hotter. The yellow flame is "
                    "around 1000 °C against the blue flame's 1500 °C, and "
                    "the brightness is soot that never burned."},
            {"text": "The yellow one, because it wraps further around the "
                     "beaker", "correct": False,
             "why": "A yellow flame is taller, and it also leaves soot on the "
                    "base of the beaker — and soot is fuel that never "
                    "released its energy. Shape does not make up for that."},
            {"text": "Neither, because the gas tap was set the same for both",
             "correct": False,
             "why": "The gas tap was the same and the air hole was not, and "
                    "the air hole is what decides how much of the gas "
                    "finishes reacting. Same fuel in, different energy out."},
            {"text": "The blue one, because complete combustion releases all "
                     "the energy", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c5-01-h01",
        "band": "harder",
        "text": "A family brings a barbecue that is still glowing into a tent "
                "to keep warm overnight. Why is this so dangerous?",
        "options": [
            {"text": "The charcoal keeps burning with too little air, making "
                     "carbon monoxide", "correct": True},
            {"text": "The glowing charcoal could easily set the tent fabric "
                     "alight", "correct": False,
             "why": "That is a real risk and it is not the one that kills "
                    "people here. A barbecue that is only glowing, with no "
                    "flame at all, is still making the gas."},
            {"text": "The carbon dioxide it makes slowly pushes all the "
                     "oxygen out", "correct": False,
             "why": "Carbon dioxide is made and it pushes nothing anywhere. "
                    "Long before there is enough of it to matter, the short "
                    "air supply has turned the carbon into carbon monoxide."},
            {"text": "The smoke from the charcoal is full of soot you can "
                     "breathe", "correct": False,
             "why": "There is soot, and it is not the danger. Soot you can "
                    "see and cough at; the gas that kills has no colour and "
                    "no smell and gives no warning at all."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-01-h02",
        "band": "harder",
        "text": "A gas fire is burning with a yellow flame and there is black "
                "marking on the wall above it. Which is the strongest reason "
                "to have it checked at once?",
        "options": [
            {"text": "The soot on the wall will be expensive to clean off "
                     "properly", "correct": False,
             "why": "It will be, and that is a decorating problem rather than "
                    "a reason to act today. The soot matters as a sign of "
                    "something you cannot see."},
            {"text": "Incomplete combustion is making carbon monoxide as well "
                     "as the soot", "correct": True},
            {"text": "A yellow flame means the fire is burning far too hot",
             "correct": False,
             "why": "The yellow flame is the cooler one, at around 1000 °C "
                    "against 1500 °C for the blue. What is wrong is the air "
                    "supply, not the temperature."},
            {"text": "The fire is using more gas than it should for the heat "
                     "given out", "correct": False,
             "why": "It is wasting gas, and that is true and not urgent. What "
                    "makes it urgent is the gas the same fault is putting "
                    "into the room."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-01-h03",
        "band": "harder",
        "text": "A rocket has to burn its fuel hundreds of kilometres up, "
                "where there is effectively no air. What must it carry as "
                "well as fuel?",
        "options": [
            {"text": "Nothing else, because a fuel carries all its own energy",
             "correct": False,
             "why": "Energy is not something a fuel holds on its own. It "
                    "comes out of the reaction between the fuel and the "
                    "oxygen, and with nothing to react with, nothing "
                    "happens."},
            {"text": "A heater, because fuel will not catch alight when cold",
             "correct": False,
             "why": "A rocket engine is not short of heat once it has "
                    "started. What it is short of is the other reactant, and "
                    "no amount of heating supplies that."},
            {"text": "Its own supply of oxygen, because oxygen is a reactant",
             "correct": True},
            {"text": "More fuel than usual, because burning is slower up "
                     "there", "correct": False,
             "why": "More of one reactant does not help when the other one is "
                    "missing. A hundred tonnes of fuel with no oxygen burns "
                    "exactly as well as none."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-01-h04",
        "band": "harder",
        "text": "An advert says a hydrogen car is completely clean, because "
                "its exhaust is only water. What is wrong with the claim?",
        "options": [
            {"text": "Burning hydrogen also makes a little carbon monoxide "
                     "and soot", "correct": False,
             "why": "It does not. There is no carbon in hydrogen, so neither "
                    "of those products is possible however the air supply is "
                    "set."},
            {"text": "The water in the exhaust is itself a harmful pollutant",
             "correct": False,
             "why": "Water vapour out of an exhaust is not a pollutant in any "
                    "ordinary sense — it is what comes out of your own "
                    "breath. The problem is somewhere else entirely."},
            {"text": "Nothing is wrong — the exhaust really is only water",
             "correct": False,
             "why": "The exhaust really is only water, and that is half the "
                    "story. Ask where the hydrogen came from before it went "
                    "into the tank."},
            {"text": "Most hydrogen is made from natural gas, which releases "
                     "carbon dioxide", "correct": True},
                   ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-01-e05",
        "band": "easier",
        "text": "What is combustion?",
        "options": [
            {"text": "A fuel reacting with oxygen and giving out energy",
             "correct": True},
            {"text": "A substance being broken down into simpler ones by the "
                     "heat of a flame, which is why a fire leaves ash behind "
                     "where the fuel used to be",
             "correct": False,
             "why": "Breaking one substance down by heat is thermal "
                    "decomposition, and it needs no oxygen at all"},
            {"text": "Any reaction at all that gets hot enough to feel while "
                     "it runs",
             "correct": False,
             "why": "Plenty of reactions get hot without burning. Combustion "
                    "needs oxygen and a fuel"},
            {"text": "A solid turning straight into a gas when it is heated "
                     "strongly",
             "correct": False,
             "why": "That is a change of state. Nothing new is made"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e06",
        "band": "easier",
        "text": "What is a hydrocarbon?",
        "options": [
            {"text": "A compound of carbon, hydrogen and oxygen, which is why "
                     "burning one of them can produce both carbon dioxide and "
                     "water from what was already in it",
             "correct": False,
             "why": "A hydrocarbon holds no oxygen. The oxygen in the "
                    "products comes from the air"},
            {"text": "A compound made of carbon and hydrogen only",
             "correct": True},
            {"text": "Any fuel at all that burns with a visible flame in the "
                     "air",
             "correct": False,
             "why": "Hydrogen and charcoal both burn and neither is a "
                    "hydrocarbon"},
            {"text": "Water with some carbon dissolved right through it evenly",
             "correct": False,
             "why": "Nothing is dissolved. The carbon and hydrogen are "
                    "chemically joined"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e07",
        "band": "easier",
        "text": "What is soot?",
        "options": [
            {"text": "Ash left behind by the parts of the fuel that could "
                     "never have burned in the first place, however much air "
                     "had reached them",
             "correct": False,
             "why": "Soot is carbon that COULD have burned and did not. With "
                    "enough air there is none"},
            {"text": "Carbon dioxide that has cooled and gone solid",
             "correct": False,
             "why": "Carbon dioxide is a gas at these temperatures and does "
                    "not go solid on a beaker"},
            {"text": "Carbon from the fuel that never finished reacting",
             "correct": True},
            {"text": "Dust drawn into the flame from the room",
             "correct": False,
             "why": "It comes out of the fuel. Burn the same gas with the air "
                    "hole open and none appears"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e08",
        "band": "easier",
        "text": "Which gas does INCOMPLETE combustion produce that complete "
                "combustion does not?",
        "options": [
            {"text": "Carbon dioxide, which is only made once the oxygen "
                     "supply has run short enough for the flame to turn "
                     "yellow",
             "correct": False,
             "why": "Carbon dioxide is what COMPLETE combustion makes. It is "
                    "the finished product"},
            {"text": "Water vapour",
             "correct": False,
             "why": "Both kinds produce water, from the hydrogen in the "
                    "fuel"},
            {"text": "Oxygen",
             "correct": False,
             "why": "Oxygen is used UP by burning. Neither kind produces "
                    "any"},
            {"text": "Carbon monoxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e09",
        "band": "easier",
        "text": "Which Bunsen flame is the hotter?",
        "options": [
            {"text": "The blue one",
             "correct": True},
            {"text": "The yellow one, because it is taller and brighter and "
                     "there is visibly more fire in it than in the other",
             "correct": False,
             "why": "Brightness is glowing soot. The blue flame is hotter, at "
                    "around 1500 °C"},
            {"text": "They are the same, because it is the same gas",
             "correct": False,
             "why": "Same gas, and different amounts of air. That is what "
                    "changes the temperature"},
            {"text": "It depends how far the gas tap is opened",
             "correct": False,
             "why": "The tap changes the size of the flame. The AIR HOLE "
                    "changes the colour and the temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e10",
        "band": "easier",
        "text": "What does complete combustion need plenty of?",
        "options": [
            {"text": "Fuel",
             "correct": False,
             "why": "More fuel without more air makes it LESS complete. Fuel "
                    "is not what runs short"},
            {"text": "Oxygen",
             "correct": True},
            {"text": "Time, because a reaction given long enough will always "
                     "finish whatever else is short",
             "correct": False,
             "why": "A flame starved of air goes on making soot for as long "
                    "as it burns. Time does not fix it"},
            {"text": "Heat",
             "correct": False,
             "why": "Combustion supplies its own heat once it has started. "
                    "What decides whether it finishes is the air"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e11",
        "band": "easier",
        "text": "What is a fuel?",
        "options": [
            {"text": "A substance that catches fire easily, so that it can be "
                     "lit with a match rather than needing anything hotter to "
                     "start it off",
             "correct": False,
             "why": "How easily it lights is a separate matter. Coal is hard "
                    "to light and is a fuel"},
            {"text": "Any liquid that can be poured into an engine",
             "correct": False,
             "why": "Gas and coal are fuels and neither is a liquid"},
            {"text": "A substance burned to release energy",
             "correct": True},
            {"text": "A substance that gives out oxygen when it is heated",
             "correct": False,
             "why": "A fuel takes oxygen IN. Giving it out is what an "
                    "oxidiser does"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c5-01-s05",
        "band": "standard",
        "text": "Methane burns completely in plenty of air. Which word "
                "equation is right?",
        "options": [
            {"text": "methane + oxygen makes carbon dioxide + water",
             "correct": True},
            {"text": "methane + oxygen makes carbon monoxide + water",
             "correct": False,
             "why": "Carbon monoxide is what INCOMPLETE combustion gives. "
                    "With plenty of air the carbon reaches carbon dioxide"},
            {"text": "methane + air makes carbon dioxide + water + soot, "
                     "because a little of the carbon always fails to react "
                     "however much air is supplied to the flame",
             "correct": False,
             "why": "Complete combustion leaves no soot at all, and it is "
                    "OXYGEN that reacts rather than the whole of the air"},
            {"text": "methane makes carbon + hydrogen",
             "correct": False,
             "why": "That would be a decomposition, and nothing here is "
                    "reacting with the oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s06",
        "band": "standard",
        "text": "A candle under a jar goes out in a few seconds. What would "
                "make it burn for longer?",
        "options": [
            {"text": "A taller candle, since the flame would then be closer "
                     "to the top of the jar where the air is freshest and "
                     "least used up",
             "correct": False,
             "why": "The air inside the jar mixes. What runs out is the "
                    "oxygen in the whole jar, whatever the candle's height"},
            {"text": "A larger jar",
             "correct": True},
            {"text": "A thicker wick",
             "correct": False,
             "why": "A bigger flame uses the oxygen up FASTER, so it would go "
                    "out sooner"},
            {"text": "Lighting it before the jar goes on",
             "correct": False,
             "why": "That is what happens anyway. The clock starts when the "
                    "jar seals the air in"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s07",
        "band": "standard",
        "text": "A beaker held over a yellow flame comes away black, and over "
                "a blue flame it stays clean. What has the black deposit cost "
                "the person heating the beaker?",
        "options": [
            {"text": "Nothing — the soot is a by-product and costs nothing",
             "correct": False,
             "why": "Soot is carbon that never reacted, so its energy was "
                    "never released. The yellow flame delivers less"},
            {"text": "Only the time spent cleaning the beaker afterwards",
             "correct": False,
             "why": "That is a nuisance and not the real cost. Less energy "
                    "reached the water"},
            {"text": "Fuel and energy, because soot is carbon that never "
                     "released its energy",
             "correct": True},
            {"text": "Oxygen, which the soot has used up",
             "correct": False,
             "why": "Soot is carbon that did NOT get oxygen. Too little "
                    "oxygen is what made it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s08",
        "band": "standard",
        "text": "A boiler is burning with a yellow flame. Name the two "
                "problems that creates.",
        "options": [
            {"text": "It burns too hot and wears the boiler out faster than "
                     "it should",
             "correct": False,
             "why": "A yellow flame is COOLER than a blue one. Heat is not "
                    "the problem"},
            {"text": "It uses more oxygen and makes more carbon dioxide",
             "correct": False,
             "why": "It uses LESS oxygen — that is what makes it yellow — and "
                    "makes less carbon dioxide, not more"},
            {"text": "It is harder to see and easier to leave on by "
                     "accident",
             "correct": False,
             "why": "A yellow flame is the easier one to see. The problems "
                    "are chemical"},
            {"text": "It makes soot and carbon monoxide, and it releases less "
                     "energy from the same gas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s09",
        "band": "standard",
        "text": "Why does burning hydrogen produce no soot at all, however "
                "little air it is given?",
        "options": [
            {"text": "Because soot is unreacted carbon, and hydrogen contains "
                     "no carbon",
             "correct": True},
            {"text": "Because hydrogen burns so hot that any soot formed "
                     "would be burned away again before it could settle "
                     "anywhere",
             "correct": False,
             "why": "There is no soot to burn away. Soot is unreacted carbon, "
                    "and hydrogen has none"},
            {"text": "Because hydrogen always burns completely",
             "correct": False,
             "why": "Starve it of air and less of it burns. What it cannot do "
                    "is make soot"},
            {"text": "Because the water that it makes washes all the soot away "
                     "as fast as it can form",
             "correct": False,
             "why": "The water leaves as vapour, and there is no soot for it "
                    "to wash"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s10",
        "band": "standard",
        "text": "Shutting the air hole on a burner makes the flame yellow "
                "rather than putting it out. Why does it not go out "
                "altogether?",
        "options": [
            {"text": "Because a flame carries on burning on its own heat once "
                     "it is lit",
             "correct": False,
             "why": "No oxygen means no combustion, as the candle under the "
                    "jar shows. Some air is still getting in"},
            {"text": "Because air still reaches the flame from around it, so "
                     "it burns incompletely rather than not at all",
             "correct": True},
            {"text": "Because the gas contains enough oxygen of its own to "
                     "keep going",
             "correct": False,
             "why": "Methane is carbon and hydrogen only. Every oxygen atom "
                    "has to come from the air"},
            {"text": "Because the air hole controls the gas rather than the "
                     "air",
             "correct": False,
             "why": "The gas tap controls the gas. The collar controls how "
                    "much air is mixed in before the flame"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-01-h05",
        "band": "harder",
        "text": "Why does incomplete combustion release LESS energy from the "
                "same amount of fuel?",
        "options": [
            {"text": "Because some of the carbon has not finished reacting, "
                     "so the energy that would have come from it is still "
                     "locked in the soot",
             "correct": True},
            {"text": "Because the yellow flame spreads its energy over a "
                     "larger area",
             "correct": False,
             "why": "That is about where the heat goes. Less energy is "
                    "RELEASED in the first place"},
            {"text": "Because the soot absorbs the energy as it forms",
             "correct": False,
             "why": "The soot never released its energy at all. It is not "
                    "taking any back"},
            {"text": "Because carbon monoxide is a cold gas",
             "correct": False,
             "why": "It leaves at flame temperature like everything else. "
                    "What it carries away is unreleased energy"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h06",
        "band": "harder",
        "text": "Carbon monoxide sticks to the haemoglobin in red blood cells "
                "far more strongly than oxygen does, and does not let go. Why "
                "does that make it so hard to notice?",
        "options": [
            {"text": "Because it acts only after several days, by which time "
                     "the person has usually left the room and cannot connect "
                     "the two things",
             "correct": False,
             "why": "It acts within an hour or two in a poorly ventilated "
                    "room. The problem is that the symptoms are ordinary "
                    "ones"},
            {"text": "Because the blood keeps circulating normally while it "
                     "carries less and less oxygen, and the early symptoms "
                     "look like tiredness",
             "correct": True},
            {"text": "Because it smells faintly of gas, which people ignore",
             "correct": False,
             "why": "It has no smell whatever. The smell in a gas leak is "
                    "added to the gas on purpose"},
            {"text": "Because it makes breathing painful, which people put "
                     "down to a cold",
             "correct": False,
             "why": "Breathing feels normal, which is part of the danger. The "
                    "blood is the thing affected"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h07",
        "band": "harder",
        "text": "A candle burns with a yellow flame and a gas hob with a blue "
                "one. Is the candle badly designed?",
        "options": [
            {"text": "Yes — a yellow flame wastes fuel, so a candle would "
                     "last longer",
             "correct": False,
             "why": "It would last longer and give almost no light. The soot "
                    "glowing is the whole point of a candle"},
            {"text": "No — a candle's flame is blue at the base, so it is "
                     "burning completely after all",
             "correct": False,
             "why": "There is a blue region, and most of the flame is "
                    "burning incompletely. That is what makes it bright"},
            {"text": "No — the yellow glow is soot burning brightly, and "
                     "light is what a candle is for",
             "correct": True},
            {"text": "Yes — the soot is dangerous to breathe",
             "correct": False,
             "why": "A candle's real hazard is the carbon monoxide in an "
                    "unventilated room, and the design question is about "
                    "what a candle is FOR"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h08",
        "band": "harder",
        "text": "A fuel is burned in plenty of air and the only product is "
                "water. What does that tell you about the fuel?",
        "options": [
            {"text": "That it contains no oxygen of its own, which is why "
                     "everything in the products has had to come out of the "
                     "air instead",
             "correct": False,
             "why": "A hydrocarbon holds no oxygen either and still gives "
                    "carbon dioxide. What is missing here is carbon"},
            {"text": "That it burned incompletely",
             "correct": False,
             "why": "Incomplete combustion gives soot and carbon monoxide. "
                    "Water alone is a complete burn of a carbon-free fuel"},
            {"text": "That it was burned in oxygen rather than in air",
             "correct": False,
             "why": "The nitrogen in air takes no part either way. The "
                    "products depend on the fuel"},
            {"text": "That it contains no carbon",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h09",
        "band": "harder",
        "text": "A car engine draws in air and still puts carbon monoxide out "
                "of the exhaust. What does that show?",
        "options": [
            {"text": "That an air supply does not guarantee complete "
                     "combustion — inside a cylinder there is not always "
                     "enough oxygen where the fuel is",
             "correct": True},
            {"text": "That petrol is a fuel that cannot burn completely under "
                     "any conditions at all, which is why every engine ever "
                     "built produces the gas",
             "correct": False,
             "why": "Petrol burns completely given enough oxygen. The "
                    "difficulty is mixing it well enough inside a cylinder"},
            {"text": "That the engine is faulty and needs servicing",
             "correct": False,
             "why": "Even a healthy engine makes some, which is why a "
                    "catalytic converter is fitted"},
            {"text": "That air contains carbon monoxide already",
             "correct": False,
             "why": "Clean air holds almost none. It is made in the "
                    "cylinder"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h10",
        "band": "harder",
        "text": "The lesson says a clean flame is not the same as a clean "
                "fuel. What does that mean for a hydrogen car?",
        "options": [
            {"text": "That the water coming out of the exhaust pipe is not "
                     "really clean, because it carries traces of the fuel "
                     "that did not manage to burn on the way through",
             "correct": False,
             "why": "The water is clean. What is not clean is how the "
                    "hydrogen was produced"},
            {"text": "That the exhaust is water, and the carbon dioxide may "
                     "have been released where the hydrogen was made",
             "correct": True},
            {"text": "That hydrogen does not burn completely",
             "correct": False,
             "why": "It burns completely to water. The problem is upstream of "
                    "the car"},
            {"text": "That the car is bound to be worse for the atmosphere "
                     "than a petrol one, whatever anybody says about its "
                     "exhaust",
             "correct": False,
             "why": "That depends entirely on how the hydrogen was made, "
                    "which is the point — the question has to be asked"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h11",
        "band": "harder",
        "text": "Charcoal is almost pure carbon. Burned on an open "
                "barbecue it gives carbon dioxide; brought into a tent it "
                "kills people. What has changed?",
        "options": [
            {"text": "The tent traps the smoke, and smoke is what does the "
                     "harm",
             "correct": False,
             "why": "Smoke is unpleasant and visible. What kills is a "
                    "colourless gas made because the air ran short"},
            {"text": "The temperature, because charcoal burns hotter indoors",
             "correct": False,
             "why": "It burns cooler with less air. The change that matters "
                    "is which gas it produces"},
            {"text": "The air supply — with too little oxygen the charcoal "
                     "makes carbon monoxide instead",
             "correct": True},
            {"text": "Nothing chemical — the danger is the fire spreading",
             "correct": False,
             "why": "Fire is a real risk and it is not what makes this case "
                    "notorious. The poisoning happens with no flames "
                    "spreading at all"},
        ],
        "figure": None,
    },
]
