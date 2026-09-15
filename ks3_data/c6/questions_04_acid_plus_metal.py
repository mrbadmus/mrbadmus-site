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
            {"text": "The zinc would stop corroding",
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
        "text": "A tube of magnesium and acid is stoppered tightly while it "
                "is still fizzing hard. What happens inside, and why does it "
                "matter?",
        "options": [
            {"text": "The reaction stops at once, because a sealed tube runs "
                     "out of air and the hydrogen cannot be made without it",
             "correct": False,
             "why": "The hydrogen comes out of the acid, not the air. The "
                    "reaction carries on"},
            {"text": "The hydrogen dissolves back into the acid, so nothing "
                     "builds up",
             "correct": False,
             "why": "Hydrogen is barely soluble, which is why it bubbles out "
                    "in the first place"},
            {"text": "Nothing changes, because the tube was open for only a "
                     "few seconds before it was stoppered",
             "correct": False,
             "why": "The gas is produced fastest at the start, and it goes on "
                    "being produced after the stopper is in"},
            {"text": "Hydrogen keeps being made with nowhere to go, so the "
                     "pressure climbs until the stopper or the glass gives",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-04-e09",
        "band": "easier",
        "text": "A tube of magnesium and dilute acid becomes hot to hold. What does "
                "that tell you?",
        "options": [
            {"text": "That energy is being given out by the reaction", "correct": True},
            {"text": "That the acid was warm before it was poured in", "correct": False,
             "why": "Both were at room temperature at the start. The warmth appears "
                    "only once the reaction begins."},
            {"text": "That the tube is being warmed by the hand holding it", "correct": False,
             "why": "A hand cannot heat a tube that quickly, and the same warming "
                    "happens in a rack."},
            {"text": "That the reaction is taking energy in from the room", "correct": False,
             "why": "Taking energy in would leave the tube cold. This one goes the "
                    "other way."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e10",
        "band": "easier",
        "text": "Which acid makes salts whose names end in chloride?",
        "options": [
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid makes sulfates. The ending always comes from the "
                    "acid."},
            {"text": "Nitric acid", "correct": False,
             "why": "Nitric acid makes nitrates, which is a different family again."},
            {"text": "Citric acid", "correct": False,
             "why": "Citric acid is the acid in lemons and is not one of the three "
                    "that names these families."},
            {"text": "Hydrochloric acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e11",
        "band": "easier",
        "text": "Iron filings are dropped into dilute sulfuric acid. What colour does"
                " the liquid become?",
        "options": [
            {"text": "Pale green", "correct": True},
            {"text": "Deep blue", "correct": False,
             "why": "Blue solutions come from copper compounds, and copper does not "
                    "react with dilute acid at all."},
            {"text": "Bright orange", "correct": False,
             "why": "Nothing here is orange. The colour comes from the iron salt "
                    "dissolving."},
            {"text": "It stays colourless", "correct": False,
             "why": "The iron goes into solution and colours it. A colourless result"
                    " would mean nothing had dissolved."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e12",
        "band": "easier",
        "text": "Which metal and acid does a school use when it wants to fill a jar "
                "with hydrogen?",
        "options": [
            {"text": "Copper and sulfuric acid", "correct": False,
             "why": "Copper gives no gas at all, so there would be nothing to "
                    "collect."},
            {"text": "Zinc and sulfuric acid", "correct": True},
            {"text": "Magnesium and sulfuric acid", "correct": False,
             "why": "Magnesium works but is over in under a minute, which is hard to"
                    " collect and hard to control."},
            {"text": "Iron and sulfuric acid", "correct": False,
             "why": "Iron is so slow that filling a jar would take most of a lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e13",
        "band": "easier",
        "text": "A salt's name has two words. What is the first word?",
        "options": [
            {"text": "The acid", "correct": False,
             "why": "The acid decides the second word. The first comes from the "
                    "other reactant."},
            {"text": "The metal", "correct": True},
            {"text": "The gas given off", "correct": False,
             "why": "The gas leaves the tube and takes no part in the name at all."},
            {"text": "The solution's colour", "correct": False,
             "why": "Colour is an observation, not part of a chemical name."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e14",
        "band": "easier",
        "text": "What is the reactivity series?",
        "options": [
            {"text": "The order of metals from most reactive to least", "correct": True},
            {"text": "The order metals were found in", "correct": False,
             "why": "History and reactivity are different lists. Copper was known "
                    "long before magnesium."},
            {"text": "The order of metals by weight", "correct": False,
             "why": "Density plays no part. A heavy metal can be very unreactive."},
            {"text": "The order of metals by hardness", "correct": False,
             "why": "Hardness is a physical property and does not predict what a "
                    "metal does in acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e15",
        "band": "easier",
        "text": "Where must a metal sit in the reactivity series if it is to react "
                "with a dilute acid?",
        "options": [
            {"text": "Below hydrogen", "correct": False,
             "why": "A metal below hydrogen cannot push it out of the acid, so "
                    "nothing happens."},
            {"text": "At the very top of the series", "correct": False,
             "why": "Zinc and iron are nowhere near the top and both react perfectly"
                    " well."},
            {"text": "Above hydrogen", "correct": True},
            {"text": "Anywhere, since every metal reacts with acid", "correct": False,
             "why": "Some metals do nothing at all in dilute acid, however long they"
                    " are left."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e16",
        "band": "easier",
        "text": "Hydrogen that has mixed with air does not squeak when lit. What does"
                " it do?",
        "options": [
            {"text": "Nothing", "correct": False,
             "why": "Air does not put the flame out here. The mixture catches "
                    "violently."},
            {"text": "It burns quietly", "correct": False,
             "why": "A slow, quiet flame is what happens at the mouth of a "
                    "stoppered tube, not in a mixture with air."},
            {"text": "It changes colour", "correct": False,
             "why": "Hydrogen is colourless throughout, and colour has nothing to do"
                    " with the hazard."},
            {"text": "It bangs", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e17",
        "band": "easier",
        "text": "Which of these substances is a salt made by an acid and a metal?",
        "options": [
            {"text": "Zinc sulfate", "correct": True},
            {"text": "Sulfuric acid", "correct": False,
             "why": "That is one of the reactants. The salt is what is made once its"
                    " hydrogen has been replaced."},
            {"text": "Hydrogen", "correct": False,
             "why": "Hydrogen is the gas given off. It is an element, not a salt."},
            {"text": "Magnesium", "correct": False,
             "why": "Magnesium is a metal element. It becomes part of a salt only "
                    "after it has reacted."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e18",
        "band": "easier",
        "text": "Iron reacts with dilute acid, but so slowly that it takes most of a "
                "lesson. What does that suggest?",
        "options": [
            {"text": "That iron sits only just above hydrogen in the series", "correct": True},
            {"text": "That iron sits just below hydrogen in the series", "correct": False,
             "why": "Below hydrogen means no reaction at all. Iron does react, so it"
                    " must be above."},
            {"text": "That the acid used on iron was weaker than usual", "correct": False,
             "why": "The same acid is used on all four metals, and three of them "
                    "behave quite differently in it."},
            {"text": "That iron is the most reactive metal on the bench", "correct": False,
             "why": "The most reactive metal would be the fastest. Iron is the "
                    "slowest of the ones that react."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e19",
        "band": "easier",
        "text": "A metal is left in dilute acid and no gas is produced at all. What "
                "does that place it below?",
        "options": [
            {"text": "Below zinc in the reactivity series", "correct": False,
             "why": "Iron is below zinc and still reacts. The line that matters is "
                    "somewhere else."},
            {"text": "Below iron in the reactivity series", "correct": False,
             "why": "Being below iron is not enough on its own. What decides it is "
                    "where hydrogen sits."},
            {"text": "Below hydrogen in the reactivity series", "correct": True},
            {"text": "Below magnesium in the reactivity series", "correct": False,
             "why": "Zinc and iron are both below magnesium and both fizz, so this "
                    "cannot be the line."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e20",
        "band": "easier",
        "text": "Zinc fizzes steadily for several minutes while magnesium is finished"
                " inside one. What explains that?",
        "options": [
            {"text": "The zinc was in a weaker acid than the magnesium", "correct": False,
             "why": "Both tubes hold the same acid at the same concentration. Only "
                    "the metal is different."},
            {"text": "Magnesium is more reactive than zinc", "correct": True},
            {"text": "Zinc is more reactive than magnesium", "correct": False,
             "why": "The more reactive metal is the faster one, and that is the "
                    "magnesium here."},
            {"text": "Zinc produces a different gas, which comes off more slowly", "correct": False,
             "why": "Both give hydrogen. What differs is how fast it arrives."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e21",
        "band": "easier",
        "text": "A tube of magnesium and acid fizzes hard and then stops. Why has it "
                "stopped?",
        "options": [
            {"text": "The hydrogen has filled the tube and blocked the reaction", "correct": False,
             "why": "The gas escapes from an open tube as fast as it is made, so "
                    "nothing is blocked."},
            {"text": "All the magnesium has been used up", "correct": True},
            {"text": "The acid has turned into an alkali", "correct": False,
             "why": "Nothing turns the acid alkaline. It is simply being consumed "
                    "along with the metal."},
            {"text": "The tube has cooled down too far to carry on", "correct": False,
             "why": "The tube ends up warmer than it started. Cooling is not what "
                    "stopped it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s09",
        "band": "standard",
        "text": "Magnesium fizzes just as hard in hydrochloric acid as in sulfuric "
                "acid. What does that show?",
        "options": [
            {"text": "That the two acids are really the same substance under "
                      "different names", "correct": False,
             "why": "They are different acids and give different salts. Only the "
                    "rate is alike."},
            {"text": "That the metal's reactivity decides the rate, not which acid is"
                      " used", "correct": True},
            {"text": "That magnesium reacts with anything it is dropped into, acid or"
                      " not", "correct": False,
             "why": "The comparison was between two acids. It says nothing about "
                    "other liquids."},
            {"text": "That the products of the two reactions must therefore be "
                      "identical", "correct": False,
             "why": "The salts differ — a chloride in one tube and a sulfate in the "
                    "other."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s10",
        "band": "standard",
        "text": "A technician picks zinc rather than magnesium for preparing a jar of"
                " hydrogen. Suggest why.",
        "options": [
            {"text": "Zinc gives a different gas, which is easier to store than "
                      "hydrogen", "correct": False,
             "why": "Both give hydrogen. The choice is about the pace of the "
                    "reaction."},
            {"text": "Zinc is the only one of the two that is above hydrogen in the "
                      "series", "correct": False,
             "why": "Magnesium is above hydrogen as well, and further above it than "
                    "zinc is."},
            {"text": "Zinc gives more gas in total from the same mass of metal", "correct": False,
             "why": "That is not the reason a technician chooses it. What matters is"
                    " being able to control it."},
            {"text": "Zinc is fast enough to fill a jar and slow enough to control", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s11",
        "band": "standard",
        "text": "An iron nail and the same mass of iron filings are put into "
                "identical tubes of acid. Predict what happens.",
        "options": [
            {"text": "The filings react faster, because far more of the iron is in "
                      "contact with the acid", "correct": True},
            {"text": "The nail reacts faster, because a lump holds its heat better", "correct": False,
             "why": "Neither is heated, and the lump has less surface in contact "
                    "with the acid rather than more."},
            {"text": "Both react at the same rate, since the mass of iron is the same", "correct": False,
             "why": "Equal masses give equal gas in the end, but not at the same "
                    "speed."},
            {"text": "Neither reacts, because iron is below hydrogen in the "
                      "reactivity series", "correct": False,
             "why": "Iron is above hydrogen and does react. It is simply the slowest"
                    " of the ones that do."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s12",
        "band": "standard",
        "text": "A student writes: zinc + hydrochloric acid makes zinc nitrate + "
                "hydrogen. What is wrong with it?",
        "options": [
            {"text": "The gas is wrong — an acid and a metal give carbon dioxide "
                      "rather than hydrogen", "correct": False,
             "why": "Hydrogen is right. It comes out of the acid, and a lit splint "
                    "pops in it."},
            {"text": "The metal is wrong — zinc cannot react with hydrochloric acid "
                      "at all", "correct": False,
             "why": "Zinc reacts steadily with it. The metal in the equation is "
                    "fine."},
            {"text": "The salt is wrong — hydrochloric acid gives chlorides, not "
                      "nitrates", "correct": True},
            {"text": "Nothing is wrong, because the salt takes its ending from the "
                      "metal used", "correct": False,
             "why": "The metal names the first word only. The ending always comes "
                    "from the acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s13",
        "band": "standard",
        "text": "Two tubes hold identical magnesium strips. One has 15 cm³ of acid "
                "and one has 30 cm³ of the same acid, both far more than enough. "
                "Compare the hydrogen made.",
        "options": [
            {"text": "Twice as much from the tube with 30 cm³, since twice the acid "
                      "was available to it", "correct": False,
             "why": "Both tubes had acid to spare. What runs out first is the "
                    "magnesium, and that was the same."},
            {"text": "The same from both, because the magnesium is what runs out", "correct": True},
            {"text": "More from the tube with 15 cm³, because a smaller volume of "
                      "acid is more concentrated", "correct": False,
             "why": "A smaller volume of the same acid is not stronger. It is simply"
                    " less of it."},
            {"text": "None from either — excess acid stops it", "correct": False,
             "why": "Excess acid makes the reaction more certain to finish, not less"
                    " likely to begin."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s14",
        "band": "standard",
        "text": "The magnesium disappears and the liquid stays clear throughout. What"
                " does that tell you about the salt?",
        "options": [
            {"text": "That no salt was made, since a new solid would be visible in "
                      "the tube", "correct": False,
             "why": "A salt was made. Boiling the liquid dry leaves it behind as "
                    "white crystals."},
            {"text": "That the salt is soluble and dissolves as it forms", "correct": True},
            {"text": "That the salt sank to the bottom before it could be seen "
                      "properly", "correct": False,
             "why": "Nothing settles. A clear liquid throughout means nothing solid "
                    "is present."},
            {"text": "That the salt left with the hydrogen", "correct": False,
             "why": "Only the gas leaves. The salt stays behind, dissolved in the "
                    "liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s15",
        "band": "standard",
        "text": "How would you show that the gas from zinc and acid is hydrogen "
                "rather than ordinary air?",
        "options": [
            {"text": "Weigh the collected gas and compare it with the same volume of "
                      "air", "correct": False,
             "why": "A school balance cannot weigh a tube of gas accurately enough "
                    "to separate the two."},
            {"text": "Smell it, since hydrogen has a sharper smell than air does", "correct": False,
             "why": "Hydrogen has no smell, and no gas is ever identified by "
                    "smelling it."},
            {"text": "Look at it, since hydrogen is faintly coloured and air is not", "correct": False,
             "why": "Both are colourless, which is precisely why a test is needed at"
                    " all."},
            {"text": "Hold a lit splint to it: air does not pop and hydrogen does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s16",
        "band": "standard",
        "text": "A student says only the metal is used up in this reaction. Is that "
                "right?",
        "options": [
            {"text": "Yes, because the acid is only there to provide a liquid for the"
                      " metal to sit in", "correct": False,
             "why": "The acid is a reactant. The hydrogen that bubbles off came out "
                    "of it."},
            {"text": "Yes, because an acid is never consumed by anything it reacts "
                      "with", "correct": False,
             "why": "Acids are consumed in every reaction they take part in, this "
                    "one included."},
            {"text": "No, because the acid is a reactant and is used up too", "correct": True},
            {"text": "No, because the water in the acid is what is really used up", "correct": False,
             "why": "The water is the solvent and is still there at the end. It is "
                    "the acid itself that is consumed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s17",
        "band": "standard",
        "text": "The gas is collected in a syringe instead of a test tube. What extra"
                " information does that give?",
        "options": [
            {"text": "How much gas there is, and how quickly it arrives", "correct": True},
            {"text": "Which gas it is, since a syringe identifies what it has "
                      "collected", "correct": False,
             "why": "A syringe measures a volume. Identifying the gas still needs a "
                    "lit splint."},
            {"text": "How pure the metal was before it was dropped in", "correct": False,
             "why": "Nothing about the starting metal can be read off a volume of "
                    "gas alone."},
            {"text": "Whether the reaction gives out heat as it runs", "correct": False,
             "why": "Heat is felt through the flask or measured with a thermometer, "
                    "not read from a syringe."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s18",
        "band": "standard",
        "text": "Two students use the same metal and the same acid and report very "
                "different rates of fizzing. Suggest the most likely cause.",
        "options": [
            {"text": "One of them used a gas that the other did not", "correct": False,
             "why": "Neither adds a gas. The same reaction gives off the same gas in"
                    " both tubes."},
            {"text": "The reaction is unpredictable and gives a different rate every "
                      "time", "correct": False,
             "why": "It is entirely predictable. A difference in the result means a "
                    "difference in the set-up."},
            {"text": "The pieces of metal were different sizes", "correct": True},
            {"text": "One tube was held and the other stood in a rack", "correct": False,
             "why": "A hand cannot change the rate noticeably. Something about the "
                    "metal or the acid did."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s19",
        "band": "standard",
        "text": "A tube of iron filings and dilute sulfuric acid is left overnight. "
                "In the morning there are no filings and the liquid has taken on a "
                "colour. What happened?",
        "options": [
            {"text": "The filings rusted and the rust coloured the liquid green", "correct": False,
             "why": "Rust is orange-brown and forms in damp air, not in a tube of "
                    "acid."},
            {"text": "The filings sank and dissolved in the water rather than "
                      "reacting", "correct": False,
             "why": "Iron does not dissolve in water. It was the acid that took it "
                    "into solution."},
            {"text": "The filings evaporated, leaving the acid behind", "correct": False,
             "why": "A metal does not evaporate from a cold tube. It reacted and "
                    "went into solution."},
            {"text": "The iron reacted away and is now dissolved as iron sulfate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s20",
        "band": "standard",
        "text": "An acid gives off a gas with a reactive metal but gives off none at "
                "all with an alkali. Explain the difference.",
        "options": [
            {"text": "With a metal the hydrogen is pushed out as gas; with an alkali "
                      "it ends up in water", "correct": True},
            {"text": "With an alkali the acid is not really reacting, so nothing can "
                      "be produced from it", "correct": False,
             "why": "It reacts fully, giving a salt and water. Both products stay in"
                    " the beaker."},
            {"text": "An alkali holds the gas dissolved in the solution instead of "
                      "letting it escape", "correct": False,
             "why": "No gas is made at all in that reaction, so there is none to be "
                    "held."},
            {"text": "A metal contains hydrogen and an alkali does not, so only the "
                      "metal can supply gas", "correct": False,
             "why": "A pure metal contains no hydrogen. The gas comes out of the "
                    "acid in both cases."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h09",
        "band": "harder",
        "text": "A student suggests swapping hydrochloric acid for sulfuric acid to "
                "make copper react. Explain why that cannot work.",
        "options": [
            {"text": "Because sulfuric acid is the weaker of the two, so it is even "
                      "less likely to attack the metal", "correct": False,
             "why": "Both are strong acids, and strength is not what is stopping the"
                    " reaction."},
            {"text": "Because what decides it is where copper sits relative to "
                      "hydrogen, which no acid changes", "correct": True},
            {"text": "Because sulfates cannot be made from a metal, only from a metal"
                      " oxide", "correct": False,
             "why": "Magnesium and zinc both give sulfates straight from the metal, "
                    "so that is not the obstacle."},
            {"text": "Because the two acids give the same salt, so swapping them "
                      "changes nothing at all", "correct": False,
             "why": "They give different salts. The reason nothing happens lies with"
                    " the metal, not the salt."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h10",
        "band": "harder",
        "text": "Gas is collected from zinc and acid for five minutes and the rate "
                "falls steadily. Suggest why.",
        "options": [
            {"text": "The hydrogen already collected is pressing back and slowing the"
                      " reaction down", "correct": False,
             "why": "The gas leaves freely into the syringe. Back-pressure is not "
                    "what changes here."},
            {"text": "The acid is being used up, so there is less of it left to react", "correct": True},
            {"text": "The zinc is being coated by the hydrogen it produces, which "
                      "blocks the surface", "correct": False,
             "why": "Bubbles break away as they form. The acid running down is the "
                    "reason the rate falls."},
            {"text": "The tube is cooling, and a cold reaction always stops before a "
                      "warm one", "correct": False,
             "why": "The tube warms as it goes rather than cooling, so this cannot "
                    "be the explanation."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h11",
        "band": "harder",
        "text": "From one tube of magnesium and acid a student concludes that every "
                "metal reacts with acid. Evaluate that.",
        "options": [
            {"text": "Sound, because one clear result is enough to establish a rule "
                      "about metals", "correct": False,
             "why": "A rule about all metals needs testing across metals. One tube "
                    "can only speak for one."},
            {"text": "Sound, because magnesium is a typical metal and what it does "
                      "the others will do", "correct": False,
             "why": "Magnesium is near the top of the series. It is not typical of "
                    "the metals below hydrogen."},
            {"text": "Unsound, because a claim about all metals needs more than one, "
                      "and copper disproves it", "correct": True},
            {"text": "Unsound, because a single tube can never be trusted and the "
                      "result has to be repeated", "correct": False,
             "why": "Repeating the same tube would only confirm magnesium. The gap "
                    "is in which metals were tried."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h12",
        "band": "harder",
        "text": "One metal bubbles within seconds and another takes ten minutes to "
                "show anything. A student says the slow one is below hydrogen. "
                "Evaluate.",
        "options": [
            {"text": "Correct, because anything that slow must be below hydrogen", "correct": False,
             "why": "Slowness is not the test. Producing any gas at all settles "
                    "which side it is on."},
            {"text": "Correct, because a metal above hydrogen always reacts quickly", "correct": False,
             "why": "Iron is above hydrogen and takes most of a lesson, so there is "
                    "no such time limit."},
            {"text": "Wrong, because it reacted at all, so it must be above hydrogen "
                      "but less reactive", "correct": True},
            {"text": "Wrong, because the rate on its own tells you nothing about "
                      "where a metal sits", "correct": False,
             "why": "The rate does rank the metals that react. It simply does not "
                    "decide which side of hydrogen they are."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h13",
        "band": "harder",
        "text": "A strip of pure magnesium contains magnesium and nothing else. What "
                "does that settle about the gas?",
        "options": [
            {"text": "That the gas must be magnesium vapour, since the strip is the "
                      "only thing that disappears", "correct": False,
             "why": "Magnesium vapour would need a furnace, and it would not pop "
                    "with a lit splint."},
            {"text": "That the gas must have come out of the acid, because the metal "
                      "held no hydrogen to give", "correct": True},
            {"text": "That the gas must be air that was trapped in the metal before "
                      "it was dropped in", "correct": False,
             "why": "Trapped air would be a bubble or two, and it would not pop with"
                    " a lit splint."},
            {"text": "That the gas could have come from either, since pure metals "
                      "contain a little hydrogen", "correct": False,
             "why": "A pure element contains only that element. There is no hydrogen"
                    " in it to release."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h14",
        "band": "harder",
        "text": "Compare the hazard of a stoppered tube of hydrogen with a tube in "
                "which hydrogen has mixed with air.",
        "options": [
            {"text": "The stoppered tube is the more dangerous, because the gas "
                      "inside it is under pressure", "correct": False,
             "why": "A stoppered test tube is not pressurised. What makes a tube "
                    "dangerous here is the air in it."},
            {"text": "Both are equally dangerous, the same gas in each", "correct": False,
             "why": "Hydrogen alone burns quietly. Mixed with air it does something "
                    "quite different."},
            {"text": "The mixture is the more dangerous: pure hydrogen burns with a "
                      "squeak, a mixture explodes", "correct": True},
            {"text": "Neither is dangerous, because hydrogen is too light to stay in "
                      "a tube long enough", "correct": False,
             "why": "It stays long enough to be tested, and it is genuinely "
                    "hazardous while it is there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h15",
        "band": "harder",
        "text": "A fixed mass of magnesium in excess acid gives 50 cm³ of hydrogen. "
                "The experiment is repeated with half the mass in the same excess "
                "acid. Predict the volume.",
        "options": [
            {"text": "50 cm³", "correct": False,
             "why": "Excess acid means the magnesium sets the total, and there is "
                    "now half as much of it."},
            {"text": "100 cm³", "correct": False,
             "why": "Speed and total volume are different things. Half the metal "
                    "cannot make more gas."},
            {"text": "None at all", "correct": False,
             "why": "Any amount of magnesium reacts. A smaller piece simply gives a "
                    "smaller amount of gas."},
            {"text": "25 cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h16",
        "band": "harder",
        "text": "Iron is reacted with dilute hydrochloric acid and then with dilute "
                "sulfuric acid. What stays the same, and what changes?",
        "options": [
            {"text": "The metal and the gas stay the same; the salt changes from a "
                      "chloride to a sulfate", "correct": True},
            {"text": "The salt stays the same; the gas changes from hydrogen to "
                      "carbon dioxide", "correct": False,
             "why": "The gas is hydrogen from both acids, and it is the salt that "
                    "differs."},
            {"text": "Everything changes, because two different acids share no "
                      "products at all", "correct": False,
             "why": "The iron and the hydrogen appear in both. Only the salt's "
                    "second word moves."},
            {"text": "Nothing changes at all, because the metal decides both products"
                      " on its own", "correct": False,
             "why": "The metal decides the first word of the salt. The acid decides "
                    "the second."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h17",
        "band": "harder",
        "text": "A student writes acid + metal makes salt + water. Correct it, and "
                "say why the mistake is an easy one.",
        "options": [
            {"text": "It should be salt + hydrogen; water is what an acid makes with "
                      "an alkali instead", "correct": True},
            {"text": "It should be salt + oxygen; the confusion comes from the oxide "
                      "on the surface of the metal", "correct": False,
             "why": "No oxygen is produced. The gas pops with a lit splint, which "
                    "oxygen does not do."},
            {"text": "It should be salt + carbon dioxide; the confusion comes from "
                      "the fizzing, which looks the same", "correct": False,
             "why": "Carbon dioxide comes from a carbonate. A metal gives hydrogen."},
            {"text": "Nothing needs correcting; water is always a product when an "
                      "acid reacts with anything", "correct": False,
             "why": "Water is a product with a base. With a metal the second product"
                    " is a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e22",
        "band": "easier",
        "text": "The eight-tube grid crosses four metals with two acids. Which two"
                " acids are they?",
        "options": [
            {"text": "Hydrochloric and sulfuric", "correct": True},
            {"text": "Citric and ethanoic", "correct": False,
             "why": "Those are the mild acids of the kitchen, not the dilute "
                    "laboratory acids used here."},
            {"text": "Carbonic and citric", "correct": False,
             "why": "Neither is used on this grid, and carbonic acid is far too "
                    "weak to strip hydrogen out."},
            {"text": "Sulfuric and ethanoic acid", "correct": False,
             "why": "Only one of that pair is on the grid; the second acid is a "
                    "laboratory one as well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e23",
        "band": "easier",
        "text": "Zinc granules are dropped into dilute sulfuric acid. Name the "
                "salt that forms.",
        "options": [
            {"text": "Zinc chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid, and that is not "
                    "the acid here."},
            {"text": "Zinc hydroxide", "correct": False,
             "why": "A hydroxide is an alkali rather than the salt made by an "
                    "acid."},
            {"text": "Sulfur zincate", "correct": False,
             "why": "The metal always comes first in a salt's name, and there "
                    "is no such compound."},
            {"text": "Zinc sulfate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e24",
        "band": "easier",
        "text": "Zinc granules sit in dilute acid. What is seen on the surface of the"
                " metal?",
        "options": [
            {"text": "A layer of black powder forming on it", "correct": False,
             "why": "Nothing black is made; the zinc simply goes into solution."},
            {"text": "Small bubbles forming on it and rising", "correct": True},
            {"text": "The metal turning bright orange", "correct": False,
             "why": "Zinc keeps its grey colour while it reacts away."},
            {"text": "A crust of crystals growing over it", "correct": False,
             "why": "The salt made dissolves in the liquid rather than crusting "
                    "on the metal."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e25",
        "band": "easier",
        "text": "Hydrogen in a test tube burns with the oxygen around it. What"
                " substance is made?",
        "options": [
            {"text": "Carbon dioxide", "correct": False,
             "why": "There is no carbon in hydrogen, so no carbon dioxide can be "
                    "made."},
            {"text": "A salt", "correct": False,
             "why": "Salts are made in the liquid by the acid and the metal, not "
                    "by a burning gas."},
            {"text": "Water", "correct": True},
            {"text": "More hydrogen", "correct": False,
             "why": "The hydrogen is what burns away; burning cannot make more of "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e26",
        "band": "easier",
        "text": "Zinc slabs bolted to a ship's hull are much smaller when the ship is"
                " next in dry dock. What has happened to the zinc?",
        "options": [
            {"text": "It has worn away against the water as the ship moved",
             "correct": False,
             "why": "It is a chemical attack rather than rubbing that removes "
                    "it."},
            {"text": "It has reacted away, in place of the steel", "correct": True},
            {"text": "It has been dissolved by the salt already in the sea",
             "correct": False,
             "why": "Salt in the water is not what consumes it; it is attacked "
                    "because it is the more reactive metal there."},
            {"text": "It has turned into steel where it touched the hull",
             "correct": False,
             "why": "One metal does not turn into another by being bolted to it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e27",
        "band": "easier",
        "text": "The liquid in the iron and sulfuric acid tube slowly takes on "
                "a pale green colour. What is the colour coming from?",
        "options": [
            {"text": "Rust washing off the surface of the filings", "correct": False,
             "why": "Rust is orange-brown, and the filings are reacting rather "
                    "than rusting."},
            {"text": "The acid, which turns green as it is used up", "correct": False,
             "why": "The acid is colourless at the start and colourless in the "
                    "part that is left."},
            {"text": "The hydrogen dissolving back into the liquid", "correct": False,
             "why": "Hydrogen leaves as a gas, and it has no colour to give."},
            {"text": "The iron salt now dissolved in it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e28",
        "band": "easier",
        "text": "A strip of magnesium is dropped into dilute sulfuric acid. Name the"
                " salt that forms.",
        "options": [
            {"text": "Magnesium chloride", "correct": False,
             "why": "That would need hydrochloric acid, which is not the acid in "
                    "this tube."},
            {"text": "Magnesium nitrate", "correct": False,
             "why": "Nitrates come from nitric acid, which is not being used "
                    "here."},
            {"text": "Magnesium sulfate", "correct": True},
            {"text": "Magnesium hydride", "correct": False,
             "why": "The hydrogen leaves the tube as a gas rather than joining "
                    "the metal."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e29",
        "band": "easier",
        "text": "A school uses iron filings rather than an iron nail for this tube."
                " Why?",
        "options": [
            {"text": "Because filings are a purer form of iron than a nail is",
             "correct": False,
             "why": "Both are iron; it is the shape rather than the purity that "
                    "is being chosen."},
            {"text": "Because filings react faster, with more iron in contact "
                      "with the acid", "correct": True},
            {"text": "Because a nail would give a different salt from the one the filings give", "correct": False,
             "why": "The same metal and the same acid give the same salt, "
                    "whatever the shape."},
            {"text": "Because filings produce a gas that a nail would not",
             "correct": False,
             "why": "Both give hydrogen; the difference is how quickly it "
                    "arrives."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e30",
        "band": "easier",
        "text": "Which observation in one of these tubes is evidence that a "
                "reaction is happening?",
        "options": [
            {"text": "The liquid in the tube is colourless", "correct": False,
             "why": "The acid was colourless before anything was added to it."},
            {"text": "The metal sinks to the bottom of the tube", "correct": False,
             "why": "A dense solid sinks whether it reacts or not."},
            {"text": "The tube is made of glass and stays clear", "correct": False,
             "why": "The apparatus says nothing about whether a reaction has "
                    "started."},
            {"text": "Bubbles of gas stream off the metal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e31",
        "band": "easier",
        "text": "Of the four metals on the grid, which ones sit above hydrogen in the"
                " reactivity series?",
        "options": [
            {"text": "All four of them", "correct": False,
             "why": "One of the four gives no gas at all, which places it below "
                    "hydrogen."},
            {"text": "Magnesium only", "correct": False,
             "why": "Two of the others fizz as well, and anything that fizzes is "
                    "above hydrogen."},
            {"text": "Magnesium, zinc and iron", "correct": True},
            {"text": "Zinc and iron, but not the others", "correct": False,
             "why": "That leaves out the fastest of them, which is furthest above "
                    "hydrogen of all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-e32",
        "band": "easier",
        "text": "Which two things are deliberately changed from one tube to another on"
                " the grid?",
        "options": [
            {"text": "The metal and the acid", "correct": True},
            {"text": "The temperature and the metal", "correct": False,
             "why": "Every tube is run at room temperature so that the comparison "
                    "holds."},
            {"text": "The volume of acid and the metal", "correct": False,
             "why": "Each tube gets the same volume of acid; changing it would "
                    "spoil the comparison."},
            {"text": "The acid and the size of the test tube", "correct": False,
             "why": "The same tubes are used throughout, and their size is not "
                    "part of the experiment."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s21",
        "band": "standard",
        "text": "One tube of magnesium and acid and one of iron and the same "
                "acid are held after thirty seconds. Compare how warm each "
                "feels.",
        "options": [
            {"text": "Neither warms, because the acid was cold to begin with", "correct": False,
             "why": "The starting temperature does not stop a reaction giving "
                    "out energy."},
            {"text": "The iron tube is much warmer, because it reacts for "
                      "longer", "correct": False,
             "why": "Reacting for longer spreads the same warming out rather "
                    "than concentrating it."},
            {"text": "Both feel the same, because both make hydrogen", "correct": False,
             "why": "Making the same gas does not mean making it at the same "
                    "rate."},
            {"text": "The magnesium tube is much warmer", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s22",
        "band": "standard",
        "text": "Two identical tubes of zinc and acid are set up and one is stood in"
                " water at 40 °C. Predict how the two runs compare.",
        "options": [
            {"text": "The warmed tube fizzes faster and ends with more hydrogen",
             "correct": False,
             "why": "Warming changes the pace, and the same zinc can only give "
                    "the same gas."},
            {"text": "The warmed tube fizzes faster and both end with the same "
                      "hydrogen", "correct": True},
            {"text": "The warmed tube fizzes more slowly, because heat drives the "
                      "acid off", "correct": False,
             "why": "Gentle warming does not drive the acid away, and it speeds "
                    "the reaction up."},
            {"text": "The two behave identically, because the zinc decides "
                      "everything", "correct": False,
             "why": "The metal sets which reaction happens; temperature still "
                    "changes how fast it runs."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s23",
        "band": "standard",
        "text": "A school runs these tubes with dilute acid rather than the"
                " concentrated bottles in the prep room. Explain why.",
        "options": [
            {"text": "Because concentrated acid would give a different salt",
             "correct": False,
             "why": "The salt is set by which acid it is, not by how concentrated "
                    "it is."},
            {"text": "Because concentrated acid would react violently and burns "
                      "far worse", "correct": True},
            {"text": "Because concentrated acid contains no hydrogen to displace",
             "correct": False,
             "why": "It holds more acid in each cm³, so there is more hydrogen "
                    "rather than less."},
            {"text": "Because concentrated acid works only on the metals that sit below hydrogen", "correct": False,
             "why": "No acid reaches below hydrogen, however concentrated it is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s24",
        "band": "standard",
        "text": "A buried steel pipeline is protected with blocks of magnesium rather"
                " than zinc. Suggest why magnesium is chosen.",
        "options": [
            {"text": "Because magnesium is cheaper than zinc to dig into the "
                      "ground", "correct": False,
             "why": "Cost is not what decides it, and magnesium is not the cheap "
                    "option."},
            {"text": "Because magnesium is even more reactive, so it is attacked "
                      "first", "correct": True},
            {"text": "Because magnesium does not react with anything in soil at "
                      "all", "correct": False,
             "why": "It has to react; a block that did nothing would protect "
                    "nothing."},
            {"text": "Because magnesium is harder than zinc and protects the pipe "
                      "physically", "correct": False,
             "why": "The protection is chemical rather than a shield over the "
                    "metal."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s25",
        "band": "standard",
        "text": "A copper coin and an iron nail are dropped into two tubes of the same"
                " dilute acid. Predict what is seen in each after an hour.",
        "options": [
            {"text": "Bubbles in both, faster on the coin", "correct": False,
             "why": "The coin gives no bubbles at all, whatever it is left for."},
            {"text": "Bubbles on the nail only", "correct": True},
            {"text": "Bubbles on the coin only", "correct": False,
             "why": "That has the two the wrong way round; iron is the one above "
                    "hydrogen."},
            {"text": "Nothing in either, because both are solid metals",
             "correct": False,
             "why": "Being solid is no barrier; magnesium and zinc are solid and "
                    "react readily."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s26",
        "band": "standard",
        "text": "A metal not on the grid is tested in the same acid. It fizzes "
                "faster than zinc but more slowly than magnesium. Where does "
                "it sit in the reactivity series?",
        "options": [
            {"text": "Below hydrogen, with the unreactive metals", "correct": False,
             "why": "Anything that fizzes at all has displaced hydrogen, so it "
                    "is above it."},
            {"text": "Above magnesium", "correct": False,
             "why": "It is slower than magnesium, which places it below rather "
                    "than above."},
            {"text": "Between zinc and iron", "correct": False,
             "why": "That would make it slower than zinc, and it was faster."},
            {"text": "Between magnesium and zinc", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s27",
        "band": "standard",
        "text": "A tube stops fizzing while a piece of the metal is still sitting at"
                " the bottom. Explain what has happened.",
        "options": [
            {"text": "The metal has stopped being reactive after so long",
             "correct": False,
             "why": "A metal does not lose its place in the reactivity series by "
                    "sitting in a tube."},
            {"text": "The acid has all been used up", "correct": True},
            {"text": "The hydrogen in the tube is now stopping the reaction",
             "correct": False,
             "why": "The gas leaves the liquid rather than holding the reaction "
                    "back."},
            {"text": "The salt has sealed it",
             "correct": False,
             "why": "The salt dissolves as it forms and leaves the surface "
                    "clear."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s28",
        "band": "standard",
        "text": "A gas syringe collects 60 cm³ of hydrogen in 4 minutes. Calculate the"
                " mean rate at which the gas was produced.",
        "options": [
            {"text": "240 cm³ per minute", "correct": False,
             "why": "That multiplies the two numbers instead of dividing one by "
                    "the other."},
            {"text": "64 cm³ per minute", "correct": False,
             "why": "That adds the time to the volume, which is not a rate at "
                    "all."},
            {"text": "15 cm³ per minute", "correct": True},
            {"text": "0.067 cm³ per minute", "correct": False,
             "why": "That divides the time by the volume, giving minutes per cm³ "
                    "instead."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s29",
        "band": "standard",
        "text": "Zinc sulfate can be made from zinc metal or from zinc oxide, "
                "both with sulfuric acid. State one difference you would see "
                "between the two.",
        "options": [
            {"text": "The oxide route needs no acid at all to work", "correct": False,
             "why": "The acid is what supplies the sulfate in both routes."},
            {"text": "The oxide gives off bubbles and the metal does not", "correct": False,
             "why": "Hydrogen comes from the metal route; an oxide gives a "
                    "salt and water only."},
            {"text": "The metal route gives a different salt from the oxide "
                      "route", "correct": False,
             "why": "Both give zinc sulfate, which is why either can be used."},
            {"text": "The metal gives off bubbles and the oxide does not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s30",
        "band": "standard",
        "text": "A student says the acid cannot have been used up because the tube is"
                " still full of liquid. Correct that.",
        "options": [
            {"text": "The liquid is mostly water, and the acid in it can still be "
                      "gone", "correct": True},
            {"text": "The acid is never used up, because only the metal reacts",
             "correct": False,
             "why": "Both reactants are consumed; the acid supplies the hydrogen "
                    "that leaves."},
            {"text": "The liquid would have disappeared entirely if the acid had "
                      "reacted", "correct": False,
             "why": "The water the acid was dissolved in stays in the tube "
                    "throughout."},
            {"text": "The acid turns into hydrogen, so the liquid should have "
                      "vanished", "correct": False,
             "why": "Only part of the acid leaves as gas; the rest stays "
                    "dissolved as the salt."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s31",
        "band": "standard",
        "text": "Iron and magnesium are both above hydrogen, yet iron takes most of a"
                " lesson while magnesium is finished in a minute. Explain.",
        "options": [
            {"text": "Iron is much closer to hydrogen in the series, so it reacts "
                      "far more slowly", "correct": True},
            {"text": "Iron is below hydrogen, which is why it is so slow",
             "correct": False,
             "why": "A metal below hydrogen gives nothing at all, and iron does "
                    "react."},
            {"text": "Iron makes a different gas from magnesium, and that gas takes far longer to appear",
             "correct": False,
             "why": "Both tubes give hydrogen; only the pace is different."},
            {"text": "Iron needs a more concentrated acid before it can react",
             "correct": False,
             "why": "It reacts in the same dilute acid, just slowly."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-s32",
        "band": "standard",
        "text": "A magnesium strip is cut into two halves and both halves are dropped"
                " into the same tube of excess acid. Predict the total hydrogen"
                " collected.",
        "options": [
            {"text": "Twice as much, because there are now two pieces",
             "correct": False,
             "why": "Cutting a strip does not add any magnesium to the tube."},
            {"text": "The same as from the whole strip", "correct": True},
            {"text": "Half as much, because each piece is half the size",
             "correct": False,
             "why": "The two halves together hold all of the original magnesium."},
            {"text": "None — it cannot react",
             "correct": False,
             "why": "Cut edges react perfectly well, and rather more readily."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h18",
        "band": "harder",
        "text": "One student measures the rate by counting bubbles a minute and another"
                " by reading a gas syringe. Evaluate the two methods.",
        "options": [
            {"text": "Counting is better, because every bubble is the same size",
             "correct": False,
             "why": "Bubbles vary in size, which is exactly why a count is a poor "
                    "measure."},
            {"text": "Counting is better, because a syringe leaks some of the gas as it arrives", "correct": False,
             "why": "A syringe holds the gas it collects; leaking is a fault "
                    "rather than a feature."},
            {"text": "The syringe is better, because it reports a volume rather "
                      "than a count", "correct": True},
            {"text": "The two are equally good, because both rise with the rate",
             "correct": False,
             "why": "Both rise, and only one of them gives a number that can be "
                    "compared between runs."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h19",
        "band": "harder",
        "text": "The copper tube is run even though everybody knows nothing will"
                " happen. Explain what running it adds.",
        "options": [
            {"text": "It shows that the acid used was fresh enough to work",
             "correct": False,
             "why": "A tube in which nothing happens cannot report anything about "
                    "the acid's condition."},
            {"text": "It shows that a metal has to be reactive enough for the "
                      "reaction at all", "correct": True},
            {"text": "It shows that copper reacts if it is given long enough",
             "correct": False,
             "why": "It never reacts, which is the result the tube is there to "
                    "record."},
            {"text": "It shows that the reaction needs warming before it will start in any tube",
             "correct": False,
             "why": "The other tubes started unheated, so warming is plainly not "
                    "required."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h20",
        "band": "harder",
        "text": "The magnesium tube is repeated with a more concentrated acid, "
                "still far more than enough to use the strip up. Compare the "
                "rate and the total hydrogen with the first run.",
        "options": [
            {"text": "Slower, and the same total hydrogen", "correct": False,
             "why": "Nothing here slows the reaction; the acid is more "
                    "concentrated rather than less."},
            {"text": "Faster, and more hydrogen in total", "correct": False,
             "why": "The magnesium sets the total, and there is no more of it "
                    "than before."},
            {"text": "The same rate, and more hydrogen in total", "correct": False,
             "why": "A more crowded acid meets the metal more often, so the "
                    "rate does rise."},
            {"text": "Faster, and the same total hydrogen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h21",
        "band": "harder",
        "text": "The same magnesium strip is used again but with only 2 cm³ of the acid"
                " instead of 10 cm³. Predict what is seen at the end.",
        "options": [
            {"text": "The strip disappears as before, only more slowly",
             "correct": False,
             "why": "There is not enough acid present to use all of the strip up, "
                    "however long it is left."},
            {"text": "Fizzing stops with some of the strip still there",
             "correct": True},
            {"text": "Fizzing goes on until the tube is empty of liquid",
             "correct": False,
             "why": "The water stays in the tube; it is the acid in it that runs "
                    "out."},
            {"text": "Nothing happens at all, because 2 cm³ is too little to "
                      "react", "correct": False,
             "why": "A small volume of acid reacts perfectly well as far as it "
                    "goes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h22",
        "band": "harder",
        "text": "The grid is read twice: once down its columns and once across its"
                " rows. State what each reading teaches.",
        "options": [
            {"text": "Down a column the acid sets the rate; across a row the "
                      "metal sets the salt", "correct": False,
             "why": "That swaps the two: the same metal fizzes alike in both "
                    "acids."},
            {"text": "Down a column the metal sets the rate; across a row the "
                      "acid sets the salt", "correct": True},
            {"text": "Both readings show the same thing, which is the reactivity "
                      "series", "correct": False,
             "why": "Only one direction reports reactivity; the other reports "
                    "which salt was made."},
            {"text": "Down a column the tube warms; across a row the tube cools",
             "correct": False,
             "why": "Every reacting tube warms, in whichever direction it is "
                    "read."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h23",
        "band": "harder",
        "text": "Compare what decides the total volume of hydrogen when the "
                "acid is in excess with what decides it when the metal is in "
                "excess.",
        "options": [
            {"text": "The acid decides it in both cases, because the hydrogen "
                      "is its own", "correct": False,
             "why": "The hydrogen comes from the acid, and the total still "
                    "stops when either runs out."},
            {"text": "The metal decides it in both cases, because it does the "
                      "displacing", "correct": False,
             "why": "A metal left sitting in an empty acid has nothing to "
                    "displace from."},
            {"text": "The size of the tube decides it, because the gas must "
                      "fit in it", "correct": False,
             "why": "The gas is led away to a syringe, so the tube's size sets "
                    "nothing."},
            {"text": "Whichever of the two runs out first sets the total", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h24",
        "band": "harder",
        "text": "A student leaves copper in acid for a week, sees nothing, and writes"
                " that copper reacts extremely slowly. Evaluate.",
        "options": [
            {"text": "Sound, because a week is not long enough to see a slow "
                      "reaction", "correct": False,
             "why": "A week with no bubbles at all is not a slow reaction being "
                    "missed."},
            {"text": "Sound, because every metal reacts with acid to some extent",
             "correct": False,
             "why": "Metals below hydrogen do not react with dilute acid at all."},
            {"text": "Unsound, because copper is below hydrogen and does not "
                      "react", "correct": True},
            {"text": "Unsound, because copper reacts quickly once the acid is "
                      "dilute enough", "correct": False,
             "why": "Diluting the acid makes any reaction slower, and copper has "
                    "none to slow."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h25",
        "band": "harder",
        "text": "0.10 g of magnesium in excess acid gives 100 cm³ of hydrogen."
                " Calculate the volume that 0.25 g of magnesium would give in excess"
                " acid.",
        "options": [
            {"text": "125 cm³", "correct": False,
             "why": "That adds a quarter of the volume rather than scaling it by "
                    "two and a half."},
            {"text": "40 cm³", "correct": False,
             "why": "That divides where it should multiply, giving less gas from "
                    "more metal."},
            {"text": "250 cm³", "correct": True},
            {"text": "100 cm³", "correct": False,
             "why": "More magnesium in excess acid gives more hydrogen, not the "
                    "same."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h26",
        "band": "harder",
        "text": "A student claims the order of the four metals in the reactivity series"
                " can be read off these tubes alone. Evaluate.",
        "options": [
            {"text": "Sound for these four, because the order of the rates is the "
                      "order of reactivity", "correct": True},
            {"text": "Unsound, because rate has nothing to do with reactivity",
             "correct": False,
             "why": "Rate is precisely how the tubes report reactivity here."},
            {"text": "Unsound, because a reactivity series can only be written "
                      "from displacement in solutions", "correct": False,
             "why": "Acid tubes give the same order and are a legitimate route to "
                    "it."},
            {"text": "Sound for every metal, because the tubes settle the whole "
                      "series", "correct": False,
             "why": "Only the metals actually tested have been placed by these "
                    "tubes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h27",
        "band": "harder",
        "text": "The same mass of magnesium gives the same volume of hydrogen "
                "in hydrochloric acid as in sulfuric acid, both in excess. "
                "Explain why.",
        "options": [
            {"text": "Because the two salts made happen to weigh the same", "correct": False,
             "why": "The salts differ in mass, and the gas is not weighed "
                    "against them."},
            {"text": "Because both acids contain exactly the same amount of "
                      "hydrogen in each cm³", "correct": False,
             "why": "The two bottles need not match at all, and the totals are "
                    "equal anyway because both are in excess."},
            {"text": "Because hydrogen is made by the metal rather than by the "
                      "acid", "correct": False,
             "why": "The hydrogen comes out of the acid; the metal displaces "
                    "it."},
            {"text": "Because the same magnesium can displace only the same "
                      "amount of hydrogen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h28",
        "band": "harder",
        "text": "Explain why the grid uses two different acids rather than running all"
                " four metals in one acid.",
        "options": [
            {"text": "So that the acid can be changed halfway through to save "
                      "chemicals", "correct": False,
             "why": "Nothing is saved, and the second acid is there to be "
                    "compared with the first."},
            {"text": "So that a second acid can react with the metals the first "
                      "cannot", "correct": False,
             "why": "Both acids reach exactly the same three metals and neither "
                    "reaches copper."},
            {"text": "So that the metal's effect and the acid's effect can be "
                      "separated", "correct": True},
            {"text": "So that a metal can be given a second chance if the first "
                      "tube fails", "correct": False,
             "why": "A repeat would use the same acid, not a different one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h29",
        "band": "harder",
        "text": "A tube has stopped fizzing and no metal can be seen at the bottom."
                " State what is left in the tube and why the reaction ended.",
        "options": [
            {"text": "Salt solution and unused acid, because the metal ran out "
                      "first", "correct": True},
            {"text": "Salt solution only, because both of them were used up at the same moment",
             "correct": False,
             "why": "An exact match is possible but nothing here shows it "
                    "happened; the metal disappearing does not."},
            {"text": "Acid only, because the salt leaves with the gas",
             "correct": False,
             "why": "The salt stays dissolved in the tube; only hydrogen "
                    "leaves."},
            {"text": "Water only, because the acid was entirely consumed",
             "correct": False,
             "why": "The metal disappearing shows it was the metal that ran out, "
                    "not the acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h30",
        "band": "harder",
        "text": "The liquid from a finished tube of zinc granules in dilute sulfuric"
                " acid is evaporated to dryness. Describe what is left and how its mass"
                " compares with the zinc that was added.",
        "options": [
            {"text": "Zinc sulfate crystals, weighing more than the zinc did",
             "correct": True},
            {"text": "Zinc sulfate crystals, weighing exactly what the zinc did",
             "correct": False,
             "why": "The sulfate from the acid is part of the crystals, so they "
                    "must weigh more."},
            {"text": "Zinc metal, weighing exactly what it did at the start",
             "correct": False,
             "why": "The zinc has reacted into a compound and does not come back "
                    "as the metal."},
            {"text": "Nothing at all, because everything left as gas",
             "correct": False,
             "why": "Only the hydrogen left; the zinc and the sulfate stayed "
                    "behind."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h31",
        "band": "harder",
        "text": "Explain what is wrong with this equation: copper + hydrochloric acid"
                " makes copper chloride + hydrogen.",
        "options": [
            {"text": "The salt should be a sulfate rather than a chloride",
             "correct": False,
             "why": "Hydrochloric acid does give chlorides; that part is written "
                    "correctly."},
            {"text": "The gas should be oxygen rather than hydrogen",
             "correct": False,
             "why": "Acids give hydrogen with metals; oxygen comes into none of "
                    "this."},
            {"text": "There is no reaction at all, so there are no products to "
                      "write", "correct": True},
            {"text": "The products are right but the copper should be written "
                      "first", "correct": False,
             "why": "The order of the reactants is not what makes this equation "
                    "wrong."},
        ],
        "figure": None,
    },
    {
        "id": "c6-04-h32",
        "band": "harder",
        "text": "An unlabelled metal gives no gas at all in dilute acid, and a student"
                " concludes it must be copper. Evaluate.",
        "options": [
            {"text": "Sound, because copper is the only metal that gives no gas",
             "correct": False,
             "why": "Several metals sit below hydrogen and behave in exactly the "
                    "same way."},
            {"text": "Sound, because a metal that gives no gas must be the least "
                      "reactive of all", "correct": False,
             "why": "Giving no gas places a metal below hydrogen without ranking "
                    "it against the others there."},
            {"text": "Unsound, because it shows only that the metal is below "
                      "hydrogen", "correct": True},
            {"text": "Unsound, because a metal giving no gas may still be above "
                      "hydrogen", "correct": False,
             "why": "Anything above hydrogen displaces it, so no gas places the "
                    "metal below."},
        ],
        "figure": None,
    },
]
