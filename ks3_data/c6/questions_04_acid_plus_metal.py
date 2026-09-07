"""C6 lesson 04 — Acid + metal: twelve questions (MRB-269).

The lesson's argument is that the hydrogen comes OUT OF THE ACID and the metal
goes INTO SOLUTION, and that whether it happens at all is decided by where the
metal sits relative to hydrogen. These twelve probe the angles the mastery
ladder leaves alone.

The distractors are built from the lesson's declared misconception.

`ACID-07` (the bubbles are the metal turning into gas) drives e02, s01, h01 and
h03. h01 is the one that matters: it evaporates the liquid and finds crystals,
so "the metal became the gas" has to explain where a white solid came from. h03
weighs the whole apparatus in a sealed flask, which removes the "it escaped"
answer entirely.

A second strand, everywhere on the page and in no register entry, is that a
NEGATIVE RESULT IS A FAILURE. e04, s04 and h04 are built on it: a tube that
does nothing, a splint that does not pop, and a week of waiting are all real
results and all say the same precise thing about copper.

A third strand is that a stronger or hotter version of the same thing would
work. s02 and h02 offer concentration, temperature and time as ways round a
reaction that cannot happen at all.

A fourth strand is the naming rule, which arrives here before
`making-a-pure-dry-salt` formalises it. e03 and s03 test the acid half of the
name, which is the half a student drops.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "acid-plus-metal"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-04-e01",
        "band": "easier",
        "text": "What two products does a reactive metal make with an acid?",
        "options": [
            {"text": "A salt and hydrogen", "correct": True},
            {"text": "A salt and water", "correct": False,
             "why": "Water is what an acid makes with an ALKALI. With a metal "
                    "the second product is a gas."},
            {"text": "A metal oxide and water", "correct": False,
             "why": "No oxide forms. The metal joins the part of the acid "
                    "that is left behind once the hydrogen has gone."},
            {"text": "A salt and carbon dioxide", "correct": False,
             "why": "Carbon dioxide comes from a CARBONATE. There is no "
                    "carbon in a metal or in dilute hydrochloric acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e02",
        "band": "easier",
        "text": "Magnesium is dropped into acid and bubbles come off. What "
                "are the bubbles made of?",
        "options": [
            {"text": "Magnesium, which has boiled and turned into a gas",
             "correct": False,
             "why": "Magnesium boils at over a thousand degrees. The tube is "
                    "warm, not white hot, and the metal has gone into "
                    "solution."},
            {"text": "Hydrogen, which came out of the acid", "correct": True},
            {"text": "Air, which was trapped in the metal and pushed out",
             "correct": False,
             "why": "Air does not pop with a lit splint, and a solid strip of "
                    "metal has no air in it to push out."},
            {"text": "Steam, because the acid boiled as the tube warmed up",
             "correct": False,
             "why": "The tube gets warm and nowhere near boiling. Steam does "
                    "not squeak with a splint either."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e03",
        "band": "easier",
        "text": "Zinc reacts with hydrochloric acid. What is the salt called?",
        "options": [
            {"text": "Zinc sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid. The acid names the "
                    "second word."},
            {"text": "Zinc nitrate", "correct": False,
             "why": "Nitrates come from nitric acid. Hydrochloric acid gives "
                    "chlorides."},
            {"text": "Zinc chloride", "correct": True},
            {"text": "Zinc hydroxide", "correct": False,
             "why": "A hydroxide is a base, not the salt this makes. The salt "
                    "takes its ending from the acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e04",
        "band": "easier",
        "text": "Copper is left in dilute acid and nothing happens at all. "
                "What does that tell you?",
        "options": [
            {"text": "That the experiment was set up wrongly somewhere",
             "correct": False,
             "why": "Nothing was set up wrongly. A tube that does nothing is "
                    "reporting something precise about copper."},
            {"text": "That the acid used had gone off and lost its strength",
             "correct": False,
             "why": "The same acid fizzes hard with magnesium in the tube "
                    "beside it. The acid is fine."},
            {"text": "That copper needs a much longer time than the others",
             "correct": False,
             "why": "A week gives the same result as twenty minutes. Time "
                    "cannot make an impossible reaction happen."},
            {"text": "That copper sits below hydrogen in the reactivity "
                     "series", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-04-s01",
        "band": "standard",
        "text": "The magnesium strip disappears completely. Where has the "
                "magnesium gone?",
        "options": [
            {"text": "It has escaped from the tube as part of the gas",
             "correct": False,
             "why": "The gas pops with a lit splint, which is the test for "
                    "hydrogen. Magnesium vapour would not do that."},
            {"text": "It is dissolved in the liquid as a salt", "correct":
             True},
            {"text": "It has been destroyed by the acid attacking it",
             "correct": False,
             "why": "Nothing is destroyed in a reaction. Every magnesium atom "
                    "that went in is still in the tube."},
            {"text": "It has settled as a fine powder at the bottom",
             "correct": False,
             "why": "The liquid ends up clear with nothing on the bottom. The "
                    "magnesium is in solution, not sitting under it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s02",
        "band": "standard",
        "text": "Iron reacts with acid very slowly. A student warms the tube "
                "and it speeds up. Would warming make copper react?",
        "options": [
            {"text": "Yes, because heat speeds up every chemical reaction",
             "correct": False,
             "why": "Heat speeds up a reaction that can happen. There is no "
                    "reaction here to speed up."},
            {"text": "Yes, because warming pushes copper up the reactivity "
                     "series", "correct": False,
             "why": "A metal's place in the series is a fact about the metal. "
                    "Heating it does not move it."},
            {"text": "No, because copper cannot displace hydrogen at any "
                     "temperature", "correct": True},
            {"text": "No, because copper melts before it would get hot enough",
             "correct": False,
             "why": "Copper melts at over a thousand degrees and the tube "
                    "never gets near it. Melting is not what stops this."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s03",
        "band": "standard",
        "text": "A student makes magnesium sulfate from a metal and an acid. "
                "Which acid did they use?",
        "options": [
            {"text": "Hydrochloric acid, because it is the standard one",
             "correct": False,
             "why": "Hydrochloric acid gives chlorides. The salt's ending "
                    "tells you which acid it came from."},
            {"text": "Nitric acid, because nitrates and sulfates are the same "
                     "thing", "correct": False,
             "why": "They are different endings from different acids. Nitric "
                    "acid gives nitrates only."},
            {"text": "Any acid, because the metal decides the whole name",
             "correct": False,
             "why": "The metal decides the FIRST word. The acid decides the "
                    "second, which is what sulfate is."},
            {"text": "Sulfuric acid, because sulfuric acid gives sulfates",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s04",
        "band": "standard",
        "text": "Gas from a tube is tested with a lit splint and there is no "
                "pop. What is the best conclusion?",
        "options": [
            {"text": "There was no hydrogen in the tube to burn",
             "correct": True},
            {"text": "The test failed and should be run again with a fresh "
                     "splint", "correct": False,
             "why": "A test that correctly reports nothing has not failed. "
                    "The absence is the result."},
            {"text": "The gas was hydrogen but too little of it to hear",
             "correct": False,
             "why": "Even a small amount of hydrogen squeaks. A silent tube "
                    "is a tube with no hydrogen in it."},
            {"text": "The gas must be carbon dioxide instead", "correct":
             False,
             "why": "A splint that does not pop rules hydrogen out and names "
                    "nothing. Identifying another gas needs its own test."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-04-h01",
        "band": "harder",
        "text": "After magnesium and acid have finished reacting, the liquid "
                "is evaporated and white crystals appear. What do they show?",
        "options": [
            {"text": "That some of the acid was left over at the end",
             "correct": False,
             "why": "The acid is a liquid and it would evaporate. What is "
                    "left is a solid that was not there at the start."},
            {"text": "That the magnesium is still there, as part of a new "
                     "compound", "correct": True},
            {"text": "That the gas condensed back into a solid as it cooled",
             "correct": False,
             "why": "Hydrogen left the tube and does not come back. It stays "
                    "a gas at every temperature a lab reaches."},
            {"text": "That the water in the acid froze into crystals",
             "correct": False,
             "why": "The water was evaporated away by heating. Ice would not "
                    "survive it, and these crystals do."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h02",
        "band": "harder",
        "text": "A student wants to compare four metals fairly. Which change "
                "would spoil the comparison?",
        "options": [
            {"text": "Using the same volume of acid in every tube",
             "correct": False,
             "why": "Keeping the volume the same is what makes it fair. That "
                    "is the opposite of spoiling it."},
            {"text": "Using pieces of the same size for each of the metals",
             "correct": False,
             "why": "Equal pieces keep the surface area comparable, which is "
                    "part of a fair test."},
            {"text": "Using a more concentrated acid for the slowest metal",
             "correct": True},
            {"text": "Timing how long each tube takes to stop bubbling",
             "correct": False,
             "why": "Timing is the measurement. Doing it the same way for "
                    "each tube is exactly what is wanted."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h03",
        "band": "harder",
        "text": "Magnesium and acid react in a flask sealed with a balloon "
                "over the neck, weighed before and after. What does the "
                "balance read afterwards?",
        "options": [
            {"text": "Less, because the metal turned into gas and gas weighs "
                     "nothing", "correct": False,
             "why": "Gas has mass, and nothing has left the sealed apparatus. "
                    "The balloon is holding all of it."},
            {"text": "Less, because the balloon lifts and takes weight off "
                     "the flask", "correct": False,
             "why": "The balloon is attached to the flask and pulls on it "
                    "either way. Nothing has been removed from the balance."},
            {"text": "More, because a gas takes up far more room than a solid",
             "correct": False,
             "why": "Room is not mass. The same atoms weigh the same whether "
                    "they are packed tight or spread out."},
            {"text": "The same, because nothing has left the sealed "
                     "apparatus", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h04",
        "band": "harder",
        "text": "Slabs of zinc are bolted to a steel ship's hull below the "
                "waterline. Why does that protect the steel?",
        "options": [
            {"text": "Zinc is more reactive, so the seawater attacks it "
                     "instead", "correct": True},
            {"text": "The zinc coats the steel and keeps the seawater off it",
             "correct": False,
             "why": "The slabs are bolted on in a few places and most of the "
                    "hull is bare. Coating is not what is happening."},
            {"text": "Zinc is less reactive, so it survives seawater better "
                     "than iron", "correct": False,
             "why": "The slabs corrode away and are replaced, which is the "
                    "opposite of surviving better. That is the point of them."},
            {"text": "The zinc neutralises the acid in the seawater around "
                     "the hull", "correct": False,
             "why": "Zinc is a metal, not a base. It reacts with the acid "
                    "rather than cancelling it out."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-04-e05",
        "band": "easier",
        "text": "What does it mean to say a metal displaces the hydrogen in "
                "an acid?",
        "options": [
            {"text": "It takes the place of the hydrogen, and the hydrogen "
                     "leaves as a gas",
             "correct": True},
            {"text": "It pushes the acid out of the way so that the two are "
                     "no longer in contact, which is why the reaction stops "
                     "once the metal is coated",
             "correct": False,
             "why": "Nothing is pushed aside. The metal takes the hydrogen's "
                    "place inside the compound"},
            {"text": "It dissolves the hydrogen into itself",
             "correct": False,
             "why": "The hydrogen leaves the tube as bubbles. It does not go "
                    "into the metal"},
            {"text": "It turns into hydrogen",
             "correct": False,
             "why": "No atom changes kind. The magnesium is still magnesium, "
                    "now part of a salt"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e06",
        "band": "easier",
        "text": "What is the test for hydrogen?",
        "options": [
            {"text": "Bubbling it through limewater and watching the "
                     "limewater turn a milky white, which no other gas on a "
                     "school bench will do",
             "correct": False,
             "why": "That is the test for carbon dioxide. Hydrogen leaves "
                    "limewater clear"},
            {"text": "A lit splint held in the tube gives a squeaky pop",
             "correct": True},
            {"text": "A glowing splint relights",
             "correct": False,
             "why": "That is the test for oxygen. Hydrogen makes a sharp "
                    "squeak instead"},
            {"text": "A lit splint goes out",
             "correct": False,
             "why": "Most gases put a splint out, so it identifies nothing. "
                    "Hydrogen burns with a pop"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e07",
        "band": "easier",
        "text": "Nitric acid reacts with a reactive metal. What family does "
                "the salt belong to?",
        "options": [
            {"text": "Chlorides",
             "correct": False,
             "why": "Chlorides come from hydrochloric acid"},
            {"text": "Sulfates",
             "correct": False,
             "why": "Sulfates come from sulfuric acid"},
            {"text": "Nitrates",
             "correct": True},
            {"text": "Carbonates, since the acid supplies the second half of "
                     "the salt's name and nitric acid is one of the carbonate "
                     "family",
             "correct": False,
             "why": "The acid does supply the ending, and nitric acid is not "
                    "a carbonate. Carbonates react WITH acids"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e08",
        "band": "easier",
        "text": "Four tubes hold magnesium, zinc, iron and copper, each in "
                "the same dilute acid. Which fizzes hardest?",
        "options": [
            {"text": "Copper, because it is the densest of the four and so "
                     "has the most metal in contact with the acid at the "
                     "bottom of the tube",
             "correct": False,
             "why": "Copper does nothing at all. It sits below hydrogen in "
                    "the reactivity series"},
            {"text": "Iron",
             "correct": False,
             "why": "Iron reacts, and slowly. Two of the four are above it in "
                    "the series"},
            {"text": "Zinc",
             "correct": False,
             "why": "Zinc reacts steadily, and one metal here is well above "
                    "it"},
            {"text": "Magnesium",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-04-s05",
        "band": "standard",
        "text": "Iron is added to hydrochloric acid. Name both products.",
        "options": [
            {"text": "Iron chloride and hydrogen",
             "correct": True},
            {"text": "Iron chloride and water, because water is one of the "
                     "two products of every reaction an acid takes part in",
             "correct": False,
             "why": "Water is what an acid gives with an ALKALI. With a metal "
                    "the second product is hydrogen"},
            {"text": "Iron oxide and hydrogen",
             "correct": False,
             "why": "There is no oxide here. The iron joins the part of the "
                    "acid left behind, which is the chloride"},
            {"text": "Iron sulfate and hydrogen",
             "correct": False,
             "why": "Sulfates come from sulfuric acid. This is hydrochloric"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s06",
        "band": "standard",
        "text": "A tube of gas is stoppered and carried away from the "
                "fizzing tube before a lit splint is put to it. Why bother?",
        "options": [
            {"text": "So the gas has time to cool down before a flame is put "
                     "to it",
             "correct": False,
             "why": "The gas is barely warm. The danger is bringing a flame "
                    "near a tube that is still producing hydrogen"},
            {"text": "Because a flame near a tube still making hydrogen is a "
                     "flame near a growing supply of it",
             "correct": True},
            {"text": "Because the pop is louder away from the bench",
             "correct": False,
             "why": "The sound is the same. This is a safety step, not an "
                    "acoustic one"},
            {"text": "Because the hydrogen would otherwise react with the "
                     "acid",
             "correct": False,
             "why": "The hydrogen came out of the acid and does not go back "
                    "into it"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s07",
        "band": "standard",
        "text": "A student says the bubbles coming off the magnesium are "
                "magnesium turning into a gas. What is the strongest evidence "
                "against?",
        "options": [
            {"text": "Magnesium is a solid, and solids cannot turn into a gas "
                     "at room temperature under any circumstances whatever",
             "correct": False,
             "why": "Dry ice does exactly that. The real evidence is where "
                    "the magnesium ends up"},
            {"text": "The gas pops with a lit splint, and magnesium does not "
                     "burn",
             "correct": False,
             "why": "Magnesium burns brilliantly, so this argument fails. The "
                    "pop does identify the gas as hydrogen, which helps"},
            {"text": "Evaporate the liquid afterwards and the magnesium is "
                     "there, in the white crystals",
             "correct": True},
            {"text": "The tube gets warm, which shows a reaction rather than "
                     "a change of state",
             "correct": False,
             "why": "Suggestive and not decisive — changes of state involve "
                    "energy too. The crystals settle it"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s08",
        "band": "standard",
        "text": "A tanker that carries concentrated sulfuric acid is lined "
                "rather than being plain steel. Why does that matter?",
        "options": [
            {"text": "Because the lining stops the acid getting cold enough "
                     "to freeze inside the tank on a winter night and crack "
                     "the steel from within",
             "correct": False,
             "why": "The lining is nothing to do with temperature. A steel "
                    "tank full of acid makes hydrogen"},
            {"text": "Because the steel would make the acid weaker over "
                     "time",
             "correct": False,
             "why": "The acid would be used up slowly, and that is not the "
                    "worry. The gas produced is"},
            {"text": "Because acid dissolves any metal it touches, so no tank "
                     "could ever hold it",
             "correct": False,
             "why": "Copper is untouched by dilute hydrochloric acid. It is "
                    "reactive metals that are attacked"},
            {"text": "Because acid on steel makes hydrogen, and hydrogen and "
                     "air together need only a spark",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-04-h05",
        "band": "harder",
        "text": "The same mass of magnesium is dropped into two tubes, one of "
                "hydrochloric acid and one of sulfuric acid, both dilute. How "
                "do the products compare?",
        "options": [
            {"text": "Magnesium chloride from one and magnesium sulfate from "
                     "the other, with hydrogen from both",
             "correct": True},
            {"text": "The same salt in each, because the salt is named after "
                     "the metal",
             "correct": False,
             "why": "The metal gives the first word only. The acid supplies "
                    "the ending, and the two acids differ"},
            {"text": "Hydrogen from the hydrochloric acid and water from the "
                     "sulfuric acid",
             "correct": False,
             "why": "Water comes from an acid and an ALKALI. Both of these "
                    "tubes give hydrogen"},
            {"text": "Nothing from either, because dilute acid is too weak to "
                     "attack a metal",
             "correct": False,
             "why": "Magnesium reacts vigorously with both dilute acids. "
                    "Dilute is not the same as inactive"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h06",
        "band": "harder",
        "text": "A student wants to prove hydrogen came out of the acid "
                "rather than out of the metal. Which observation does most to "
                "settle it?",
        "options": [
            {"text": "The metal disappears completely as the reaction goes "
                     "on, which shows that everything the metal was made of "
                     "must have left the tube as a gas",
             "correct": False,
             "why": "It disappears from sight into solution as a salt, and "
                    "evaporating brings it back. Nothing left as gas but the "
                    "hydrogen"},
            {"text": "The salt left behind still contains all the metal, and "
                     "the acid's hydrogen is what is missing",
             "correct": True},
            {"text": "Copper in the same acid gives no gas at all, although "
                     "the acid is unchanged",
             "correct": False,
             "why": "It shows the metal has to be reactive enough. It does "
                    "not say where the hydrogen came from"},
            {"text": "The gas pops with a lit splint",
             "correct": False,
             "why": "That identifies the gas as hydrogen and says nothing "
                    "about which substance supplied it"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h07",
        "band": "harder",
        "text": "Zinc slabs are bolted to a steel hull below the waterline "
                "and have to be replaced every few years. What would happen if "
                "they were left off?",
        "options": [
            {"text": "Nothing, as long as the hull is painted, since paint "
                     "keeps the seawater off the steel just as well as a slab "
                     "of zinc does",
             "correct": False,
             "why": "Paint chips, and the slabs are there for where it does. "
                    "They protect steel the paint no longer covers"},
            {"text": "The zinc would stop corroding, because there would be "
                     "no steel for it to protect",
             "correct": False,
             "why": "There would be no zinc there at all. The question is "
                    "what happens to the steel"},
            {"text": "The seawater would attack the steel hull instead",
             "correct": True},
            {"text": "The hull would corrode more slowly, because the zinc "
                     "was speeding the process up",
             "correct": False,
             "why": "Exactly backwards. The zinc is corroded INSTEAD of the "
                    "hull, which is why it needs replacing"},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h08",
        "band": "harder",
        "text": "Copper does not react with dilute hydrochloric acid. Which "
                "change would make it react?",
        "options": [
            {"text": "Warming the acid to just below boiling, since heating "
                     "speeds up any reaction between an acid and a metal by a "
                     "large factor",
             "correct": False,
             "why": "Heating speeds up a reaction that can happen. This one "
                    "cannot, at any temperature"},
            {"text": "Using a more concentrated dilute acid",
             "correct": False,
             "why": "Concentration changes how fast a possible reaction goes. "
                    "It cannot make an impossible one start"},
            {"text": "Leaving it for a year rather than a week",
             "correct": False,
             "why": "Time cannot make an impossible reaction happen. A year "
                    "gives exactly what a week gave"},
            {"text": "None of these — copper sits below hydrogen and cannot "
                     "displace it",
             "correct": True},
        ],
        "figure": None,
    },
]
