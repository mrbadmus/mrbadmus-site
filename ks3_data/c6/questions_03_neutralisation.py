"""C6 lesson 03 — Neutralisation: twelve questions (MRB-269).

The lesson's argument is one shape: an acid and a base react, they make two new
substances, and neutral is a point rather than a region. These twelve probe the
angles the mastery ladder leaves alone — where the atoms went, why the curve is
flat then steep then flat, and the four places outside a laboratory where this
reaction is somebody's job.

The distractors are built from the lesson's two declared misconceptions.

`ACID-05` (neutralising an acid destroys it; only water is left) drives e02,
s01, s04 and h01. h01 is the one that matters: it weighs the beaker before and
after, so "the acid was destroyed" has to explain a balance that has not moved.

`ACID-06` (the pH climbs steadily as alkali is added) drives e04, s02 and h02.
s02 is the register's own case put as a question about the shape rather than
about a single drop, and h02 asks what would happen if the alkali were added
five drops at a time — where a steady-climb model predicts the same reading and
the real curve says you would step straight over the answer.

A third strand, everywhere on the page and in neither register entry, is that
NEUTRALISING MEANS MAKING SAFE. e03 and h03 are built on it: pushing an acid
past 7 is not making it safer, and a river needs near-neutral rather than
alkaline.

A fourth strand is that a salt is table salt. e01 and s03 separate the family
from the member.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "neutralisation"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-03-e01",
        "band": "easier",
        "text": "In chemistry, what does the word “salt” mean?",
        "options": [
            {"text": "A whole family of compounds made when an acid reacts "
                     "with a base", "correct": True},
            {"text": "Only sodium chloride, the white stuff that goes on "
                     "chips", "correct": False,
             "why": "Sodium chloride is one salt out of thousands. It is a "
                    "member of the family, not the family."},
            {"text": "Any white crystalline solid left after a liquid "
                     "evaporates", "correct": False,
             "why": "Plenty of white crystals are not salts — sugar is one. "
                    "What makes a salt is what made it."},
            {"text": "Anything that tastes salty when it is dissolved in "
                     "water", "correct": False,
             "why": "Most salts are never tasted and some are poisonous. "
                    "Taste is not how the family is defined."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e02",
        "band": "easier",
        "text": "Hydrochloric acid is neutralised with sodium hydroxide. What "
                "is in the beaker afterwards?",
        "options": [
            {"text": "Nothing but water, because both were destroyed",
             "correct": False,
             "why": "Boil the water off and white crystals are left in the "
                    "dish. They were not in either bottle at the start."},
            {"text": "A salt dissolved in water, made from both of them",
             "correct": True},
            {"text": "A weaker acid, watered down until it stopped mattering",
             "correct": False,
             "why": "Nothing was watered down. Both reactants were used up "
                    "making two new substances."},
            {"text": "The same acid and alkali, sitting there side by side",
             "correct": False,
             "why": "They reacted. If both were still there the mixture would "
                    "still burn, and it does not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e03",
        "band": "easier",
        "text": "An acid at pH 2 has so much alkali added that it reaches pH "
                "12. Is it safer than it was?",
        "options": [
            {"text": "Yes, because anything that has been neutralised is safe",
             "correct": False,
             "why": "It was neutral for one drop and then went straight past. "
                    "pH 12 is a strong alkali."},
            {"text": "Yes, because the acid has all gone", "correct": False,
             "why": "The acid has gone and something just as corrosive has "
                    "taken its place on the other side of 7."},
            {"text": "No, because pH 12 is about as far from neutral as pH 2 "
                     "was", "correct": True},
            {"text": "No, because adding anything to an acid always makes it "
                     "worse", "correct": False,
             "why": "Adding the right amount of alkali makes it harmless. "
                    "What went wrong here is the amount, not the idea."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-e04",
        "band": "easier",
        "text": "Alkali is added to acid one drop at a time and the pH is "
                "recorded. What shape does the graph make?",
        "options": [
            {"text": "A straight line climbing evenly from start to finish",
             "correct": False,
             "why": "For the first nine drops the reading barely moves. A "
                    "steady climb is what a student expects and not what "
                    "happens."},
            {"text": "A curve that rises fastest at the very beginning",
             "correct": False,
             "why": "The beginning is the flattest part. There is far more "
                    "acid than alkali there, so each drop is used up at once."},
            {"text": "A line that falls, because adding alkali lowers the pH",
             "correct": False,
             "why": "Alkali raises the pH. Adding it can never send the "
                    "reading back down."},
            {"text": "A flat stretch, then a sudden jump, then flat again",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-03-s01",
        "band": "standard",
        "text": "A neutralised beaker is left on a windowsill until all the "
                "water has gone. What is left in it?",
        "options": [
            {"text": "Crystals of the salt that the reaction made",
             "correct": True},
            {"text": "Nothing at all, because everything in it evaporated",
             "correct": False,
             "why": "Water evaporates and a solid salt does not. What is left "
                    "is the crystals."},
            {"text": "The original acid, concentrated back to its old "
                     "strength", "correct": False,
             "why": "The acid was used up in the reaction. Removing water "
                    "cannot bring back a substance that no longer exists."},
            {"text": "A film of alkali, which does not evaporate the way acid "
                     "does", "correct": False,
             "why": "The alkali was used up too. What stayed behind is the "
                    "new compound both of them became."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s02",
        "band": "standard",
        "text": "Nine drops of alkali barely move the reading and the tenth "
                "sends it from 3 to 11. Why?",
        "options": [
            {"text": "The tenth drop was larger than the ones before it",
             "correct": False,
             "why": "Every drop came out of the same dropper. What changed "
                    "was what was waiting for it in the beaker."},
            {"text": "The last of the acid was used up, so nothing consumed "
                     "that drop", "correct": True},
            {"text": "The indicator reached its limit and stopped reporting "
                     "properly", "correct": False,
             "why": "The indicator reported faithfully. The change it "
                    "reported was real and it was sudden."},
            {"text": "The mixture had warmed up enough to change its own pH",
             "correct": False,
             "why": "It warms a little and warming does not move a solution "
                    "across the scale by eight units."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s03",
        "band": "standard",
        "text": "A tank of dilute sulfuric acid must be disposed of safely. "
                "What is done first?",
        "options": [
            {"text": "Add much more water, so the acid is too dilute to harm "
                     "anything", "correct": False,
             "why": "Dilution lowers the concentration and the water going "
                    "into the river is still acidic. A river needs near "
                    "neutral."},
            {"text": "Boil it off, so the acid leaves as a vapour",
             "correct": False,
             "why": "Boiling removes water and leaves the acid behind more "
                    "concentrated than it started."},
            {"text": "Add a stronger acid, so the two cancel each other out",
             "correct": False,
             "why": "Two acids never cancel. Cancelling an acid takes "
                    "something from the other side of 7."},
            {"text": "Add a base until it is neutral, then measure the pH "
                     "before releasing it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-s04",
        "band": "standard",
        "text": "A beaker of acid and alkali is weighed before mixing and "
                "again afterwards. What does the balance read?",
        "options": [
            {"text": "Less, because the acid was destroyed in the reaction",
             "correct": False,
             "why": "Nothing is destroyed. The atoms are all still in the "
                    "beaker, rearranged into a salt and water."},
            {"text": "Less, because some of the mixture escaped as a gas",
             "correct": False,
             "why": "An acid with an alkali gives no gas at all. That is what "
                    "an acid with a CARBONATE does."},
            {"text": "More, because two substances have become two new ones",
             "correct": False,
             "why": "Two into two does not add mass. The same atoms are on "
                    "the balance in a different arrangement."},
            {"text": "Exactly the same, because mass is conserved in every "
                     "reaction", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-03-h01",
        "band": "harder",
        "text": "A student says neutralisation destroys the acid. Which "
                "single piece of evidence refutes it?",
        "options": [
            {"text": "The mixture warms up while the reaction is happening",
             "correct": False,
             "why": "Warming shows a reaction happened and says nothing about "
                    "what is left. Plenty of reactions warm up."},
            {"text": "Universal indicator comes out green at the end",
             "correct": False,
             "why": "Green shows the mixture is neutral, which is what the "
                    "student already believes. It settles nothing."},
            {"text": "Boiling the water off leaves white crystals in the dish",
             "correct": True},
            {"text": "The mixture can be poured down the sink afterwards",
             "correct": False,
             "why": "Being safe to pour away is not the same as being empty. "
                    "The salt goes down the sink dissolved in the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h02",
        "band": "harder",
        "text": "The same titration is repeated adding five drops at a time "
                "instead of one. What is lost?",
        "options": [
            {"text": "Nothing, because the same total volume goes in either "
                     "way", "correct": False,
             "why": "The total is the same and the resolution is not. The "
                    "reading crosses 7 inside a single one of those five-drop "
                    "steps."},
            {"text": "The exact point of neutrality, because the reading "
                     "steps straight over it", "correct": True},
            {"text": "The colour change, because five drops dilute the "
                     "indicator", "correct": False,
             "why": "The colour still changes and it changes just as "
                    "sharply. What is lost is knowing exactly when."},
            {"text": "The reaction itself, because it needs time between "
                     "drops", "correct": False,
             "why": "The reaction is essentially instant. Adding faster does "
                    "not stop it happening."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h03",
        "band": "harder",
        "text": "Lime is added to an acidic lake to save the fish. Why is it "
                "added gradually rather than all at once?",
        "options": [
            {"text": "Because lime dissolves slowly and would sink to the "
                     "bottom", "correct": False,
             "why": "How fast it dissolves is a practical detail. The reason "
                    "is what happens to the water if too much goes in."},
            {"text": "Because the fish need time to move away from the "
                     "treated area", "correct": False,
             "why": "The fish cannot leave a lake. What harms them is the "
                    "change in the water they are already in."},
            {"text": "Because a large amount would push the lake past 7 and "
                     "make it alkaline", "correct": True},
            {"text": "Because lime reacts violently with water and would boil "
                     "the lake", "correct": False,
             "why": "Slaked lime added to a lake does nothing dramatic. The "
                    "danger is the pH it produces, not the heat."},
        ],
        "figure": None,
    },
    {
        "id": "c6-03-h04",
        "band": "harder",
        "text": "Toothpaste is described as mildly alkaline. Why mildly, "
                "rather than strongly?",
        "options": [
            {"text": "Because a strong alkali would damage the mouth far more "
                     "than the acid does", "correct": True},
            {"text": "Because a strong alkali would not neutralise the acid "
                     "properly", "correct": False,
             "why": "A strong alkali neutralises acid very well indeed. The "
                    "problem is what it does to everything else."},
            {"text": "Because the acid from bacteria is itself very weak",
             "correct": False,
             "why": "That acid takes enamel below pH 5.5, which is not weak "
                    "in its effect. The limit is on what a mouth can hold."},
            {"text": "Because toothpaste has to stay neutral to be safe to "
                     "use", "correct": False,
             "why": "It is not neutral — it is above 7 on purpose, which is "
                    "how it works against the acid."},
        ],
        "figure": None,
    },
]
