"""C2 lesson 06 — Conservation of mass: twelve questions (MRB-269).

These probe the one move the lesson exists to teach: separating what a reaction
did from what the balance was able to weigh. A reading that falls, a reading
that rises and a reading that does not budge are all the same rule, and the
questions push a student to say which gas went where rather than which way the
number moved. The distractors are built from the lesson's declared
misconception ATOM-11 — burning destroys mass, turning it into heat and light —
and from the three habits the bench is aimed at: counting only the solid you
can see, treating a sealed flask as a flask where less happens, and reading
"before = after" as though the air were not part of the before. The lesson
carries no figures, so every question is figure=None.
"""

UNIT = "C2"
LESSON = "conservation-of-mass"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-06-e01",
        "band": "easier",
        "text": "A reaction is run and everything is weighed. Which statement "
                "is the conservation of mass rule?",
        "options": [
            {"text": "The total mass of everything before equals the total "
                     "mass of everything after.",
             "correct": True},
            {"text": "The mass of the solid before equals the mass of the "
                     "solid after.",
             "correct": False,
             "why": "This only counts what you can see sitting on the pan. "
                    "Gases have mass too, and leaving them out is exactly why "
                    "an open flask looks like it breaks the rule."},
            {"text": "The mass after is always the mass before plus the mass "
                     "of a gas.",
             "correct": False,
             "why": "A gas can join, but it can also leave — marble and acid "
                    "in an open flask drop 2.20 g. The rule counts everything "
                    "on both sides; it does not always add."},
            {"text": "The mass after is always a little less, because some is "
                     "used up in reacting.",
             "correct": False,
             "why": "Nothing is used up in the sense of vanishing. Atoms are "
                    "rearranged into new substances, so reacting on its own "
                    "never costs you a gram."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e02",
        "band": "easier",
        "text": "In a chemical reaction, what happens to the atoms that were "
                "there at the start?",
        "options": [
            {"text": "Some are destroyed, which is why a burning candle "
                     "disappears from the plate.",
             "correct": False,
             "why": "Burning destroys no atoms at all. The wax leaves the "
                    "plate as carbon dioxide and water vapour — invisible, "
                    "floating away, and still every atom that was in the wax."},
            {"text": "They are rearranged into new substances, and none is "
                     "made and none is destroyed.",
             "correct": True},
            {"text": "New atoms are made, because the substances you end up "
                     "with are new ones.",
             "correct": False,
             "why": "A new substance is the same atoms joined up differently, "
                    "not new atoms. Rearranging alone is enough to make "
                    "something that looks and behaves completely different."},
            {"text": "They stay where they are and turn into atoms of a "
                     "different element instead.",
             "correct": False,
             "why": "Atoms do move — that is the rearranging. But an atom of "
                    "one element does not become an atom of another in a "
                    "chemical reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e03",
        "band": "easier",
        "text": "Marble chips and acid are sealed in a flask with a bung. The "
                "balance reads 152.00 g before, and inside the flask the "
                "mixture fizzes hard. What does it read after?",
        "options": [
            {"text": "149.80 g — the gas that formed has escaped the flask.",
             "correct": False,
             "why": "That is the open-flask reading. With a bung in, the "
                    "carbon dioxide cannot get out, so it is still sitting on "
                    "the balance."},
            {"text": "A little under 152.00 g, since gases weigh less than "
                     "solids do.",
             "correct": False,
             "why": "A gas does weigh less than the same volume of solid, but "
                    "nothing has left the flask. Nothing can be missing from a "
                    "reading if nothing has gone anywhere."},
            {"text": "152.00 g — exactly the same reading as before.",
             "correct": True},
            {"text": "Over 152.00 g, because a new gas has been made inside.",
             "correct": False,
             "why": "The gas is not new matter. Its atoms came out of the "
                    "marble and the acid that were already on the balance, so "
                    "the total cannot climb."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e04",
        "band": "easier",
        "text": "The bench has three tiles: Mass before, Mass after, and "
                "Where it went. The third one never shows a number off the "
                "balance. Why not?",
        "options": [
            {"text": "Because a gas has no mass until you have collected it "
                     "in something.",
             "correct": False,
             "why": "A gas has mass wherever it is. The 2.20 g that leaves an "
                    "open flask is 2.20 g of carbon dioxide in the room, "
                    "whether you catch it or not."},
            {"text": "Because a top-pan balance is not sensitive enough to "
                     "read a mass that small.",
             "correct": False,
             "why": "The balance is fine — it reads to 0.01 g. The problem is "
                    "not precision: gas that has drifted into the room is not "
                    "on the pan at all."},
            {"text": "Because a balance can only read solids, not liquids or "
                     "gases.",
             "correct": False,
             "why": "It reads whatever is on the pan, the acid and any trapped "
                    "gas included. What it cannot read is the part that has "
                    "left the flask."},
            {"text": "Because nothing can weigh a gas that has gone. You work "
                     "it out by subtracting.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-06-s01",
        "band": "standard",
        "text": "Marble chips and acid in an open flask: the reading falls "
                "from 152.00 g to 149.80 g. What has actually happened to "
                "those 2.20 g?",
        "options": [
            {"text": "They were used up making the bubbles and the fizzing "
                     "noise.",
             "correct": False,
             "why": "Bubbling and noise are not made of matter, so they cannot "
                    "account for a single gram. The 2.20 g is carbon dioxide, "
                    "and it has gone into the room."},
            {"text": "2.20 g of carbon dioxide has left the flask and is now "
                     "in the room.",
             "correct": True},
            {"text": "2.20 g of the acid has evaporated off the top of the "
                     "mixture.",
             "correct": False,
             "why": "A little water does evaporate slowly, but that is not "
                    "what this is. The flask is fizzing because carbon dioxide "
                    "is being made and pushed out."},
            {"text": "2.20 g of mass was destroyed as the marble was broken "
                     "down.",
             "correct": False,
             "why": "Nothing destroys mass. The marble's atoms are all still "
                    "there — some in the solution, and some in the gas that "
                    "has just left."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s02",
        "band": "standard",
        "text": "The same marble-and-acid reaction is run twice: once open to "
                "the air, once sealed with a bung. How does the mass of "
                "carbon dioxide made compare?",
        "options": [
            {"text": "The same mass is made both times. Only how much of it "
                     "stays on the balance changes.",
             "correct": True},
            {"text": "Less is made in the sealed flask, because the bung stops "
                     "it forming.",
             "correct": False,
             "why": "A bung does not reach inside the chemistry. The marble "
                    "and the acid react exactly the same way — the bung only "
                    "decides whether the gas can leave."},
            {"text": "More is made in the sealed flask, because pressure "
                     "builds up inside it.",
             "correct": False,
             "why": "Pressure does build up, but how much gas forms is set by "
                    "how much marble and acid react, not by whether the flask "
                    "is shut."},
            {"text": "None is made in the sealed flask, since there is nowhere "
                     "for it to go.",
             "correct": False,
             "why": "It has somewhere to go — the space above the liquid. The "
                    "gas forms either way; sealed, it simply stays where the "
                    "balance can still feel it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s03",
        "band": "standard",
        "text": "A student writes: 'The candle burned away, so its mass was "
                "destroyed — it turned into heat and light.' What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong. Mass really is destroyed when "
                     "something burns away to nothing.",
             "correct": False,
             "why": "This is the idea the lesson is built to break. Burn 60 g "
                    "of wax in a sealed box and the box reads exactly what it "
                    "read before, warm or not."},
            {"text": "Only the second half. The mass does turn into heat, and "
                     "heat has weight.",
             "correct": False,
             "why": "Heat is not a substance and has no mass to weigh. If it "
                    "did, a sealed box would get heavier as it warmed up, and "
                    "it does not."},
            {"text": "Only the first half. The mass is not destroyed, it stays "
                     "behind in the ash.",
             "correct": False,
             "why": "The plate is clean — there is no ash holding it. The wax "
                    "has left the plate completely, as gas."},
            {"text": "Heat and light are not made of atoms. The wax left as "
                     "carbon dioxide and water vapour.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s04",
        "band": "standard",
        "text": "3.00 g of magnesium ribbon is burned in an open crucible. "
                "The white powder left behind weighs 5.00 g. What mass of "
                "oxygen joined from the air?",
        "options": [
            {"text": "8.00 g — add the mass of the metal to the mass of the "
                     "powder.",
             "correct": False,
             "why": "That adds the start to the finish. The powder already "
                    "contains the 3.00 g of magnesium, so adding it in again "
                    "counts the metal twice."},
            {"text": "5.00 g — the powder is the new substance the oxygen "
                     "made.",
             "correct": False,
             "why": "The powder is magnesium and oxygen joined together. Only "
                    "the extra 2.00 g came out of the air; the rest is the "
                    "metal you started with."},
            {"text": "2.00 g — the powder is heavier than the metal by exactly "
                     "that much.",
             "correct": True},
            {"text": "None — a reaction cannot leave you with more mass than "
                     "you started with.",
             "correct": False,
             "why": "It can, whenever something joins from the air. Nothing "
                    "was added by hand, but the oxygen was in the room all "
                    "along and it has mass."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-06-h01",
        "band": "harder",
        "text": "For two hundred years burning was explained by saying a "
                "substance called phlogiston escaped as things burnt. Why did "
                "weighing a burning metal carefully finish the theory off?",
        "options": [
            {"text": "The metal lost mass, and phlogiston was never supposed "
                     "to have any.",
             "correct": False,
             "why": "Metals gain mass when they burn, and that is the whole "
                    "problem. Losing mass is what phlogiston predicted, so "
                    "that result would have propped the theory up."},
            {"text": "Phlogiston had never been seen, and a substance nobody "
                     "can see is not real.",
             "correct": False,
             "why": "Plenty of real things are invisible — the carbon dioxide "
                    "leaving an open flask, for one. The theory died on a "
                    "measurement, not on being invisible."},
            {"text": "The metal got heavier, so escaping phlogiston would need "
                     "negative mass.",
             "correct": True},
            {"text": "The weighing was done in a sealed flask, which "
                     "phlogiston had no way out of.",
             "correct": False,
             "why": "Sealing changes what you weigh, not what reacts. The "
                    "result that broke the theory was the gain in mass itself, "
                    "and it shows up in an open crucible."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h02",
        "band": "harder",
        "text": "A sealed bottle of fizzy drink is weighed. The cap is taken "
                "off, the drink is left until it goes flat, and the bottle is "
                "weighed again. What happens to the reading?",
        "options": [
            {"text": "It falls, because dissolved carbon dioxide has escaped "
                     "into the room.",
             "correct": True},
            {"text": "It stays the same, because going flat is not a chemical "
                     "reaction.",
             "correct": False,
             "why": "The reading tracks atoms, not reactions. Once the cap is "
                    "off, carbon dioxide leaves the bottle — and anything that "
                    "leaves takes its mass with it."},
            {"text": "It rises, because air moves in to fill the space the "
                     "bubbles left.",
             "correct": False,
             "why": "Air does move about above the drink, but it is not being "
                    "trapped — the bottle is open the whole time. What has "
                    "changed is the gas that has gone."},
            {"text": "It falls, because the bubbles burst and the drink loses "
                     "its energy.",
             "correct": False,
             "why": "You have the direction right for the wrong reason. Energy "
                    "has no mass to lose; the reading falls because carbon "
                    "dioxide that was dissolved in the drink is now in the "
                    "room."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h03",
        "band": "harder",
        "text": "Open, marble and acid run 152.00 g to 149.80 g. Sealed, the "
                "same reaction runs 152.00 g to 152.00 g. A student says the "
                "sealed flask made no gas. What mass did it really make?",
        "options": [
            {"text": "None. If gas had been made in there, the reading would "
                     "have gone up.",
             "correct": False,
             "why": "Gas made inside a sealed flask never moves the reading, "
                    "because its atoms were already on the balance. No change "
                    "is what conservation predicts, not evidence of nothing."},
            {"text": "2.20 g, but it was destroyed again inside the sealed "
                     "flask.",
             "correct": False,
             "why": "Nothing destroys mass, sealed or not. Those 2.20 g of "
                    "carbon dioxide are still in there, filling the space "
                    "above the liquid."},
            {"text": "You cannot tell without opening the flask and weighing "
                     "it a second time.",
             "correct": False,
             "why": "You can tell, from the open run. Same chemicals, same "
                    "reaction, same mass of gas — the bung changes only where "
                    "that gas ends up."},
            {"text": "2.20 g. The same reaction makes the same gas; the bung "
                     "just keeps it on the balance.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h04",
        "band": "harder",
        "text": "60 g of candle wax burns away completely in an open room. "
                "What is the total mass of the gases it produces?",
        "options": [
            {"text": "Exactly 60 g, because the mass before has to equal the "
                     "mass after.",
             "correct": False,
             "why": "The rule is right but the counting is short. The gases "
                    "are made from the wax and the oxygen that joined it, so "
                    "60 g is only part of what went in."},
            {"text": "More than 60 g, because oxygen from the air is in those "
                     "gases too.",
             "correct": True},
            {"text": "Less than 60 g, because some of the wax left as heat and "
                     "light instead.",
             "correct": False,
             "why": "Heat and light are not made of atoms and weigh nothing at "
                    "all. Every gram of the wax is in the gases; none of it "
                    "was subtracted on the way out."},
            {"text": "Just under 60 g, since the soot and the wick are left "
                     "behind on the plate.",
             "correct": False,
             "why": "The plate is clean, so nothing is being held back. Even a "
                    "little soot would not pull the total under 60 g, because "
                    "the oxygen adds far more than that."},
        ],
        "figure": None,
    },
]
