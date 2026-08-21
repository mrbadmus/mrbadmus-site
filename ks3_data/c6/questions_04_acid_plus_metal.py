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
]
