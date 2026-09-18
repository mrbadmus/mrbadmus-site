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
                     "escapes changes.",
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
            {"text": "2.20 g. The same reaction makes the same gas; the "
                     "bung keeps it in.",
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-06-e05",
        "band": "easier",
        "text": "What is a closed system?",
        "options": [
            {"text": "A container nothing can get into or out of, so "
                     "everything that takes part is on the balance",
             "correct": True},
            {"text": "A container that has had all of the air pumped out of "
                     "it first",
             "correct": False,
             "why": "Nothing has to be pumped out. What matters is that "
                    "nothing can cross the boundary either way"},
            {"text": "A reaction that has finished and cannot restart",
             "correct": False,
             "why": "The word describes the container, not the state of the "
                    "reaction"},
            {"text": "A flask that is too strong to break",
             "correct": False,
             "why": "Strength is not the point. A thin sealed bag is a closed "
                    "system too"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e06",
        "band": "easier",
        "text": "A reaction gives out a great deal of heat and light. Do heat "
                "and light have mass?",
        "options": [
            {"text": "Yes — that is why an open flask reads lower after the "
                     "reaction than it did before it started fizzing",
             "correct": False,
             "why": "The open flask lost a GAS, and the gas has mass. Heat "
                    "and light are not made of atoms"},
            {"text": "No — they are not made of atoms",
             "correct": True},
            {"text": "Yes, but far too little to weigh on a school balance",
             "correct": False,
             "why": "This sounds careful and is still wrong. They are not "
                    "matter at all"},
            {"text": "Only heat does, because you can feel it",
             "correct": False,
             "why": "Feeling something is not weighing it. Neither is made of "
                    "atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e07",
        "band": "easier",
        "text": "What is a product?",
        "options": [
            {"text": "The substance that is left in the flask at the end, as "
                     "opposed to anything that has escaped into the room",
             "correct": False,
             "why": "A gas that escapes is a product too. Where it ends up "
                    "does not change what it is"},
            {"text": "A substance you start a reaction with",
             "correct": False,
             "why": "Those are the things you begin with. A product is what "
                    "comes out"},
            {"text": "A substance a reaction makes",
             "correct": True},
            {"text": "The heat a reaction gives out",
             "correct": False,
             "why": "Heat is not a substance. A product is made of atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e08",
        "band": "easier",
        "text": "A reaction is run in an OPEN flask and the balance reading "
                "goes down. What must have happened?",
        "options": [
            {"text": "Some of the mass has been destroyed by the reaction, "
                     "which is what makes an open flask different",
             "correct": False,
             "why": "Nothing is ever destroyed. The flask is open, so "
                    "something has simply left it"},
            {"text": "A gas has joined from the air",
             "correct": False,
             "why": "That would make the reading go UP, as it does when "
                    "magnesium burns"},
            {"text": "Heat has escaped, and heat has mass",
             "correct": False,
             "why": "Heat is not made of atoms and weighs nothing. What left "
                    "was a gas"},
            {"text": "A gas has left the flask",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-06-s05",
        "band": "standard",
        "text": "A candle is lit and immediately sealed inside a large glass "
                "jar standing on a balance. What does the reading do while it "
                "burns?",
        "options": [
            {"text": "It stays exactly the same",
             "correct": True},
            {"text": "It falls, because the wax is being used up and its mass "
                     "goes into the heat and light given off",
             "correct": False,
             "why": "Heat and light have no mass. Everything the wax became "
                    "is still inside the jar"},
            {"text": "It rises, because oxygen joins the wax",
             "correct": False,
             "why": "The oxygen joining the wax was already inside the jar, "
                    "and already on the balance"},
            {"text": "It falls, then rises again as the candle goes out",
             "correct": False,
             "why": "Nothing crosses the glass in either direction, so the "
                    "reading never moves"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s06",
        "band": "standard",
        "text": "A sealed tube holds 2.40 g of magnesium and 1.60 g of "
                "oxygen, and they react completely. The tube is opened and the "
                "white powder is weighed. What should it read?",
        "options": [
            {"text": "0.80 g, which is the difference between the two masses "
                     "that went into the tube in the first place",
             "correct": False,
             "why": "Subtracting is the wrong move — nothing was taken away. "
                    "The two substances joined"},
            {"text": "4.00 g",
             "correct": True},
            {"text": "2.40 g, because only the magnesium is left as a solid",
             "correct": False,
             "why": "The oxygen is in the powder. That is what makes "
                    "magnesium oxide heavier than the ribbon"},
            {"text": "1.60 g",
             "correct": False,
             "why": "That is the oxygen alone. The magnesium has not gone "
                    "anywhere"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s07",
        "band": "standard",
        "text": "A heavy log burns in an open grate and leaves a small heap "
                "of ash weighing far less. Has mass been destroyed?",
        "options": [
            {"text": "Yes — burning is the one process that genuinely "
                     "destroys matter, which is why so little ash is left "
                     "behind",
             "correct": False,
             "why": "Burning destroys nothing. Most of the log left the grate "
                    "as gases you cannot see"},
            {"text": "Yes, but only the part that turned into heat and light",
             "correct": False,
             "why": "Heat and light are not made of atoms, so they carry no "
                    "mass away at all"},
            {"text": "No — most of the log left as gases, which have mass",
             "correct": True},
            {"text": "No — the ash weighs the same as the log, and the "
                     "balance must be faulty",
             "correct": False,
             "why": "The balance is right: the ash really is lighter. What is "
                    "missing is in the air"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s08",
        "band": "standard",
        "text": "Marble and acid are reacted in a SEALED flask on a balance. "
                "The reaction finishes, then the bung is taken out. What "
                "happens to the reading?",
        "options": [
            {"text": "It rises, because air rushes into the flask to fill the "
                     "space the gas was taking up inside it",
             "correct": False,
             "why": "The gas inside is at a higher pressure and leaves rather "
                    "than air coming in. The reading falls"},
            {"text": "Nothing happens, because the reaction has already "
                     "finished",
             "correct": False,
             "why": "The reaction has finished, but the gas it made is still "
                    "on the balance until the bung comes out"},
            {"text": "It falls and then rises back, as the flask refills",
             "correct": False,
             "why": "Air is far lighter than the carbon dioxide that left. "
                    "The reading does not come back"},
            {"text": "It falls, as the trapped carbon dioxide escapes",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-06-h05",
        "band": "harder",
        "text": "A student says the sealed flask's reading does not move "
                "because nothing is reacting inside it. What is the evidence "
                "against?",
        "options": [
            {"text": "It fizzes hard, and the marble is used up — a reaction "
                     "is plainly happening",
             "correct": True},
            {"text": "The sealed flask is warmer afterwards, and only an "
                     "unreacted mixture would stay at room temperature "
                     "throughout",
             "correct": False,
             "why": "Warmth is suggestive, and there is something far more "
                    "direct to point at: you can watch it fizzing"},
            {"text": "The bung would blow out if nothing were happening",
             "correct": False,
             "why": "The bung stays in. What shows the reaction is the "
                    "fizzing and the marble disappearing"},
            {"text": "Nothing — the student is right, since the balance never "
                     "moves",
             "correct": False,
             "why": "The balance not moving is exactly what conservation of "
                    "mass predicts for a sealed vessel"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h06",
        "band": "harder",
        "text": "Steel wool burned in an open dish gets HEAVIER. A log burned "
                "in an open grate gets LIGHTER. Both are burning. Explain the "
                "difference.",
        "options": [
            {"text": "The steel takes oxygen in and the log gives it out",
             "correct": False,
             "why": "Nothing gives oxygen out when it burns. Both take it "
                    "in — the difference is where the products end up"},
            {"text": "Oxygen joins in both, but iron oxide stays as a solid "
                     "while the log's products leave as gases",
             "correct": True},
            {"text": "Iron is a metal, and only metals obey conservation of "
                     "mass",
             "correct": False,
             "why": "Conservation of mass holds for everything. Both readings "
                    "obey it once the gases are counted"},
            {"text": "The log burns hotter, so more of its mass is turned "
                     "into heat",
             "correct": False,
             "why": "Heat carries no mass at any temperature. The log's mass "
                    "left as carbon dioxide and water vapour"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h07",
        "band": "harder",
        "text": "A student insists the 2.20 g missing from the open flask "
                "turned into heat. Which experiment settles it?",
        "options": [
            {"text": "Repeat the reaction and take the temperature "
                     "throughout, to see how much heat is given out for every "
                     "gram that disappears",
             "correct": False,
             "why": "You could measure that all day. It would not show "
                    "whether the heat came from the missing mass"},
            {"text": "Weigh the flask again once it has cooled to room "
                     "temperature",
             "correct": False,
             "why": "It reads 149.80 g cold as well as warm. Cooling brings "
                    "nothing back"},
            {"text": "Run exactly the same reaction sealed, and see that the "
                     "reading does not move",
             "correct": True},
            {"text": "Use a bigger flask, so that less heat escapes",
             "correct": False,
             "why": "The size makes no difference to the loss. Sealing it "
                    "does"},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h08",
        "band": "harder",
        "text": "12 g of carbon burns completely in 32 g of oxygen. What mass "
                "of carbon dioxide is made, and what would an open balance "
                "show?",
        "options": [
            {"text": "44 g is made, and the balance would show no change at "
                     "all, because the carbon dioxide has exactly the mass of "
                     "everything that made it",
             "correct": False,
             "why": "True about the 44 g, and the gas floats away — so the "
                    "balance loses the 12 g of carbon that was sitting on "
                    "it"},
            {"text": "20 g is made, and the balance would show a loss of "
                     "20 g",
             "correct": False,
             "why": "20 g is 32 − 12. Nothing was subtracted here: the two "
                    "joined, so the masses add"},
            {"text": "12 g is made, and the balance would show no change",
             "correct": False,
             "why": "The oxygen is in the product too, so the carbon dioxide "
                    "weighs more than the carbon did"},
            {"text": "44 g is made, and the balance would show a loss of "
                     "12 g as the gas left",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c2-06-e09",
        "band": "easier",
        "text": "What does the word mass mean?",
        "options": [
            {"text": "How much substance there is, measured on a balance in "
                     "grams",
             "correct": True},
            {"text": "How much space it takes up, in cubic centimetres",
             "correct": False,
             "why": "That is volume. A litre of air and a litre of water take "
                    "up the same space and weigh nothing like the same."},
            {"text": "How hot a substance is, measured with a thermometer",
             "correct": False,
             "why": "That is temperature. A warm flask and a cold one of the "
                    "same stuff have the same mass."},
            {"text": "How much energy a substance holds, measured in joules",
             "correct": False,
             "why": "Energy is not weighed on a balance, and a substance does "
                    "not get heavier by being heated."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e10",
        "band": "easier",
        "text": "Magnesium is burned in an open crucible and the balance "
                "reads more afterwards. Where has the extra mass come from?",
        "options": [
            {"text": "From the heat the burning gave out",
             "correct": False,
             "why": "Heat is not made of atoms, so it cannot add a gram to "
                    "anything."},
            {"text": "From oxygen in the air, which has joined the magnesium",
             "correct": True},
            {"text": "From the crucible, which gives up some of its own mass to "
                     "the powder as it heats",
             "correct": False,
             "why": "The crucible sits on the balance throughout. Nothing "
                    "moving between it and the powder could change a total."},
            {"text": "From nowhere: burning creates new matter",
             "correct": False,
             "why": "Nothing creates matter. Every atom in the powder was "
                    "either in the metal or in the air."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e11",
        "band": "easier",
        "text": "A sealed flask on a balance reads 40.00 g before a reaction "
                "and 40.00 g after it. What does that show?",
        "options": [
            {"text": "That the reaction never got going",
             "correct": False,
             "why": "A reaction that is going full tilt reads the same, so "
                    "long as nothing can leave the flask."},
            {"text": "That whatever was made is still inside the flask",
             "correct": True},
            {"text": "That the reaction made no gas of any kind",
             "correct": False,
             "why": "Gas made inside a sealed flask stays on the balance, so "
                    "the reading cannot tell you whether any was made."},
            {"text": "That the balance is not sensitive enough",
             "correct": False,
             "why": "A balance reading to 0.01 g would show a real change. "
                    "There is no change to show."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e12",
        "band": "easier",
        "text": "Candle wax burns away on a clean plate. Which of these is "
                "one of the substances the burning makes?",
        "options": [
            {"text": "Soot from the wick",
             "correct": False,
             "why": "A little soot can form, and the plate here is clean. "
                    "Nearly all of the wax leaves as gas."},
            {"text": "Heat from the flame",
             "correct": False,
             "why": "Heat is given out, and it is not a substance. A product "
                    "is made of atoms."},
            {"text": "Carbon dioxide",
             "correct": True},
            {"text": "Ash left on the plate",
             "correct": False,
             "why": "The plate is clean at the end. Wax burns away without "
                    "leaving ash of any kind."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e13",
        "band": "easier",
        "text": "Which piece of apparatus would you use to find the mass of a "
                "flask and its contents?",
        "options": [
            {"text": "A measuring cylinder",
             "correct": False,
             "why": "A measuring cylinder gives a volume in cubic "
                    "centimetres, and volume is not mass."},
            {"text": "A lab thermometer",
             "correct": False,
             "why": "A thermometer reads a temperature. Nothing about it "
                    "reports how much substance is there."},
            {"text": "A stopwatch and a ruler",
             "correct": False,
             "why": "A stopwatch times a reaction. It says nothing about how "
                    "much of anything is in the flask."},
            {"text": "A top-pan balance",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e14",
        "band": "easier",
        "text": "A log burns in a grate and leaves a small heap of ash. Most "
                "of the log's mass has left as what?",
        "options": [
            {"text": "Invisible gases",
             "correct": True},
            {"text": "Heat and light",
             "correct": False,
             "why": "Both are given out and neither is made of atoms, so "
                    "neither can carry mass away."},
            {"text": "Smoke, the one thing that leaves a fire",
             "correct": False,
             "why": "Smoke is small solid bits, and it is a tiny part of it. "
                    "Most of the log leaves as gas you cannot see."},
            {"text": "Nothing at all",
             "correct": False,
             "why": "Flames destroy no mass. Everything that was in the log "
                    "is still somewhere in the room."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e15",
        "band": "easier",
        "text": "A hundred atoms take part in a chemical reaction. How many "
                "atoms are there when it has finished?",
        "options": [
            {"text": "Fewer than a hundred, since some are used up",
             "correct": False,
             "why": "Being used up means being joined into something else. No "
                    "atom is spent or lost."},
            {"text": "More than a hundred, since new substances are made",
             "correct": False,
             "why": "New substances are the same atoms joined differently. "
                    "The joining makes no new ones."},
            {"text": "A hundred",
             "correct": True},
            {"text": "It depends on how much heat is given out",
             "correct": False,
             "why": "Heat carries no atoms away with it, however much of it "
                    "there is."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e16",
        "band": "easier",
        "text": "A sealed bag of ice is left on a balance until the ice has "
                "melted. What does the reading do?",
        "options": [
            {"text": "It falls a little",
             "correct": False,
             "why": "Melting rearranges the particles and removes none of "
                    "them. The same water is there throughout."},
            {"text": "It rises a little",
             "correct": False,
             "why": "Heat has no mass, so taking it in cannot make anything "
                    "heavier."},
            {"text": "It falls, then rises",
             "correct": False,
             "why": "The bag is sealed, so any vapour is still inside it and "
                    "still on the balance."},
            {"text": "It stays the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e17",
        "band": "easier",
        "text": "Which of these is a closed system?",
        "options": [
            {"text": "A garden bonfire",
             "correct": False,
             "why": "A bonfire is as open as anything gets. Gases pour away "
                    "from it in every direction."},
            {"text": "A flask stoppered with a bung",
             "correct": True},
            {"text": "A beaker standing open on a bench",
             "correct": False,
             "why": "Anything made as a gas can leave a beaker, and oxygen "
                    "from the room can get in."},
            {"text": "A chimney above a coal fire, once the fire is out",
             "correct": False,
             "why": "A chimney is built to let gases out. Nothing about it "
                    "keeps anything in."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e18",
        "band": "easier",
        "text": "Sugar is stirred into a cup of tea until none of it can be "
                "seen. What happens to the mass of the cup and everything in "
                "it?",
        "options": [
            {"text": "It goes down a little",
             "correct": False,
             "why": "The sugar has spread out between the water particles "
                    "rather than disappearing. All of it is still there."},
            {"text": "It goes up a little",
             "correct": False,
             "why": "Nothing has been added to the cup. The water was already "
                    "in it and is already on the balance."},
            {"text": "It goes down, then up",
             "correct": False,
             "why": "Nothing leaves the cup at all. Being invisible is not "
                    "the same as being gone."},
            {"text": "It stays the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e19",
        "band": "easier",
        "text": "Which statement about gases is correct?",
        "options": [
            {"text": "Gases have mass",
             "correct": True},
            {"text": "Only when cold",
             "correct": False,
             "why": "A gas weighs the same amount of matter whether it is a "
                    "gas or a liquid. Cooling changes nothing about that."},
            {"text": "Gases have mass when sealed in",
             "correct": False,
             "why": "The 2.20 g that leaves an open flask is 2.20 g of gas in "
                    "the room. Where it is makes no difference."},
            {"text": "Only heavy gases have mass",
             "correct": False,
             "why": "Every gas has mass, hydrogen included. Some simply have "
                    "more of it in the same space."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e20",
        "band": "easier",
        "text": "Can a chemical reaction make a brand new atom?",
        "options": [
            {"text": "Yes, whenever a new substance is made, since a substance "
                     "nobody had before needs atoms nobody had before",
             "correct": False,
             "why": "A new substance is old atoms joined in a new way, and "
                    "none of them is new."},
            {"text": "No — a reaction never creates an atom, it only "
                     "rearranges the ones it started with",
             "correct": True},
            {"text": "Yes, but only in a sealed container",
             "correct": False,
             "why": "Sealing a container decides what you can weigh. It "
                    "cannot make an atom appear."},
            {"text": "Yes, given heat",
             "correct": False,
             "why": "Heat gets a reaction going. No amount of it builds an "
                    "atom out of nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e21",
        "band": "easier",
        "text": "Magnesium ribbon is burned and leaves a white powder. Is the "
                "powder heavier or lighter than the ribbon was?",
        "options": [
            {"text": "Lighter, because burning always uses some of it up",
             "correct": False,
             "why": "Nothing is used up and lost. Something has been added to "
                    "the metal instead."},
            {"text": "The same: the ribbon is all there",
             "correct": False,
             "why": "The ribbon's atoms are all there, and oxygen has joined "
                    "them, so the powder weighs more."},
            {"text": "Heavier, because oxygen has joined the magnesium",
             "correct": True},
            {"text": "Lighter, because the bright light carries some of the mass "
                     "away as it burns",
             "correct": False,
             "why": "Light is not made of atoms and carries no mass, however "
                    "bright it is."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e22",
        "band": "easier",
        "text": "Coal burns in an open grate. Which of these leaves the "
                "grate carrying mass away with it?",
        "options": [
            {"text": "The gases that are made",
             "correct": True},
            {"text": "The heat that is given out",
             "correct": False,
             "why": "Heat warms the room without being made of atoms, so it "
                    "takes no mass with it."},
            {"text": "The light",
             "correct": False,
             "why": "Light is not matter at all. A dark fire and a bright one "
                    "lose mass the same way."},
            {"text": "Nothing does: the mass is simply destroyed",
             "correct": False,
             "why": "Nothing destroys mass. The gases carry every atom of the "
                    "coal out of the grate."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e23",
        "band": "easier",
        "text": "A balloon is stretched over the neck of a flask of reacting "
                "chemicals. The balloon blows up. What does the balance "
                "reading do?",
        "options": [
            {"text": "It rises as the balloon fills",
             "correct": False,
             "why": "The gas was made from what was already in the flask, and "
                    "it has not gone anywhere."},
            {"text": "It falls as the gas leaves",
             "correct": False,
             "why": "The gas has left the flask and not the apparatus. The "
                    "balloon is on the balance too."},
            {"text": "It drops",
             "correct": False,
             "why": "A balloon of carbon dioxide lifts nothing. This is not a "
                    "helium balloon on a string."},
            {"text": "It stays the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e24",
        "band": "easier",
        "text": "When we say mass is conserved in a reaction, what does "
                "conserved mean?",
        "options": [
            {"text": "Saved up and spent again on whatever reaction comes next",
             "correct": False,
             "why": "Nothing is being stored for later. The total simply does "
                    "not change."},
            {"text": "Kept safe inside the flask by the bung",
             "correct": False,
             "why": "A bung decides what you can weigh, not whether the rule "
                    "holds. It holds in an open flask too."},
            {"text": "The total stays the same from start to finish",
             "correct": True},
            {"text": "Used up slowly, not at once",
             "correct": False,
             "why": "Mass is not used up at any speed. None of it goes "
                    "anywhere at all."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e25",
        "band": "easier",
        "text": "A stick of wood is snapped in half while it sits on a "
                "balance. What happens to the reading?",
        "options": [
            {"text": "It stays the same",
             "correct": True},
            {"text": "It falls by a little",
             "correct": False,
             "why": "Energy has no mass, so using it cannot lighten the "
                    "wood."},
            {"text": "It rises by a little",
             "correct": False,
             "why": "Two halves are the same wood as one stick. Counting the "
                    "pieces changes nothing."},
            {"text": "It falls, then recovers",
             "correct": False,
             "why": "Any dust made is still lying on the pan, so the total "
                    "does not move."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e26",
        "band": "easier",
        "text": "Which of these would make the balance reading go UP during a "
                "reaction in an open dish?",
        "options": [
            {"text": "A gas bubbling out of the dish",
             "correct": False,
             "why": "Anything leaving the dish takes its mass with it, so the "
                    "reading goes down."},
            {"text": "Heat being given out by the reaction",
             "correct": False,
             "why": "Heat is not made of atoms. Giving it out or taking it in "
                    "moves no mass at all."},
            {"text": "A gas from the air joining the substances",
             "correct": True},
            {"text": "Light being given out by the reaction",
             "correct": False,
             "why": "Light carries no mass either way. A bright reaction and "
                    "a dull one behave the same."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e27",
        "band": "easier",
        "text": "A student says gases float upwards, so they cannot have any "
                "mass. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong: only solids and liquids have mass",
             "correct": False,
             "why": "Every gas has mass. A sealed flask that makes a gas "
                    "reads exactly what it read before."},
            {"text": "Gases do have mass, and a balloon of gas weighs more "
                     "than the same balloon empty",
             "correct": True},
            {"text": "Gases have mass, but far too little to make any "
                     "difference to a balance",
             "correct": False,
             "why": "It makes a plain difference. An open flask can drop "
                    "2.20 g as its gas leaves."},
            {"text": "Gases have mass only while they are being made",
             "correct": False,
             "why": "A gas has the same mass before, during and after. It "
                    "does not lose it by drifting off."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e28",
        "band": "easier",
        "text": "In a chemical reaction, can an atom of one element turn into "
                "an atom of a different element?",
        "options": [
            {"text": "Yes, and that changing of one element into another is what "
                     "makes a new substance",
             "correct": False,
             "why": "New substances come from atoms joining up differently, "
                    "with every atom still the element it was."},
            {"text": "Yes, if it is hot enough",
             "correct": False,
             "why": "Temperature changes how fast atoms react, never which "
                    "element they are."},
            {"text": "No — the atoms are rearranged, and each stays the "
                     "element it started as",
             "correct": True},
            {"text": "Yes, but only in a sealed container",
             "correct": False,
             "why": "A seal decides what stays on the balance. It has no "
                    "effect on what the atoms are."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e29",
        "band": "easier",
        "text": "A reaction in a sealed flask gives out heat and the flask "
                "becomes warm. What happens to the balance reading?",
        "options": [
            {"text": "It falls, because the heat has left the flask",
             "correct": False,
             "why": "Heat does leave a warm flask, and it is not matter, so "
                    "it takes no mass with it."},
            {"text": "It rises while the flask is warm",
             "correct": False,
             "why": "Warmth adds nothing to a balance. The flask holds the "
                    "same atoms hot as cold."},
            {"text": "It falls, then returns as the flask cools",
             "correct": False,
             "why": "The reading does not move in the first place, so it has "
                    "nothing to return from."},
            {"text": "It stays the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-e30",
        "band": "easier",
        "text": "A balloon is weighed empty, then filled with carbon dioxide "
                "and weighed again. What is found?",
        "options": [
            {"text": "It weighs more when it is full",
             "correct": True},
            {"text": "It weighs the same either way, since gas has no weight",
             "correct": False,
             "why": "Carbon dioxide is made of atoms and every one of them "
                    "has mass."},
            {"text": "It weighs less when it is full, since gas lifts it",
             "correct": False,
             "why": "Carbon dioxide is heavier than air and lifts nothing. "
                    "Only a lighter gas such as helium does that."},
            {"text": "It weighs more, but only if the gas is squeezed in",
             "correct": False,
             "why": "Squeezing more in adds more mass. Any gas at all in "
                    "there already weighs something."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c2-06-s09",
        "band": "standard",
        "text": "In a sealed flask, magnesium reacts completely with oxygen "
                "and the product has a mass of 50 g. The magnesium used had "
                "a mass of 30 g. Calculate the mass of oxygen that reacted.",
        "options": [
            {"text": "20 g",
             "correct": True},
            {"text": "50 g",
             "correct": False,
             "why": "That is the product's own mass, not the oxygen's share "
                    "of it. The magnesium's 30 g is already part of that 50 g."},
            {"text": "80 g",
             "correct": False,
             "why": "That adds the product's mass to the magnesium's, which "
                    "double-counts the magnesium instead of subtracting it "
                    "out."},
            {"text": "30 g",
             "correct": False,
             "why": "That is the magnesium's own mass, not the oxygen's. The "
                    "oxygen makes up whatever of the 50 g the magnesium does "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s10",
        "band": "standard",
        "text": "An open flask reads 96.00 g before a reaction, and 4.50 g of "
                "gas escapes during it. Calculate the reading afterwards.",
        "options": [
            {"text": "100.50 g",
             "correct": False,
             "why": "Adding the gas would be right if it had joined from the "
                    "air. This gas left, so it has to come off."},
            {"text": "91.50 g",
             "correct": True},
            {"text": "96.00 g",
             "correct": False,
             "why": "The reading would hold at 96.00 g only in a sealed "
                    "flask. This one is open and the gas has gone."},
            {"text": "4.50 g",
             "correct": False,
             "why": "That is the gas on its own. Everything else is still "
                    "sitting on the balance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s11",
        "band": "standard",
        "text": "An open dish of metal is heated. It reads 60.00 g before and "
                "63.20 g after. Calculate the mass of gas that joined from "
                "the air.",
        "options": [
            {"text": "123.20 g",
             "correct": False,
             "why": "Adding the two readings counts the metal twice. The "
                    "second reading already contains the first."},
            {"text": "60.00 g",
             "correct": False,
             "why": "That is the metal you started with, not the gas that "
                    "has joined it."},
            {"text": "3.20 g",
             "correct": True},
            {"text": "63.20 g",
             "correct": False,
             "why": "That is everything on the pan at the end. Most of it is "
                    "the metal that was there all along."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s12",
        "band": "standard",
        "text": "A student says a sealed reaction that gets hot must get "
                "heavier, since heat has gone into it. Explain why not.",
        "options": [
            {"text": "Because the flask gives the heat back out again as it "
                     "cools, so any gain it made is undone by the time you "
                     "weigh it",
             "correct": False,
             "why": "A warm sealed flask reads the same as a cold one. There "
                    "is no gain to be undone."},
            {"text": "Because the heat was made inside the flask rather than "
                     "coming in from outside",
             "correct": False,
             "why": "Where heat comes from makes no difference. It has no "
                    "mass in either direction."},
            {"text": "Because a sealed flask cannot take heat in at all",
             "correct": False,
             "why": "Heat crosses glass easily, which is why a flask feels "
                    "warm. It carries no mass when it does."},
            {"text": "Because heat is not made of atoms, so it has no mass "
                     "to add",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s13",
        "band": "standard",
        "text": "Explain why a candle burning on a balance looks as though it "
                "breaks the conservation of mass rule.",
        "options": [
            {"text": "Because burning is one of the few changes the rule was "
                     "never meant to cover",
             "correct": False,
             "why": "The rule covers burning like anything else. Seal the "
                    "candle in a jar and the reading holds."},
            {"text": "Because the products float away, so the balance is "
                     "weighing only part of what is there",
             "correct": True},
            {"text": "Because a flame makes the balance read low while it is "
                     "alight",
             "correct": False,
             "why": "The reading is honest. What it is missing is the gas "
                    "that has left the pan."},
            {"text": "Because wax is used up and cannot be got back again",
             "correct": False,
             "why": "Being hard to get back is not the same as being gone. "
                    "Every atom of the wax is in the room."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s14",
        "band": "standard",
        "text": "Zinc is dropped into acid in an open beaker on a balance, "
                "and hydrogen bubbles off. Predict what the reading does.",
        "options": [
            {"text": "It rises, because a new substance has been made in the "
                     "beaker",
             "correct": False,
             "why": "Making a substance adds nothing. Its atoms came from the "
                    "zinc and the acid already on the pan."},
            {"text": "It holds steady, because the beaker is not sealed",
             "correct": False,
             "why": "An open beaker is exactly what lets the hydrogen go. A "
                    "sealed one is what holds the reading steady."},
            {"text": "It rises, because hydrogen is the lightest gas there "
                     "is",
             "correct": False,
             "why": "Hydrogen is light and it is not weightless, and it is "
                    "leaving the beaker rather than arriving."},
            {"text": "It falls",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s15",
        "band": "standard",
        "text": "50 g of a metal is heated in air and gives 70 g of oxide. "
                "Determine the mass of oxygen that joined, and say where it "
                "came from.",
        "options": [
            {"text": "120 g, from the air, since the oxide is the metal and "
                     "the oxygen added together and both were weighed",
             "correct": False,
             "why": "Adding the two counts the metal twice. The 70 g already "
                    "includes the 50 g of metal."},
            {"text": "70 g, from the air",
             "correct": False,
             "why": "70 g is the whole oxide. Only the part above the "
                    "original 50 g came out of the air."},
            {"text": "20 g, from the air",
             "correct": True},
            {"text": "20 g, from the heat of the burner",
             "correct": False,
             "why": "Heat is not matter and adds no mass. The 20 g is oxygen "
                    "that was in the room."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s16",
        "band": "standard",
        "text": "A student weighs only the solid before and after a reaction "
                "and reports that mass has been lost. Explain the error.",
        "options": [
            {"text": "The balance should have been zeroed with the flask on "
                     "it before anything was weighed at all",
             "correct": False,
             "why": "Zeroing changes what number you read, not whether a gas "
                    "was counted."},
            {"text": "The reaction should have been given longer, because the "
                     "solid was still reacting when it was weighed",
             "correct": False,
             "why": "Weighing early gives a part-finished reaction, not a "
                    "false rule. The gas is what was missed."},
            {"text": "The rule is about everything, and a gas that was made "
                     "or used was never on the balance",
             "correct": True},
            {"text": "A warm solid always reads low on a balance",
             "correct": False,
             "why": "A warm solid weighs what a cold one does. Nothing about "
                    "temperature explains the missing mass."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s17",
        "band": "standard",
        "text": "A class tests the conservation of mass rule. Explain why "
                "they are told to seal the flask.",
        "options": [
            {"text": "So that nothing can leave or enter, which puts "
                     "everything that takes part on the balance",
             "correct": True},
            {"text": "So that the reaction goes to completion, which it "
                     "cannot do in an open flask",
             "correct": False,
             "why": "A reaction finishes perfectly well in an open flask. "
                    "What changes is what you can weigh."},
            {"text": "So that the gas is made more slowly and is easier to "
                     "measure as it forms",
             "correct": False,
             "why": "Sealing does not slow the chemistry down. It stops the "
                    "gas getting off the balance."},
            {"text": "So that the heat stays in, since heat is part of the "
                     "mass being measured",
             "correct": False,
             "why": "Heat is not part of any mass. Keeping it in would change "
                    "no reading at all."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s18",
        "band": "standard",
        "text": "200 g of coal burns in an open grate and leaves 5 g of ash. "
                "State what happened to the other 195 g.",
        "options": [
            {"text": "It was destroyed by the fire, which is what burning "
                     "does to most of a fuel and is why so little ash is left",
             "correct": False,
             "why": "Fire destroys nothing. Those 195 g are in the air above "
                    "the grate."},
            {"text": "It went up the chimney as gases, which weigh more than "
                     "195 g because oxygen joined them",
             "correct": True},
            {"text": "It was given out as heat and light, which is where most "
                     "of a fuel's mass ends up",
             "correct": False,
             "why": "Heat and light are not made of atoms and can account "
                    "for none of it."},
            {"text": "It is still in the ash, which is heavier than it looks",
             "correct": False,
             "why": "The ash weighs 5 g on a balance, and that is all of it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s19",
        "band": "standard",
        "text": "A balloon is fitted over the neck of a flask of marble and "
                "acid, and the whole set-up sits on a balance throughout. "
                "Explain what the balance shows as the balloon fills, and "
                "why.",
        "options": [
            {"text": "Because a gas inside a balloon weighs nothing, being "
                     "held up by the rubber around it",
             "correct": False,
             "why": "A balloon of carbon dioxide is heavier than an empty "
                    "one. Rubber holds up nothing."},
            {"text": "Because the balloon lifts as it fills, and that lift "
                     "cancels out the gas that has been made",
             "correct": False,
             "why": "Carbon dioxide does not lift a balloon at all, so there "
                    "is nothing to cancel."},
            {"text": "Because no gas is made once the flask has been closed "
                     "off from the room",
             "correct": False,
             "why": "The gas is made either way — you can watch the balloon "
                    "fill with it."},
            {"text": "Because the gas has not left the balance",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s20",
        "band": "standard",
        "text": "36 g of water is made from 4 g of hydrogen. Calculate the "
                "mass of oxygen that reacted.",
        "options": [
            {"text": "40 g",
             "correct": False,
             "why": "Adding the two gives more than the water made. The "
                    "hydrogen is already inside the 36 g."},
            {"text": "36 g",
             "correct": False,
             "why": "That is the water. Part of it is the hydrogen you were "
                    "given."},
            {"text": "4 g",
             "correct": False,
             "why": "That is the hydrogen, which is the mass you already "
                    "know."},
            {"text": "32 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s21",
        "band": "standard",
        "text": "Explain why the gases made by burning a fuel weigh more than "
                "the fuel itself did.",
        "options": [
            {"text": "Because burning stretches the fuel's particles out, and "
                     "a gas takes up far more room than a solid",
             "correct": False,
             "why": "Taking up more room is not weighing more. Volume and "
                    "mass are different things."},
            {"text": "Because oxygen from the air joins the fuel, and that "
                     "oxygen has mass of its own",
             "correct": True},
            {"text": "Because heat from the flame is absorbed into the gases "
                     "as they are made",
             "correct": False,
             "why": "Heat has no mass to be absorbed into anything."},
            {"text": "Because a gas is always heavier than the solid it came "
                     "from",
             "correct": False,
             "why": "A gas is lighter than a solid of the same size. What "
                    "matters is that something has been added."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s22",
        "band": "standard",
        "text": "A tube is sealed for a reaction, then opened once it has "
                "finished, and the reading drops by 0.80 g. State what those "
                "0.80 g were.",
        "options": [
            {"text": "Heat that had been trapped in the tube and was let out "
                     "with the bung, taking its mass with it",
             "correct": False,
             "why": "Heat leaves a warm tube whether it is open or shut, and "
                    "it never has mass to take."},
            {"text": "Air that had been forced out of the tube by the "
                     "reaction as it went on",
             "correct": False,
             "why": "Air pushed out of a sealed tube could not get past the "
                    "bung. What left was made inside."},
            {"text": "Liquid that evaporated the moment the pressure inside "
                     "was released",
             "correct": False,
             "why": "The drop comes as the gas escapes, and it is the gas the "
                    "reaction produced."},
            {"text": "Gas that the reaction made, which had been held in the "
                     "tube until it was opened",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s23",
        "band": "standard",
        "text": "Vinegar is poured onto baking soda in an open glass on a "
                "balance and it fizzes over. Predict the reading and name the "
                "gas.",
        "options": [
            {"text": "The reading falls, and the gas is carbon dioxide",
             "correct": True},
            {"text": "It rises, and the gas is carbon dioxide",
             "correct": False,
             "why": "The gas is right. It is leaving the glass, though, so "
                    "the reading goes down and not up."},
            {"text": "The reading falls, and the gas is oxygen",
             "correct": False,
             "why": "The direction is right and the gas is not. This "
                    "reaction gives off carbon dioxide."},
            {"text": "It holds, and the gas is carbon dioxide",
             "correct": False,
             "why": "It would hold in a sealed container. In an open glass "
                    "the gas is gone."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s24",
        "band": "standard",
        "text": "5.00 g of a solid and 45.00 g of a solution are sealed in a "
                "flask and react completely. Calculate the reading "
                "afterwards.",
        "options": [
            {"text": "40.00 g",
             "correct": False,
             "why": "Subtracting is the wrong move. Nothing was taken out of "
                    "the flask."},
            {"text": "45.00 g",
             "correct": False,
             "why": "That is the solution alone, as though the solid had "
                    "vanished into it."},
            {"text": "50.00 g",
             "correct": True},
            {"text": "Less than 50.00 g, since some was given off as gas",
             "correct": False,
             "why": "Any gas is still in the sealed flask, and therefore "
                    "still on the balance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s25",
        "band": "standard",
        "text": "A balance reading falls while a reaction runs. State the two "
                "things that must both be true.",
        "options": [
            {"text": "The vessel is open, and something has left it as a gas",
             "correct": True},
            {"text": "The vessel is open, and some of the mass has been "
                     "destroyed by the reaction going on inside it",
             "correct": False,
             "why": "No reaction destroys mass, open or sealed. Something has "
                    "left the pan instead."},
            {"text": "The vessel is sealed, and a gas has been made inside "
                     "it",
             "correct": False,
             "why": "Gas made in a sealed vessel stays on the balance, so the "
                    "reading would not move."},
            {"text": "It is open, and heat was given out",
             "correct": False,
             "why": "Heat leaves an open vessel and a sealed one alike, and "
                    "carries no mass with it either way."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s26",
        "band": "standard",
        "text": "Explain why the heat given out by a reaction can never "
                "account for a fall in the balance reading.",
        "options": [
            {"text": "Because heat is not made of atoms, so it never carries "
                     "mass away",
             "correct": True},
            {"text": "Because the heat goes into the flask rather than out of "
                     "it, and the flask stays on the pan",
             "correct": False,
             "why": "Heat does leave a warm flask into the room. It takes no "
                    "mass when it goes."},
            {"text": "Because heat weighs too little to read",
             "correct": False,
             "why": "It is not a matter of a small amount. Heat is not "
                    "matter, so there is nothing to weigh."},
            {"text": "Because a reaction that gives out heat also takes the "
                     "same amount back in",
             "correct": False,
             "why": "Some reactions give heat out and stop there. The "
                    "reading still does not move."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s27",
        "band": "standard",
        "text": "Magnesium is burned in a crucible whose lid is lifted every "
                "so often. The mass gained is less than expected. Suggest "
                "why.",
        "options": [
            {"text": "Some of the white powder escapes as smoke each time the "
                     "lid is lifted",
             "correct": True},
            {"text": "Lifting the lid lets heat out, and the lost heat is "
                     "part of the missing mass",
             "correct": False,
             "why": "Heat carries no mass, so letting it out changes no "
                    "reading."},
            {"text": "Lifting the lid lets oxygen out, so less of it can join "
                     "the metal",
             "correct": False,
             "why": "Lifting the lid lets more air in, not less. It is the "
                    "powder getting out that costs you."},
            {"text": "Magnesium burns more slowly when the lid is off, so "
                     "less of it reacts",
             "correct": False,
             "why": "More air reaches it with the lid off, and the ribbon is "
                    "burned until it is used up regardless."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s28",
        "band": "standard",
        "text": "A reaction in an open flask makes a gas that dissolves in "
                "the liquid instead of bubbling off. Predict the reading.",
        "options": [
            {"text": "It falls by the mass of the gas, because a dissolved "
                     "gas is no longer part of what is being weighed",
             "correct": False,
             "why": "A dissolved gas is in the liquid, and the liquid is on "
                    "the pan. Nothing has left."},
            {"text": "It does not change",
             "correct": True},
            {"text": "It rises, because a dissolved gas weighs more than a "
                     "free one",
             "correct": False,
             "why": "Dissolving changes nothing about a gas's mass, and adds "
                    "nothing to the flask."},
            {"text": "It falls by half the mass of the gas",
             "correct": False,
             "why": "There is no half-way loss. Either something leaves the "
                    "flask or it does not."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s29",
        "band": "standard",
        "text": "Everything before a reaction equals what is left in the "
                "flask plus the gas that left it. An open flask reads 88.00 g "
                "before and 84.60 g after. Calculate the gas.",
        "options": [
            {"text": "172.60 g",
             "correct": False,
             "why": "Adding the two readings counts everything in the flask "
                    "twice over."},
            {"text": "84.60 g",
             "correct": False,
             "why": "That is what is left in the flask, which is the other "
                    "part of the sum."},
            {"text": "88.00 g",
             "correct": False,
             "why": "That is everything you started with, gas and flask "
                    "contents together."},
            {"text": "3.40 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-s30",
        "band": "standard",
        "text": "Explain how conservation of mass lets a chemist state the "
                "mass of a gas that was never put on a balance.",
        "options": [
            {"text": "The gas is weighed later, once it has been caught and "
                     "cooled into a liquid that will sit on a pan",
             "correct": False,
             "why": "Nothing is caught in the open runs. The number comes "
                    "from the two readings alone."},
            {"text": "The gas is estimated from how fast the reaction fizzed "
                     "and for how long it went on",
             "correct": False,
             "why": "Fizzing is not measured, and the answer would be a guess "
                    "rather than a figure."},
            {"text": "Everything before must equal everything after, so the "
                     "gas is the difference between the two readings",
             "correct": True},
            {"text": "The gas is looked up in a table, since every reaction "
                     "gives off the same amount of it",
             "correct": False,
             "why": "Reactions give off wildly different masses of gas, and "
                    "no table could stand in for weighing."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c2-06-h09",
        "band": "harder",
        "text": "The same reaction is run in two sealed flasks, one twice the "
                "size of the other, each on its own balance. Predict what "
                "each reading does.",
        "options": [
            {"text": "Neither moves",
             "correct": True},
            {"text": "Neither moves, unless the larger flask holds more air, "
                     "in which case that extra air joins in and lifts its "
                     "reading",
             "correct": False,
             "why": "Air already sealed inside a flask is already on its "
                    "balance, so using it changes no reading."},
            {"text": "The larger one falls, because the gas has more room to "
                     "spread out in",
             "correct": False,
             "why": "Room to spread out is not room to escape. A sealed "
                    "flask keeps everything on the pan."},
            {"text": "Both fall, since a bigger flask loses more gas than a "
                     "small one does",
             "correct": False,
             "why": "Neither loses any gas. Both are sealed, so nothing "
                    "crosses either boundary."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h10",
        "band": "harder",
        "text": "12.0 g of magnesium burns completely to 20.0 g of magnesium "
                "oxide. Determine the oxygen that joined, then predict the "
                "oxide made from 6.0 g of magnesium.",
        "options": [
            {"text": "8.0 g of oxygen, and 14.0 g of oxide",
             "correct": False,
             "why": "The oxygen is right. Halving the metal halves everything "
                    "else, so the oxide comes to 10.0 g."},
            {"text": "8.0 g of oxygen joined, so half the magnesium gives "
                     "half the oxide, which is 10.0 g",
             "correct": True},
            {"text": "32.0 g of oxygen, and 16.0 g of oxide",
             "correct": False,
             "why": "Adding the two masses counts the magnesium twice. The "
                    "20.0 g already contains it."},
            {"text": "8.0 g of oxygen, and 20.0 g of oxide",
             "correct": False,
             "why": "Less magnesium cannot give the same oxide. Half of it "
                    "makes half as much."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h11",
        "band": "harder",
        "text": "An open flask loses 2.00 g during a reaction. The run is "
                "repeated with the same masses, but with a balloon sealed "
                "over the neck. Determine the change in reading.",
        "options": [
            {"text": "A loss of 2.00 g, since the same gas is made either way "
                     "and a balloon cannot weigh it",
             "correct": False,
             "why": "The same gas is made, and this time it is still on the "
                    "balance inside the balloon."},
            {"text": "A loss of 1.00 g",
             "correct": False,
             "why": "There is no half-way case. Either the gas leaves the "
                    "balance or it does not."},
            {"text": "No change at all",
             "correct": True},
            {"text": "A gain of 2.00 g, because the gas is now being weighed "
                     "on top of everything else",
             "correct": False,
             "why": "The gas was made from what was already on the pan, so "
                    "keeping it adds nothing to the total."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h12",
        "band": "harder",
        "text": "Balances existed for centuries before anyone accepted that "
                "mass is conserved in a reaction. Suggest why it took so "
                "long.",
        "options": [
            {"text": "Because balances were not accurate enough to read the "
                     "small changes involved until quite recently",
             "correct": False,
             "why": "The changes are large — grams, not specks. Accuracy was "
                    "not what stood in the way."},
            {"text": "Because chemists were not interested in weighing "
                     "things until the last two hundred years",
             "correct": False,
             "why": "Chemists weighed things constantly. What they missed was "
                    "the part that floated away."},
            {"text": "Because nobody had thought of the idea before, and it "
                     "cannot be tested without the idea first",
             "correct": False,
             "why": "The idea is not what was missing. Sealing the vessel is "
                    "what made it testable."},
            {"text": "Because the gases involved are invisible, so reactions "
                     "looked as though they gained or lost matter",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h13",
        "band": "harder",
        "text": "In a sealed flask, 30.00 g of one substance reacts with "
                "20.00 g of another. The solid left weighs 38.00 g and the "
                "rest is gas. Calculate the mass of gas.",
        "options": [
            {"text": "12.00 g",
             "correct": True},
            {"text": "10.00 g",
             "correct": False,
             "why": "10.00 g is 30.00 − 20.00. The two starting masses are "
                    "added, not subtracted from each other."},
            {"text": "88.00 g",
             "correct": False,
             "why": "88.00 g adds the solid to both starting masses, which "
                    "counts the same matter twice."},
            {"text": "18.00 g",
             "correct": False,
             "why": "18.00 g is 38.00 − 20.00. The solid has to be taken off "
                    "the whole 50.00 g that went in."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h14",
        "band": "harder",
        "text": "Burning metals were once said to give off a substance "
                "called phlogiston. A modern chemist weighs the same "
                "experiment. State what the mass gain measures.",
        "options": [
            {"text": "The heat the metal took in while it was burning",
             "correct": False,
             "why": "Heat is not matter and shows up on no balance, however "
                    "fiercely the metal burns."},
            {"text": "The oxygen from the air that has joined the metal",
             "correct": True},
            {"text": "The phlogiston that stayed behind in the metal rather "
                     "than escaping from it",
             "correct": False,
             "why": "No such substance exists. What the balance has found is "
                    "something arriving from the air."},
            {"text": "The mass of the ash the metal leaves",
             "correct": False,
             "why": "The powder left is the whole product, and the gain is "
                    "only the part of it that came from the air."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h15",
        "band": "harder",
        "text": "A student says mass is conserved only in a closed system. "
                "Evaluate that claim.",
        "options": [
            {"text": "Fair, since the rule is stated for closed systems and "
                     "an open flask is free to break it however it likes",
             "correct": False,
             "why": "Nothing about an open flask breaks it. Its gases simply "
                    "leave the pan and have to be counted elsewhere."},
            {"text": "Fair, because mass really does leave an open system "
                     "for good",
             "correct": False,
             "why": "It leaves the flask and not the world. Weigh the room "
                    "and it is all still there."},
            {"text": "Wrong: the rule holds everywhere, and closing a system "
                     "only makes it possible to weigh everything",
             "correct": True},
            {"text": "Wrong, because an open system has no mass to conserve "
                     "in the first place",
             "correct": False,
             "why": "An open flask and its contents have mass throughout. "
                    "The claim fails for another reason."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h16",
        "band": "harder",
        "text": "Two students each react 10.00 g of marble with excess acid "
                "in the open — one in a tall flask, one in a wide dish. "
                "Predict how the mass lost compares.",
        "options": [
            {"text": "The dish loses more, since gas escapes a wide opening "
                     "more easily",
             "correct": False,
             "why": "How fast it escapes may differ. How much is made does "
                    "not, and in the end it all leaves."},
            {"text": "The flask loses more",
             "correct": False,
             "why": "A tall flask slows the gas on its way out and keeps none "
                    "of it. The final loss is the same."},
            {"text": "The two lose the same mass, because the same marble and "
                     "acid make the same mass of gas",
             "correct": True},
            {"text": "It cannot be predicted from the information given",
             "correct": False,
             "why": "It can: same chemicals, same amounts, same reaction, so "
                    "the same mass of gas."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h17",
        "band": "harder",
        "text": "A gas syringe is joined to a flask of reacting chemicals, "
                "and the whole apparatus stands on one balance. The syringe "
                "fills. Determine what the reading does.",
        "options": [
            {"text": "It falls by the mass of gas collected, since that gas "
                     "is now in the syringe rather than in the flask",
             "correct": False,
             "why": "The syringe is on the balance too, so moving gas from "
                    "one part of the apparatus to another changes nothing."},
            {"text": "It rises, because the gas pushing the plunger out "
                     "presses down on the balance as it goes",
             "correct": False,
             "why": "Gas pushing a plunger moves nothing onto the pan. No "
                    "mass has been added to the apparatus."},
            {"text": "It stays the same",
             "correct": True},
            {"text": "It falls a little, because the gas in the syringe is "
                     "at a lower pressure than the gas in the flask",
             "correct": False,
             "why": "Pressure is not mass. The same atoms are inside the "
                    "apparatus either way."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h18",
        "band": "harder",
        "text": "56 g of iron reacts completely with 32 g of oxygen. "
                "Determine the mass of oxygen needed to react with 28 g of "
                "iron.",
        "options": [
            {"text": "16 g",
             "correct": True},
            {"text": "32 g",
             "correct": False,
             "why": "Half as much iron needs half as much oxygen. The 32 g "
                    "goes with the full 56 g."},
            {"text": "28 g",
             "correct": False,
             "why": "The two masses are not equal to each other. Iron and "
                    "oxygen react in a fixed proportion of 56 to 32."},
            {"text": "64 g",
             "correct": False,
             "why": "Doubling is the wrong way. Less iron takes less oxygen, "
                    "not more."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h19",
        "band": "harder",
        "text": "A student proposes testing conservation of mass by weighing "
                "a bonfire before it is lit and the ash afterwards. Evaluate "
                "the design.",
        "options": [
            {"text": "Poor: the gases leave, so most of what was there is "
                     "never weighed at the end",
             "correct": True},
            {"text": "Poor, because a bonfire is too heavy to weigh and the "
                     "test would work on any smaller fire",
             "correct": False,
             "why": "Size is not the flaw. The same fire in a sealed vessel "
                    "would test the rule perfectly well."},
            {"text": "Good, and it will show a loss, which is what the rule "
                     "predicts for burning",
             "correct": False,
             "why": "The rule predicts no loss once everything is counted. A "
                    "loss here means the counting is short."},
            {"text": "Good, since ash is what the wood turns into",
             "correct": False,
             "why": "Ash is a small part of what the wood turns into. Most of "
                    "it went into the air."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h20",
        "band": "harder",
        "text": "An open flask's reading falls by 1.20 g in the first minute "
                "and by 0.30 g in the second. Determine what that tells you.",
        "options": [
            {"text": "The reaction is speeding up, and 0.90 g of gas has left "
                     "so far",
             "correct": False,
             "why": "A smaller loss in the second minute means it is slowing, "
                    "and the two losses add rather than subtract."},
            {"text": "The gas is being destroyed more slowly as the reaction "
                     "goes on",
             "correct": False,
             "why": "No gas is destroyed at any speed. It is leaving the "
                    "flask, and less of it in the second minute."},
            {"text": "The reaction is slowing down, and 1.50 g of gas has "
                     "left so far",
             "correct": True},
            {"text": "The balance is drifting, since a steady reaction would "
                     "lose the same each minute",
             "correct": False,
             "why": "Reactions slow as their chemicals are used up. There is "
                    "nothing wrong with the balance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h21",
        "band": "harder",
        "text": "One sealed flask holds the substances a reaction starts "
                "with. An identical sealed flask holds everything that "
                "reaction makes. Compare the two readings.",
        "options": [
            {"text": "They are equal",
             "correct": True},
            {"text": "The products weigh more, because a reaction that makes "
                     "new substances has made new matter to go with them",
             "correct": False,
             "why": "New substances are the old atoms rearranged. Nothing new "
                    "has been made to weigh."},
            {"text": "The products weigh less, because some was given off as "
                     "heat while the reaction ran",
             "correct": False,
             "why": "Heat carries no mass, so giving it out costs the flask "
                    "nothing at all."},
            {"text": "It depends on whether a gas was one of the products",
             "correct": False,
             "why": "Both flasks are sealed, so a gas is weighed exactly as a "
                    "solid is."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h22",
        "band": "harder",
        "text": "40.00 g of chemicals react in an open flask. The solid and "
                "liquid left in the flask together weigh 37.40 g. Calculate "
                "the mass of gas that escaped.",
        "options": [
            {"text": "77.40 g",
             "correct": False,
             "why": "Adding the two counts the flask's contents twice. The "
                    "37.40 g came out of the 40.00 g."},
            {"text": "2.60 g",
             "correct": True},
            {"text": "37.40 g",
             "correct": False,
             "why": "That is what stayed behind, which is the part you can "
                    "still see."},
            {"text": "None, since the gas is still dissolved in the liquid",
             "correct": False,
             "why": "If it were still there the flask would read 40.00 g. The "
                    "reading has dropped."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h23",
        "band": "harder",
        "text": "A student says that sealing the flask is cheating, because "
                "it hides the gas that would otherwise be seen to leave. "
                "Evaluate.",
        "options": [
            {"text": "Fair, since the sealed run is arranged so that the "
                     "reading cannot move, which proves nothing at all about "
                     "what the reaction did",
             "correct": False,
             "why": "It proves the total is unchanged, which is the claim "
                    "being tested."},
            {"text": "Fair: the open run is the honest one",
             "correct": False,
             "why": "The open run is honest and incomplete. It weighs only "
                    "the part that stayed."},
            {"text": "Unfair: sealing hides nothing and weighs more, because "
                     "the gas stays where the balance can read it",
             "correct": True},
            {"text": "Unfair, because a sealed flask stops the gas from ever "
                     "being made",
             "correct": False,
             "why": "The gas is made in both runs. Sealing decides only "
                    "whether it is still on the pan."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h24",
        "band": "harder",
        "text": "In an open vessel one reaction's reading rises and "
                "another's falls. Compare what each result tells you.",
        "options": [
            {"text": "A rise means matter was created and a fall means some "
                     "was destroyed",
             "correct": False,
             "why": "Neither happens. Both readings are about what crossed "
                    "the edge of the vessel."},
            {"text": "A rise means the reaction was faster than the one that "
                     "fell",
             "correct": False,
             "why": "Speed is not what the direction reports. It reports "
                    "which way matter travelled."},
            {"text": "A rise means heat went in, and a fall means heat came "
                     "out again",
             "correct": False,
             "why": "Heat moves in and out of both, and moves no mass in "
                    "either direction."},
            {"text": "A rise means a gas joined from outside; a fall means a "
                     "gas left, and the total is unchanged in both",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h25",
        "band": "harder",
        "text": "A reaction in a sealed flask takes heat IN from the room, "
                "and the flask turns cold. Determine what the balance does.",
        "options": [
            {"text": "It stays the same",
             "correct": True},
            {"text": "It rises, because the heat taken in has been added to "
                     "what is in the flask",
             "correct": False,
             "why": "Heat has no mass, so taking it in adds nothing to a "
                    "reading."},
            {"text": "It falls, because a cold gas takes up less room than a "
                     "warm one does",
             "correct": False,
             "why": "Taking up less room is not weighing less, and the flask "
                    "is sealed in any case."},
            {"text": "It rises, because cold air from the room is drawn "
                     "towards the flask",
             "correct": False,
             "why": "Nothing can get into a sealed flask, and air around it "
                    "is not on the balance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h26",
        "band": "harder",
        "text": "100 g of limestone is heated in an open crucible until only "
                "56 g of lime is left, the rest having been driven off as "
                "gas. Calculate the mass of gas.",
        "options": [
            {"text": "156 g",
             "correct": False,
             "why": "Adding the two counts the lime twice. It came out of "
                    "the 100 g."},
            {"text": "44 g",
             "correct": True},
            {"text": "56 g",
             "correct": False,
             "why": "That is the lime left in the crucible, not the part "
                    "that went into the air."},
            {"text": "100 g",
             "correct": False,
             "why": "That is everything you started with. Most of it is "
                    "still in the crucible."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h27",
        "band": "harder",
        "text": "Magnesium is burned inside a sealed capsule taken to the "
                "Moon, where there is no air. Predict whether the capsule "
                "gains mass, and explain.",
        "options": [
            {"text": "It gains mass, because burning always adds oxygen to a "
                     "metal wherever the burning happens to be done",
             "correct": False,
             "why": "There is no oxygen outside the capsule to add. On Earth "
                    "the gain comes from the air."},
            {"text": "It gains mass, because the heat of burning is trapped "
                     "inside the capsule",
             "correct": False,
             "why": "Trapped heat weighs nothing. Only matter crossing the "
                    "boundary could change a reading."},
            {"text": "No gain: nothing can cross into a sealed capsule, so "
                     "its total is unchanged",
             "correct": True},
            {"text": "It loses mass, because the magnesium is used up with "
                     "nothing to replace it",
             "correct": False,
             "why": "The magnesium's atoms are still in the capsule, joined "
                    "to whatever was in there with them."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h28",
        "band": "harder",
        "text": "An open-flask run is repeated three times and the losses "
                "are 2.18 g, 2.21 g and 2.20 g. Determine what those results "
                "show.",
        "options": [
            {"text": "That the rule holds only roughly, since the three "
                     "numbers are not the same",
             "correct": False,
             "why": "Small differences are ordinary measuring, not a rule "
                    "bending. The same gas is made each time."},
            {"text": "That the same reaction makes the same mass of gas, to "
                     "within the balance's precision",
             "correct": True},
            {"text": "That mass is destroyed",
             "correct": False,
             "why": "Nothing is destroyed. The gas has left the flask and is "
                    "in the room."},
            {"text": "That the balance is faulty, since a reliable one would "
                     "give an identical number every time",
             "correct": False,
             "why": "No balance and no practical repeats exactly. Agreement "
                    "to 0.03 g is close agreement."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h29",
        "band": "harder",
        "text": "One open crucible gains 1.60 g during a reaction and one "
                "open flask loses 2.20 g. State what the two runs have in "
                "common.",
        "options": [
            {"text": "In both, the total mass of everything is unchanged; "
                     "only what stayed on the pan differs",
             "correct": True},
            {"text": "In both, a gas has left the vessel and gone into the "
                     "room around it",
             "correct": False,
             "why": "Gas left one of them. In the other, gas arrived from "
                    "the air."},
            {"text": "In both, the rule has been broken, since a reading that "
                     "moves is a mass that has changed",
             "correct": False,
             "why": "A reading that moves is a weighing that is incomplete, "
                    "which is not the same thing."},
            {"text": "In both, heat has carried mass across the edge of the "
                     "vessel in one direction or the other",
             "correct": False,
             "why": "Heat carries no mass in any direction. What moved was "
                    "gas."},
        ],
        "figure": None,
    },
    {
        "id": "c2-06-h30",
        "band": "harder",
        "text": "A student says a burning candle proves the conservation of "
                "mass rule has exceptions. Evaluate, and state what the rule "
                "actually claims.",
        "options": [
            {"text": "Right, and burning is the exception the rule has always "
                     "had, which is why sealed containers are used to hide it",
             "correct": False,
             "why": "There is no exception to hide. Sealing lets you weigh "
                    "the gases rather than concealing anything."},
            {"text": "Right, because the rule claims the plate's reading will "
                     "not change, and it plainly does",
             "correct": False,
             "why": "The rule is about everything, not about one pan. The "
                    "plate's reading was never the claim."},
            {"text": "Wrong: the rule counts everything, and the candle's "
                     "gases were never counted",
             "correct": True},
            {"text": "Wrong, because a candle gains mass rather than losing "
                     "it",
             "correct": False,
             "why": "The plate does lose mass. The rule survives because the "
                    "gases that left have mass too."},
        ],
        "figure": None,
    },
]
