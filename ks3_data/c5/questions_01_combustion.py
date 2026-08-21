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
        "band": "s",
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
        "band": "s",
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
        "band": "s",
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
        "band": "s",
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
        "band": "h",
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
        "band": "h",
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
        "band": "h",
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
        "band": "h",
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
]
