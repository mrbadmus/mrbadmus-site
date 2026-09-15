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

    # ── easier · MRB-338 night-3 top-up ─────────────────────────────────
    #
    # The fire triangle is the lesson's largest untouched block — a reference
    # panel with three cards and a closing line about chip-pan and electrical
    # fires — and nothing in the first twenty-two rows asked about it. It
    # carries e12–e15 and e23 here, the Bunsen's own controls carry e16, e17,
    # e21 and e28, and the rest are the fuels and the vocabulary the page
    # defines and then never tests.
    {
        "id": "c5-01-e12",
        "band": "easier",
        "text": "Name the three things a fire needs.",
        "options": [
            {"text": "Fuel, smoke and heat",
             "correct": False,
             "why": "Smoke is something a fire produces. It is not one of the "
                    "things it needs in order to keep going"},
            {"text": "Oxygen, heat and carbon dioxide",
             "correct": False,
             "why": "Carbon dioxide is a product, and an extinguisher full of "
                    "it is used to put fires OUT"},
            {"text": "Fuel, oxygen and heat",
             "correct": True},
            {"text": "Fuel, oxygen and water",
             "correct": False,
             "why": "Water is what you put on a fire to stop it, by cooling "
                    "the fuel down"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e13",
        "band": "easier",
        "text": "A fire blanket is pulled over a burning frying pan and the "
                "flames stop. Which of the three things a fire needs has the "
                "blanket taken away?",
        "options": [
            {"text": "The heat",
             "correct": False,
             "why": "A blanket traps heat rather than removing it, and the oil "
                    "underneath stays hot for a long time"},
            {"text": "The smoke",
             "correct": False,
             "why": "Smoke is made by the fire, and it is not one of the three "
                    "things a fire needs"},
            {"text": "The fuel",
             "correct": False,
             "why": "All of the oil is still in the pan. Nothing has been "
                    "taken out of it"},
            {"text": "The oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e14",
        "band": "easier",
        "text": "A firebreak is a strip cleared through a forest ahead of a "
                "wildfire. Which of the three things a fire needs does it "
                "remove?",
        "options": [
            {"text": "The heat of the flames",
             "correct": False,
             "why": "The ground on either side of the strip is just as hot. "
                    "Clearing it cools nothing"},
            {"text": "The oxygen in the air",
             "correct": False,
             "why": "The air over a cleared strip is the same air. A firebreak "
                    "shuts none of it out"},
            {"text": "The fuel ahead of it",
             "correct": True},
            {"text": "The smoke it makes",
             "correct": False,
             "why": "Smoke drifts straight across a cleared strip, and it is "
                    "not one of the three in any case"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e15",
        "band": "easier",
        "text": "Water is sprayed onto a burning log. How does that help to "
                "put the fire out?",
        "options": [
            {"text": "It cools the wood below the temperature it needs to keep "
                     "burning",
             "correct": True},
            {"text": "It washes the fuel away from the flames",
             "correct": False,
             "why": "The log is still there, soaked but whole. Nothing has "
                    "been carried off"},
            {"text": "It reacts with the wood and turns it into something that "
                     "will not burn",
             "correct": False,
             "why": "Water does not react with wood at all. What it does is "
                    "take heat away from it"},
            {"text": "It adds hydrogen to the flames, which burns in place of "
                     "the wood",
             "correct": False,
             "why": "Nothing splits water apart on a bonfire. Water put on a "
                    "fire takes energy out of it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e16",
        "band": "easier",
        "text": "Which control on a Bunsen burner changes the SIZE of the "
                "flame?",
        "options": [
            {"text": "The collar at the bottom",
             "correct": False,
             "why": "The collar changes how much air mixes in, which changes "
                    "the colour rather than the size"},
            {"text": "The gas tap",
             "correct": True},
            {"text": "The height of the chimney",
             "correct": False,
             "why": "Every Bunsen has the same chimney and it does not move. "
                    "The size follows the gas supply"},
            {"text": "The flame colour",
             "correct": False,
             "why": "The colour is something you read off the flame, not a "
                    "control you can turn"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e17",
        "band": "easier",
        "text": "A Bunsen burner is lit but nothing is being heated yet. Which "
                "flame should it be left on?",
        "options": [
            {"text": "The yellow flame, because it can be seen from across a "
                     "bench",
             "correct": True},
            {"text": "The blue flame, because it uses less gas than a yellow "
                     "one does",
             "correct": False,
             "why": "Both flames use whatever gas the tap lets through. The "
                    "blue one simply finishes the reaction"},
            {"text": "The blue flame, because it is the safer of the two to "
                     "leave standing",
             "correct": False,
             "why": "A blue flame is almost invisible, which is exactly why it "
                    "is not the one to leave unattended"},
            {"text": "The yellow flame, because it is cool enough not to burn "
                     "anyone",
             "correct": False,
             "why": "A yellow flame is cooler and will still burn you. It is "
                    "left on because it can be SEEN"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e18",
        "band": "easier",
        "text": "Hydrogen is burned in a laboratory burner. What does the "
                "flame look like?",
        "options": [
            {"text": "Bright yellow",
             "correct": False,
             "why": "Yellow comes from glowing soot, and hydrogen has no "
                    "carbon in it to leave any"},
            {"text": "Almost invisible",
             "correct": True},
            {"text": "Green all the way through",
             "correct": False,
             "why": "Hydrogen gives no colour of its own. There is nothing "
                    "solid in the flame to glow"},
            {"text": "Orange and sooty",
             "correct": False,
             "why": "A candle is bright because of the soot in it. A hydrogen "
                    "flame has none"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e19",
        "band": "easier",
        "text": "Charcoal is burning on a barbecue in the open air. What do "
                "you see?",
        "options": [
            {"text": "A tall blue flame",
             "correct": False,
             "why": "A roaring blue flame is what a gas burner gives. Charcoal "
                    "is a solid and reacts at its surface"},
            {"text": "An orange glow with hardly any flame",
             "correct": True},
            {"text": "A yellow flame with black smoke",
             "correct": False,
             "why": "That is a fuel burning badly. Charcoal in the open air "
                    "glows rather than flames"},
            {"text": "No light until the fuel is gone",
             "correct": False,
             "why": "You can see the charcoal glowing, which is how you know "
                    "it is lit"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e20",
        "band": "easier",
        "text": "Which of these fuels contains no carbon at all?",
        "options": [
            {"text": "Candle wax",
             "correct": False,
             "why": "Candle wax is a hydrocarbon, so it is made of carbon and "
                    "hydrogen"},
            {"text": "Charcoal",
             "correct": False,
             "why": "Charcoal is almost pure carbon, which is why burning it "
                    "gives carbon dioxide"},
            {"text": "Methane",
             "correct": False,
             "why": "Methane is a hydrocarbon. Burning it completely gives "
                    "carbon dioxide as well as water"},
            {"text": "Hydrogen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e21",
        "band": "easier",
        "text": "What does the metal collar at the bottom of a Bunsen burner "
                "control?",
        "options": [
            {"text": "How much gas comes out of the jet",
             "correct": False,
             "why": "The gas is set by the tap. The collar is nowhere near the "
                    "supply"},
            {"text": "How tall the flame is allowed to grow above the chimney",
             "correct": False,
             "why": "The height follows the gas supply. Open the collar and "
                    "the colour changes, not the height"},
            {"text": "How hot the gas is before it reaches the flame",
             "correct": False,
             "why": "The gas arrives at room temperature whatever the collar "
                    "is set to"},
            {"text": "How much air is mixed with the gas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e22",
        "band": "easier",
        "text": "Which gas in the air does a fuel react with when it burns?",
        "options": [
            {"text": "Nitrogen",
             "correct": False,
             "why": "Nitrogen makes up most of the air and takes no part in "
                    "ordinary burning"},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "Carbon dioxide is a product of burning, and a jar of it "
                    "will put a flame out"},
            {"text": "Oxygen",
             "correct": True},
            {"text": "Water vapour",
             "correct": False,
             "why": "Water is made by burning a hydrocarbon rather than used "
                    "up by it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e23",
        "band": "easier",
        "text": "Why must water never be used on an electrical fire?",
        "options": [
            {"text": "Because water conducts electricity",
             "correct": True},
            {"text": "Because water puts the fire out too quickly",
             "correct": False,
             "why": "Putting a fire out quickly is what you want. The hazard "
                    "here is the current"},
            {"text": "Because water reacts with copper",
             "correct": False,
             "why": "Water does not react with copper wiring. What it does is "
                    "carry a current"},
            {"text": "Because the steam is dangerous",
             "correct": False,
             "why": "Steam is not the hazard. A shock carried through the "
                    "water is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e24",
        "band": "easier",
        "text": "What does the word INCOMPLETE mean in incomplete combustion?",
        "options": [
            {"text": "That only part of the fuel was put into the burner",
             "correct": False,
             "why": "All of the fuel reaches the flame. What is short is the "
                    "oxygen"},
            {"text": "That the reaction did not finish, because the oxygen ran "
                     "short",
             "correct": True},
            {"text": "That the flame went out before the fuel was used up",
             "correct": False,
             "why": "The flame is still burning. It is the reaction inside it "
                    "that is not finishing"},
            {"text": "That some of the fuel leaked out of the pipe before it "
                     "could reach the flame at all",
             "correct": False,
             "why": "Nothing leaks. The fuel arrives at the flame and does not "
                    "finish reacting there"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e25",
        "band": "easier",
        "text": "A candle is burning steadily. What is the fuel?",
        "options": [
            {"text": "The wick",
             "correct": False,
             "why": "The wick carries melted wax up to the flame. It is the "
                    "wax that burns"},
            {"text": "The air around the flame",
             "correct": False,
             "why": "The air supplies the oxygen. A fuel is the substance that "
                    "reacts with it"},
            {"text": "The wax",
             "correct": True},
            {"text": "The heat of the match that lit it",
             "correct": False,
             "why": "The match starts it off. After that the candle burns its "
                    "own wax"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e26",
        "band": "easier",
        "text": "Which of these fuels is a hydrocarbon?",
        "options": [
            {"text": "Charcoal",
             "correct": False,
             "why": "Charcoal is almost pure carbon, with no hydrogen in it at "
                    "all"},
            {"text": "Hydrogen",
             "correct": False,
             "why": "Hydrogen holds no carbon, so it cannot be a hydrocarbon"},
            {"text": "Propane",
             "correct": True},
            {"text": "Carbon",
             "correct": False,
             "why": "Carbon on its own is one element. A hydrocarbon has "
                    "hydrogen joined to it as well"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e27",
        "band": "easier",
        "text": "Where does the oxygen for an ordinary flame come from?",
        "options": [
            {"text": "From the air around it",
             "correct": True},
            {"text": "From the fuel itself",
             "correct": False,
             "why": "A fuel such as methane is carbon and hydrogen only. Every "
                    "oxygen atom comes from outside"},
            {"text": "From the heat of the flame",
             "correct": False,
             "why": "Heat makes no new substance. It only gets the reaction "
                    "going"},
            {"text": "From the water vapour",
             "correct": False,
             "why": "Water is a product of burning a hydrocarbon, not the "
                    "source of the oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e28",
        "band": "easier",
        "text": "A clean beaker is held over a blue Bunsen flame and comes "
                "away still clean. What does that tell you?",
        "options": [
            {"text": "That the flame is too cool to mark the glass",
             "correct": False,
             "why": "The blue flame is the hotter of the two. Temperature is "
                    "not what makes the mark"},
            {"text": "That the gas is burning completely",
             "correct": True},
            {"text": "That the beaker was wet, so nothing could stick to it",
             "correct": False,
             "why": "A dry beaker over a blue flame stays clean too. There is "
                    "simply no soot being made"},
            {"text": "That the gas supply is running low",
             "correct": False,
             "why": "The flame is burning normally. A blue flame leaves no "
                    "soot however much gas flows"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e29",
        "band": "easier",
        "text": "Which fuel is almost pure carbon?",
        "options": [
            {"text": "Methane",
             "correct": False,
             "why": "Methane is a hydrocarbon, so it holds hydrogen as well as "
                    "carbon"},
            {"text": "Propane",
             "correct": False,
             "why": "Propane is a hydrocarbon, so it holds hydrogen as well as "
                    "carbon"},
            {"text": "Candle wax",
             "correct": False,
             "why": "Candle wax is a hydrocarbon, made of carbon and hydrogen "
                    "together"},
            {"text": "Charcoal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-e30",
        "band": "easier",
        "text": "Carbon monoxide is described as odourless. What does that "
                "word mean?",
        "options": [
            {"text": "It has no smell",
             "correct": True},
            {"text": "It has no colour",
             "correct": False,
             "why": "It has no colour either, and that is a different word. "
                    "Odourless is about smell"},
            {"text": "It cannot be tasted",
             "correct": False,
             "why": "Taste is a third thing again. Odourless means there is "
                    "nothing to smell"},
            {"text": "It does not dissolve",
             "correct": False,
             "why": "Whether it dissolves is not what the word describes at "
                    "all"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night-3 top-up ───────────────────────────────
    {
        "id": "c5-01-s11",
        "band": "standard",
        "text": "Why does throwing water on a burning chip pan make it far "
                "worse rather than putting it out?",
        "options": [
            {"text": "The water sinks into the hot oil, turns to steam at once "
                     "and throws burning oil out of the pan",
             "correct": True},
            {"text": "The water puts the flames out for a moment and leaves "
                     "the oil hot enough to catch again straight afterwards",
             "correct": False,
             "why": "The flames are not put out even for a moment. The oil "
                    "leaves the pan still burning"},
            {"text": "The water reacts with the oil and makes a gas that burns "
                     "more fiercely",
             "correct": False,
             "why": "Oil and water do not react. What happens is a change of "
                    "state, and it happens instantly"},
            {"text": "The water cools the metal pan so quickly that it splits "
                     "open",
             "correct": False,
             "why": "The pan is not what fails. The burning oil is thrown out "
                    "of it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s12",
        "band": "standard",
        "text": "Turning the gas tap up makes a Bunsen flame taller, but it "
                "stays blue. Why does the colour not change?",
        "options": [
            {"text": "Because a flame keeps whatever colour it had when it was "
                     "lit, whatever is done to it afterwards",
             "correct": False,
             "why": "Shut the collar on a lit burner and the same flame turns "
                    "yellow within a second"},
            {"text": "Because the colour depends on the temperature of the gas "
                     "arriving, which the tap does not change",
             "correct": False,
             "why": "The gas arrives at room temperature whatever the tap "
                    "does, and moving the collar still changes the colour"},
            {"text": "Because the colour depends on how much air is mixed in, "
                     "which the tap does not change",
             "correct": True},
            {"text": "Because more gas always brings more air in with it",
             "correct": False,
             "why": "The collar decides the air. More gas through the same "
                    "collar means less air for each bit of gas"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s13",
        "band": "standard",
        "text": "Propane in a camping stove and wax in a candle burn to give "
                "the same two products, though one is a gas and one is a "
                "solid. Why?",
        "options": [
            {"text": "Because both are burned in the same air, and the air is "
                     "what decides the products",
             "correct": False,
             "why": "The air supplies oxygen to both. What comes out depends "
                    "on what the fuel is made of"},
            {"text": "Because anything that burns gives carbon dioxide and "
                     "water, whatever it happens to be made of",
             "correct": False,
             "why": "Hydrogen burns and gives water only; charcoal burns and "
                    "gives carbon dioxide only"},
            {"text": "Because a solid melts and then boils, so every fuel is "
                     "really burning as a gas by the time it reaches the flame",
             "correct": False,
             "why": "The wax does melt, and that is not the reason. The "
                    "products follow the atoms in the fuel"},
            {"text": "Because both are hydrocarbons, so the carbon becomes "
                     "carbon dioxide and the hydrogen becomes water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s14",
        "band": "standard",
        "text": "A gas ring is badly adjusted and the base of a saucepan used "
                "on it turns black. Explain what is happening.",
        "options": [
            {"text": "The pan is far colder than the flame, so the carbon "
                     "dioxide from the burning gas freezes onto its base",
             "correct": False,
             "why": "Carbon dioxide stays a gas on a warm saucepan. The black "
                    "mark is solid carbon"},
            {"text": "Too little air is reaching the flame, so some carbon "
                     "does not finish reacting and lands on the cold metal",
             "correct": True},
            {"text": "The gas supply is dirty, and the dirt in it is being "
                     "left behind on the pan",
             "correct": False,
             "why": "The same gas burns clean on a well adjusted ring. The "
                    "soot is made in the flame"},
            {"text": "The metal of the pan is being burned away by the heat",
             "correct": False,
             "why": "The pan is unharmed underneath. Wipe the black off and "
                    "the metal is as it was"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s15",
        "band": "standard",
        "text": "A gas fire burns with a blue flame until the air vents in the "
                "room are blocked up, and then it turns yellow. Explain.",
        "options": [
            {"text": "The gas pressure rises once the room is sealed, so more "
                     "gas reaches the flame",
             "correct": False,
             "why": "Sealing a room does nothing to a gas supply that comes "
                    "along a pipe"},
            {"text": "The room gets warmer, and a warmer room makes a flame "
                     "burn yellow",
             "correct": False,
             "why": "A flame is far hotter than any room. Blocking a vent "
                    "changes the air supply, not the temperature"},
            {"text": "Less air can reach the flame, so the gas no longer "
                     "finishes reacting",
             "correct": True},
            {"text": "Blocked vents trap dust, which is drawn into the flame "
                     "and glows",
             "correct": False,
             "why": "The yellow is soot made from the gas itself, and it "
                    "appears in a spotless room too"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s16",
        "band": "standard",
        "text": "Why is a carbon dioxide extinguisher a good choice for a fire "
                "in electrical equipment?",
        "options": [
            {"text": "It smothers the fire without conducting electricity the "
                     "way water would",
             "correct": True},
            {"text": "It cools the equipment down faster than water does",
             "correct": False,
             "why": "Cooling is not what it is for. It works by keeping air "
                    "away from the fuel"},
            {"text": "It reacts with the burning material so that it cannot "
                     "catch again",
             "correct": False,
             "why": "Carbon dioxide takes no part in the reaction. It simply "
                    "keeps the oxygen out"},
            {"text": "It puts extra oxygen into the room, which burns the fire "
                     "out quickly",
             "correct": False,
             "why": "More oxygen would make a fire worse. This gas is there to "
                    "keep oxygen away"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s17",
        "band": "standard",
        "text": "A wildfire reaches a cleared firebreak and stops, even though "
                "the ground on the far side is hot and dry. Why?",
        "options": [
            {"text": "The air over a cleared strip holds less oxygen than the "
                     "air over trees",
             "correct": False,
             "why": "It is the same air on either side. The strip works by "
                    "removing fuel"},
            {"text": "The cleared ground is cooler than the burning ground "
                     "behind it",
             "correct": False,
             "why": "Clearing a strip does not cool it. What has gone from it "
                    "is the fuel"},
            {"text": "There is nothing left on the strip for the fire to burn",
             "correct": True},
            {"text": "The fire has used up all the oxygen by the time it "
                     "arrives",
             "correct": False,
             "why": "A wildfire in the open is never short of air. It is short "
                    "of something to burn"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s18",
        "band": "standard",
        "text": "Blowing gently on glowing embers makes them burn more "
                "brightly. Why?",
        "options": [
            {"text": "Blowing adds carbon from your breath as extra fuel",
             "correct": False,
             "why": "Your breath adds no fuel. It adds air, and with it "
                    "oxygen"},
            {"text": "Blowing cools the embers, and a cooler fire burns "
                     "brighter",
             "correct": False,
             "why": "Cooling a fire slows it down. What blowing brings is "
                    "fresh air"},
            {"text": "Blowing pushes the carbon dioxide back into the embers",
             "correct": False,
             "why": "Carbon dioxide put back would smother them. What arrives "
                    "is oxygen"},
            {"text": "Blowing supplies more oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s19",
        "band": "standard",
        "text": "Methane burns with a tall flame above the burner, while "
                "charcoal glows with hardly any flame. What is the difference?",
        "options": [
            {"text": "Charcoal is burning incompletely and methane is burning "
                     "completely, which is what makes one of them glow",
             "correct": False,
             "why": "Charcoal in the open air has plenty of oxygen. The glow "
                    "is a solid reacting at its surface"},
            {"text": "Charcoal is a solid reacting at its surface, while "
                     "methane is a gas burning above the jet",
             "correct": True},
            {"text": "Charcoal is not really burning, only being heated until "
                     "it glows",
             "correct": False,
             "why": "It is burning: it reacts with oxygen, gives out energy "
                    "and is used up"},
            {"text": "Charcoal has no carbon in it to make a flame with",
             "correct": False,
             "why": "Charcoal is almost pure carbon. What it lacks is any "
                    "hydrogen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s20",
        "band": "standard",
        "text": "A gas boiler has to be serviced by law. Which fault do those "
                "checks matter most for?",
        "options": [
            {"text": "A gas leak, because unburnt gas has no smell and would "
                     "not be noticed",
             "correct": False,
             "why": "A leak is a real hazard, and a smell is added to the gas "
                    "supply on purpose so that it is noticed"},
            {"text": "A flame burning too hot, because it can crack the heat "
                     "exchanger inside",
             "correct": False,
             "why": "A well adjusted flame is the hotter one, and heat is not "
                    "what the law is worried about"},
            {"text": "A flame burning incompletely, because it puts carbon "
                     "monoxide into the house",
             "correct": True},
            {"text": "A blocked pipe, because the boiler would use more gas "
                     "than it should",
             "correct": False,
             "why": "Wasting gas costs money. What the servicing is for is the "
                    "gas put into the room"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s21",
        "band": "standard",
        "text": "A hydrogen flame is almost invisible. Why does that make it "
                "dangerous in a laboratory?",
        "options": [
            {"text": "It spreads sideways further than a flame you can see",
             "correct": False,
             "why": "It is the same size as any other flame. What it lacks is "
                    "anything to see it by"},
            {"text": "It burns cooler than a visible flame, so a burn takes "
                     "longer to notice",
             "correct": False,
             "why": "A hydrogen flame is very hot. The danger is that you "
                    "cannot see where it is"},
            {"text": "It gives off carbon monoxide, which is invisible as well",
             "correct": False,
             "why": "Hydrogen holds no carbon, so it cannot make carbon "
                    "monoxide at any air supply"},
            {"text": "You can reach into it without seeing that it is there",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s22",
        "band": "standard",
        "text": "Carbon monoxide is very slightly lighter than air. Why does "
                "that make it more dangerous rather than less?",
        "options": [
            {"text": "It mixes right through a room instead of collecting "
                     "where it could be avoided",
             "correct": True},
            {"text": "It rises to the ceiling, where a smoke alarm cannot "
                     "reach it",
             "correct": False,
             "why": "It does not gather at the ceiling. It mixes through the "
                    "whole room"},
            {"text": "It floats out of an open window and takes the warning "
                     "with it",
             "correct": False,
             "why": "An open window helps, by bringing fresh air in. The gas "
                    "does not leave on its own"},
            {"text": "It presses down towards the floor, which is exactly "
                     "where a person lying asleep is breathing",
             "correct": False,
             "why": "That would be true of a heavy gas, and this one is not. "
                    "It mixes evenly through the room"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s23",
        "band": "standard",
        "text": "A cold lid held over a gas hob mists up, but a cold lid held "
                "over a charcoal barbecue stays dry. Why?",
        "options": [
            {"text": "The barbecue is a great deal hotter, so any water "
                     "landing on the lid boils straight off again",
             "correct": False,
             "why": "The lid stays dry from the start. No water is being made "
                    "for it to collect"},
            {"text": "Natural gas contains hydrogen, which burns to water, and "
                     "charcoal contains none",
             "correct": True},
            {"text": "Charcoal burns incompletely, so its water stays locked "
                     "up in the soot",
             "correct": False,
             "why": "Soot is carbon. With no hydrogen in the fuel no water can "
                    "be made at any air supply"},
            {"text": "The gas hob is wetter to begin with because its flame is "
                     "blue",
             "correct": False,
             "why": "A blue flame is a clean, dry flame. The water is made by "
                    "the reaction itself"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s24",
        "band": "standard",
        "text": "A fire blanket and a firebreak stop a fire in completely "
                "different ways. What does the fire triangle say about that?",
        "options": [
            {"text": "Both remove the heat, one by covering it and one by "
                     "clearing it",
             "correct": False,
             "why": "Neither of them cools anything. One shuts out air and one "
                    "takes away fuel"},
            {"text": "Only one of them can work, because the triangle allows a "
                     "single method",
             "correct": False,
             "why": "Both work. The triangle says any one of the three may be "
                    "taken away"},
            {"text": "Both remove the fuel, but at different distances from "
                     "the flames",
             "correct": False,
             "why": "A blanket leaves the fuel exactly where it was and shuts "
                    "the air out instead"},
            {"text": "Each removes a different one of the three",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s25",
        "band": "standard",
        "text": "Opening the collar makes a Bunsen hotter without the gas tap "
                "being touched. How can the same gas give out more heat?",
        "options": [
            {"text": "The gas burns faster, so all of the heat arrives in a "
                     "shorter time",
             "correct": False,
             "why": "Speed would not change how much energy the gas can give. "
                    "The amount released is what changes"},
            {"text": "The extra air is warmed as it comes in and carries heat "
                     "up into the flame with it",
             "correct": False,
             "why": "Cold air arriving cannot add heat. What it adds is "
                    "oxygen"},
            {"text": "More of it finishes reacting, and a finished reaction "
                     "gives out all the energy available",
             "correct": True},
            {"text": "The flame is smaller, so the heat is packed into less "
                     "space",
             "correct": False,
             "why": "It is not about where the heat goes. More energy is "
                    "coming out of the same gas"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s26",
        "band": "standard",
        "text": "A candle burns yellow while a Bunsen with its collar open "
                "burns blue. Both fuels are hydrocarbons. What is different?",
        "options": [
            {"text": "The candle wax is a solid, and a solid can only burn at "
                     "its surface, which never lets in enough air",
             "correct": False,
             "why": "Charcoal is a solid and burns completely in the open air. "
                    "The state of the fuel is not the point"},
            {"text": "The burner mixes air with the gas before it burns, while "
                     "a candle gets air only at the edge of its flame",
             "correct": True},
            {"text": "The candle is burning a fuel with far more carbon in it "
                     "than natural gas has",
             "correct": False,
             "why": "Both are hydrocarbons. What differs is how the air "
                    "reaches the flame"},
            {"text": "The burner is hotter to start with, and hot flames burn "
                     "blue",
             "correct": False,
             "why": "The blue flame is hotter BECAUSE it is finishing. It is "
                    "not blue because it is hot"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s27",
        "band": "standard",
        "text": "Sand is shovelled over a small fire and it goes out. Which of "
                "the three has the sand taken away, and how can you tell?",
        "options": [
            {"text": "All three of them at once, because a thick layer of sand "
                     "covers the whole of the fire",
             "correct": False,
             "why": "The fuel is still there and still hot. Only the air has "
                    "been shut out"},
            {"text": "The heat, because sand is cold and there is a great deal "
                     "of it",
             "correct": False,
             "why": "Rake the sand off quickly and the fuel underneath is "
                    "still hot enough to relight"},
            {"text": "The fuel, because the sand buries it out of reach of the "
                     "flames",
             "correct": False,
             "why": "Burying the fuel does not remove it. The sand works by "
                    "keeping air off it"},
            {"text": "The oxygen, because the fuel and the heat are both still "
                     "there under the sand",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s28",
        "band": "standard",
        "text": "A bonfire that nobody touches eventually goes out on its own. "
                "Which of the three has run out?",
        "options": [
            {"text": "The heat, because the flames cool as the night goes on",
             "correct": False,
             "why": "The fire is the thing making the heat. It cools because "
                    "the burning has stopped"},
            {"text": "The oxygen, because a fire in the open uses up the air "
                     "around it",
             "correct": False,
             "why": "Outdoors the air is replaced as fast as it is used. There "
                    "is no shortage of it"},
            {"text": "The fuel, once everything that could burn has burned",
             "correct": True},
            {"text": "The carbon dioxide it needs to keep going",
             "correct": False,
             "why": "Carbon dioxide is a product. A fire does not need it and "
                    "goes out in it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s29",
        "band": "standard",
        "text": "A blue Bunsen flame is around 1500 °C and a yellow one is "
                "around 1000 °C. How much hotter is the blue flame?",
        "options": [
            {"text": "1.5 °C",
             "correct": False,
             "why": "That is one temperature divided by the other, which is "
                    "not a temperature at all"},
            {"text": "1500 °C",
             "correct": False,
             "why": "That is the temperature of the blue flame, not the "
                    "difference between the two"},
            {"text": "2500 °C",
             "correct": False,
             "why": "That is the two temperatures added together. A difference "
                    "is found by subtracting"},
            {"text": "500 °C",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-s30",
        "band": "standard",
        "text": "Charcoal glows with hardly any flame. Why is burning it still "
                "called combustion?",
        "options": [
            {"text": "Because a solid is being turned into a gas by the heat",
             "correct": False,
             "why": "That would be a change of state. Here the carbon is "
                    "reacting with oxygen"},
            {"text": "Because anything that gets hot enough to glow is "
                     "combustion",
             "correct": False,
             "why": "An electric ring glows and nothing in it is burning"},
            {"text": "Because a fuel is reacting with oxygen and giving out "
                     "energy",
             "correct": True},
            {"text": "Because carbon dioxide is being made, and that is what "
                     "names the reaction",
             "correct": False,
             "why": "Carbon dioxide comes out of other reactions too. A fuel "
                    "plus oxygen is what names this one"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night-3 top-up ─────────────────────────────────
    {
        "id": "c5-01-h12",
        "band": "harder",
        "text": "Water thrown onto a burning chip pan produces a fireball. "
                "Explain what the water does when it meets oil at frying "
                "temperature.",
        "options": [
            {"text": "It floats on top of the oil and spreads the flames "
                     "sideways right across the surface of the pan",
             "correct": False,
             "why": "Water is denser than oil and sinks through it, which is "
                    "what puts it under the heat"},
            {"text": "It sinks below the oil, flashes to steam and throws "
                     "burning oil up out of the pan",
             "correct": True},
            {"text": "It splits into hydrogen and oxygen, and the hydrogen "
                     "catches fire",
             "correct": False,
             "why": "Nothing in a kitchen splits water apart. The steam is "
                    "what does the damage"},
            {"text": "It cools the oil so quickly that the oil ignites a "
                     "second time",
             "correct": False,
             "why": "Cooling lights nothing. The oil is thrown out of the pan "
                    "while still alight"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h13",
        "band": "harder",
        "text": "The fire triangle names three things a fire needs. Why is "
                "it enough to take away only one of them?",
        "options": [
            {"text": "Because all three are needed together, so taking any one "
                     "away stops it",
             "correct": True},
            {"text": "Because the other two turn into each other once one of "
                     "them has gone",
             "correct": False,
             "why": "Nothing turns into anything else. They are three separate "
                    "requirements"},
            {"text": "Because the one you remove is the most important of the "
                     "three",
             "correct": False,
             "why": "None of them is more important than another. Any one "
                    "missing is enough"},
            {"text": "Because removing one makes the other two harder to "
                     "supply",
             "correct": False,
             "why": "The other two are untouched. The fire stops because one "
                    "requirement is simply absent"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h14",
        "band": "harder",
        "text": "In a high wind a wildfire crosses a firebreak that had been "
                "cleared down to the soil. Does that show the firebreak idea "
                "is wrong?",
        "options": [
            {"text": "No — burning material was carried over by the wind, so "
                     "fuel reached the far side",
             "correct": True},
            {"text": "Yes — clearing fuel has no effect on a fire that is hot "
                     "enough",
             "correct": False,
             "why": "Firebreaks stop fires every year. This one was crossed by "
                    "material blown across it"},
            {"text": "No — the fire crossed because the cleared soil was a "
                     "great deal hotter than the shaded trees",
             "correct": False,
             "why": "Bare soil is not a fuel and cannot carry a fire. "
                    "Something burning was blown over"},
            {"text": "Yes — a fire needs only oxygen and heat once it is going "
                     "properly",
             "correct": False,
             "why": "It needs fuel for as long as it burns, which is why a "
                    "cleared strip works at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h15",
        "band": "harder",
        "text": "A carbon dioxide extinguisher puts a fire out. A minute "
                "later, with the extinguisher put away, the fire starts again. "
                "Explain.",
        "options": [
            {"text": "The extinguisher laid new fuel onto the fire, which "
                     "caught again as soon as it had warmed through",
             "correct": False,
             "why": "Carbon dioxide is not a fuel and does not burn"},
            {"text": "Only the oxygen was taken away, and the fuel and the "
                     "heat were both still there when the air came back",
             "correct": True},
            {"text": "The carbon dioxide turned back into oxygen as it warmed "
                     "up in the room",
             "correct": False,
             "why": "It does not turn into oxygen. It drifts away and fresh "
                    "air replaces it"},
            {"text": "The fire was never out, and the gas only hid it from "
                     "view",
             "correct": False,
             "why": "The flames really did stop. What did not stop was the "
                    "fuel being hot"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h16",
        "band": "harder",
        "text": "A gas hob is lit in a small room with the door and window "
                "shut. The flames are blue at first and turn yellow after a "
                "while. Explain the change.",
        "options": [
            {"text": "The oxygen in the room is being used up, so less of it "
                     "reaches the flame and the reaction stops finishing",
             "correct": True},
            {"text": "The room warms up, and a warmer room makes any flame "
                     "burn yellow",
             "correct": False,
             "why": "A flame is far hotter than the room. What changed is how "
                    "much oxygen is left"},
            {"text": "The carbon dioxide made by the flame starts burning as "
                     "well, and it burns yellow",
             "correct": False,
             "why": "Carbon dioxide does not burn. It is what the carbon has "
                    "already become"},
            {"text": "The gas pressure falls as the supply empties, and low "
                     "pressure gives a yellow flame",
             "correct": False,
             "why": "Yellow is about air rather than pressure. A smaller "
                    "supply gives a smaller blue flame"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h17",
        "band": "harder",
        "text": "A jet engine stops working high in the atmosphere, but a "
                "rocket engine keeps running in space. Explain the difference.",
        "options": [
            {"text": "A jet is heavier, so it cannot climb as high as a rocket "
                     "can",
             "correct": False,
             "why": "Mass is not what stops it. It stops because there is no "
                    "air left to take oxygen from"},
            {"text": "A jet burns a fuel and a rocket does not need to burn "
                     "anything at all up there",
             "correct": False,
             "why": "A rocket burns fuel too. What it also carries is the "
                    "oxygen to burn it with"},
            {"text": "A rocket is hotter, and a hot enough flame does not need "
                     "oxygen",
             "correct": False,
             "why": "No flame burns without oxygen, however hot it is. The "
                    "rocket brings its own"},
            {"text": "A jet takes its oxygen from the air, and a rocket "
                     "carries its own supply",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h18",
        "band": "harder",
        "text": "Why is a blue flame on a boiler good evidence that THAT flame "
                "is not making carbon monoxide?",
        "options": [
            {"text": "Because carbon monoxide is faintly blue itself, so a "
                     "flame producing it would be coloured differently",
             "correct": False,
             "why": "Carbon monoxide has no colour at all, which is part of "
                    "what makes it dangerous"},
            {"text": "Because blue means the reaction is finishing, so every "
                     "carbon atom reaches carbon dioxide",
             "correct": True},
            {"text": "Because a hot flame destroys any carbon monoxide that "
                     "forms inside it",
             "correct": False,
             "why": "Nothing destroys it. It is simply never made when there "
                    "is enough oxygen"},
            {"text": "Because carbon monoxide comes only from solid fuels such "
                     "as charcoal",
             "correct": False,
             "why": "Any fuel containing carbon can make it, natural gas "
                    "included, once the air runs short"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h19",
        "band": "harder",
        "text": "Methane and hydrogen are burned in identical burners with the "
                "air hole shut. Describe how the two flames differ.",
        "options": [
            {"text": "Both of them go yellow and sooty, because shutting the "
                     "air hole does exactly the same thing to any fuel at all",
             "correct": False,
             "why": "Soot is unreacted carbon. Hydrogen has none, so it cannot "
                    "make any"},
            {"text": "The methane flame goes yellow and sooty, and the "
                     "hydrogen flame stays clean because it holds no carbon "
                     "at all",
             "correct": True},
            {"text": "Both stay clean, because shutting the air hole only "
                     "makes the flame smaller",
             "correct": False,
             "why": "The collar does not change the size. It makes the methane "
                    "flame incomplete"},
            {"text": "The hydrogen flame goes yellow and the methane flame "
                     "stays clean",
             "correct": False,
             "why": "It is the other way round. The carbon in the methane is "
                    "what makes the soot"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h20",
        "band": "harder",
        "text": "A yellow flame is never the flame you heat something with, "
                "yet a burner is deliberately left on a yellow flame between "
                "uses. Is that a contradiction?",
        "options": [
            {"text": "No — the safety flame is a different colour of yellow "
                     "from a heating flame",
             "correct": False,
             "why": "It is the same yellow, made the same way, by a collar "
                    "that has been shut"},
            {"text": "Yes — one of the two statements has to be wrong",
             "correct": False,
             "why": "Both are true. They describe two different jobs a flame "
                    "can be given"},
            {"text": "No — the safety flame is only ever there to be seen, "
                     "never to heat with",
             "correct": True},
            {"text": "Yes — a yellow flame is hotter when nothing is being "
                     "heated on it",
             "correct": False,
             "why": "Its temperature does not depend on what is held over it. "
                    "It is the cooler flame either way"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h21",
        "band": "harder",
        "text": "Burning charcoal is written as the word equation carbon + "
                "oxygen makes carbon dioxide. Why is it written for carbon "
                "rather than for charcoal?",
        "options": [
            {"text": "Because charcoal turns into pure carbon as soon as it "
                     "has been heated enough to start glowing",
             "correct": False,
             "why": "It does not change into something else first. It is "
                    "already mostly carbon"},
            {"text": "Because charcoal is mostly carbon, and the little else "
                     "in it takes no real part",
             "correct": True},
            {"text": "Because carbon is the only element that may be written "
                     "in a word equation",
             "correct": False,
             "why": "Word equations name substances of every kind, compounds "
                    "included"},
            {"text": "Because the ash in charcoal burns first and leaves pure "
                     "carbon behind",
             "correct": False,
             "why": "Ash does not burn at all, which is why it is what gets "
                    "left at the end"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h22",
        "band": "harder",
        "text": "A barbecue is carried indoors after the flames have died down "
                "and only a dull glow is left. Why is that more dangerous than "
                "carrying it in while it is flaming?",
        "options": [
            {"text": "A flaming barbecue would be noticed and put out, so only "
                     "a glowing one gets left alight",
             "correct": False,
             "why": "Being noticed is not the chemistry. The short air supply "
                    "is what makes the poison"},
            {"text": "A glowing barbecue is cooler, and cooler fuels give off "
                     "more smoke than hot ones do",
             "correct": False,
             "why": "Smoke is not what kills people here. The gas that does "
                    "has no colour and no smell"},
            {"text": "A glow means the charcoal is nearly finished, so it "
                     "gives off far more soot than before",
             "correct": False,
             "why": "Soot is visible and it is not the danger in a closed "
                    "room"},
            {"text": "A dull glow means very little air is reaching it, which "
                     "is the condition that makes carbon monoxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h23",
        "band": "harder",
        "text": "A candle and a gas fire are both burning with yellow flames "
                "in the same room. Which of them is producing carbon monoxide?",
        "options": [
            {"text": "Only the gas fire, because a candle is far too small to "
                     "make a poisonous gas",
             "correct": False,
             "why": "Size decides how much is made rather than whether any is. "
                    "A yellow candle flame makes some"},
            {"text": "Only the candle, because wax is a solid and solids burn "
                     "less completely",
             "correct": False,
             "why": "Both are hydrocarbons and both are short of air. The "
                    "state of the fuel is not the point"},
            {"text": "Both, because each fuel holds carbon and each is burning "
                     "incompletely",
             "correct": True},
            {"text": "Neither, because carbon monoxide comes only from coal "
                     "and charcoal",
             "correct": False,
             "why": "Any carbon fuel burning with too little air makes it, "
                    "natural gas included"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h24",
        "band": "harder",
        "text": "A flame can be producing carbon monoxide even when a beaker "
                "held in it comes away clean. Explain how that is possible.",
        "options": [
            {"text": "The beaker is too cold for soot to stick to it, so the "
                     "soot goes past and up into the room instead",
             "correct": False,
             "why": "Soot lands on cold glass readily, which is why the test "
                    "works at all"},
            {"text": "Combustion can fall short at carbon monoxide without "
                     "going all the way to soot",
             "correct": True},
            {"text": "The carbon monoxide burns the soot off the beaker as "
                     "fast as it lands there",
             "correct": False,
             "why": "Carbon monoxide leaves with the other gases and cleans "
                    "nothing"},
            {"text": "A clean beaker means complete combustion, so no carbon "
                     "monoxide is possible",
             "correct": False,
             "why": "Soot is the worst case. A flame can fail to finish "
                    "without going that far"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h25",
        "band": "harder",
        "text": "A hydrogen bus is refuelled with hydrogen made using "
                "electricity from wind turbines. How does that change the "
                "argument about hydrogen?",
        "options": [
            {"text": "It makes matters worse, because that electricity is "
                     "needed somewhere else",
             "correct": False,
             "why": "That is an argument about supply rather than about the "
                    "chemistry of the fuel"},
            {"text": "It changes nothing, because the exhaust was the part "
                     "being argued about",
             "correct": False,
             "why": "The exhaust was never the problem. The argument was about "
                    "where the hydrogen came from"},
            {"text": "The objection falls away, because no carbon dioxide is "
                     "released where the hydrogen is made either",
             "correct": True},
            {"text": "It changes nothing, because burning hydrogen releases "
                     "carbon dioxide anyway",
             "correct": False,
             "why": "Hydrogen holds no carbon, so burning it cannot release "
                    "any carbon dioxide"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h26",
        "band": "harder",
        "text": "Combustion gives out heat, yet the fire triangle lists heat "
                "as one of the things a fire needs. Explain why both can be "
                "true.",
        "options": [
            {"text": "The triangle is about putting fires out, so its heat is "
                     "the heat you remove",
             "correct": False,
             "why": "The three are what a fire needs. Removing one is only how "
                    "the triangle gets used"},
            {"text": "The heat on the triangle is the heat given out, so the "
                     "same heat is being counted twice over",
             "correct": False,
             "why": "The triangle lists what a fire needs. The heat given out "
                    "is a product of it"},
            {"text": "A fire needs heat from outside for the whole time that "
                     "it burns",
             "correct": False,
             "why": "Take the match away and a bonfire keeps going. Only the "
                    "start needs outside heat"},
            {"text": "Heat is needed to start it; once it is going the "
                     "reaction supplies its own",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h27",
        "band": "harder",
        "text": "A small fire in a metal box goes out when the lid is put on, "
                "though the fuel is untouched and still hot. How would you "
                "prove which requirement ran out?",
        "options": [
            {"text": "Weigh the box before and afterwards to find how much "
                     "fuel was used up",
             "correct": False,
             "why": "The mass tells you how much burned rather than why it "
                    "stopped"},
            {"text": "Take the lid off while the fuel is still hot and see "
                     "whether it catches again",
             "correct": True},
            {"text": "Measure the temperature inside and show that it fell "
                     "below the starting point",
             "correct": False,
             "why": "The box is still hot, which is exactly why the test is to "
                    "let air back in"},
            {"text": "Push more fuel in through a hole in the lid and see "
                     "whether the fire grows",
             "correct": False,
             "why": "Fuel is the one you already know is present. The question "
                    "is about the air"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h28",
        "band": "harder",
        "text": "With plenty of air, hydrogen gives water only, charcoal gives "
                "carbon dioxide only, and methane gives both. What decides the "
                "products?",
        "options": [
            {"text": "How much air each of the three fuels was given",
             "correct": False,
             "why": "All three had plenty of air. What differs is what the "
                    "fuel is made of"},
            {"text": "The temperature that each of the three flames reaches",
             "correct": False,
             "why": "Temperature follows from the reaction rather than "
                    "deciding what comes out of it"},
            {"text": "Which atoms the fuel is made of",
             "correct": True},
            {"text": "Whether the fuel is a solid, a liquid or a gas",
             "correct": False,
             "why": "Charcoal and candle wax are not gases, and both follow "
                    "the same rule"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h29",
        "band": "harder",
        "text": "A hydrogen flame is almost invisible and a candle flame is "
                "bright. Both are burning. What does the difference in "
                "brightness actually show?",
        "options": [
            {"text": "How much fuel is reaching each of the two flames",
             "correct": False,
             "why": "Turn a candle up and it is still yellow; a hydrogen flame "
                    "stays invisible"},
            {"text": "Which of the two flames is the hotter one",
             "correct": False,
             "why": "The hydrogen flame is very hot and gives out almost no "
                    "light"},
            {"text": "Whether there is glowing soot in the flame",
             "correct": True},
            {"text": "Whether the fuel is a solid or a gas",
             "correct": False,
             "why": "Methane is a gas and burns bright yellow once the collar "
                    "is shut"},
        ],
        "figure": None,
    },
    {
        "id": "c5-01-h30",
        "band": "harder",
        "text": "A gas hob is lit on a cold morning with an empty pan on "
                "the ring, and the kitchen window mists up. Explain where "
                "that water has come from.",
        "options": [
            {"text": "The flame drives moisture out of the food being cooked "
                     "and up onto the glass",
             "correct": False,
             "why": "The window mists with an empty pan on the ring too. The "
                    "water comes from the gas"},
            {"text": "Carbon dioxide from the flame turns liquid on a cold "
                     "surface",
             "correct": False,
             "why": "Carbon dioxide stays a gas on a cold window. What you can "
                    "see is water"},
            {"text": "The cold air outside pulls steam through the glass from "
                     "the room",
             "correct": False,
             "why": "Nothing passes through the glass. Water vapour in the "
                    "room condenses on its inner face"},
            {"text": "It is a product of burning the gas, and it condenses "
                     "on the cold glass",
             "correct": True},
        ],
        "figure": None,
    },
]
